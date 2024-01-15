import random
import qrcode
listName= ['thunderstorm','snoflake','blazefire','chillbone']
listCode= ['XYZ','AMM','hsdufh','saduuhfus','sagdfgs']
webLink='www.google.com'
appLink='wwww.playstore.com'
instaLink='https://www.instagram.com/pratishtha_sakecfest/'
aliasName='Name - '
aliasCode='Code - '
aliasWeb='Web - '
aliasApp='App - '
aliasInsta='Insta - '
i=1

def qrdata(data,count):
    img = qrcode.make(data)
    path='QRCode'+str(count)
    img.save(path+'.png')
    
    
def call(i):
    text=''
    temp=''
    text=text+aliasName
    temp=random.choice(listName)

    text=text+temp
    listName.remove(temp)
    temp=''
    text+=','
    text=text+aliasCode
    temp=random.choice(listCode)
    text=text+temp
    listCode.remove(temp)
    text+=','
    text+=aliasWeb+webLink+','+aliasApp+appLink+','+aliasInsta+instaLink
    print(text)
    qrdata(text,i)
    


call(i)
i=i+1
call(i)
i=i+1
call(i)
i=i+1
call(i)
i=i+1
from pyzbar.pyzbar import decode
from PIL import Image

def decode_qr_code(image_path):
    img = Image.open(image_path)
    decoded_objects = decode(img)
    if decoded_objects:
        return decoded_objects[0].data.decode('utf-8')
    else:
        return None

image_path = 'QRCode1.png'  
original_string = decode_qr_code(image_path)
# image_path = 'QRCode2.png'  # Replace with the path to your QR code image
# original_string = decode_qr_code(image_path)
# image_path = 'QRCode3.png'  # Replace with the path to your QR code image
# original_string = decode_qr_code(image_path)
# image_path = 'QRCode4.png'  # Replace with the path to your QR code image
# original_string = decode_qr_code(image_path)
if original_string is not None:
    print("Original String:", original_string)
else:
    print("No QR code found or unable to decode.")


