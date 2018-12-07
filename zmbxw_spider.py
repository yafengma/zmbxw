from base import Tools
from settings import *


class Spider(Tools):
    def __init__(self, name):
        super(Spider, self).__init__()
        self.name = name
        self.data = URL[name]
        self.tk = self.get_db('条款')
        self.flb = self.get_db('费率表')
        self.product = self.get_db('产品')
        self.base_url = 'https://www.zhongmin.cn'

    def all_page_html(self, index_url):
        if 'is1_' in index_url:
            uri = index_url.split('is1_')
            page = 1
            while 1:
                url = uri[0] + 'is1_po' + str(page) + '_sr1_' + uri[-1]
                page += 1
                html = self.get_text(url, headers=HD, refer=self.base_url)
                if '没有找到您想要的产品，换个条件试试' not in html:
                    yield html
                else:
                    return None
        else:
            print('is1_不在url中')
            return None

    def mongo_save(self, pid, data):
        print(data)
        if self.tk.find_one({"pid": pid}):
            print(pid, '条款---已存在')
        else:
            self.tk.insert_one({"pid": pid, 'url': 条款.format(pid)})
            print(pid, '---存储成功')

        if self.flb.find_one({"pid": pid}):
            print(pid, '费率表---已存在')
        else:
            self.flb.insert_one({"pid": pid, 'url': 费率表[self.name].format(pid)})
            print(pid, '---存储成功')

        if self.product.find_one({"pid": pid}):
            print(pid, '费率表---已存在')
        else:
            self.product.insert_one(data)

    def parse_pro(self, pid, refer, kw):
        headers = {
            'DNT': '1', 'Origin': 'https://www.zhongmin.cn', 'Pragma': 'no-cache', 'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36',
            'Connection': 'keep-alive'
        }
        data = {'uid': '', 'pid': pid, 'sid': '1', 'mark': '0'}
        text = self.get_text(url=self.data[1].format(pid), headers=headers, method=self.data[0], refer=refer, data=data)
        json_obj = self.json_loads(text)
        if json_obj['code'] != 200:
            print('------------', json_obj)
            return
        print(self.data[1].format(pid))
        print(json_obj)
        return
        # self.mongo_save(pid, kw)

    def pro(self, kw):
        html = kw.pop('html')
        et = self.get_etree(html)
        ps = et.xpath("//p[@class='pro-title']")
        for p in ps:
            kw['产品名'] = p.xpath("@title")[0]  # 产品名
            pid = p.xpath("a/@relid")[0]  # 产品id
            kw['pid'] = pid
            pro_url = p.xpath("a/@href")[0]  # 产品url
            url = self.urljoin(self.base_url, pro_url)
            kw.update({"url": url})
            self.parse_pro(pid, url, kw.copy())

    def run(self, name):
        for key, value in name.items():
            html_gen = self.all_page_html(self.urljoin(self.base_url, value))
            for html in html_gen:
                self.pro({'一级': self.name, '二级': key, 'html': html})


if __name__ == '__main__':

    s = Spider('人寿')
    s.run(人寿)
