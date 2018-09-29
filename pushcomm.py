#!/usr/bin/python3
# coding:utf8
import pymysql
import requests
import json
import logging
from datetime import datetime
import time
import os
import random
import threading
import redis

DEBUG = False
# 获取公众号token的接口
WX_TOKEN_URL = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={}&secret={}"
# 模板消息推送接口
WX_TEMPLATE_MSG_API = "https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={}"

# niuxiongbao
OLD_WX_APPID = "wxe031013412e9afdb"
OLD_WX_SECRET = "4f548e1c06f224f8b44cf805246e5f3b"

WX_APPID = "wx4a0bb2c0fd6d0277"
WX_SECRET = "96edcadda33d38ef3604174ad069f744"

# xiaomi push
MPUSH_APP_SECRET = 'xk9v4twXb82nqsJwini4zg=='
MPUSH_PACKAGE_NAME = 'com.lixun.gpxj'
# MPUSH_APP_SECRET = 'TnhfFD+XwAbeFjf28H9DUQ=='
# MPUSH_PACKAGE_NAME='com.mmxh.cgrj'
ApnsProduction = False

# ios 推送参数
if DEBUG:
    # 开发环境
    ApnsProduction = False
else:
    # 生产环境
    ApnsProduction = True

if DEBUG:
    db_host = "debug.gupiaoxianji.com"
    db_user = "wallace"
    db_password = "wallace@gpxj115566"
    db_database = "stock_app"
    db_port = 3309
    db_charset = "utf8mb4"
else:
    db_host = "10.116.46.52"
    db_user = "gpxj"
    db_password = "xianji"
    db_database = "stock_app"
    db_port = 3306
    db_charset = "utf8mb4"

# jpush验证参数
if DEBUG:
    # 股票先机测试
    app_key = "c796f59b2d2999808770a1e0"
    master_secret = "c297dfbd855eb9bf73a6a7d9"

    app_key_dxw = "bb7490aa2674642378eb3ff6"
    master_secret_dxw = "b3e1bb150dfa69d9daea94bc"

    app_key_bizhang = "54ab847e30a66fab4c3323e8"
    master_secret_bizhang = "9cc8e80bc09fb7e835a92697"
else:
    # 股票先机
    app_key = "fedf1913031c3fce71cd2a09"
    master_secret = "4b1b6464410ef8e75cbfbf20"

    app_key_dxw = "bb7490aa2674642378eb3ff6"
    master_secret_dxw = "b3e1bb150dfa69d9daea94bc"

    app_key_bizhang = "54ab847e30a66fab4c3323e8"
    master_secret_bizhang = "9cc8e80bc09fb7e835a92697"

conn = pymysql.Connect(host=db_host, user=db_user, password=db_password, database=db_database, port=db_port,
                       charset=db_charset, )
cur = conn.cursor()


def init_mysql():
    newconn = pymysql.Connect(host=db_host, user=db_user, password=db_password, database=db_database, port=db_port,
                              charset=db_charset, )
    newcur = newconn.cursor()
    return newconn, newcur


def init_mysql2(host=db_host, user=db_user, password=db_password, database=db_database, port=db_port,
                charset=db_charset):
    newconn = pymysql.Connect(host=host, user=user, password=password, database=database, port=port, charset=charset, )
    newcur = newconn.cursor()
    return newconn, newcur


def close_mysql():
    global conn
    global cur
    conn.close()
    cur.close()


def is_transday():
    try:
        nw = time.localtime()
        nwday = time.strftime("%Y%m%d", nw)
        querystr = "select day from t_transday where day={} ".format(nwday)
        cur.execute(querystr)
        conn.commit()
        day = cur.fetchone()

        if day == None:
            logging.info('today stock is not open,exit!!')
            return False

        if len(day) != 0:
            return True
        else:
            return False
    except  Exception as e:
        logging.exception(e)
        return False


def reconnect_mysql():
    global conn
    global cur
    conn = pymysql.Connect(host=db_host, user=db_user, password=db_password, database=db_database, port=db_port,
                           charset=db_charset, )
    cur = conn.cursor()


