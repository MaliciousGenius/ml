CREATE TABLE IF NOT EXISTS Docs (
  uuid UUID DEFAULT generateUUIDv4(),
  lines Array(UUID),
  tag Enum8(
    'draft' = 0,
    'cached' = 1,
    'analyzed' = 2
  ) DEFAULT 0,
  date Date DEFAULT toDate(time),
  time DateTime DEFAULT now()
) ENGINE = MergeTree
PARTITION BY toYYYYMM(date)
ORDER BY (time);
