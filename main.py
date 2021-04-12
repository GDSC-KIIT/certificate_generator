import pandas as pd
import smtplib 
import string
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
from PIL import Image, ImageDraw, ImageFont
from pandas import ExcelWriter
from pandas import ExcelFile
from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os
df = pd.read_csv('D:\\Dev\\Python\\VS Code\\certificate_generator\\participants\\Book1.csv')
font = ImageFont.truetype('D:\\Dev\\Python\\VS Code\\certificate_generator\\fonts\\GoogleSans-Bold.ttf',60)
for index,j in df.iterrows():
    img = Image.open('D:\\Dev\\Python\\VS Code\\certificate_generator\\Templates\\new.png')
    draw = ImageDraw.Draw(img)
    draw.text(xy=(900,600),text='{}'.format(j['name'].title()),fill=(1,2,3),font=font)
    img=img.convert('RGB')
    img.save('pictures/{}.jpg'.format(j['name']))
    fromaddr = "darkwhite435@gmail.com"
    password = "Uzair@Saad786"
    toaddr = j['Email']
    # instance of MIMEMultipart
    msg = MIMEMultipart()
    # storing the senders email address
    msg['From'] = "darkwhite435@gmail.com"
    msg['To'] = j['Email']
    msg['Subject'] = "Certificate for Partiicipation [DSC-KIIT]"
    # string to store the body of the mail
    body = "Hey, Thank you for participating in our event attached below is the certificate for your Partiicipation"
    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))
    # open the file to be sent
    filename = 'pictures/{}.jpg'.format(j['name'])
    attachment = open(filename, "rb")
    # instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')
    # To change the payload into encoded form
    p.set_payload((attachment).read())


    # encode into base64
    encoders.encode_base64(p)

    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    # attach the instance 'p' to instance 'msg'
    msg.attach(p)

    # creates SMTP session
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr,password)

    # Converts the Multipart msg into a string
    text = msg.as_string()

    server.send_message(msg)

server.quit()