# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 09:03:06 2019

@author: jxm72
"""
import re
import smtplib
from smtplib import SMTPException
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
import getpass


address=open(r"address_information.csv",'r')
cr_address=[]
name=[]
subject=[]
for line in address:
    line=re.split(',',line)
    if re.match(r'(\S+)@(\S+)+(\.\S+)',line[1]):#judge whether address is correct
        print(line[1],':','correct address')
        #collect data of address, name and subject
        cr_address.append(line[1])
        name.append(line[0])
        subject.append(line[2])
    else:
        print(line[1],':','Wrong address!')
address.close()        
 

with open(r"body.txt", 'r') as myfile:
    data = myfile.read()
    print(data)
    data1=data[::]#replicate data to complete the iteration  
username=input('please input your zju username:')
password=getpass.getpass('please input the password:')
yourname=input('please input your name:')
for i in range(3):
    data=data1.replace('User',name[i])#modify the body
    try:
        sender = username+'@zju.edu.cn'
        receivers ='Jixin.18@intl.zju.edu.cn'#cr_address[i]
        mailserver = smtplib.SMTP('smtp.zju.edu.cn',25)
        mailserver.login(username, password)
        #define toname, fromname and subject
        msg = MIMEMultipart()
        msg['To'] = Header(name[i],'utf-8')
        msg['Subject'] = Header(subject[i], 'utf-8')
        msg['From']=Header(yourname,'utf-8')
        msg.attach(MIMEText(data, 'plain'))
        #change the body to string
        text = msg.as_string()
        mailserver.sendmail(sender, receivers,text)
        mailserver.quit()
        print("Successfully sent email")
    except SMTPException:
       print("Error: unable to send email")
       
       

