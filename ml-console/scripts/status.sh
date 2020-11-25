#!/usr/bin/env bash

clickhouse-client --host=clickhouse.local --query='show tables;'
clickhouse-client --host=clickhouse.local --query='select * from LinksStream;'
clickhouse-client --host=clickhouse.local --query='select count(*) from LinksStream;'
clickhouse-client --host=clickhouse.local --query='select * from Links;'
clickhouse-client --host=clickhouse.local --query='select count(*) from Links;'

