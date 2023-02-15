import tradingeconomics as te
import json


te.login('3aecf53b46e647f:dqfs4pyvdzdxo5y')

data = te.getMarketsBySymbol(symbols='tsla:us')

# if data[0]['Close']:
print(type(data))

if ('Symbol' in arr[0] and 'Close' in arr[0]):
    arr = json.dumps(arr).encode('utf-8')
print(arr)
print(type(arr))

data1 = te.getMarketsData(marketsField='index')
print(type(data1))
# if ('Symbol' in data1[0] and 'Close' in data1[0]):
data1 = json.dumps(data1).encode('utf-8')
print(type(data1))
