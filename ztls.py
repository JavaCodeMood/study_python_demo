#!/usr/bin/python3
# coding:utf-8
import pymysql
import requests
import json
import logging
from datetime import datetime
import time
import os
import sys
sys.path.append('../pushcomm')
import pushcomm
import threading
import threadpool  
import redis_comm
import test
import vipMsg

# 模板消息的模板ID
#WX_TEMPLATE_MSG_CHAO_DI = "mfg0SV-nkGdZXHscEOHYAOGi_zuB0tyqFXAIfuSORxQ"
# new weixin
WX_TEMPLATE_MSG_CHAO_DI = "FkvfxF62-PYn4YD1V_JcTjNOS-GMkDmZ0eieolgsinY"
# 不推荐时的模版
#WX_TEMPLATE_MSG_NO_WEIPAN_ID = "dRxlchs9ivCW_W38FTcoXXS9J-lb4PM6rpsu-QzdgHA"
# new weixin
WX_TEMPLATE_MSG_NO_WEIPAN_ID = "_nInpqSRq8IVzZUyg9V6oDCKoErfwLcWV2BVuZiH49w"

TEMPLATE_MSG = ""
file_name='ztls'
logging.basicConfig(filename=file_name+".log", level=logging.INFO,format='%(asctime)-15s:%(levelname)s:%(filename)s:%(lineno)s:%(funcName)s:%(message)s')
TOKEN=""
# 模板消息推送接口
WX_TEMPLATE_MSG_API = "https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={}"
# niuxiongbao
#WX_APPID = "wxe031013412e9afdb"
#WX_SECRET = "4f548e1c06f224f8b44cf805246e5f3b"

# new weixin
WX_APPID = "wx4a0bb2c0fd6d0277"
WX_SECRET = "96edcadda33d38ef3604174ad069f744"

#REDIS_AIXUANGU_KEY = 'weixinpush_token'

# newweixin
REDIS_AIXUANGU_KEY = 'newweixinpush_token'

blacklist = ['18682052542']
conn,cur = pushcomm.init_mysql()

conn_redbull = pymysql.Connect(host='10.29.70.251', user='gpxj', password='xianji', database='stock_app', port=3306,charset='utf8mb4', )
cur_redbull = conn_redbull.cursor()

def get_weixin_user():
    try:
        #querystr = "select b.openid from t_service a inner join t_weixin_gzh_push b on b.userid=a.userid where a.product_class='ztls' and a.enable=1 and b.weixinid='gh_74fd31d83988' group by b.openid"
        # new weixin
        querystr = "select b.openid from t_service a inner join weixin.t_weixin_gzh_push b on b.userid=a.userid where a.product_class='ztls' and a.enable=1 and b.weixinid='gh_74fd31d83988' group by b.openid"
        cur.execute(querystr)
        conn.commit()

        data = []
        for openid in cur:
            data.append(openid[0])

        #querystr = "select b.openid from t_allproduct_user a inner join t_weixin_gzh_push b on b.userid=a.userid where date(a.end_time)>=date(now()) and b.weixinid='gh_74fd31d83988' and a.userid not in (select userid from stock_app.t_service where end_date>now() and product_class='ztls') group by b.openid"
        #cur.execute(querystr)
        #conn.commit()

        #for openid in cur:
            #data.append(openid[0])

        return data
    except  Exception as e:
        logging.exception(e)
        return

def get_weixin_userid():
    try:
        querystr = "select a.userid from stock_app.t_service a where a.product_class='ztls' and a.enable=1"
        cur.execute(querystr)
        conn.commit()

        data = []
        for userid in cur:
            data.append(userid[0])

        return data
    except  Exception as e:
        logging.exception(e)
        return

