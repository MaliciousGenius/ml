#!/usr/bin/env python3

"""

"""

import os
from clickhouse_driver import Client

def get_url(client):
    return(client.execute("SELECT url FROM Urls LIMIT 1"))

if __name__ == "__main__":
    CLICKHOUSE_HOST = os.environ.get('CLICKHOUSE_HOST') or 'clickhouse.local'
    client = Client(CLICKHOUSE_HOST)
    result = get_url(client)
    print(result)
