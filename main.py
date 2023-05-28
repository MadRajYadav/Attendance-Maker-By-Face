import cv2
import face_recognition
import numpy as np
import os
from datetime import datetime


def faceEncodings(images):  # for encoding the picture into 128 value
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # converting BGR into RGB because cv2 reads in BGR format
        encode = face_recognition.face_encodings(img)[0] #for incoding || hog algorithm is used to encode by face_encoding
        encodeList.append(encode) # storing the encode value into encodeList
    return encodeList   # returning encodeList

def attendance(name):
    with open('attendance.csv','r+') as f: # opening attendance file as f
        myDataList = f.readlines()   # reading the data of the file
        nameList= []
        dateList = []
        index = 0
        for line in myDataList:
            #print(line)
            entry = line.split(',') # splitting the comma separated data
            nameList.append(entry[0])   # storing the name of a picture into a variable
            dateList.append(entry[2])
        time_now = datetime.now()  # storing date and time into time_now variable
        time = time_now.strftime('%H:%M:%S')  # storing time into time variable
        date = time_now.strftime('%d/%m/%Y')  # storing date into date variable // %I/%M/%S/%P == am/pm is returns

        if name not in nameList and name != '':
            f.writelines(f'{name},{time},{date}\n')  # writing attendance into the attendance file
            print(f'{name}, your attendance is taken.')
        elif name in nameList:
            for i in range(len(nameList)):
                if name in nameList[i]:
                   index = i
            if date not in dateList[index] and name in nameList[index]:
                f.writelines(f'{name},{time},{date}\n')  # writing attendance into the attendance file
                print(f'{name}, your attendance is taken.')
        else:
            print(f'{name}, your attendance has been already taken.')
    f.close()

imgPath = 'picture'
images = []
personName = []
myList = os.listdir(imgPath)# it contains the all picture
# print(myList)
# this loop is only for getting the pictures or images and their names from the picture file
print(myList)
for cu_img in myList:
    current_img = cv2.imread(f'{imgPath}/{cu_img}') #reading the picture from the file
    images.append(current_img)  # storing the pictue into images variable
    personName.append(os.path.splitext(cu_img)[0])# getting name throuh the picture name
#print(personName)

# print(faceEncodings(images))
encodeListKnown = faceEncodings(images) # calling faceEncodings() to encode images
print("All encoding complete!!!!!")

videoCap = cv2.VideoCapture(0) # reading images from camera
while True:
    success, cameraFrame = videoCap.read()  # reading frame into cameraFrame variable
    faces = cv2.resize(cameraFrame, (0, 0), None, 0.25, 0.25)    # resizing the frame as 1/4th part
    faces = cv2.cvtColor(faces, cv2.COLOR_BGR2RGB)  # converting the color

    facesCurrentFrame = face_recognition.face_locations(faces)  #   getting face location from picture
    encodesCurrentFrame = face_recognition.face_encodings(faces, facesCurrentFrame) # encoding the current picture

    for encodesFace, faceLock in zip(encodesCurrentFrame, facesCurrentFrame): #zip function used to pass more than 1 varable into for loop
        matches = face_recognition.compare_faces(encodeListKnown, encodesFace)  # comparing current encoded image into file's incoded image
        faceDis = face_recognition.face_distance(encodeListKnown, encodesFace)  # getting distance of both encoded picture

        matchIndex = np.argmin(faceDis)     #  getting index number of matched piture
        #print(matchIndex)

        if matches[matchIndex]:
            name = personName[matchIndex]   # getting name of the image by its indexed number
            if name == '':
                y1, x2, y2, x1 = faceLock  # getting face location
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4  # making its size normal
                cv2.rectangle(cameraFrame, (x1, y1), (x2, y2), (0, 255, 0), 2)  # making rectangle for the face
                # cv2.rectangle(cameraFrame,(x1+20,y2-35), (y2+35,y2),(0,255,0),cv2.FILLED) # making rectangle for the name
                cv2.putText(cameraFrame, 'Unknown!!!', (x1 + 6, y2 + 6), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)  # inserting name on picture
            else:
                y1, x2, y2, x1 = faceLock   # getting face location
                y1, x2, y2, x1  = y1*4, x2*4, y2*4, x1*4    # making its size normal
                cv2.rectangle(cameraFrame, (x1,y1), (x2,y2), (0,255,0), 2)  #  making rectangle for the face
                # cv2.rectangle(cameraFrame,(x1+20,y2-35), (y2+35,y2),(0,255,0),cv2.FILLED) # making rectangle for the name
                cv2.putText(cameraFrame, name, (x1+6, y2+6),cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255),2) #  inserting name on picture
                attendance(name)
        cv2.imshow("camera", cameraFrame) # showing the camera on screen
        if cv2.waitKey(1) & 0xFF==ord('q') : # for terminating the program
            videoCap.release()  # releasing the camera
            cv2.destroyAllWindows()
            break



