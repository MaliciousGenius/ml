#!/usr/bin/env python3

"""

"""

import os
# from clickhouse_driver import Client

import redis
import clickhouse_driver

# import urls_util

# def url_generator():
#     urls_util.save_url()

def get_url(client):
    return(client.execute("SELECT url FROM Urls LIMIT 1"))

if __name__ == "__main__":
    # connect to redis
    redis_client = redis.Redis(host='redis.local', port=6379)
    
    # set a key
    redis_client.set('test-key', 'test-value')
    
    # get a value
    redis_value = redis_client.get('test-key')
    print(redis_value)

    ## todo: need fix for hardcodes of env vars
    # CLICKHOUSE_HOST = os.environ.get('CLICKHOUSE_HOST') or 'clickhouse.local'
    clickhouse_client = clickhouse_driver.Client('clickhouse.local')

    clickhouse_value = get_url(clickhouse_client)
    print(clickhouse_value)

    # url_generator(get_url(client))