def get_token():
    try:
        # querystr = "select access_token,update_time,expire_date from t_weixin_access_token where appid='{}'".format(WX_APPID)
        querystr = "select access_token,update_time,expire_date from weixin.t_weixin_access_token where appid='{}'".format(
            WX_APPID)
        cur.execute(querystr)
        conn.commit()
        ret = cur.fetchone()
        if len(ret) == 0:
            return None

        access_token = str(ret[0])
        update_time = str(ret[1])
        expire_date = str(ret[2])
        logging.info(
            'get access_token from mysql:' + access_token + ',update_time=' + update_time + ',expire_date=' + expire_date)
        return access_token
    except  Exception as e:
        logging.exception(e)
        reconnect_mysql()
        access_token = get_token()
        return access_token


def get_token_old():
    try:
        querystr = "select access_token,update_time,expire_date from t_weixin_access_token where appid='{}'".format(
            OLD_WX_APPID)
        # querystr = "select access_token,update_time,expire_date from weixin.t_weixin_access_token where appid='{}'".format(WX_APPID)
        cur.execute(querystr)
        conn.commit()
        ret = cur.fetchone()
        if len(ret) == 0:
            return None

        access_token = str(ret[0])
        update_time = str(ret[1])
        expire_date = str(ret[2])
        logging.info(
            'get access_token old from mysql:' + access_token + ',update_time=' + update_time + ',expire_date=' + expire_date)
        return access_token
    except  Exception as e:
        logging.exception(e)
        reconnect_mysql()
        access_token = get_token_old()
        return access_token


def refresh_token():
    try:
        tokenurl = WX_TOKEN_URL.format(WX_APPID, WX_SECRET)
        r = requests.post(tokenurl)
        data = r.json()
        logging.info(json.dumps(data))
        token = ''
        if "access_token" in data:
            token = data["access_token"]
            logging.info("refresh token from wx:" + token)

            # write back to mysql
            # updatestr = "update t_weixin_access_token set access_token='{}',expire_date=now()+ interval 2 hour,update_time=now() where appid='{}'".format(token,WX_APPID)
            updatestr = "update weixin.t_weixin_access_token set access_token='{}',expire_date=now()+ interval 2 hour,update_time=now() where appid='{}'".format(
                token, WX_APPID)
            cur.execute(updatestr)
            conn.commit()
        return token
    except  Exception as e:
        logging.exception(e)
        return


def refresh_token_old():
    try:
        tokenurl = WX_TOKEN_URL.format(OLD_WX_APPID, OLD_WX_SECRET)
        r = requests.post(tokenurl)
        data = r.json()
        logging.info(json.dumps(data))
        token = ''
        if "access_token" in data:
            token = data["access_token"]
            logging.info("refresh token from old wx:" + token)

            # write back to mysql
            updatestr = "update t_weixin_access_token set access_token='{}',expire_date=now()+ interval 2 hour,update_time=now() where appid='{}'".format(
                token, OLD_WX_APPID)
            # updatestr = "update weixin.t_weixin_access_token set access_token='{}',expire_date=now()+ interval 2 hour,update_time=now() where appid='{}'".format(token,WX_APPID)
            cur.execute(updatestr)
            conn.commit()
        return token
    except  Exception as e:
        logging.exception(e)
        return


def send_weixin_msg(users, template_id, template_msg, jump_url=''):
    if len(users) == 0:
        logging.error("users is empty ")
        return

    token = get_token()
    if token == None or token == '':
        logging.info("token is none,try again!")
        token = get_token()
    wx_url = WX_TEMPLATE_MSG_API.format(token)
    count = 0
    for user in users:
        try:
            count = count + 1
            payload = {
                "touser": user["openid"],
                "template_id": template_id,
                "url": jump_url,
                "data": template_msg
            }
            r = requests.post(url=wx_url, json=payload, timeout=6)
            logging.info("count=" + str(count) + "," + str(user["userid"]) + "," + user["openid"] + "," + r.text)
            retdata = r.json()
            if "errcode" in retdata:
                if int(retdata["errcode"]) == 40001:
                    token2 = get_token()
                    if token2 == token:
                        token = refresh_token()
                        if token != '':
                            wx_url = WX_TEMPLATE_MSG_API.format(token)
                    else:
                        token = token2
        except Exception as e:
            logging.exception(e)
            logging.error("send wx error!")


