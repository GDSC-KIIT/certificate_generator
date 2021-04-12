from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os
df = pd.read_csv('D:\\Dev\\Python\\VS Code\\certificate_generator\\participants\\Book1.csv')
font = ImageFont.truetype('D:\Dev\Python\VS Code\certificate_generator\fonts\ChopinScript.ttf',60)
for index,j in df.iterrows():
    img = Image.open('D:\\Dev\\Python\\VS Code\\certificate_generator\\Templates\\new.png')
    draw = ImageDraw.Draw(img)
    draw.text(xy=(900,600),text='{}'.format(j['name'].title()),fill=(1,2,3),font=font)
    img=img.convert('RGB')
    img.save('pictures/{}.jpg'.format(j['name']))