import cv2
import numpy as np
import os
import sqlite3

facedetect = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cam = cv2.VideoCapture(0)

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("recognizer/trainingdata.yml")

def getprofile(id):
    conn = sqlite3.connect("sqlite.db")
    cmd = "SELECT * FROM STUDENTS WHERE ID = "+str(id)
    cursor = conn.execute(cmd)
    profile = None
    for row in cursor:
        profile = row
    conn.close()
    return profile

if not cam.isOpened():
    print("Error: Camera could not be opened.")
else:
    while True:
        ret, img = cam.read()
        if not ret:
            print("Failed to grab frame")
            break

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = facedetect.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            id, conf = recognizer.predict(gray[y:y + h, x:x + w])
            profile = getprofile(id)
            print(profile)
            if (profile != None):
                cv2.putText(img, "Name:" + str(profile[1]), (x, y + h + 20), cv2.FONT_HERSHEY_SIMPLEX, 1,
                            (255, 255, 255), 2)
                cv2.putText(img, "Age:" + str(profile[2]), (x, y + h + 45), cv2.FONT_HERSHEY_COMPLEX, 1,
                            (255, 255, 255), 2)

        cv2.imshow("FACE", img)
        if cv2.getWindowProperty("FACE", cv2.WND_PROP_VISIBLE) < 1:
            break

        if cv2.waitKey(1) == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()
