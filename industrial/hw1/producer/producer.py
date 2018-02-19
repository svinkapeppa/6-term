#!/usr/bin/env python3


import pika

connection = pika.BlockingConnection(
    pika.URLParameters("amqp://guest:guest@rabbit:5672"))
channel = connection.channel()
channel.queue_declare(queue='batman')
print('[x] Connection established.')
print('[*] Write your messages. To exit press CTRL+C.')
try:
    while 1:
        data = input('[*] Enter your message: ')
        channel.basic_publish(exchange='',
                              routing_key='batman',
                              body=data)
        print('[x] Sent!')
except KeyboardInterrupt:
    exit()
