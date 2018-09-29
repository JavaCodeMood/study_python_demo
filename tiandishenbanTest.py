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

#定义日志文件
file_name = 'tiandishenban_push'
logging.basicConfig(filename=file_name + ".log", level=logging.INFO,
                    format='%(asctime)-15s:%(levelname)s:%(filename)s:%(lineno)s:%(funcName)s:%(message)s')

# 模板消息推送接口
WX_TEMPLATE_MSG_API = "https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={}"
# 消息模板
WX_TEMPLATE_ID = "-rCw1uIdOaj44cGbFGqm5tw00ipTADPoJVChmBa8JCU"
# new weixin
WX_TEMPLATE_NO_MSG = "_nInpqSRq8IVzZUyg9V6oDCKoErfwLcWV2BVuZiH49w"

TEMPLATE_MSG = ""
TEMPLATE_NO_MSG = ""

# 使用新微信 先机客户服务
WX_APPID = "wx4a0bb2c0fd6d0277"
WX_SECRET = "96edcadda33d38ef3604174ad069f744"
TOKEN = ''
# new weixin
REDIS_TIANDISHENBAN_KEY = 'newweixinpush_token'

#初始化连接mysql  conn表示数据库连接 cur表示数据库游标
conn, cur = pushcomm.init_mysql()

#获取天地神板信息
def get_tiandishenban_stock():
    try:
        #查询数据库，获取股票代码，股票名称(获取当天的股票信息)
        querystr = '''
          SELECT a.stockid, b.stockname FROM stock_app.t_reversal_history a 
          LEFT JOIN stock_app.t_stock_base b ON a.stockid = b.stockid 
          WHERE DATE(a.recommand_time) = DATE(NOW())
        '''
        #执行sql语句
        queryResult = cur.execute(querystr)
        #提交数据
        conn.commit()

        logging.info("queryResult="+str(queryResult))
        data = []  #空列表
        for stockid, stockname in cur:
            tmp = {}   #创建一个空字典
            tmp["stockid"] = stockid
            tmp["stockname"] = stockname
            data.append(tmp)   #添加数据到列表中
        logging.info(data)
        return data

    except  Exception as e:
        logging.exception(e)
        return


#处理数据
def convert_data_to_str(data, sep):
    pushstr = ""
    for v in data:
        pushstr = pushstr + v["stockname"] + "(" + v["stockid"][0:6] + ")" + sep
    pushstr = pushstr[0:len(pushstr) - 1]

    return pushstr


#获取微信用户信息
def get_weixin_user():
    try:
        #查询数据库，获取微信用户的openid
        queryStr = '''
           SELECT b.openid FROM stock_app.t_service a 
           INNER JOIN weixin.t_weixin_gzh_push b ON b.userid=a.userid 
           WHERE a.product_class='reverse_king' AND a.enable=1 AND b.weixinid='gh_74fd31d83988' GROUP BY b.openid
        '''
        #执行SQL语句
        #queryResult = cur.execute(queryStr)
        cur.execute(queryStr)
        # 提交数据
        conn.commit()

        logging.info("queryResult="+str(cur))

        data = []   #定义空列表
        for openid in cur:
            data.append(openid[0])   #添加数据到列表

        return data

    except  Exception as e:
        logging.exception(e)
        return


#获取微信推送模板
def get_wx_template(data):
    t = time.localtime()
    now = time.strftime("%Y-%m-%d %H:%M:%S", t)
    #定义一个字典
    wx_template = {
        "first":{
            "value": "【天地神板】通过大数据监测出下列个股有反转机会",
            "color": "#173177"
        },
        "keyword1":{
            "value": "{}".format(data),
            "color": "#173177"
        },
        "keyword2":{
            "value": "{}".format(now),
            "color": "#173177"
        },
        "remark":{
            "value": "大数据量化选股，请谨慎参考，更多信息请至股票先机APP查看> ",
            "color": "#173177"
        }
    }
    return wx_template


def get_no_stock_wx_template():
    t = time.localtime()
    now = time.strftime("%Y-%m-%d %H:%M:%S",t)
    #定义一个字典
    wx_template = {
        "first":{
            "value": "【天地神板】为降低您的风险，今天没有发现合适的标的，谢谢！",
            "color": "#173177"
        },
        "keyword1":{
            "value": "天地神板已更新",
            "color": "#173177"
        },
        "keyword2": {
            "value": "{}".format(now),
            "color": "#173177"
        },
        "remark":{
            "value": "大数据量化监测，请谨慎参考，更多信息请至股票先机APP查看> ",
            "color": "#173177"
        }
    }
    return wx_template


