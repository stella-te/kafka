const msg = {'s': 'TSLA:US', 'p': 214.5, 'd': 1676501880104, 'source': 'APISTREAM', 'origin_script': 'message.py'}

let obj = {
  "s":msg.s,
  "p":msg.p,
  "dt":msg.d,
  "type":"index",
  "origin_script":"fetch.js",
  "source":"APISTREAM"
}

console.log(typeof obj)

const str = JSON.stringify(obj)

console.log(typeof str)