def get_chaodi_stock():
    try:
        querystr = "select a.id,a.ext_1,b.stockname from t_message_affairs a join t_stock_base b on a.ext_1=b.stockid where a.affairs='ztls_push_on_wx' and date(a.create_time)=date(now()) ORDER BY a.ext_1 DESC"
        #querystr = "select a.id,a.ext_1,b.stockname from t_message_affairs a join t_stock_base b on a.ext_1=b.stockid where a.affairs='ztls_push_on_wx' and date(a.create_time)=date(now())"
        #querystr = "select a.id,a.ext_1,b.stockname,format(a.ext_2,2),a.ext_3 from t_message_affairs a join t_stock_base b on a.ext_1=b.stockid where a.affairs='test'"
        affected_rows = cur.execute(querystr)
        conn.commit()

        logging.info("affected_rows="+str(affected_rows))
        data = []
        for uid,stockid,stockname in cur:
            tmp = {}
            tmp["uid"] = uid
            tmp["stockid"] = stockid
            tmp["stockname"] = stockname
            data.append(tmp)
        logging.info(data)
        return data

    except  Exception as e:
        logging.exception(e)
        return


def update_redbull(data):
    try:
        for v in data:
            insertstr = "insert into stock_app.t_product_news_surgepioneer (transday,stockid,operate,buy_price,create_time) (select date_format(now(),'%Y%m%d'),stockid,'1',currentprice/10000,now() from stock_app.t_realtime_quotation where stockid='{}')".format(v["stockid"])
            logging.info(insertstr)
            affected_rows = cur_redbull.execute(insertstr)
            conn_redbull.commit()
            logging.info("insertstr="+insertstr+',affected_rows='+str(affected_rows))

        return

    except  Exception as e:
        logging.exception(e)
        return

def update_forredbull_stockexpert_all(data):
    try:
        t = time.localtime()
        now = time.strftime("%Y-%m-%d %H:%M:%S", t)
        data = "【涨停先锋】今日选股如下，请留意：<br/>股票简称：{}<br/>入选时间：{}<br/>后续将发出交易信号，请留意。服务信息仅供参考，请投资者独立作出决策。股市有风险，投资须谨慎。".format(data,now)
        insertsql = "insert into stock_app.t_product_all_ad (product_class,content,vip,enable,del_time,create_time) values ('surgepioneer','{}','1','1','2099-12-30 23:59:59',now())".format(data)
        updatesql = "update stock_app.t_product_homepage set product_news = '{}',update_time=now() where product_class = 'surgepioneer'".format(data)
        
        logging.info(insertsql)
        cur_redbull.execute(insertsql)
        conn_redbull.commit()
        
        logging.info(updatesql)
        cur_redbull.execute(updatesql)
        conn_redbull.commit()
        return

    except Exception as e:
        logging.exception(e)
        return

#def get_wx_template(data):
#   t = time.localtime()
#   now = time.strftime("%Y-%m-%d %H:%M:%S", t)
#   wx_template = {
#       "first": {
#           "value": "您订阅的【涨停猎手】今日个股筛选结果如下：",
#           "color": "#173177"
#       },
#       "keyword1": {
#           "value": "先机智能交易员-Beta Mind",
#           "color": "#173177"
#       },
#       "keyword2": {
#           "value": "{}".format(data),
#           "color": "#173177"
#       },
#       "keyword3": {
#           "value": "{}".format(now),
#           "color": "#173177"
#       },
#       "remark": {
#           "value": "\n建议买入后T+1内完成买卖操作，（本信息仅供参考，不构成投资建议，股市有风险，投资需谨慎）",
#           "color": "#173177"
#       }
#   }
#
#   return wx_template

def get_wx_template(data):
    t = time.localtime()
    now = time.strftime("%Y-%m-%d %H:%M:%S", t)
    wx_template = {
        "first": {
            "value": "【涨停猎手】大数据监测到下列个股发出涨停信号，建议保持关注",
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
            "value": "\n大数据量化监测，回测统计1天1涨停，请谨慎参考，更多信息请至股票先机APP查看>",
            "color": "#173177"
        }
    }

    return wx_template