# 旧微信
def send_weixin_msg_old(users, template_id, template_msg, jump_url=''):
    if len(users) == 0:
        logging.error("users is empty ")
        return

    token = get_token_old()
    if token == None or token == '':
        logging.info("token is none,try again!")
        token = get_token_old()
    wx_url = WX_TEMPLATE_MSG_API.format(token)
    count = 0
    for user in users:
        try:
            count = count + 1
            payload = {
                "touser": user["openid"],
                "template_id": template_id,
                "url": jump_url,
                "data": template_msg
            }
            r = requests.post(url=wx_url, json=payload, timeout=6)
            logging.info("count=" + str(count) + "," + str(user["userid"]) + "," + user["openid"] + "," + r.text)
            retdata = r.json()
            if "errcode" in retdata:
                if int(retdata["errcode"]) == 40001:
                    token2 = get_token_old()
                    if token2 == token:
                        token = refresh_token_old()
                        if token != '':
                            wx_url = WX_TEMPLATE_MSG_API.format(token)
                    else:
                        token = token2
        except Exception as e:
            logging.exception(e)
            logging.error("send wx error!")


def OneRunningOnly(name):
    cmd = "ps aux |grep " + str(name) + " |grep python|grep -v 'grep'|grep -v '\-c'"
    cmdmsg = os.popen(cmd).readlines()
    logging.info(cmdmsg)
    lines = len(cmdmsg)
    logging.info(str(name) + ' running num is num=' + str(lines))
    if lines > 1:
        logging.error(str(name) + ' running more than 1,exit!')
        exit(1)


def get_weixin_user(product_class):
    if product_class == "":
        return None
    try:
        # querystr = "select b.userid,b.openid from t_service a inner join t_weixin_gzh_push b on b.userid=a.userid where a.product_class='{}' and a.enable=1 and b.weixinid='gh_74fd31d83988' and a.end_date > now() group by b.openid".format(product_class)
        querystr = "select b.userid,b.openid from t_service a inner join weixin.t_weixin_gzh_push b on b.userid=a.userid where a.product_class='{}' and a.enable=1 and b.weixinid='gh_74fd31d83988' and a.end_date > now() group by b.openid".format(
            product_class)
        cur.execute(querystr)
        conn.commit()

        data = []
        for userid, openid in cur:
            tmp = {}
            tmp["userid"] = userid
            tmp["openid"] = openid
            data.append(tmp)

        return data
    except  Exception as e:
        logging.exception(e)
        return


def mpush_msg_to_topic(title, content, topic, extra=None):
    try:
        rand_notify_id = random.randint(1, 100000)
        post_data = {
            'restricted_MPUSH_PACKAGE_NAME': MPUSH_PACKAGE_NAME,
            'description': content,
            'title': title,
            'notify_type': -1,
            'notify_id': rand_notify_id,
            'payload': '消息的内容',
            'pass_through': 0,
            'topic': topic,
        }

        if extra != None and extra != '':
            extra_data = {'sound_uri': 'android.resource://com.lixun.gpxj/raw/cowboy'}
            for k in extra:
                post_data['extra.' + k] = extra[k]
            for k in extra_data:
                post_data['extra.' + k] = extra_data[k]

        headers = {'Authorization': 'key=' + MPUSH_APP_SECRET, 'Content-Type': 'application/json'}
        r = requests.request(method="POST", url='https://api.xmpush.xiaomi.com/v3/message/topic', params=post_data,
                             headers=headers, timeout=5)
        logging.info('mpush ret:' + str(r.status_code) + "----" + r.text)
    # print(r.text)
    except Exception as e:
        logging.exception(e)
        return


def getTimeDaySec():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


def getTimeDay():
    return time.strftime("%Y%m%d", time.localtime())


def getTimeSec():
    return time.strftime("%H:%M:%S", time.localtime())


def get_majia_list():
    data = []
    try:
        querystr = "select pushtype,pushkey,secret from stock_app.t_majia_pushkey where pushtype='jpush'"
        cur.execute(querystr)
        conn.commit()

        for pushtype, key, secret in cur:
            tmp = {}
            tmp["pushtype"] = pushtype
            tmp["key"] = key
            tmp["secret"] = secret
            data.append(tmp)

        return data
    except  Exception as e:
        logging.exception(e)
        return []


def pushMajia(pushMethod, pushstr):
    if pushstr == "" or pushstr == None:
        return
    majia_list = get_majia_list()
    for v in majia_list:
        pushMethod(pushstr, str(v['key']), str(v['secret']))


def pushMajiaByThread(pushMethod, pushstr):
    try:
        threads = []
        t1 = threading.Thread(target=pushMajia, args=(pushMethod, pushstr))
        t1.setDaemon(True)
        threads.append(t1)

        for t in threads:
            t.start()

        return threads

    except Exception as e:
        logging.exception(e)


