CREATE TABLE Texts (
  id UUID DEFAULT generateUUIDv4(),
  value String,
  status Enum8('true' = 1, 'false' = 0) DEFAULT 0,
  number_sentences Int8 DEFAULT 0,
  time DateTime DEFAULT now()
) ENGINE = MergeTree
PARTITION BY toYYYYMM(time)
ORDER BY (time);