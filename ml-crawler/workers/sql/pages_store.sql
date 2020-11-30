CREATE TABLE IF NOT EXISTS PagesStore (
  uuid UUID DEFAULT generateUUIDv4(),
  lines Array(UUID),
  tag Enum8(
    'draft' = 0,
    'cached' = 1,
    'analyzed' = 2,
    'filled' = 3
  ) DEFAULT 0,
  seed Enum8(
    'false' = 0,
    'true' = 1
  ) DEFAULT 0,
  link_uuid UUID,
  date Date DEFAULT toDate(time),
  time DateTime DEFAULT now()
) ENGINE = MergeTree
PARTITION BY toYYYYMM(date)
ORDER BY (time);
