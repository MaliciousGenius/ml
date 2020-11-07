#!/bin/bash

kafkacat -b kafka.local:9092 -L
clickhouse-client --host=clickhouse.local --port=9000 --query='SELECT 1'