#!/usr/bin/env python3

from Links import clickhouse_client

def get_links_from_stream(client, limit):
    return(client.execute("SELECT * FROM LinksStream LIMIT {}".format(limit)))

def check_existence(client, link):
    # print("check_existence : " + "SELECT count(*) FROM Links WHERE link=\'{}\'".format(link))
    if client.execute("SELECT count(*) FROM Links WHERE link=\'{}\'".format(link))[0][0] > 0:
        return True
    else:
        return False

def remove_link_from_stream(client, link):
    # print("remove_link_from_stream : " + "ALTER TABLE LinksStream DELETE WHERE link=\'{}\'".format(link))
    return(client.execute("ALTER TABLE LinksStream DELETE WHERE link=\'{}\'".format(link)))

def add_link_to_store(client, link):
    # print("add_link_to_store : " + "INSERT INTO Links (link) VALUES (\'{}\')".format(link))
    return(client.execute("INSERT INTO Links (link) VALUES (\'{}\')".format(link)))

def main():
    links = get_links_from_stream(clickhouse_client, 3)
    if len(links) > 0:
        for link in links:
            if check_existence(clickhouse_client, link[0]):
                remove_link_from_stream(clickhouse_client, link[0])
            else:
                add_link_to_store(clickhouse_client, link[0])
                remove_link_from_stream(clickhouse_client, link[0])

    else:
        print('No links, no work.')   

if __name__ == '__main__':
    main()
