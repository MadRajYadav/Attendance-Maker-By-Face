import numpy as np
import face_recognition
import cv2
import os # search os and find the function of it
from datetime import datetime
path='images'
image=[]
className=[]
myList=os.listdir(path)
print(myList)
# myLIst = ['Director_sir.png', 'elon.png', 'Nilesh_sir.png']

for cl in myList:
    curImg=cv2.imread(f'{path}/{cl}')
    image.append(curImg)
    className.append(os.path.splitext(cl)[0])
print(className)
# className = ['Director_sir', 'elon', 'Nilesh_sir']
# print(image)

def findEncodings(image):
    encodeList=[]
    for img in image:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode=face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList