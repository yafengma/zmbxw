from apscheduler.schedulers.blocking import BlockingScheduler
from threading import Thread
from datetime import datetime
import redis
import requests
import random
import json
import sys

rd = redis.from_url('localhost')


class IPPool(object):
    proxy_api = "http://http.tiqu.alicdns.com/getip3?num={}&type=1&pro=&city=0&yys=0&port=11&pack=14529&ts=0&ys=0&cs=0&lb=1&sb=0&pb=5&mr=1&regions="

    def __init__(self):
        self.pool = []
        self._ip_name = 'ip_pool'
        self.update_pool()
        self._thread()

    def get_http(self):
        # while True:
        r = requests.get(url=self.proxy_api.format(sys.argv[-1]), headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'})
        text = r.content.decode()
        return text

    def update_pool(self):
        ips = self.get_http()
        print('----', ips)
        lst = ips.strip().split("\r\n")
        rd.set(self._ip_name, json.dumps(lst))
        print('update_pool ', datetime.now().strftime("%Y-%m-%d %H-%M-%S"), len(lst))

    def _thread(self):
        t = Thread(target=self._scheduler)
        t.start()

    def _scheduler(self):
        scheduler = BlockingScheduler()
        scheduler.add_job(self.update_pool, 'interval', minutes=int(sys.argv[-2]))
        scheduler.start()

    @property
    def ip(self):
        return random.choice(self.pool)


def get_ip():
    t = rd.get('ip_pool')
    _ip = random.choice(json.loads(t.decode()))
    return _ip


if __name__ == "__main__":
    _pool = IPPool()
