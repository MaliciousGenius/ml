#!/usr/bin/env python3

import clickhouse_driver


clickhouse_client = clickhouse_driver.Client('clickhouse.local')


def create_links_pipeline(client):
    with open('sql/links_queue.sql') as sql_file:
        query = sql_file.read()
        client.execute(query)

    with open('sql/links_stream.sql') as sql_file:
        query = sql_file.read()
        client.execute(query)

    with open('sql/links_mv.sql') as sql_file:
        query = sql_file.read()
        client.execute(query)

    with open('sql/links_store.sql') as sql_file:
        query = sql_file.read()
        client.execute(query)

## TODO: TASK-1 - need del create page tables in links modele
def create_pages_pipeline(client):
    with open('sql/pages_store.sql') as sql_file:
        query = sql_file.read()
        client.execute(query)


create_links_pipeline(clickhouse_client)
create_pages_pipeline(clickhouse_client) ## TODO: TASK-1 - need del create page tables in links modele
