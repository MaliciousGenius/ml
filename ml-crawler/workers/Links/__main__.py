#!/usr/bin/env python3

from Links import clickhouse_client

def get_links_from_stream(client, limit):
    return(client.execute("SELECT * FROM LinksStream LIMIT {}".format(limit)))

def check_link_existence(client, link):
    if client.execute("SELECT count(*) FROM LinksStore WHERE link=\'{}\'".format(link))[0][0] > 0:
        return True
    else:
        return False

def remove_link_from_stream(client, link):
    return(client.execute("ALTER TABLE LinksStream DELETE WHERE link=\'{}\'".format(link)))

def add_link_to_store(client, link):
    return(client.execute("INSERT INTO LinksStore (link) VALUES (\'{}\')".format(link)))

def main():
    links_from_stream = get_links_from_stream(clickhouse_client, 3)
    if len(links_from_stream) > 0:
        for link in links_from_stream:
            if check_link_existence(clickhouse_client, link[0]):
                remove_link_from_stream(clickhouse_client, link[0])
            else:
                add_link_to_store(clickhouse_client, link[0])
                remove_link_from_stream(clickhouse_client, link[0])

    else:
        print('No links, no work.')   

if __name__ == '__main__':
    main()
