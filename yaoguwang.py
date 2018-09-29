#!/usr/bin/python3
# coding:utf-8

import logging
import sys

sys.path.append('../pushcomm')
import pushcomm
import redis_comm
import requests
import threadpool
import time

file_name = 'yaoguwang_push'
logging.basicConfig(filename=file_name + ".log", level=logging.INFO,
                    format='%(asctime)-15s:%(levelname)s:%(filename)s:%(lineno)s:%(funcName)s:%(message)s')

# 模板消息推送接口
WX_TEMPLATE_MSG_API = "https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={}"
# 消息模板
WX_TEMPLATE_MSG = "-rCw1uIdOaj44cGbFGqm5tw00ipTADPoJVChmBa8JCU"
TEMPLATE_MSG = ""

# 使用新微信 先机客户服务
WX_APPID = "wx4a0bb2c0fd6d0277"
WX_SECRET = "96edcadda33d38ef3604174ad069f744"
TOKEN = ''
# new weixin
REDIS_YAOGUWANG_KEY = 'newweixinpush_token'

conn, cur = pushcomm.init_mysql()


def get_yaoguwang_stock():
    try:
        querystr = '''
        SELECT a.stockid, b.stockname
        FROM stock_app.t_recommand a 
        LEFT JOIN stock_app.t_stock_base b ON a.stockid = b.stockid 
        WHERE a.enable = 1 
        AND DATE(a.recommand_time) = (SELECT MAX(DATE(recommand_time)) FROM stock_app.t_recommand)'''
        affected_rows = cur.execute(querystr)
        conn.commit()

        logging.info("affected_rows=" + str(affected_rows))
        data = []
        for stockid, stockname in cur:
            tmp = {}   #创建一个空字典
            tmp["stockid"] = stockid        #股票代码
            tmp["stockname"] = stockname    #股票名字（证券简称）
            data.append(tmp)   #添加数据到字典中
        logging.info(data)
        return data

    except  Exception as e:
        logging.exception(e)
        return


def convert_data_to_str(data, sep):
    pushstr = ""
    for v in data:
        pushstr = pushstr + v["stockname"] + "(" + v["stockid"][0:6] + ")" + sep
    pushstr = pushstr[0:len(pushstr) - 1]

    return pushstr


def get_weixin_user():
    try:
        querystr = "SELECT b.openid FROM stock_app.t_service a INNER JOIN weixin.t_weixin_gzh_push b ON b.userid=a.userid WHERE a.product_class='banker_stock' AND a.enable=1 AND b.weixinid='gh_74fd31d83988' GROUP BY b.openid"
        cur.execute(querystr)
        conn.commit()

        data = []
        for openid in cur:
            data.append(openid[0])

        return data
    except  Exception as e:
        logging.exception(e)
        return


def get_wx_template(data):
    t = time.localtime()
    now = time.strftime("%Y-%m-%d %H:%M:%S", t)
    wx_template = {
        "first": {
            "value": "【妖股王】大数据检测到下列个股有妖股潜质，建议保持关注",
            "color": "#173177"
        },
        "keyword1": {
            "value": "{}".format(data),
            "color": "#173177"
        },
        "keyword2": {
            "value": "{}".format(now),
            "color": "#173177"
        },
        "remark": {
            "value": "大数据量化选股，请谨慎参考，更多信息请至股票先机APP查看>",
            "color": "#173177"
        }
    }

    return wx_template


def action(users):
    send_weixin_msg(users, WX_TEMPLATE_MSG, TEMPLATE_MSG, "http://t.cn/RGBQsBV")


def send_weixin_msg(users, template_id, template_msg,
                    jump_url='http://a.app.qq.com/o/simple.jsp?pkgname=com.lixun.gpxj', i=0):
    tmp_int = i
    global TOKEN
    wx_url = WX_TEMPLATE_MSG_API.format(TOKEN)
    try:
        payload = {
            "touser": users,
            "template_id": template_id,
            "url": jump_url,
            "data": template_msg
        }
        r = requests.post(url=wx_url, json=payload, timeout=6)
        logging.info(str(users) + "," + users + "," + r.text)
        retdata = r.json()
        if "errcode" in retdata:
            if int(retdata["errcode"]) == 40001:
                TOKEN = redis_comm.get_key(REDIS_YAOGUWANG_KEY)
                wx_url = WX_TEMPLATE_MSG_API.format(TOKEN)
                if tmp_int <= 3:
                    tmp_int = tmp_int + 1
                    send_weixin_msg(users, template_id, template_msg, jump_url, tmp_int)
    except Exception as e:
        logging.exception(e)
        logging.error("send wx error!")


if __name__ == '__main__':
    logging.info('妖股王推送 start ' + file_name)
    # step1 progamme run only 1
    pushcomm.OneRunningOnly(__file__)

    t = time.localtime()
    now_date = time.strftime("%Y-%m-%d", t)
    if str(now_date) < "2018-08-13":
        logging.error('no in push date:' + str(now_date))
        exit(1)

    # step2 if day right
    if pushcomm.is_transday() == False:
        logging.error('today is not transday,exit!')
        exit(1)

    time_start = time.time()

    data = get_yaoguwang_stock()
    push_data = convert_data_to_str(data, "、")

    TEMPLATE_MSG = get_wx_template(push_data)

    if len(data) > 0:
        #App
        push_str = "妖股王：今日大数据发现{}符合妖股潜质，建议您保持关注>>".format(push_data)
        # userids = "13766406820,13145844655,18659279519"
        # userid_arr = ['18659279519','13766406820','13145844655']
        # jumpUrl = "gpxj://banker_stock"
        # iOS推送
        # pushcomm.jpush2user(push_str, userid_arr, pushcomm.app_key, pushcomm.master_secret,{'type':4,'title':'股票先机','content': push_str,'linkUrl':jumpUrl})
        pushcomm.jpush2topic(pushcomm.app_key, pushcomm.master_secret, "股票先机", push_str, "banker_stock",
                             {'type': 4, 'linkUrl': 'gpxj://banker_stock'})

        # Android推送
        # pushcomm.mpush2user('股票先机',push_str,userids,{'type':4,'linkUrl':jumpUrl,'content':push_str,'title':'股票先机'})
        pushcomm.mpush_msg_to_topic("股票先机", push_str, "banker_stock", {'type': 4, 'linkUrl': 'gpxj://banker_stock'})

        # 推送微信消息
        users = get_weixin_user()
        # users = ['oa-Zf0Q6IQv-wtInhB9nWuVJvXV8','oa-Zf0f2jnyr8Fj4Be71Hj49DxxM','oa-Zf0Uyxuuht4UjDBM698voBS7E']
        TOKEN = pushcomm.get_token()

        pool = threadpool.ThreadPool(20)
        allrequests = threadpool.makeRequests(action, users)
        [pool.putRequest(req) for req in allrequests]
        pool.wait()

    time_end = time.time()
    logging.info("本次推送耗时：{}".format(time_end - time_start))
    pushcomm.close_mysql()
    cur.close()
    conn.close()
    logging.info('end ' + file_name)
