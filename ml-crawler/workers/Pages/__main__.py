#!/usr/bin/env python3

import requests
import redis
from kafka import KafkaProducer
from lxml import html
from bs4 import BeautifulSoup
from urllib.parse import urlparse

from Pages import clickhouse_client, redis_client, kafka_producer

def get_new_links_from_store(client):
    return(client.execute("SELECT * FROM LinksStore WHERE tag=0"))

def get_page_from_store(client, tag):
    return(client.execute("SELECT * FROM PagesStore WHERE tag={}".format(tag)))

def check_page_existence(client, link_uuid):
    if client.execute("SELECT count(*) FROM PagesStore WHERE link_uuid=\'{}\'".format(link_uuid))[0][0] > 0:
        return True
    else:
        return False

def check_cache_existence(client, link):
    if client.get("'{}\'".format(link)):
        return True
    else:
        return False

def update_tag_of_link(client, link_uuid, tag):
    return(client.execute("ALTER TABLE LinksStore UPDATE tag={} WHERE uuid=\'{}\'".format(tag, link_uuid)))

def update_tag_of_page(client, page_uuid, tag):
    return(client.execute("ALTER TABLE PagesStore UPDATE tag={} WHERE uuid=\'{}\'".format(tag, page_uuid)))

def add_page_to_store(client, link_uuid, seed='false'):
    return(client.execute("INSERT INTO PagesStore (link_uuid, seed) VALUES (\'{}\', \'{}\')".format(link_uuid, seed)))

def add_page_to_cache(clickhouse_client, redis_client, link_uuid):
    link = clickhouse_client.execute("SELECT * FROM LinksStore WHERE uuid=\'{}\'".format(link_uuid))[0]
    response = requests.get(link[0])
    response.encoding = 'utf-8'
    redis_client.set("\'{}\'".format(link[1]), "{}".format(response.text))

def add_links_to_queue(kafka_producer, html_doc):
    soup = BeautifulSoup(html_doc, 'html.parser', from_encoding='utf-8')
    links = []
    for link in soup.find_all('a'):
        if link.get('href') and link.get('title'):
            if link.get('href') not in links and link.get('href')[:6] == "/wiki/":
                msg = "\"link\":\"https://ru.wikipedia.org{}\",\"seed\":\"false\"".format(requests.utils.unquote(link.get('href')))
                kafka_producer.send('links', str.encode('{' + msg + '}'))

def add_lines_to_queue(html_doc):
    html_root = html.fromstring(html_doc)
    lines = html_root.text_content().split('\n')
    for line in lines:
        print(line)

def main():
    # links from store processing
    links = get_new_links_from_store(clickhouse_client)
    if len(links) > 0:
        for link in links:
            if check_page_existence(clickhouse_client, link[1]):
                update_tag_of_link(clickhouse_client, link[1], 1)
            else:
                add_page_to_store(clickhouse_client, link[1], link[3])
                update_tag_of_link(clickhouse_client, link[1], 1)
    else:
        print('No new links in store. No work.')

    # cache of page processing
    pages = get_page_from_store(clickhouse_client, 0)
    if len(pages) > 0:
        for page in pages:
            if check_cache_existence(redis_client, page[3]):
                update_tag_of_page(clickhouse_client, page[0], 1)
            else:
                add_page_to_cache(clickhouse_client, redis_client, page[4])
                update_tag_of_page(clickhouse_client, page[0], 1)
    else:
        print('No new pages in store. No work.')

    # pages processing
    pages = get_page_from_store(clickhouse_client, 1)
    if len(pages) > 0:
        for page in pages:
            page_value = redis_client.get("\'{}\'".format(page[4])).decode("utf-8")
            add_links_to_queue(kafka_producer, page_value)
            add_lines_to_queue(page_value)
            update_tag_of_page(clickhouse_client, page[0], 2)
    else:
        print('No new cached pages. No work.')

if __name__ == '__main__':
    main()
