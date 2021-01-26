#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 16:22:56 2021

@author: lin
"""


import tesserocr
from selenium import webdriver
from PIL import Image
import time
import smtplib
from email.mime.text import MIMEText
o=0
while True:
    try:
        k=0
        while True:
            options = webdriver.ChromeOptions()
            options.add_argument('--headless')
            browser = webdriver.Chrome(options=options)
            browser.get('https://fangkong.hnu.edu.cn/app/#/login?redirect=%2Fhome')
            browser.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[1]/input').send_keys('202001130910')
            browser.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/input').send_keys('Lxycrash132465')
            browser.implicitly_wait(2)
            currentPageUrl = browser.current_url
            hnuurl='https://fangkong.hnu.edu.cn/app/#/login?redirect=%2Fhome'
            #网页判断#
            ###暴力识别
            n=0
            while browser.current_url==hnuurl:
                browser.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[3]/div/input').send_keys('')
                browser.implicitly_wait(10)
                browser.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[3]/img').click()
                browser.implicitly_wait(5)
                browser.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[3]/img').screenshot('test.png')
                browser.implicitly_wait(5)
                #######验证码识别#######
                img = Image.open('test.png')
                Img = img.convert('L')   #灰度化处理
                 
                threshold = 175    
                table = []
                for i in range(256):
                    if i < threshold:
                        table.append(0)
                    else:
                        table.append(1)
                # 图片二值化
                photo = Img.point(table, '1')
                photo.save('test.jpeg')  #得到二值化处理后图片test.jpg
                img=Image.open('test.jpeg')
                a=tesserocr.image_to_text(img)
                browser.implicitly_wait(5)
                browser.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[3]/div/input').send_keys(a)
                browser.implicitly_wait(5)
                browser.find_element_by_xpath('/html/body/div[1]/div/div[3]/button').click()
                time.sleep(2)
                n=n+1
                if n>20:
                    browser.close()
                    break
            if browser.current_url!=hnuurl:
                k=-2
            k=k+1
            if k>2:
                mail_server = "smtp.126.com"
                mail_port = 25
                sender = "linxinyu0110@126.com"
                sender_password = "ISDUSHZOCHKHIJIJ"  # 授权码
                receivers = "1078404883@qq.com"
                
                
                message = MIMEText('错误原因:验证码错误', 'plain', 'utf-8')
                message['From'] = sender
                message['To'] = receivers
                
                send_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
                subject = '打卡失败' + send_time 
                message['Subject'] = subject
                
                
                
                smtp_obj = smtplib.SMTP()
                smtp_obj.connect(mail_server, mail_port)
                smtp_obj.login(sender, sender_password)
                smtp_obj.sendmail(sender, [receivers], message.as_string())
                break
            elif k==-1:
                break
        ###网页跳转
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div/div/div/div[2]/div[2]/div[2]').click()
        time.sleep(1)
        ####地点点击
        for i in range(1,19):
            h='/html/body/div[1]/div/div[5]/div/div[2]/div[1]/ul/li['+str(i)+']'
            browser.find_element_by_xpath(h).click()
            time.sleep(0.5)
        browser.find_element_by_xpath('/html/body/div[1]/div/div[5]/div/div[2]/div[2]/ul/li[1]').click()
        browser.find_element_by_xpath('/html/body/div[1]/div/div[5]/div/div[2]/div[3]/ul/li[3]').click()
        browser.find_element_by_xpath('/html/body/div[1]/div/div[5]/div/div[1]/button[2]').click()
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div/div/div/div[2]/div[2]/div[3]/div[2]/div/input').send_keys('湖南大学')
        browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div/div/div/div[2]/div[3]/div/div[2]/div[2]/input').send_keys('36.5')
        browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div/div/div/div[2]/div[3]/div/div[3]/div[2]/input').send_keys('36.5')
        browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[1]/div/div/div/div[2]/button').click
        mail_server = "smtp.126.com"
        mail_port = 25
        sender = "linxinyu0110@126.com"
        sender_password = "ISDUSHZOCHKHIJIJ"  # 授权码
        receivers = "1078404883@qq.com"
        
        
        message = MIMEText('打卡成功', 'plain', 'utf-8')
        message['From'] = sender
        message['To'] = receivers
        
        send_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        subject = '打卡成功' + send_time 
        message['Subject'] = subject
        
        
        
        smtp_obj = smtplib.SMTP()
        smtp_obj.connect(mail_server, mail_port)
        smtp_obj.login(sender, sender_password)
        smtp_obj.sendmail(sender, [receivers], message.as_string())
        break
    except:
        o=o+1
        if o>4:
            break
        pass
if o==5:
    mail_server = "smtp.126.com"
    mail_port = 25
    sender = "linxinyu0110@126.com"
    sender_password = "ISDUSHZOCHKHIJIJ"  # 授权码
    receivers = "1078404883@qq.com"
    
    
    message = MIMEText('错误原因:程序出错', 'plain', 'utf-8')
    message['From'] = sender
    message['To'] = receivers
    
    send_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    subject = '打卡失败' + send_time 
    message['Subject'] = subject
    
    
    
    smtp_obj = smtplib.SMTP()
    smtp_obj.connect(mail_server, mail_port)
    smtp_obj.login(sender, sender_password)
    smtp_obj.sendmail(sender, [receivers], message.as_string())
        
    


