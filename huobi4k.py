#!/usr/bin/python3
# coding:utf-8

import requests
import pymysql
import time

# 打开数据库连接
db = pymysql.connect("localhost", "root", "root", "huobi")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# url= https://www.hbg.com/-/x/quotation/market/history/kline?r=u3sg5zj1yaj&limit=1&symbol=huobi10&period=4hour
paylod = {"r": "u3sg5zj1yaj", "limit": "2000", "symbol": "huobi10", "period": "4hour"}
r = requests.get("https://www.hbg.com/-/x/quotation/market/history/kline", params=paylod)
print(r.url)
# print(r.content)
print(r.json())

res = r.json()
json = res['data']

"""
print(json)
print(len(json))
for i in json :
    print(i,"\n")
    for k,v in i.items() :
        print(k,"->",v)
"""

#data = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
for i in json:
    print('---->>>',i)
    print(i['open'])
    # sql插入语句
    sql = """ INSERT INTO t_4h_k_line_huobi
       values({},{},{},{},{},{},{},"huobi")""".format(i['id'], i['amount'], i['open'],
                   i['high'],i['low'], i['close'], i['vol'])

    # 执行sql语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()

db.close()


# data = res['data'][0]['amount']
# print(data)

"""
DROP TABLE IF EXISTS `t_4h_k_line_huobi`;
CREATE TABLE `t_4h_k_line_huobi` (
  `id` varchar(20) NOT NULL COMMENT 'id',
  `amount` double NOT NULL COMMENT '交易金额',
  `open` double DEFAULT NULL COMMENT '开盘价',
  `high` double DEFAULT NULL COMMENT '最高价',
  `low` double DEFAULT NULL COMMENT '最低价',
  `close` double DEFAULT NULL COMMENT '收盘价',
  `vol` double DEFAULT NULL COMMENT '成交量',
  `exchange` varchar(40) NOT NULL COMMENT '交易所名字',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='4小时行情';
"""