def get_no_stock_wx_template():
    t = time.localtime()
    now = time.strftime("%Y-%m-%d %H:%M:%S", t)
    wx_template = {
        "first": {
            "value": "尊敬的用户",
            "color": "#173177"
        },
        "keyword1": {
            "value": "涨停猎手已更新",
            "color": "#173177"
        },
        "keyword2": {
            "value": "{}".format(now),
            "color": "#173177"
        },
        "remark": {
            "value": "\n当前市场风险较高，为了降低您的投资风险，系统今日不进行个股推荐。",
            "color": "#173177"
        }
    }

    return wx_template

def write_push_history(data):
    nw = time.localtime()
    nwday = time.strftime("%Y%m%d", nw)
    try:
        deletestr = "delete from t_message_affairs where id='{}'".format(data["uid"])
        logging.info('deletestr='+deletestr)
        cur.execute(deletestr)
        conn.commit()
    except  Exception as e:
        logging.exception(e)
        return

def save_push_history(msg):
        nw = time.localtime()
        nwday = time.strftime("%Y%m%d", nw)
        try:
                insertstr = "insert into t_push_history set type='ztls',day="+str(nwday)+",content='" +msg+ "',update_time=now()"
                logging.info('insertstr='+insertstr)
                cur.execute(insertstr)
                conn.commit()
        except  Exception as e:
                logging.exception(e)
                return

def action(userid):
    send_weixin_msg(userid, WX_TEMPLATE_MSG_CHAO_DI,TEMPLATE_MSG,"http://t.cn/RGBQsBV")
    
def action_no_stock(userid):
    send_weixin_msg(userid, WX_TEMPLATE_MSG_NO_WEIPAN_ID,TEMPLATE_MSG)

def push_app_msg(msg):
    try:
        logging.info("start push msg:"+msg)
        if msg == "":
            logging.info("get_ztls_stock is empty")
            return
        payload = {
            "platform": "all",
            "audience": {
            "tag": ["ztls"]
            },
            "notification": {
            "android": {
                "alert": msg,
                "extras": {
                    "type": 4,
                    "linkUrl": "gpxj://ztls"
                }
            },
            "ios": {
                "alert": msg,
                "sound": "cowboy.wav",
                "badge": "+1",
                "extras": {
                    "type": 4,
                    "linkUrl": "gpxj://ztls"
                }
            }
            },
            "options": {
            "apns_production": pushcomm.ApnsProduction
            }
        }
        headers = {"Content-Type": "application/json"}
        r = requests.request(method="POST", url="https://api.jpush.cn/v3/push", json=payload, headers=headers, auth=(pushcomm.app_key, pushcomm.master_secret))
        logging.info(str(r.status_code) + "----" + r.text)
    except Exception as e:
        logging.exception(e)
        return

def send_weixin_msg(users, template_id,template_msg,jump_url='',i=0):
        tmp_int = i
        global TOKEN
        global REDIS_AIXUANGU_KEY
        wx_url = WX_TEMPLATE_MSG_API.format(TOKEN)
        try:
                payload = {
                        "touser": users,
                        "template_id": template_id,
                        "url":jump_url,
                        "data":template_msg
                }
                r = requests.post(url=wx_url, json=payload,timeout=6)
                logging.info(str(users) + "," + users + "," + r.text)
                retdata = r.json()
                if "errcode" in retdata:
                        if int(retdata["errcode"]) == 40001:
                                TOKEN = redis_comm.get_key(get_key)
                                wx_url = WX_TEMPLATE_MSG_API.format(TOKEN)
                                if tmp_int <= 3:
                                        tmp_int = tmp_int + 1
                                        send_weixin_msg(users, template_id, template_msg, jump_url, tmp_int)
        except Exception as e:
                logging.exception(e)
                logging.error("send wx error!")

