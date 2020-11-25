CREATE TABLE IF NOT EXISTS LinesQueue (
  line String
) ENGINE = Kafka
SETTINGS kafka_broker_list = 'kafka.local:9092',
         kafka_topic_list = 'lines',
         kafka_group_name = 'clickhouse',
         kafka_format = 'JSONEachRow',
         kafka_skip_broken_messages = 1,
         kafka_num_consumers = 1,
         kafka_max_block_size = 1048576;

CREATE TABLE IF NOT EXISTS LinesStream (
  line String,
  time DateTime DEFAULT now(),
  date Date DEFAULT toDate(time)
) ENGINE = MergeTree
PARTITION BY toYYYYMM(date)
ORDER BY (line, time);

CREATE MATERIALIZED VIEW IF NOT EXISTS LinesSync TO LinesStream
  AS SELECT line FROM LinesQueue;

CREATE TABLE IF NOT EXISTS Lines (
  line String,
  uuid UUID DEFAULT generateUUIDv4(),
  time DateTime DEFAULT now(),
  date Date DEFAULT toDate(time)  
) ENGINE = MergeTree
PARTITION BY toYYYYMM(date)
ORDER BY (time);
