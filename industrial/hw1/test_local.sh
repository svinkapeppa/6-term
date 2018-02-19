#!/usr/bin/env bash

docker-compose up -d

sleep 30

docker cp consumer/consumer.py hw1_consumer_1:/consumer.py
docker cp producer/producer.py hw1_producer_1:/producer.py

docker exec -it hw1_consumer_1 python3 consumer.py