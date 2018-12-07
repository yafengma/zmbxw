MONGO_URL = 'localhost:27017'
MONGO_DB = '中民保险网'
ROBOT_URL = ''

意外 = {
    "综合意外": "/product/accid/list/is1_st9_acHPPLNG.html",
    "意外医疗": "/product/accid/list/is1_hs514_acHPPLNG.html",
    "少儿意外": "/product/accid/list/is1_sc13_acHPPLNG.html",
    "成人意外": "/product/accid/list/is1_sc14_acHPPLNG.html",
    "老年意外": "/product/accid/list/is1_sc15_acHPPLNG.html",
    "航空意外": "/product/accid/list/is1_hs522_acHPPLNG.html"
}
健康 = {
    "百万医疗": "/product/health/list/is1_hs560_acHPPLNG.html",
    "重大疾病": "/product/health/list/is1_st11_acHPPLNG.html",
    "保费豁免": "/product/health/list/is1_hs554_acHPPLNG.html",
    "少儿健康": "/product/health/list/is1_sc42%3A18%3A1_acHPPLNG.html",
    "成人健康": "/product/health/list/is1_sc43%3A60%3A1_acHPPLNG.html",
    "老年健康": "/product/health/list/is1_sc44%3A90%3A1_acHPPLNG.html"
}
人寿 = {
    "定期寿险": "/product/life/list/is1_st37_acHPPLNG.html",
    "终身寿险": "/product/life/list/is1_st38_acHPPLNG.html",
    "理财储蓄": "/product/annuity/list/is1_acHPPLNG_acHPPLNG.html"
}
HD = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36',
    "Cookie": '__jsluid=efcae4e221ec661aa2d3c4fd29f77cd5; Hm_lvt_d7682ab43891c68a00de46e9ce5b76aa=1542350078; areaCodeOut=%22PROPCSY%22; cookieUserName=cookied227cf6308af27467a8e793fd8a8f5f6; Hm_lvt_9634323798be51b19359016bdfd65b32=1544065391; LXB_REFER=sp0.baidu.com; areaCode=%22HPPLNG%22; browseInfo=%5B%7B%22url%22%3A%22https%3A//www.zhongmin.cn/travel/detail/ip9018_is1.html%22%2C%22productImg%22%3A%22//images.zhongmin.cn/images/2018/320/9018.jpg%22%2C%22productName%22%3A%22%u5B89%u8054%u5883%u5916%u957F%u9014%u65C5%u884C%u4FDD%u969C%u8BA1%u5212%uFF082017%uFF09%22%2C%22price%22%3A%2260%22%2C%22pid%22%3A%229018%22%7D%2C%7B%22url%22%3A%22https%3A//www.zhongmin.cn/accid/detail/ip11486_is1.html%22%2C%22productImg%22%3A%22//images.zhongmin.cn/images/2018/320/11486.jpg%22%2C%22productName%22%3A%22%u4EBA%u4FDD%u767E%u4E07%u7EFC%u5408%u610F%u5916%u4FDD%u969C%u8BA1%u5212%uFF08%u7ECF%u5178%u6B3E%uFF09%22%2C%22price%22%3A%22165%22%2C%22pid%22%3A%2211486%22%7D%2C%7B%22url%22%3A%22https%3A//www.zhongmin.cn/accid/detail/ip10962_is1.html%22%2C%22productImg%22%3A%22//images.zhongmin.cn/images/2018/320/10962.jpg%22%2C%22productName%22%3A%22%u6CF0%u5EB7%u5728%u7EBF%u4F4F%u9662%u5B9D2018%u5FC5%u5907%u7248%uFF0818-49%u5468%u5C81%uFF09%22%2C%22price%22%3A%22249%22%2C%22pid%22%3A%2210962%22%7D%5D; JSESSIONID=E40716BDD527460F9A90F012119C1D67; Hm_lpvt_9634323798be51b19359016bdfd65b32=1544148230',
    'Pragma': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
}

KEY = {
    '适合人群': 'peopleFit',
    '保障计划': 'zmProductArrList',
    '承保职业': 'jobRiskBelong',
    '投保年龄': 'ageBelong',
}
条款 = 'https://www.zhongmin.cn/product/clause/getClause?pid={}&sid=1'
费率表 = {
    '人寿': 'https://baodan.zhongmin.cn/rate2018/regular/regular_{}_5.pdf',
    '意外': 'https://baodan.zhongmin.cn/rate2018/accid/accid_{}_5.pdf',
    '健康': 'https://baodan.zhongmin.cn/rate2018/health/health_{}_5.pdf',
}

URL = {
    '意外': ['post', 'https://www.zhongmin.cn/accid/getDetailsInfo'],
    '健康': ['get', 'https://www.zhongmin.cn/product/health/getHealthProDetail?pid={}&sid=1'],
    '人寿': ['get', 'https://www.zhongmin.cn/product/life/getLifeProDetail?pid={}&sid=1']
}
