#!/usr/bin/env bash

clickhouse-client --host=clickhouse.local --query='show tables;'
clickhouse-client --host=clickhouse.local --query='select * from LinksStore;'
clickhouse-client --host=clickhouse.local --query='select count(*) from LinksStore;'
clickhouse-client --host=clickhouse.local --query='select * from PagesStore;'
clickhouse-client --host=clickhouse.local --query='select count(*) from PagesStore;'
clickhouse-client --host=clickhouse.local --query='select * from LinesStore;'
clickhouse-client --host=clickhouse.local --query='select count(*) from LinesStore;'
