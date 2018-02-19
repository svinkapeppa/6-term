#!/usr/bin/env python3


import pika
import sqlite3

QUEUE_PARAMS = "amqp://guest:guest@rabbit:5672"


def callback(ch, method, properties, body):
    print('[x] Received \'{0}\''.format(body))

    cursor.execute('INSERT INTO tmp (message) VALUES (?)',
                   (body,))
    db_connection.commit()
    print('[x] INSERT was successful.')


queue_connection = pika.BlockingConnection(
    pika.URLParameters(QUEUE_PARAMS))
channel = queue_connection.channel()
channel.queue_declare(queue='batman')

db_connection = sqlite3.connect('messages.db')
print('[x] Connected to db.')

cursor = db_connection.cursor()
print('[x] Cursor created.')

cursor.execute('CREATE TABLE IF NOT EXISTS tmp (message VARCHAR(256))')
print('[x] Creation completed.')

print('[*] Waiting for messages. To exit press CTRL+C.')

channel.basic_consume(callback,
                      queue='batman',
                      no_ack=True)

try:
    channel.start_consuming()
except KeyboardInterrupt:
    cursor.execute('SELECT * FROM tmp LIMIT 5')
    print(cursor.fetchall())
    print('[x] TOP 5 rows from database.')
    channel.stop_consuming()

db_connection.close()
channel.close()
print('[x] Connection closed.')
