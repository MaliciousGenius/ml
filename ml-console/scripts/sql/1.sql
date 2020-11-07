CREATE TABLE urlsQueue (
  url String
) ENGINE = Kafka
SETTINGS kafka_broker_list = 'kafka.local:9092',
         kafka_topic_list = 'urls',
         kafka_group_name = 'clickhouse',
         kafka_format = 'JSONEachRow',
         kafka_skip_broken_messages = 1,
         kafka_num_consumers = 1,
         kafka_max_block_size = 1048576;

CREATE TABLE urls (
  createdDate DateTime DEFAULT now() COMMENT 'Created time',
  url String
) ENGINE = MergeTree
PARTITION BY toYYYYMM(createdDate)
ORDER BY (createdDate);

CREATE MATERIALIZED VIEW urlsMV TO urls AS SELECT * FROM urlsQueue;
