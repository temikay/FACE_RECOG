from symbol import parameters

import cv2
import numpy as np
import sqlite3

from cv3 import imshow

faceDetect = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

cam = cv2.VideoCapture(0)


def insertorupdate(Id,Name, age):       #funcion is for sqlite database
    conn = sqlite3.connect("sqlite.db") #connecct database
    cmd = "SELECT * FROM STUDENTS WHERE ID = "+str(Id)
    cursor = conn.execute(cmd) #cursor to execute
    isRecordexist=0     #assume there is nor record in our table
    for row in cursor:
        isRecordexist = 1
    if (isRecordexist == 1):
        conn.execute("UPDATE STUDENTS SET Name = ? WHERE Id = ?",(Name, Id, ))
        conn.execute("UPDATE STUDENTS SET age = ? WHERE Id = ?",(age, Id))
    else:
        conn.execute("INSERT INTO STUDENTS (Id, Name, age) values(?, ? ,?)" ,(Id, Name, age))

    conn.commit()
    conn.close()


#Insert User-defined values into table

Id =  input('Enter User Id: ')
Name = input('Enter User Name: ')
age = input('Enter User age: ')

insertorupdate(Id, Name, age)

#detect face in web camera coding

sampleNum =0
while True:
    ret,img = cam.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(gray, scaleFactor=1.3, minNeighbors = 5)
    for (x,y,w,h) in faces:
        sampleNum = sampleNum+1
        cv2.imwrite("dataset/user."+str(Id)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,255, 0) ,2)
    cv2.imshow("Face", img)
    cv2.waitKey(1)
    if sampleNum > 20:    #if the dataset is > 20 break
            break
cam.release()
cv2.destroyAllWindows()     #quit


#download hairCascade