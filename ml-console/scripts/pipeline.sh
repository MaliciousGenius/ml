#!/usr/bin/env bash

clickhouse-client --host=clickhouse.local -n < ./sql/UrlsStream.sql
clickhouse-client --host=clickhouse.local -n < ./sql/StringsStream.sql
clickhouse-client --host=clickhouse.local -n < ./sql/Texts.sql
clickhouse-client --host=clickhouse.local --query='show tables;'

echo "{\"url\":\"https://ru.wikipedia.org/wiki/Бобры\"}" | kafkacat -P -b kafka.local:9092 -t urls
sleep 1s
echo "{\"url\":\"https://ru.wikipedia.org/wiki/Медведи\"}" | kafkacat -P -b kafka.local:9092 -t urls
sleep 2s
echo "{\"url\":\"https://ru.wikipedia.org/wiki/Утки\"}" | kafkacat -P -b kafka.local:9092 -t urls
sleep 5s
echo "{\"url\":\"https://ru.wikipedia.org/wiki/Гуси\"}" | kafkacat -P -b kafka.local:9092 -t urls
sleep 1s
echo "{\"url\":\"https://ru.wikipedia.org/wiki/Козы\"}" | kafkacat -P -b kafka.local:9092 -t urls
sleep 1s
echo "{\"url\":\"https://ru.wikipedia.org/wiki/Кошки\"}" | kafkacat -P -b kafka.local:9092 -t urls
sleep 1s

clickhouse-client --host=clickhouse.local --query='select * from UrlsStream;'