def getStockRecommand(stockid):
    try:
        recommandstr = ''
        headers = {"Content-Type": "application/json"}
        r = requests.request(method="POST", url="http://10.26.220.23:4000/getString", data='idlist=' + stockid,
                             headers=headers, timeout=2)
        logging.info(str(r.status_code) + "----" + r.text)
        jdata = json.loads(r.text)
        if type(jdata) == type([]) and len(jdata) >= 1:
            jdata2 = json.loads(jdata[0])
            if type(jdata2) == type([]) and len(jdata2) >= 1:
                if 'full_description' in jdata2[0]:
                    return jdata2[0]['full_description']

        return recommandstr
    except Exception as e:
        logging.exception(e)
        return ''


def jpush_app_msg(msg, pclass, app_key, master_secret, extra=None):
    try:
        payload = {
            "platform": "all",
            "audience": {
                "tag": [pclass]
            },
            "notification": {
                "android": {
                    "alert": msg,
                    "extras": extra

                },
                "ios": {
                    "alert": msg,
                    "sound": "default",
                    "badge": "+1",
                    "extras": extra
                }
            },
            "options": {
                "apns_production": ApnsProduction
            }
        }

        headers = {"Content-Type": "application/json"}
        r = requests.request(method="POST", url="https://api.jpush.cn/v3/push", json=payload, headers=headers,
                             auth=(app_key, master_secret))
        logging.info(str(r.status_code) + "----" + r.text + ",key=" + app_key + ",secret=" + master_secret)
    except Exception as e:
        logging.exception(e)
        return


# jpush2user(pushstr,users,pushcomm.app_key,pushcomm.master_secret,{'type':4,'title':'股票先机','content': pushstr,'linkUrl':jumpUrl})
def jpush2user(msg, users, app_key, master_secret, extra={}):
    try:
        payload = {
            "platform": "all",
            "audience": {
                "alias": users
            },
            "notification": {
                "android": {
                    "alert": msg,
                    "extras": extra

                },
                "ios": {
                    "alert": msg,
                    "sound": "cowboy.wav",
                    "badge": "+1",
                    "extras": extra
                }
            },
            "options": {
                "apns_production": True
                # "apns_production": False
            }
        }

        headers = {"Content-Type": "application/json"}
        r = requests.request(method="POST", url="https://api.jpush.cn/v3/push", json=payload, headers=headers,
                             auth=(app_key, master_secret))
        logging.info(str(r.status_code) + "----" + r.text + ",key=" + app_key + ",secret=" + master_secret)
    except Exception as e:
        logging.exception(e)
        return


# mpush2user('股票先机',pushstr,users,{'type':9,'linkUrl':jumpUrl,'content':pushstr,'title':'股票先机'})
def mpush2user(title, content, users, extra=None):
    try:
        rand_notify_id = random.randint(1, 100000)
        post_data = {
            'restricted_MPUSH_PACKAGE_NAME': MPUSH_PACKAGE_NAME,
            'description': content,
            'title': title,
            'notify_type': -1,
            'notify_id': rand_notify_id,
            'payload': '消息的内容',
            'pass_through': 0,
            'alias': users
        }

        if extra != None and extra != '':
            extra_data = {'sound_uri': 'android.resource://com.lixun.gpxj/raw/cowboy'}
            for k in extra:
                post_data['extra.' + k] = extra[k]
            for k in extra_data:
                post_data['extra.' + k] = extra_data[k]

        headers = {'Authorization': 'key=' + MPUSH_APP_SECRET, 'Content-Type': 'application/json'}
        r = requests.request(method="POST", url='https://api.xmpush.xiaomi.com/v3/message/alias', params=post_data,
                             headers=headers, timeout=10)
        logging.info('mpush ret:' + str(r.status_code) + "----" + r.text)
    except Exception as e:
        logging.exception(e)
        return


def sendSmsByMengWang(phone, msgcontent):
    try:
        url = "http://61.145.229.29:8895/MWGate/wmgw.asmx/MongateSendSubmit?userId=HE0315&password=988172&pszMobis=" + str(
            phone) + "&pszMsg=" + msgcontent + "&iMobiCount=1&pszSubPort=*"
        r = requests.request(method="GET", url=url, timeout=5)
        logging.info("phone=," + str(phone) + "," + str(r.status_code) + "----" + r.text)
    except Exception as e:
        logging.exception(e)


