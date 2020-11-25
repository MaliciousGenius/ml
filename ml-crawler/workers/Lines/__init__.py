#!/usr/bin/env python3

import clickhouse_driver
import redis

clickhouse_client = clickhouse_driver.Client('clickhouse.local')
redis_client = redis.Redis(host='redis.local', port=6379, db=0, socket_timeout=5)

def create_lines_pipeline(client):
    with open('sql/lines_queue.sql') as sql_file:
        query = sql_file.read()
        client.execute(query)

    with open('sql/lines_stream.sql') as sql_file:
        query = sql_file.read()
        client.execute(query)

    with open('sql/lines_mv.sql') as sql_file:
        query = sql_file.read()
        client.execute(query)

    with open('sql/lines_store.sql') as sql_file:
        query = sql_file.read()
        client.execute(query)

create_lines_pipeline(clickhouse_client)
