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

// const generate_message = function() {
//   let obj = {
//
//   }
// }

const run = async () => {
  await client.connect()
  var s = await clientGet('tsla')

  await consumer.connect()
    await consumer.subscribe({ topic: 'stella_stream', fromBeginning: false })

    await consumer.run({
      eachMessage: async ({ topic, partition, message }) => {

        msg = JSON.parse(message.value)
        ssg = JSON.parse(s)
        close = ssg[0].Close
        var diff = msg.p - close
        var pct = (diff * 100) / close
        console.log('p', msg.p, 'close', close, 'diff', diff, 'percentage', pct)
        console.log({
          partition,
          offset: message.offset,
          value: message.value.toString(),
        })
        // Producing
        await producer.connect()
        await producer.send({
          topic: 'stella_markets',
          messages: [
            { value: {"s":msg.s},
            "p":msg.p,
            "prev":close,
            "nch":diff,
            "pch":pct,
            "dt":msg.d,
            "type":"tsla:us",
            "origin_script":"fetch.js",
            "source":"APISTREAM"} },
          ],

        })
      },
    })
  }




run().catch(console.error)
