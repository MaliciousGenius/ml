CREATE TABLE IF NOT EXISTS LinksStream (
  link String,
  time DateTime DEFAULT now(),
  date Date DEFAULT toDate(time)
) ENGINE = MergeTree
PARTITION BY toYYYYMM(date)
ORDER BY (link, time);
