from core.pika_connect import connection, channel, pika
import random
import time

channel.queue_declare(queue='8891-queue', durable=True)

total_pages = 1065

page_urls = [ f'https://auto.8891.com.tw/usedauto-newSearch.html?page={page}' for page in range(1, total_pages+1)]

for url in page_urls:
    channel.basic_publish(exchange='',
                          routing_key='8891-queue',
                          body=url,
                          properties=pika.BasicProperties(delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE))
    
    print(f'page {url} already basic publish')
    
    
connection.close()
