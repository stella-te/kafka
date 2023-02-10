import tradingeconomics as te
import json
from key import key

te.login('3aecf53b46e647f:dqfs4pyvdzdxo5y')

print('logged in')

te.subscribe('TSLA:US')

arr = []
str = ''

def on_message(ws, msg):
    price = json.loads(msg)['price']
    # Timestamp of last market price (epoch)
    datetime = json.loads(msg)['dt']
    msg = {"s":"TSLA:US","p":price,"d":datetime,"source":"APISTREAM","origin_script":"message.py"}
    print('on_message', msg)
    return msg

def generate_message() -> dict:
    # msg = {'user_id': 1, 'recipient_id': 2, 'message': 'hi from stella' }
    msg = {"s":"TSLA:US","p":"151,42","d":1663718400,"source":"APISTREAM","origin_script":"message.py"}
    # msg = te.run(on_message)

    return msg
    
generate_message()













# end
