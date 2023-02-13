import tradingeconomics as te
import redis
import time
import json
from datetime import datetime

te.login('3aecf53b46e647f:dqfs4pyvdzdxo5y')

host = 'localhost'
password = 'university'
port = 6379


def save_redis_cache():
    try:
        data = te.getMarketsData(marketsField='commodities')
        data = json.dumps(data).encode('utf-8')

        # localhost:6379 (the default)
        # r = redis.Redis()
        # r.ping()
        r = redis.Redis(host=host, password=password, port=port)
        r.set('Commodities', data)
        print(f'Saving cache on redis @ {datetime.now()} | Message = {str(data)}' )
    except:
        print('redis error')

if __name__ == '__main__':
    while True:
        save_redis_cache()
        # 12*60*60
        time.sleep(43200)


# end
