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
import string

address=open(r"C:\Users\jxm72\Desktop\semester2\IBI1\6\6_Practical_data(1)\address_information1.csv",'r')
#print(str(address))
#c_address=re.split(',')
#print(c_address)

#with open(r"C:\Users\jxm72\Desktop\semester2\IBI1\6\6_Practical_data(1)\address_information1.csv", 'rb') as csvfile:
#spamreader = csv.reader(r"C:\Users\jxm72\Desktop\semester2\IBI1\6\6_Practical_data(1)\address_information1.csv", delimiter=',')
#print(spamreader)  
cr_address=[]
name=[]
subject=[]
for line in address:
    print(line)
    line=re.split(',',line)
    if re.match(r'(\S+)@(\S+)\.(\S+)',line[1]):
        print(line[1],':','correct address')
        cr_address.append(line[1])
        name.append(line[0])
        subject.append(line[2])
    else:
        print(line[1],':','Wrong address!')
print(cr_address)
print(name)
print(subject)
for i in range(3):
    print(name[i])
    
    
    
    
    
with open(r"C:\Users\jxm72\Desktop\semester2\IBI1\6\6_Practical_data(1)\body.txt", 'r') as myfile:
    data = myfile.read()
    data1=data[::]
print(data)    

for i in range(3):
   
    data=data1.replace('User',name[i])
    print(data)
    
        
#    msg['From'] = sender
#    msg['To'] = receivers
    #msg['Subject'] = email.header.Header(subject, 'utf-8').encode()
    
#    #msg.attach(MIMEText(body, 'plain'))
    
    try:
        sender = '3180110708@zju.edu.cn'
        receivers = cr_address[i]
        mailserver = smtplib.SMTP('smtp.zju.edu.cn',25)
        mailserver.login('3180110708', 'a1193644683')
        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = receivers
        msg['Subject'] = subject[i]
        body = data
        msg.attach(MIMEText(body, 'plain'))
#        msg = MIMEMultipart()
#        msg['Subject'] = subject[i]
#        content = MIMEText(body, 'plain')
#        msg.attach(data)
#        filename = "body.txt"
#        f = file(filename)
#        attachment = MIMEText(f.read())
#        attachment.add_header('Content-Disposition', 'attachment', filename=filename)           
#        msg.attach(attachment)
        #password=input('please input the password:')
        
        #message = str(body)
        mailserver.ehlo()
        mailserver.starttls()
        mailserver.ehlo()

        text = msg.as_string()

        mailserver.sendmail(sender, receivers,text)  
        print("Successfully sent email")
    except SMTPException:
       print("Error: unable to send email")
    
#    y=re.search(r'(\S+)@(\S+)\.(\S+)',line[1])
#    if y=='None':
#        print('Wrong address!')
#    else:
#        print('correct address')
#    print(y)
    


 #for row in spamreader:
        #print(', '.join(row))