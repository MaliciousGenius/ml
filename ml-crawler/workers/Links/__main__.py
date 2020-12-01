#!/usr/bin/env python3

from Links import clickhouse_client


def get_links_from_stream(clickhouse_client, limit=3):
    return(clickhouse_client.execute("SELECT * FROM LinksStream LIMIT {}".format(limit)))

def get_links_from_store(clickhouse_client, limit=3, tag=0):
    return(clickhouse_client.execute("SELECT * FROM LinksStore WHERE tag={} LIMIT {}".format(tag, limit)))

def check_link_existence(clickhouse_client, link):
    if clickhouse_client.execute("SELECT count(*) FROM LinksStore WHERE link=\'{}\'".format(link))[0][0] > 0:
        return True
    else:
        return False

def check_page_existence(clickhouse_client, link_uuid):
    if clickhouse_client.execute("SELECT count(*) FROM PagesStore WHERE link_uuid=\'{}\'".format(link_uuid))[0][0] > 0:
        return True
    else:
        return False

def remove_link_from_stream(clickhouse_client, link):
    return(clickhouse_client.execute("ALTER TABLE LinksStream DELETE WHERE link=\'{}\'".format(link)))

def add_link_to_store(clickhouse_client, link, seed='false'):
    return(clickhouse_client.execute("INSERT INTO LinksStore (link, seed) VALUES (\'{}\', \'{}\')".format(link, seed)))

def update_tag_of_link(clickhouse_client, link_uuid, tag):
    return(clickhouse_client.execute("ALTER TABLE LinksStore UPDATE tag={} WHERE uuid=\'{}\'".format(tag, link_uuid)))

def add_page_to_store(clickhouse_client, link_uuid, seed='false'):
    return(clickhouse_client.execute("INSERT INTO PagesStore (link_uuid, seed) VALUES (\'{}\', \'{}\')".format(link_uuid, seed)))


def main():
    # links from stream processing
    links_from_stream = get_links_from_stream(clickhouse_client)
    if len(links_from_stream) > 0:
        for link in links_from_stream:
            if check_link_existence(clickhouse_client, link[0]):
                remove_link_from_stream(clickhouse_client, link[0])
            else:
                add_link_to_store(clickhouse_client, link[0], link[1])
                remove_link_from_stream(clickhouse_client, link[0])
    else:
        print('No new links in stream. No work.')   

    # links from store processing
    links_from_store = get_links_from_store(clickhouse_client)
    if len(links_from_store) > 0:
        for link in links_from_store:
            if check_page_existence(clickhouse_client, link[1]):
                update_tag_of_link(clickhouse_client, link[1], 1)
            else:
                add_page_to_store(clickhouse_client, link[1], link[3])
                update_tag_of_link(clickhouse_client, link[1], 1)
    else:
        print('No new links in store. No work.')


if __name__ == '__main__':
    main()
