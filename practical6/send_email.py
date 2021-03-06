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

#The file 'address_information.csv' has be in the working directory so we directly open it
address=open(r"address_information.csv",'r')
cr_address=[]
name=[]
subject=[]
lines=[]
#get information from csv file
for line in address:
    lines.append(line)
del lines[0]#delete the line of column name

for line in lines:
    line=re.split(',',line)
    #check whether address is correct
    if re.match(r'(\S+)@(\S+)+(\.\S+)',line[1]):
        print(line[1],':','correct address')
        #collect the name and subject of correct address
        cr_address.append(line[1])
        name.append(line[0])
        subject.append(line[2])
    else:
        print(line[1],':','Wrong address!')
address.close()        
 

with open(r"body.txt", 'r') as myfile:
    data = myfile.read()
    #replicate data to complete the iteration
    data1=data[::]
    
loginname=input('please input your zju loginname:')
password=getpass.getpass('please input the password:')
yourname=input('please input your name:')
for i in range(3):
    #modify the body, change the User to the specific name
    data=data1.replace('User',name[i])
    myfile.close()
    #send email
    try:
        #assign sender's address, receivers' address and the SMTP for zju
        sender = loginname+'@zju.edu.cn'
        receivers = cr_address[i]
        mailserver = smtplib.SMTP('smtp.zju.edu.cn',25)
        #log in with sender's account
        mailserver.login(loginname, password)
        #define toname, fromname and subject
        msg = MIMEMultipart()
        msg['To'] = Header(name[i],'utf-8')
        msg['Subject'] = Header(subject[i], 'utf-8')
        msg['From']=Header(yourname,'utf-8')
        msg.attach(MIMEText(data, 'plain'))
        #change the body to string
        text = msg.as_string()
        #send mail
        mailserver.sendmail(sender, receivers,text)
        mailserver.quit()
        print("Successfully sent email")
    except SMTPException:
       print("Error: unable to send email")
       
       

