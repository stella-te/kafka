import json
from kafka import KafkaConsumer

topic = 'stella_stream'
server = 'localhost:9092'

if __name__  == '__main__':

    consumer = KafkaConsumer(
        topic,
        bootstrap_servers=server,
        auto_offset_reset='earliest'
        )

    for message in consumer:
        print(json.loads(message.value))
