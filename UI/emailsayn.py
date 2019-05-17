#!/usr/bin/env python
# coding: utf-8

# In[7]:


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
import string
def sender(code, user_email):
    from_user = 'saynsec2019@gmail.com'
    to_user = user_email
    password = 'sayn2019'
    
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(from_user,password)
    subject = 'Sayn Securities'
    
    msg = MIMEMultipart()
    msg['From'] = from_user
    msg['To'] = to_user
    msg['Subject'] = subject
    body = ''
    if(code <= 1):
        body = 'Your device has been accessed. If this is you then please ignore this email. If this is not you then please check your device.'
    else:
        body = randomStringwithDigitsAndSymbols(10)
    msg.attach(MIMEText(body, 'plain'))
    text = msg.as_string()
    server.sendmail('',to_user,text)
    server.close()
    return body

def randomStringwithDigitsAndSymbols(stringLength=10):
    """Generate a random string of letters, digits and special characters """
    password_characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(password_characters) for i in range(stringLength))

if __name__ == "__main__":
    print(sender(2,'wasabiijunior@gmail.com'))


# In[ ]:




