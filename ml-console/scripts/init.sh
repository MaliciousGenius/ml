#!/usr/bin/env bash

clickhouse-client --host=clickhouse.local -n < ./sql/Links.sql
clickhouse-client --host=clickhouse.local -n < ./sql/Docs.sql
clickhouse-client --host=clickhouse.local -n < ./sql/Links.sql
