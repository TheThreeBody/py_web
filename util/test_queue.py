import redis
import sys

pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)

if __name__ == '__main__':
    print(pool)