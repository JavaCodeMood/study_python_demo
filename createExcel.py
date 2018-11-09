#!/usr/bin/python
# coding: utf-8

import sys
import xlwt
import pymysql
import datetime
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os.path

host = 'localhost'
user = 'root'
password = 'root'
port = 3306
dbname = 'test'

sheet_name = 'report' + time.strftime("%Y-%m-%d")
filename = 'report_' + time.strftime("%Y-%m-%d") + '.xls'
out_path = 'report_' + time.strftime("%Y-%m-%d") + '.xls'
print(out_path)
sql = 'Select * from userinfo;'

#查询数据，并生成excel
def export():
    conn = pymysql.connect(host, user, password, dbname, charset='utf8')
    cursor = conn.cursor()
    count = cursor.execute(sql)
    print("查询出" + str(count) + "条记录")
    if count > 0:
        # 来重置游标的位置
        cursor.scroll(0, mode='absolute')
        # 搜取所有结果
        results = cursor.fetchall()
        # 获取MYSQL里面的数据字段名称
        fields = cursor.description
        workbook = xlwt.Workbook(encoding='utf-8')  # workbook是sheet赖以生存的载体。
        sheet = workbook.add_sheet(sheet_name, cell_overwrite_ok=True)
        # 写上字段信息
        for field in range(0, len(fields)):
            sheet.write(0, field, fields[field][0])
        # 获取并写入数据段信息
        row = 1
        col = 0
        for row in range(1, len(results) + 1):
            for col in range(0, len(fields)):
                sheet.write(row, col, u'%s' % results[row - 1][col])
        workbook.save(out_path)
    else:
        print("无数据")


"""
邮箱服务器地址：
QQ:smtp.qq.com
163:smtp.163.com
gpxj:smtp.exmail.qq.com
"""
email_host = 'smtp.163.com'
#发件者
email_user = "xxxxx@163.com"
email_pass = "xxxx"
#收件者
areceiver = "xxxxx@gupiaoxianji.com"
acc = "xxxxx"

# 如名字所示Multipart就是分多个部分
msg = MIMEMultipart()
msg["Subject"] = u'【数据统计_' + time.strftime("%Y-%m-%d") + u'】'
msg["From"] = email_user
msg["To"] = areceiver
msg["Cc"] = acc


def send_email():
    conn = pymysql.connect(host, user, password, dbname, charset='utf8')
    cursor = conn.cursor()
    count = cursor.execute(sql)
    # ---这是文字部分---
    content = '''Deal all,\n附件是系统每日统计情况，请查收！
    总计结果数为：''' + str(count)

    part = MIMEText(content, 'plain', 'utf-8')
    msg.attach(part)
    if count > 0:
        # ---这是附件部分---
        # xls类型附件
        #file_name = '/data/monitor/temp/' + filename
        file_name = filename
        part = MIMEText(open(file_name, 'rb').read(), 'base64', 'gb2312')
        part["Content-Type"] = 'application/octet-stream'
        basename = os.path.basename(file_name)
        part["Content-Disposition"] = 'attachment; filename=%s' % basename.encode('gb2312')
        msg.attach(part)
        s = smtplib.SMTP(email_host, timeout=30)  # 连接smtp邮件服务器,端口默认是25
        s.login(email_user, email_pass)  # 登陆服务器
        s.sendmail(email_user, areceiver.split(',') + acc.split(','), msg.as_string())  # 发送邮件
        print("Email send successfully")
        s.close()
    else:
        print("nothing to send!")


# 调用函数
if __name__ == "__main__":
    export()
    send_email()