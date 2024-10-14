import types

# Create a new submodule
face_module = types.ModuleType('face')


# Create a custom function for the submodule
def LBPHFaceRecognizer_create():
    print("This would create an LBPH face recognizer")
    return "LBPHFaceRecognizer instance"


# Add the function to the submodule
face_module.LBPHFaceRecognizer_create = LBPHFaceRecognizer_create

# Attach the submodule to cv2
import cv2

cv2.face = face_module

# Using the newly added submodule
recognizer = cv2.face.LBPHFaceRecognizer_create()
print(recognizer)