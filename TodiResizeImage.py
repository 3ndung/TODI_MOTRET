from PIL import Image
import os, sys
from datetime import datetime

today = datetime.now()
P1 = "TEST/"
P2 = "HASIL/"+today.strftime('%Y%m%d')

dirs = os.listdir(P1)




def ResizeImg():
    ''' resize dari image 6000 x 4000 into 1333 x 2000'''
    for XXX in dirs:
        image = Image.open(P1+XXX)
        logo = Image.open('TODI_MOTRET.png')
        logo1 = Image.open('TODI_MOTRET2.png')

        #new_image = image.resize((2000,1333))
        #new_image.save('NEW'+XXX)
        #print(image.size)

        xi,yi = image.size

        if xi > yi :
            new_image = image.resize((2000,1333))
            image_copy = new_image.copy()
            position = (int(image_copy.width/2 - logo.width/2), int(image_copy.height/2 - logo.height/2))
            image_copy.paste(logo1, position, logo1)
            image_copy.save(P2+XXX)

        else:
            new_image = image.resize((1333,2000))
            image_copy = new_image.copy()
            position = (int(image_copy.width/2 - logo.width/2), int(image_copy.height/2 - logo.height/2))
            image_copy.paste(logo, position)
            image_copy.save(P2+XXX)




#ResizeImg('_DSC1354 (1).jpg')    
#ResizeImg('_DSC1354.JPG')
ResizeImg()







