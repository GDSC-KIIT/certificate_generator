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
import sys
import time

count=1

xCoordinate = int(sys.argv[3]) # 990
yCoordinate = int(sys.argv[4]) # 680

imageExtension = sys.argv[7]

                                                                                            # Selecting desired font and .csv file contaning participants
df = pd.read_csv('cert_files/certificateCSV.csv')
font = ImageFont.truetype('cert_files/certificateFont.ttf', 60)

                                                                                               # Itrating over each participant from the .csv file
for index,j in df.iterrows():
    img = Image.open('cert_files/certificateImage{}'.format(imageExtension))    # selecting certificate template
    draw = ImageDraw.Draw(img)
    draw.text(xy=(xCoordinate,yCoordinate),text='{}'.format(j['name'].title()),fill=(1,2,3),font=font, anchor="mm")         # Enscribing name over template
    img=img.convert('RGB') 
    img.save('certificates/{}.pdf'.format(j['name']))                                              # saving the image
    fromaddr = sys.argv[1]                                                                          #Specify the E-Mail ID through which you want to send mail
    password = sys.argv[2]                                                                          #Specify password of the E-Mail ID through which you want to send mail
    toaddr = j['email']
                                                                                               # instance of MIMEMultipart
    msg = MIMEMultipart()
                                                                                               # storing the senders email address
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = sys.argv[5]
                                                                                               # string to store the body of the mail
    body = sys.argv[6]
                                                                                               # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))
                                                                                               # open the file to be sent
    filename = '{}.pdf'.format(j['name'])
    attachment = open(os.path.join('certificates', filename), "rb")
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
    print(f'Sucesfully sent to : {count} Particants')
    count=count+1
    server.send_message(msg)

server.quit()
