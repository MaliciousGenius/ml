CREATE TABLE StringsQueue (
  url String
) ENGINE = Kafka
SETTINGS kafka_broker_list = 'kafka.local:9092',
         kafka_topic_list = 'strings',
         kafka_group_name = 'clickhouse',
         kafka_format = 'JSONEachRow',
         kafka_skip_broken_messages = 1,
         kafka_num_consumers = 1,
         kafka_max_block_size = 1048576;

CREATE TABLE StringsStream (
  id UUID DEFAULT generateUUIDv4(),
  string String,
  status Enum8('true' = 1, 'false' = 0) DEFAULT 0,
  time DateTime DEFAULT now()
) ENGINE = MergeTree
PARTITION BY toYYYYMM(time)
ORDER BY (time);

CREATE MATERIALIZED VIEW StringsMaterializedView TO StringsStream
  AS SELECT * FROM StringsQueue;
