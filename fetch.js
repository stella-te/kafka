const { Kafka } = require('kafkajs')
const redis = require('redis');


const kafka = new Kafka({
  clientId: 'stella-fetch-app',
  brokers: ['localhost:9092']
})

const client = redis.createClient({
    socket: {
        host: 'localhost',
        port: 6379
    },
    password: 'university'
});


client.on('error', err => {
    console.log('Error ' + err);
});

// const run = async () => {
//   // Producing
//   await producer.connect()
//   await producer.send({
//     topic: 'test-topic',
//     messages: [
//       { value: 'Hello KafkaJS user!' },
//     ],
//   })

const producer = kafka.producer()

const consumer = kafka.consumer({ groupId: 'stella-fetch-app' })

await consumer.connect()
  await consumer.subscribe({ topic: 'stella_stream', fromBeginning: true })

  await consumer.run({
    eachMessage: async ({ topic, partition, message }) => {
      console.log({
        partition,
        offset: message.offset,
        value: message.value.toString(),
      })
    },
  })
}

run().catch(console.error)
