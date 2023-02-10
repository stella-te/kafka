import json
import time
from datetime import datetime
from kafka import KafkaProducer
from message import generate_message

def serializer(msg):
    return json.dumps(msg).encode('utf-8')

topic = 'stella_stream'
server = 'localhost:9092'
# server = '62.183.156.240:9092'


producer = KafkaProducer(
    bootstrap_servers=server,
    value_serializer = serializer
    )

if __name__ == '__main__':
    while True:
        # binary
        # msg = b'hi from stella!!!'
        msg = generate_message()

        print(f'Sending msg @ {datetime.now()} | Message = {str(msg)}' )
        producer.send(topic, msg)
        producer.flush()

        time.sleep(10)




# end