def sendGroupSmsByMengWang(users, msgcontent):
    logging.info('in send sms')
    i = 0
    phonelist = ''
    for v in users:
        i = i + 1
        phonelist = phonelist + str(v) + ','
        if i >= 50:
            # print('total='+str(i)+'   '+phonelist[0:len(phonelist)-1])
            try:
                url = "http://61.145.229.29:8895/MWGate/wmgw.asmx/MongateSendSubmit?userId=HE0315&password=988172&pszMobis=" + phonelist[
                                                                                                                               0:len(
                                                                                                                                   phonelist) - 1] + "&pszMsg=" + msgcontent + "&iMobiCount=" + str(
                    i) + "&pszSubPort=*"
                r = requests.request(method="GET", url=url, timeout=5)
                logging.info('url=' + url + ',resp=' + str(r.status_code) + "----" + r.text)
            except Exception as e:
                logging.exception(e)

            phonelist = ''
            i = 0

    if phonelist != '':
        try:
            url = "http://61.145.229.29:8895/MWGate/wmgw.asmx/MongateSendSubmit?userId=HE0315&password=988172&pszMobis=" + phonelist[
                                                                                                                           0:len(
                                                                                                                               phonelist) - 1] + "&pszMsg=" + msgcontent + "&iMobiCount=" + str(
                i) + "&pszSubPort=*"
            r = requests.request(method="GET", url=url, timeout=5)
            logging.info('url=' + url + ',resp=' + str(r.status_code) + "----" + r.text)
        except Exception as e:
            logging.exception(e)


def jpush2topic(app_key, master_secret, title, content, topic, extra=None):
    try:
        payload = {
            "platform": "all",
            "audience": {
                "tag": [topic]
            },
            "notification": {
                "android": {
                    "alert": content,
                    "extras": extra
                },
                "ios": {
                    "alert": content,
                    "sound": "cowboy.wav",
                    "badge": "+1",
                    "extras": extra
                }
            },
            "options": {
                "apns_production": ApnsProduction
            }
        }

        headers = {"Content-Type": "application/json"}
        r = requests.request(method="POST", url="https://api.jpush.cn/v3/push", json=payload, headers=headers,
                             auth=(app_key, master_secret))
        logging.info(str(r.status_code) + "----" + r.text + ",key=" + app_key + ",secret=" + master_secret)
    except Exception as e:
        logging.exception(e)
        return


def mpush2topic(package_name, secret, title, content, topic, extra=None):
    try:
        rand_notify_id = random.randint(1, 100000)

        post_data = {
            'restricted_MPUSH_PACKAGE_NAME': package_name,
            'description': content,
            'title': title,
            'notify_type': -1,
            'notify_id': rand_notify_id,
            'payload': '消息的内容',
            'pass_through': 0,
            'topic': topic,
        }

        if extra != None and extra != '':
            extra_data = {'sound_uri': 'android.resource://com.lixun.gpxj/raw/cowboy'}
            for k in extra:
                post_data['extra.' + k] = extra[k]
            for k in extra_data:
                post_data['extra.' + k] = extra_data[k]

        headers = {'Authorization': 'key=' + secret, 'Content-Type': 'application/json'}
        r = requests.request(method="POST", url='https://api.xmpush.xiaomi.com/v3/message/topic', params=post_data,
                             headers=headers, timeout=5)
        logging.info('mpush ret:' + str(r.status_code) + "----" + r.text)
    except Exception as e:
        logging.exception(e)
        return


def getMajiaList(tpush):
    data = []
    try:
        querystr = "select pushtype,pushkey,secret from stock_app.t_majia_pushkey where pushtype='" + tpush + "'"
        cur.execute(querystr)
        conn.commit()

        for pushtype, key, secret in cur:
            tmp = {}
            tmp["pushtype"] = pushtype
            tmp["key"] = key
            tmp["secret"] = secret
            data.append(tmp)

        return data
    except  Exception as e:
        logging.exception(e)
        return []


# jpush and mpush extra may not the same,so arg has to send tpush =jpush or mpush
def push2majia(tpush, title, content, topic, extra=None):
    majialist = getMajiaList(tpush)
    for v in majialist:
        key = v['key']
        secret = v['secret']
        pushtype = v['pushtype']
        if pushtype == 'jpush':
            jpush2topic(key, secret, title, content, topic, extra)
        elif pushtype == 'mpush':
            mpush2topic(key, secret, title, content, topic, extra)
    return


if __name__ == '__main__':
    print('hello')
# mpush2topic('com.zrgc.sbcg','TxMwyVMJiJG+4cBHB09gyg==','hello','xx','weipan',{"type": 15})
