# Importing necessary libraries
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

                                                                                            # Selecting desired font and .csv file contaning participants
df = pd.read_csv('D:\\Dev\\Python\\VS Code\\certificate_generator\\participants\\Book1.csv')
font = ImageFont.truetype('D:\\Dev\\Python\\VS Code\\certificate_generator\\fonts\\GoogleSans-Bold.ttf',60)

                                                                                               # Itrating over each participant from the .csv file
for index,j in df.iterrows():
    img = Image.open('D:\\Dev\\Python\\VS Code\\certificate_generator\\Templates\\new.png')    # selecting certificate template
    draw = ImageDraw.Draw(img)
    draw.text(xy=(990,680),text='{}'.format(j['name'].title()),fill=(1,2,3),font=font, anchor="mm")         # Enscribing name over template
    img=img.convert('RGB') 
    img.save('pictures/{}.pdf'.format(j['name']))                                              # saving the image
    fromaddr = "your-email-id@gmail.com"                                                       #Specify the E-Mail ID through which you want to send mail
    password = "YOUR-PASSWORD"                                                                 #Specify password of the E-Mail ID through which you want to send mail
    toaddr = j['Email']
                                                                                               # instance of MIMEMultipart
    msg = MIMEMultipart()
                                                                                               # storing the senders email address
    msg['From'] = fromaddr
    msg['To'] = j['Email']
    msg['Subject'] = "Certificate for Partiicipation [DSC-KIIT]"
                                                                                               # string to store the body of the mail
    txt_file = open('body.txt', 'r')
    body = (txt_file.read())
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
