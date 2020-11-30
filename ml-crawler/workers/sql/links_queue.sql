CREATE TABLE IF NOT EXISTS LinksQueue (
  link String,
  seed Enum8(
    'false' = 0,
    'true' = 1
  )
) ENGINE = Kafka
SETTINGS kafka_broker_list = 'kafka.local:9092',
         kafka_topic_list = 'links',
         kafka_group_name = 'clickhouse',
         kafka_format = 'JSONEachRow',
         kafka_skip_broken_messages = 1,
         kafka_num_consumers = 1,
         kafka_max_block_size = 1048576;
