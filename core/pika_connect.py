import pika
import time

RABBITMQ_HOST = 'rabbit_mq'
RABBITMQ_PORT = '5672'
RABBITMQ_USER = 'root'
RABBITMQ_PASS = '1234'

credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASS)
parameters = pika.ConnectionParameters(host=RABBITMQ_HOST,
                                       port=RABBITMQ_PORT,
                                       credentials=credentials)

MAX_RETRIES = 10
SLEEP_TIME = 5

for i in range(MAX_RETRIES):
    try:
        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()
        print("Connected to RabbitMQ successfully!")
        break
    except pika.exceptions.AMQPConnectionError:
        print(f"Failed to connect to RabbitMQ, retrying in {SLEEP_TIME} seconds...")
        time.sleep(SLEEP_TIME)
else:
    print(f"Failed to connect to RabbitMQ after {MAX_RETRIES} retries, exiting...")
