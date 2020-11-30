CREATE TABLE IF NOT EXISTS LinksStore (
  link String,
  uuid UUID DEFAULT generateUUIDv4(),
  tag Enum8(
    'draft' = 0,
    'processed' = 1
  ) DEFAULT 0,
  seed Enum8(
    'false' = 0,
    'true' = 1
  ) DEFAULT 0,
  time DateTime DEFAULT now(),
  date Date DEFAULT toDate(time)  
) ENGINE = MergeTree
PARTITION BY toYYYYMM(date)
ORDER BY (time);
