#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import html2text
import re
from kafka import KafkaProducer
from json import dumps

import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize, word_tokenize

from UrlsStream import clickhouse_client

def get_urls_from_stream(client):
    return(client.execute("SELECT id, url FROM UrlsStream WHERE status!=1 LIMIT 2"))

def update_url_status(client, id):
    return(client.execute("ALTER TABLE UPDATE UrlsStream SET status=\"1\" WHERE id=\"{}\"".format(id)))

def get_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        data = soup.findAll('body')
        links = soup.findAll('a')
        h = html2text.HTML2Text()
        # h.ignore_links = True
        h.ignore_images = True
        h.ignore_tables = True
        h.body_width = 0
        return h.handle(str(data)), links

def checking(text):
    sentence_counter = len(sent_tokenize(text))
    word_counter = len(sent_tokenize(text))
    if sentence_counter > 1 and word_counter > 1:
        return True
    else:
        return False

def main():
    producer = KafkaProducer(
        bootstrap_servers=['kafka.local:9092'],
        value_serializer=lambda x: dumps(x).encode('utf-8')
    )
    urls = get_urls_from_stream(clickhouse_client)
    if len(urls) > 0:
        for url in urls:
            text, new_urls = get_url(url[1])
            for string in text.split('\n'):
                string = string.rstrip().lstrip()
                if checking(string):
                    data = {'string': string}
                    producer.send('strings', value=data)
                    print(str(string))
            # new_urls = re.findall('href="(.*wikipedia.org.*)"', text)
            print (new_urls)
            update_url_status(clickhouse_client, url[0])
    else:
        print("No work. ==========================")

if __name__ == '__main__':
    main()
