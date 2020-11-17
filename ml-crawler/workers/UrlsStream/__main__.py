#!/usr/bin/env python3

from UrlsStream import clickhouse_client

def get_url_from_stream(client):
    return(client.execute("SELECT url, status FROM UrlsStream LIMIT 1"))

def main():
    clickhouse_value = get_url_from_stream(clickhouse_client)
    print(clickhouse_value)

if __name__ == '__main__':
    main()
