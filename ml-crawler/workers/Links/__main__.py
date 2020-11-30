#!/usr/bin/env python3

from Links import clickhouse_client

def get_links_from_stream(clickhouse_client, limit):
    return(clickhouse_client.execute("SELECT * FROM LinksStream LIMIT {}".format(limit)))

def check_link_existence(clickhouse_client, link):
    if clickhouse_client.execute("SELECT count(*) FROM LinksStore WHERE link=\'{}\'".format(link))[0][0] > 0:
        return True
    else:
        return False

def remove_link_from_stream(clickhouse_client, link):
    return(clickhouse_client.execute("ALTER TABLE LinksStream DELETE WHERE link=\'{}\'".format(link)))

def add_link_to_store(clickhouse_client, link, seed='false'):
    return(clickhouse_client.execute("INSERT INTO LinksStore (link, seed) VALUES (\'{}\', \'{}\')".format(link, seed)))

def main():
    # links from stream processing
    links_from_stream = get_links_from_stream(clickhouse_client, 3)
    if len(links_from_stream) > 0:
        for link in links_from_stream:
            if check_link_existence(clickhouse_client, link[0]):
                remove_link_from_stream(clickhouse_client, link[0])
            else:
                add_link_to_store(clickhouse_client, link[0], link[1])
                remove_link_from_stream(clickhouse_client, link[0])
    else:
        print('No new links in stream. No work.')   

if __name__ == '__main__':
    main()
