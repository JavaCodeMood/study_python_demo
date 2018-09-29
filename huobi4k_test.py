#!/usr/bin/python3
# coding:utf-8

import requests




# url= https://www.hbg.com/-/x/quotation/market/history/kline?r=u3sg5zj1yaj&limit=1&symbol=huobi10&period=4hour
paylod = {"r": "u3sg5zj1yaj", "limit": "2000", "symbol": "huobi10", "period": "4hour"}
r = requests.get("https://www.hbg.com/-/x/quotation/market/history/kline", params=paylod)
print(r.url)
# print(r.content)
print(r.json())

res = r.json()
json = res['data']


print(json)
print(len(json))
for i in json :
    print(i,"\n")
    for k,v in i.items() :
        print(k,"->",v)

# data = res['data'][0]['amount']
# print(data)


