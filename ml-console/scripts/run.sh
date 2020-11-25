#!/usr/bin/env bash

echo '{"link":"https://ru.wikipedia.org/wiki/Бобры"}' | kafkacat -P -b kafka.local:9092 -t links
echo '{"link":"https://ru.wikipedia.org/wiki/Медведи"}' | kafkacat -P -b kafka.local:9092 -t links
echo '{"link":"https://ru.wikipedia.org/wiki/Утки"}' | kafkacat -P -b kafka.local:9092 -t links
echo '{"link":"https://ru.wikipedia.org/wiki/Гуси"}' | kafkacat -P -b kafka.local:9092 -t links
echo '{"link":"https://ru.wikipedia.org/wiki/Козы"}' | kafkacat -P -b kafka.local:9092 -t links
echo '{"link":"https://ru.wikipedia.org/wiki/Кошки"}' | kafkacat -P -b kafka.local:9092 -t links
