#!/usr/bin/env python3

from Lines import clickhouse_client, redis_client

def get_cached_pages(client):
    return(client.execute("SELECT * FROM PagesStore WHERE tag=1"))

# def check_page_existence(client, link_uuid):
#     print("check_page_existence : " + "SELECT count(*) FROM PagesStore WHERE link_uuid=\'{}\'".format(link_uuid))
#     if client.execute("SELECT count(*) FROM PagesStore WHERE link_uuid=\'{}\'".format(link_uuid))[0][0] > 0:
#         return True
#     else:
#         return False

# def check_cache_existence(client, link_uuid):
#     print("check_page_existence : " + "SELECT count(*) FROM PagesStore WHERE link_uuid=\'{}\'".format(link_uuid))
#     # if client.execute("SELECT count(*) FROM PagesStore WHERE link_uuid=\'{}\'".format(link_uuid))[0][0] > 0:
#     #     return True
#     # else:
#     #     return False

# def update_tag_of_link(client, link_uuid):
#     print("update_tag_of_link : " + "ALTER TABLE LinksStore UPDATE tag=\'processed\' WHERE link_uuid=\'{}\'".format(link_uuid))
#     return(client.execute("ALTER TABLE LinksStore UPDATE tag=1 WHERE uuid=\'{}\'".format(link_uuid)))

# def add_page_to_store(client, link_uuid):
#     print("add_page_to_store : " + "INSERT INTO PagesStore (link_uuid) VALUES (\'{}\')".format(link_uuid))
#     return(client.execute("INSERT INTO PagesStore (link_uuid) VALUES (\'{}\')".format(link_uuid)))

# def add_page_to_cache(client, link_uuid):
#     print("add_page_to_store : " + "INSERT INTO PagesStore (link_uuid) VALUES (\'{}\')".format(link_uuid))
#     return(client.execute("INSERT INTO PagesStore (link_uuid) VALUES (\'{}\')".format(link_uuid)))

def main():
    pages = get_cached_pages(clickhouse_client)
    if len(pages) > 0:
        for page in pages:
            pass
            # print(page)
            # print(redis_client.get("\'{}\'".format(page[3])))
            # if check_page_existence(clickhouse_client, link[1]):
            #     if check_cache_existence(redis_client, link[1]):
            #         update_tag_of_link(clickhouse_client, link[1])
            #     else:
            #         print("update is not required for link: " + link)         
            # else:
            #     print(link[1])
            #     add_page_to_store(clickhouse_client, link[1])
            #     update_tag_of_link(clickhouse_client, link[1])

    else:
        print('No pages, no work.')   

if __name__ == '__main__':
    main()
