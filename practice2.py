#!/usr/bin/env python
# coding: utf-8



import smtplib
import csv
from email.mime.text import MIMEText
from email.header import Header


def read_csv(path):
    with open(path,"r") as f:
        csv_read = csv.reader(f)
        for line in csv_read:
            name = line[0]
            email = line[1]
            if name == 'name':
                continue
            print("姓名： "+ name + ",邮箱：" +email)
        




def send_email(receivers):
    sender_address = "liyy1694@chinaunicom.cn"
    password = "XXXX"

    for receiver in receivers:
        message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
        message['Subject'] = Header("Python SMTP 邮件测试", 'utf-8')
        message['From'] = Header("李源熠", 'utf-8')   
        message['To'] =  Header(receiver, 'utf-8')        #        
        try:
            smtpObj = smtplib.SMTP("hq.smtp.chinaunicom.cn",25)
            smtpObj.login(sender_address,password)
            smtpObj.sendmail(sender_address, receiver, message.as_string())
            print(receiver+"邮件发送成功")
        except smtplib.SMTPException as e:
            print(receiver+"Error: 无法发送邮件,错误原因："+ str(e))
    
    




if __name__ == '__main__':
    print('----开始读取通讯录------')
    read_csv('address_book.csv')
    print("----通讯录读取完成------" )
    mail_to = input("请输入收件人，以','分隔").split(',')
    print("----开始发送邮件------" )
    send_email(mail_to)
    







