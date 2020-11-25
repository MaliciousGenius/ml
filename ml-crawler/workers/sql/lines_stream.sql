CREATE TABLE IF NOT EXISTS LinesStream (
  line String,
  time DateTime DEFAULT now(),
  date Date DEFAULT toDate(time)
) ENGINE = MergeTree
PARTITION BY toYYYYMM(date)
ORDER BY (line, time);
