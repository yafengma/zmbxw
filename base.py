# -*- coding=utf-8 -*-
import re
import redis
import requests
import time
import json
import random
from urllib.parse import urljoin
from lxml import etree
from pymongo import MongoClient
from urllib.parse import unquote, quote
from bson.errors import InvalidDocument
from settings import MONGO_URL, MONGO_DB


class Tools(object):
    def __init__(self):
        self.redis = redis.from_url("localhost")

    @staticmethod
    def urljoin(base, uri):
        return urljoin(base, uri)

    @staticmethod
    def json_dumps(data):
        return json.dumps(data, ensure_ascii=False)

    @staticmethod
    def json_loads(data):
        return json.loads(data)

    @staticmethod
    def get_filter(text):
        if isinstance(text, list):
            text = ''.join(text)
        text = text.strip()
        filter_list = [
            '\r', '\n', '\t', '\u3000', '\xa0', '\u2002',
            '<br>', '<br/>', '    ', '	', '&nbsp;', '>>', '&quot;',
            '展开全部'
        ]
        for fl in filter_list:
            text = text.replace(fl, '')
        return text

    @staticmethod
    def save(db, data, _type):
        _id = db.insert_one(data)
        try:
            print(_type, data['title'], '---存储成功')
        except KeyError:
            print(_type, _id.inserted_id, '-存储成功')

    def decode(self, content):
        chars = content[:min([3000, len(content)])].decode(errors='ignore')
        charset = self.rm('charset="?([-a-zA-Z0-9]+)', chars)
        if charset == '':
            charset = 'utf-8'
        return content.decode(charset, errors='replace')

    @staticmethod
    def rm(patt, sr):
        mat = re.search(patt, sr, re.DOTALL | re.MULTILINE)
        return mat.group(1) if mat else ''

    @staticmethod
    def read_file(path, encoding='utf-8'):
        with open(path, encoding=encoding) as f:
            result = f.read()
        return result

    def get_etree(self, text):
        try:
            return etree.HTML(text)
        except ValueError as e:
            self.robot_msg(str(e))

    @staticmethod
    def get_unquote(text, encoding='utf-8'):  # url 解码
        return unquote(text, encoding=encoding)

    @staticmethod
    def get_quote(text):  # url编码
        return quote(text)

    @staticmethod
    def re_patt(patt, text):
        return re.findall(patt, text)

    @staticmethod
    def time_strip(now=''):  # 默认当前时间戳
        """
        :param now: 必须是时间戳, 长度可以为10+
        :return: 时间戳或者时间日期
        """
        if now:
            if isinstance(now, int):
                now = str(now)
            if len(now) >= 10:
                now = now[:10]
            else:
                raise now + ' 请检查参数'
            t = time.localtime(int(now))
            return '{}-{}-{} {}:{}:{}'.format(t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec)
        else:
            return str(int(time.time())) + str(random.randint(100, 999))

    @staticmethod
    def get_db(name):
        client = MongoClient(MONGO_URL)
        return client[MONGO_DB][name]

    @staticmethod
    def get_url(base_url, uri):
        if isinstance(uri, list):
            return urljoin(base_url, uri[0])
        return urljoin(base_url, uri)

    @staticmethod
    def get_headers():
        headers = {
            "User-Agent": random.choice(
                ["Mozilla/5.0 (Windows NT 6.1; WOW64; rv:59.0) Gecko/20100101 Firefox/59.0",
                 "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:60.0) Gecko/20100101 Firefox/60.0",
                 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36']
            )
        }
        return headers

    @staticmethod
    def robot_msg(msg):  # 通过机器人发送错误信息
        print('调用机器人')
        data = {"msgtype": "text", "text": {"content": str(msg)}}
        r = requests.post(ROBOT_URL, json=data)
        print(r.text)

    def get_text(self, url, headers=None, method="get", refer=None, encoding=None, **kwargs):
        if not headers:
            headers = self.get_headers()
        func = getattr(requests, method)
        if refer:
            headers['Referer'] = refer
        while True:
            try:
                r = func(url, headers=headers, timeout=5, **kwargs)  # , kwargs.get('ip', None)}
                if r.status_code == 200:
                    t = '���'
                    if encoding:
                        r.encoding = encoding
                        return r.text
                    else:
                        if t in self.decode(r.content):
                            r.encoding = 'utf-8'
                            if t in r.text:
                                r.encoding = 'GBK'
                            return r.text
                        else:
                            return self.decode(r.content)
                elif r.status_code in [301, 302]:
                    print(r.text)
                    return "ERROR 302 !!"
                else:
                    return "ERROR"
            except requests.exceptions.ConnectionError:
                return 'requests ConnectionError'
                # '连接超时----更换ip1----'
            except requests.exceptions.ReadTimeout:
                return '等待读取超时----更换ip2----'
            except requests.exceptions.MissingSchema:
                return "url错误, %s" % url
            except UnicodeEncodeError:
                return "编码错误---{}".format(url)
            except requests.exceptions.InvalidHeader:
                return "refer错误---url:{}--refer:{}".format(url, refer)
            # except LocationParseError as e:
            #     if '设置为白名单' in str(e):
            #         write_ip = str(e).split('请将', 1)[1].split('设置为白名单', 1)[0]
            #         write_requests = requests.get(
            #             url=IP_PROXY_URL + write_ip)
            #         if write_requests.status_code == 200:
            #             self.robot_msg(write_ip + '白名单添加成功')
            #     else:
            #         self.robot_msg(str(e))
            #         time.sleep(60 * 15)
            #     return '配置错误?'
            except:
                time.sleep(8)
                print('----其他错误----')
                raise
