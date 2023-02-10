import tradingeconomics as te
import json


te.login('3aecf53b46e647f:dqfs4pyvdzdxo5y')

print('logged in')

te.subscribe('TSLA:US')

def on_message(ws, message):
      json.loads(message)

def generate_message() -> dict:
    # msg = te.run(on_message)
    msg = {'user_id': 1, 'recipient_id': 2, 'message': 'hi from stella' }

    return(msg)


# generate_message()











# end
