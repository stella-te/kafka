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

const producer = kafka.producer()
const consumer = kafka.consumer({ groupId: 'stella-fetch-app' })

// async func to get redis key
// promise-based
async function clientGet(key) {
  return client.get(key);
}

const run = async () => {
  await client.connect()
  var s = await clientGet('tsla')
  // Producing
  // await producer.connect()
  // await producer.send({
  //   topic: 'stella_stream',
  //   messages: [
  //     { value: 'Hello KafkaJS user!' },
  //   ],
  //
  // })
  await consumer.connect()
    await consumer.subscribe({ topic: 'stella_stream', fromBeginning: false })

    await consumer.run({
      eachMessage: async ({ topic, partition, message }) => {

        msg = JSON.parse(message.value)
        ssg = JSON.parse(s)
        var diff = msg.p - ssg[0].Close
        var pct = (diff * 100) / ssg[0].Close
        console.log('p', msg.p, 'close', seg[0].Close, 'diff', diff, 'percentage', pct)
        console.log({
          partition,
          offset: message.offset,
          value: message.value.toString(),
        })
      },
    })
  }




run().catch(console.error)
