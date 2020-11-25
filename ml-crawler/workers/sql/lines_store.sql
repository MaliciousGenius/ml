CREATE TABLE IF NOT EXISTS LinesStore (
  line String,
  uuid UUID DEFAULT generateUUIDv4(),
  time DateTime DEFAULT now(),
  date Date DEFAULT toDate(time)  
) ENGINE = MergeTree
PARTITION BY toYYYYMM(date)
ORDER BY (line, time);
