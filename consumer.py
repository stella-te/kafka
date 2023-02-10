import json
from datetime import datetime
from kafka import KafkaConsumer
from kafka import TopicPartition

topic = 'stella_stream'
server = 'localhost:9092'

consumer = KafkaConsumer(
    topic,
    bootstrap_servers=server,
    auto_offset_reset='earliest'
    )

if __name__  == '__main__':

    for msg in consumer:
        print(f'Receiving msg @ {datetime.now()} | Message = {str(msg)}' )







# end