#action调用发送微信信息(有股票数据)
def action(users):
    send_weixin_msg(users,WX_TEMPLATE_ID,TEMPLATE_MSG,"http://t.cn/RGBQsBV")

#股票数据为空
def action_no_stock(users):
    send_weixin_msg(users, WX_TEMPLATE_NO_MSG,TEMPLATE_NO_MSG)

def send_weixin_msg(users, wx_template_id, template_msg,
                    jump_url='http://a.app.qq.com/o/simple.jsp?pkgname=com.lixun.gpxj',i=0):
    tmp_int = i
    global TOKEN
    wx_url = WX_TEMPLATE_MSG_API.format(TOKEN)
    try:
        #定义一个字典
        payload = {
            "touser": users,
            "template_id": wx_template_id,
            "url": jump_url,
            "data": template_msg
        }
        print(str(payload))  #打印字典信息
        #以post方式请求数据
        r = requests.post(url=wx_url, json=payload, timeout=6)
        logging.info(str(users) + "," + users + "," + r.text)
        retdata = r.json()
        print("retdata=",retdata)
        #如果errcode存在retdata中，并且为40001
        if "errcode" in retdata:
            if int(retdata["errcode"]) == 40001:
                TOKEN = redis_comm.get_key(REDIS_TIANDISHENBAN_KEY)
                wx_url = WX_TEMPLATE_MSG_API.format(TOKEN)
                if tmp_int < 3:
                    tmp_int = tmp_int + 1
                    #递归调用
                    send_weixin_msg(users, wx_template_id, template_msg, jump_url, tmp_int)
    except Exception as e:
        logging.exception(e)
        logging.error("send wx error!")


if __name__ == '__main__':
    logging.info('天地神板推送 start ' + file_name)
    # 调用查看进程的方法，确保只运行一个进程
    pushcomm.OneRunningOnly(__file__)

    #定义开始推送的时间
    t = time.localtime()
    now_date = time.strftime("%Y-%m-%d", t)
    if str(now_date) < "2018-09-03":
        logging.error('no in push date:' + str(now_date))
        exit(1)

    #判断是不是交易日
    if pushcomm.is_transday() == False:
        logging.error('today is not transday,exit!')
        exit(1)

    #开始时间
    time_start = time.time()

    #获取需要推送的数据
    data = get_tiandishenban_stock()
    push_data = convert_data_to_str(data, "、")

    if len(data) > 0 :
        TEMPLATE_MSG = get_wx_template(push_data)
    else :
        TEMPLATE_NO_MSG = get_no_stock_wx_template()


    if len(data) > 0:
        #APP推送
        app_push_str = "【天地神板】今日通过大数据发现{}有反转机会，建议尽快关注。".format(push_data)
    else :
        # APP推送
        app_push_str = "【天地神板】为降低您的风险，今天没有发现合适标的，谢谢！"

    #测试时需要去掉注释
    jumpUrl = "gpxj://reverse_king"

    #IOS推送
    #测试环境
    userid_arr = ["18295514402", "13145844655"]
    pushcomm.jpush2user(app_push_str, userid_arr, pushcomm.app_key, pushcomm.master_secret,{'type':4,'title':'股票先机','content': app_push_str,'linkUrl':jumpUrl})
    #正式环境
    #pushcomm.jpush2topic(pushcomm.app_key, pushcomm.master_secret, "股票先机", app_push_str, "reverse_king",
    #                     {'type': 4, 'linkUrl': 'gpxj://reverse_king'})

    #Android
    #测试环境
    userids = "18295514402,13145844655"
    pushcomm.mpush2user('股票先机',app_push_str,userids,{'type':4,'linkUrl':jumpUrl,'content':app_push_str,'title':'股票先机'})
    #正式环境
    #pushcomm.mpush_msg_to_topic("股票先机", app_push_str, "reverse_king", {'type': 4, 'linkUrl': 'gpxj://reverse_king'})

    #微信推送
    #获取微信用户   测试环境
    users = ['oa-Zf0WLPu4J1R4TanBghWR9oy_4']
    #正式环境
    #users = get_weixin_user()
    logging.info("users" + str(users))

    TOKEN = pushcomm.get_token()

    #定义线程池
    pool = threadpool.ThreadPool(20)
    if len(data) > 0:
        allrequests = threadpool.makeRequests(action, users)
    else:
        allrequests = threadpool.makeRequests(action_no_stock, users)

    [pool.putRequest(req) for req in allrequests]
    pool.wait()


    #结束时间
    time_end = time.time()
    logging.info("本次推送耗时：{}".format(time_end - time_start))
    #关闭资源连接
    pushcomm.close_mysql()
    cur.close()
    conn.close()
    logging.info('end ' + file_name)








