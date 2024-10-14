import os
import cv2
import numpy as  np
from PIL import Image
import face_recognition


recognizer = cv2.face.LBPHFaceRecognizer_create()   #it recognizes the faces in the camera
path = "dataset"


def get_images_with_id(path):
    images_paths = [os.path.join(path, f) for f in os.listdir(path)]
    faces = []
    ids = []
    for single_image_path in images_paths:
        faceImg = Image.open(single_image_path).convert('L')
        # face_recognition.load_image_file(single_image_path)

        faceNp = np.array(faceImg, np.uint8)
        id = int(os.path.split(single_image_path)[-1].split(".")[1])
        print(id)
        faces.append(faceNp)
        ids.append(id)
        cv2.imshow("Training", faceNp)
        cv2.waitKey(100)

        # face_encoding = face_recognition.face_encodings(faceImg)
        #
        # if face_encoding:
        #     faces.append(face_encoding[0])
        #     ids.append(id)

    return np.array(ids) ,faces

ids, faces = get_images_with_id(path)
recognizer.train(faces, ids)
# for ids, face in zip(ids, faces):
#     recognizer[id] = face

recognizer.save("recognizer/trainingdata.yml")
print("Training data saved")
cv2.destroyAllWindows()

