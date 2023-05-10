from core.pika_connect import connection, channel

import time

from models.cars_8891 import cars_8891
from core.database_mysql import get_db

import requests
import json


MAX_RETRIES = 10
SLEEP_TIME = 15


def craw8891(url, db):
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    }

    for i in range(MAX_RETRIES):
        try:
            response = requests.get(url, headers=headers)
            break
        except:
            time.sleep(SLEEP_TIME)
    else:
        print(f"Failed to request get after {MAX_RETRIES} retries, exiting...")
        return False        

    json_data = json.loads(response.text)

    datas = json_data['data']['data']

    for data in datas:

        new_data = cars_8891(data_id=data['id'],
                             data=data)
        
        record = db.query(cars_8891).filter(cars_8891.data_id == data['id']).first()
        
        if record == None:
            db.add(new_data)
            db.commit()
            db.refresh(new_data)
    
    return True



db = next(get_db())

# craw8891('https://auto.8891.com.tw/usedauto-newSearch.html?page=4', db)


def callback(ch, method, properties, body):
    
    print(f' [x] Receivde: {body.decode()}')

    url = body.decode()

    result = craw8891(url, db)

    time.sleep(5)
    
    if result:
        ch.basic_ack(method.delivery_tag)
    else:
        ch.basic_nack(method.delivery_tag)

channel.queue_declare(queue='8891-queue', durable=True)
channel.basic_qos(prefetch_count=1)

channel.basic_consume(queue='8891-queue', on_message_callback=callback)

try:
    channel.start_consuming()
except KeyboardInterrupt:
    channel.stop_consuming()


connection.close()
