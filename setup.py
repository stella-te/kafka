te.login('3aecf53b46e647f:dqfs4pyvdzdxo5y')

docker
github
python examples
nodejs

~/Downloads
sudo ssh -i university.pem ubuntu@18.206.150.247

{"s":"AAPL:US","p":"151,42"d":1663718400,"source":"APISTREAM","origin_script":"your_script"}

python3 -m venv venv

docker run hello-world

# initialize kafka and zookeeper
docker-compose -f docker-compose.yml up -d

# running port
docker ps

# transfer py file to docker
docker cp producer.py kafka:/app
docker cp consumer.py kafka:/app
docker cp message.py kafka:/app


# kafka shell
docker exec -it kafka /bin/sh
tar -xzf kafka_2.13-3.2.3.tgz

cd /opt/kafka_2.13-2.8.1/bin
cd kafka_2.13-3.2.3/bin

./zookeeper-server-start.sh ../config/zookeeper.properties
./kafka-server-start.sh ../config/server.properties

kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic stella_stream
./kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic stella_stream
./kafka-topics.sh --create --topic stella_stream --bootstrap-server localhost:9092

# localhost 
kafka-topics.sh --list --zookeeper zookeeper:2181
./kafka-topics.sh --list --bootstrap-server localhost:9092
./kafka-topics.sh --describe --topic stella_stream --bootstrap-server localhost:9092
./kafka-console-producer.sh --topic stella_stream --bootstrap-server localhost:9092

./kafka-console-consumer.sh --topic stella_stream --from-beginning --bootstrap-server localhost:9092

./kafka-console-producer.sh --broker-list localhost:9092 --topic stella_stream
{'user_id': 1, 'recipient_id': 2, 'message': 'hi from stella' }
{'user_id': 2, 'recipient_id': 1, 'message': 'hi there' }

./kafka-console-producer.sh --broker-list PLAINTEXT://localhost:9092 --topic stella_stream


kafka-console-consumer.sh --bootstrap-server kafka:9092 --topic stella_stream

kafka-console-consumer.sh --bootstrap-server kafka:9092 --topic stella_stream --from-beginning


curl -u 'stella-te' https://api.github.com/user/repos -d '{"name":"kafta"}'

git clone https://github.com/stella-te/kafka



ps aux | grep zookeeper

kill -9 76048








# end

# end