def get_chaodi_history():
    try:
        querystr = "select count(1) from stock_app.t_hunt_zhangting where transday = date_format(now(),'%Y%m%d')"
        logging.info("querystr="+querystr)
        affected_rows = cur.execute(querystr)
        conn.commit()
        if affected_rows == 0:
            logging.info("affected_rows=0,no users in sscdpackage")
            return
        for count in cur:
            data = int(count[0])
        return data
    except  Exception as e:
        logging.exception(e)
        return

if __name__ == '__main__':
    logging.info('涨停猎手推送 start '+file_name)
    #step1 progamme run only 1
    pushcomm.OneRunningOnly(__file__)

    #step2 if day right
    if pushcomm.is_transday() == False :
        logging.error('today is not transday,exit!')
        exit(1)
    while True:
        now = pushcomm.getTimeSec()
        push_count = get_chaodi_history()
        if push_count == 0 :
            logging.info(push_count)
        if now > '11:30:00':
            logging.info('now stop running')
            break
        if now > '09:55:00' and push_count == 0:
            vipMsg.update_forredbull_surgepioneer_no_msg()
            push_app_msg("【涨停猎手】今天涨停猎手没有发现合适标的，谢谢！")
            pushcomm.mpush_msg_to_topic('股票先机',"【涨停猎手】今天涨停猎手没有发现合适标的，谢谢！",'ztls',{'type':4,'linkUrl':'gpxj://ztls'})
            TEMPLATE_MSG = get_no_stock_wx_template()
            users = get_weixin_user()
            logging.info(users)
            global TOKEN
            TOKEN = pushcomm.get_token()
            pool = threadpool.ThreadPool(20) 
            allrequests = threadpool.makeRequests(action_no_stock, users) 
            [pool.putRequest(req) for req in allrequests] 
            pool.wait()
            logging.info('now stop running')
            break
        time_start=time.time()
        data = get_chaodi_stock()
        push_data = ''
        if len(data) > 0 :
            #for v in data :
            #   push_data = push_data + v["stockname"] + '（'+ v["stockid"][0:6] + '）、'
            #push_data = push_data[0:len(push_data)-1]
            #update_forredbull_stockexpert_all(push_data)
            #涨停先锋数据更新
            data_vip = data[0:2]
            push_data = vipMsg.convert_data_to_str(data,"、")
            push_data_vip = vipMsg.convert_data_to_str(data_vip,"、")
            vipMsg.update_forredbull_surgepioneer_all_new(push_data,push_data_vip)
            logging.info('涨停先锋数据更新')
        if len(data) > 0 :
            #test.send_ztls_sms(data, get_weixin_userid())
             #涨停先锋推送信息消息
            data_vip = data[0:2]
            vipMsg.send_ztxf_sms(data,data_vip)
            logging.info('涨停先锋推送信息消息')
            update_redbull(data)
        if len(data) > 0 :
            pushstr = "涨停猎手：今日大数据监测发现{}有涨停机会>>".format(push_data)
            push_app_msg(pushstr)
            save_push_history(pushstr)
            pushcomm.mpush_msg_to_topic('股票先机',pushstr,'ztls',{'type':4,'linkUrl':'gpxj://ztls'})
        if len(push_data) > 0 :
            users = get_weixin_user()
            #print(users)
            logging.info(users)
            global TOKEN
            TOKEN = pushcomm.get_token()
            pool = threadpool.ThreadPool(20) 
            #users = ['ofQzPvyiY2bAPsw6iSTG3Tw1E9CY']
            for msg in data:
                logging.info(msg)
                write_push_history(msg)
            TEMPLATE_MSG = get_wx_template(push_data)
            allrequests = threadpool.makeRequests(action, users) 
            [pool.putRequest(req) for req in allrequests] 
            pool.wait()
            time_end=time.time()
        time.sleep(5)
    #logging.info("本次推送耗时：{}".format(time_end-time_start))
    pushcomm.close_mysql()
    cur.close()
    cur_redbull.close()
    conn.close()
    conn_redbull.close()
    logging.info('end '+file_name)
