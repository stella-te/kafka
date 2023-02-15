import redis



# localhost:6379 (the default)
r = redis.Redis()
r.ping()
print(r)
