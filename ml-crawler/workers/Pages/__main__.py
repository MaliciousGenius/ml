#!/usr/bin/env python3

import requests

from Pages import clickhouse_client, redis_client

def get_new_links(client):
    return(client.execute("SELECT * FROM LinksStore WHERE tag=0"))

def check_page_existence(client, link_uuid):
    # print("check_page_existence : " + "SELECT count(*) FROM PagesStore WHERE link_uuid=\'{}\'".format(link_uuid))
    if client.execute("SELECT count(*) FROM PagesStore WHERE link_uuid=\'{}\'".format(link_uuid))[0][0] > 0:
        return True
    else:
        return False

def cache(client, link):
    if not redis_client.get("'{}\'".format(link)):
        redis_client.set("'{}\'".format(link), requests.get(link))
        print(redis_client.get("'{}\'".format(link)))
        # elif not int(redb.get('empty')):
        #     # Means not empty, so continue
        #     data = json.loads(redb.get('lstdata').decode('utf-8'))
        #     lock_redis()
        #     redb.delete('lstdata')
        #     redb.set('empty', 1)
        #     lock_redis(unlock=True)
        #     logger.info('[MAIN] Loaded new data from Redis DB. Checking labels.')
        #     check_saved_data(data)

def update_tag_of_link(client, link_uuid):
    # print("update_tag_of_link : " + "ALTER TABLE LinksStore UPDATE tag=\'processed\' WHERE link_uuid=\'{}\'".format(link_uuid))
    return(client.execute("ALTER TABLE LinksStore UPDATE tag=1 WHERE uuid=\'{}\'".format(link_uuid)))

def add_page_to_store(client, link_uuid):
    # print("add_page_to_store : " + "INSERT INTO PagesStore (link_uuid) VALUES (\'{}\')".format(link_uuid))
    return(client.execute("INSERT INTO PagesStore (link_uuid) VALUES (\'{}\')".format(link_uuid)))

def add_page_to_cache(client, link_uuid):
    # print("add_page_to_store : " + "INSERT INTO PagesStore (link_uuid) VALUES (\'{}\')".format(link_uuid))
    return(client.execute("INSERT INTO PagesStore (link_uuid) VALUES (\'{}\')".format(link_uuid)))

def main():
    links = get_new_links(clickhouse_client)
    if len(links) > 0:
        for link in links:
            print(link)
            if check_page_existence(clickhouse_client, link[1]):
                pass
                # cache(redis_client, link[1])
                # if check_cache_existence(redis_client, link[1]):
                #     update_tag_of_link(clickhouse_client, link[1])
                # else:
                #     print("update is not required for link: " + link)         
            else:
                print(link[1])
                add_page_to_store(clickhouse_client, link[1])
                update_tag_of_link(clickhouse_client, link[1])

    else:
        print('No links, no work.')   

if __name__ == '__main__':
    main()
