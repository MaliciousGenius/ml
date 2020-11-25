#!/usr/bin/env python3

import clickhouse_driver
import redis

global clickhouse_client, redis_client

clickhouse_client = clickhouse_driver.Client('clickhouse.local')
redis_client = redis.Redis(host='redis.local', port=6379, db=0, socket_timeout=5)

def create_pages_pipeline(client):
    with open('sql/pages_store.sql') as sql_file:
        query = sql_file.read()
        client.execute(query)

create_pages_pipeline(clickhouse_client)
