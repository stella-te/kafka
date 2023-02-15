import tradingeconomics as te
import redis
import time
import json
import datetime

te.login('3aecf53b46e647f:dqfs4pyvdzdxo5y')

host = 'localhost'
password = 'university'
port = 6379


r = redis.Redis(host=host, password=password, port=port)
print('connected')

def save_redis_cache():
    try:
        # data = te.getMarketsData(marketsField='index')
        data = te.getMarketsBySymbol(symbols='tsla:us')
        if data[0]['Close']:
            data = json.dumps(data).encode('utf-8')
            r.set('tsla ', data)
            print(f'Saving cache on redis @ {datetime.now()} | Message = {str(data)}' )
    except:
        print('redis error')

# save_redis_cache()

if __name__ == '__main__':
    while True:
        save_redis_cache()
        12*60*60
        time.sleep(43200)


# end
