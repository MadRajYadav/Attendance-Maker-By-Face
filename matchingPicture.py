import datetime
import os.path

import cv2
import face_recognition
import numpy as np

index=2
indext=index
path="picture"
impath = os.listdir(path)
name = os.path.splitext(impath[index])[0]
print(name)
img = cv2.imread(f'{path}\{impath[index]}')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img = cv2.resize(img,(0,0), None, 0.25,0.25)
loc = face_recognition.face_locations(img)
encode = face_recognition.face_encodings(img,loc)

imgs = cv2.imread(f'{path}\{impath[indext]}')
imgs = cv2.resize(imgs,(0,0), None, 0.25,0.25)
cv2.imshow("camera",imgs)
img1 = cv2.imread(f'{path}\{impath[indext]}')
img1 = cv2.resize(img1,(0,0), None, 0.25,0.25)
img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
loc1 = face_recognition.face_locations(img1)
encode1 = face_recognition.face_encodings(img1,loc1)
for im,loc0 in zip(encode1,loc1):
    match = face_recognition.compare_faces(encode,im)
    if match ==[True]:
        y1, x2, y2, x1 = loc0  # getting face location
        # y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4  # making its size normal
        cv2.rectangle(imgs, (x1, y1), (x2, y2), (0, 255, 0), 2)  # making rectangle for the face
        # cv2.rectangle(img2, (x1, y2 ), (x2, y2+35), (0, 255, 0), cv2.FILLED)  # making rectangle for the name
        cv2.putText(imgs, name, (x1-25 , y2 + 25), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255),2)  # inserting name on picture
        cv2.imshow("camera",imgs)
        cv2.waitKey(0)
    else:
        y1, x2, y2, x1 = loc0  # getting face location
        # y1, x2, y2, x1 = y1 * 4 , x2 * 4 , y2 * 4, x1 * 4  # making its size normal
        cv2.rectangle(imgs, (x1, y1), (x2, y2), (0, 255, 0), 2)  # making rectangle for the face
        # cv2.rectangle(img2, (x1, y2 ), (x2, y2+35), (0, 255, 0), cv2.FILLED)  # making rectangle for the name
        cv2.putText(imgs, "not matched!!!!!", (x1 - 25, y2 + 25), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255),
                    2)  # inserting name on picture
        cv2.imshow("camera", imgs)
        cv2.waitKey(0)


