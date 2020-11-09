CREATE TABLE UrlsQueue (
  url String
) ENGINE = Kafka
SETTINGS kafka_broker_list = 'kafka.local:9092',
         kafka_topic_list = 'urls',
         kafka_group_name = 'clickhouse',
         kafka_format = 'JSONEachRow',
         kafka_skip_broken_messages = 1,
         kafka_num_consumers = 1,
         kafka_max_block_size = 1048576;

CREATE TABLE Urls (
  time DateTime DEFAULT now(),
  id UUID DEFAULT generateUUIDv4(),
  url String
) ENGINE = MergeTree
PARTITION BY toYYYYMM(time)
ORDER BY (time);

CREATE MATERIALIZED VIEW UrlsMV TO Urls
  AS SELECT * FROM UrlsQueue;
