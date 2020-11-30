#!/usr/bin/env bash

echo '{"link":"https://ru.wikipedia.org/wiki/Пространство","seed":"true"}' | kafkacat -P -b kafka.local:9092 -t links
echo '{"link":"https://ru.wikipedia.org/wiki/Время","seed":"true"}' | kafkacat -P -b kafka.local:9092 -t links
echo '{"link":"https://ru.wikipedia.org/wiki/Симметрия","seed":"true"}' | kafkacat -P -b kafka.local:9092 -t links
echo '{"link":"https://ru.wikipedia.org/wiki/Информация","seed":"true"}' | kafkacat -P -b kafka.local:9092 -t links
echo '{"link":"https://ru.wikipedia.org/wiki/Энергия","seed":"true"}' | kafkacat -P -b kafka.local:9092 -t links
echo '{"link":"https://ru.wikipedia.org/wiki/Многообразие","seed":"true"}' | kafkacat -P -b kafka.local:9092 -t links
echo '{"link":"https://ru.wikipedia.org/wiki/Алгоритм","seed":"true"}' | kafkacat -P -b kafka.local:9092 -t links
echo '{"link":"https://ru.wikipedia.org/wiki/Семантика","seed":"true"}' | kafkacat -P -b kafka.local:9092 -t links
echo '{"link":"https://ru.wikipedia.org/wiki/Смысл","seed":"true"}' | kafkacat -P -b kafka.local:9092 -t links
echo '{"link":"https://ru.wikipedia.org/wiki/Вселенная","seed":"true"}' | kafkacat -P -b kafka.local:9092 -t links
echo '{"link":"https://ru.wikipedia.org/wiki/Атом","seed":"true"}' | kafkacat -P -b kafka.local:9092 -t links
echo '{"link":"https://ru.wikipedia.org/wiki/Размерность","seed":"true"}' | kafkacat -P -b kafka.local:9092 -t links
