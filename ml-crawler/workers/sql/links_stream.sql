CREATE TABLE IF NOT EXISTS LinksStream (
  link String,
  seed Enum8(
    'false' = 0,
    'true' = 1
  ) DEFAULT 0,
  time DateTime DEFAULT now(),
  date Date DEFAULT toDate(time)
) ENGINE = MergeTree
PARTITION BY toYYYYMM(date)
ORDER BY (time);
