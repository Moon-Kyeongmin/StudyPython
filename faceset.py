import cv2
import numpy as np
from PIL import Image
import os

path='dataset'
recognizer=cv2.face.createLBPHFaceRecognizer()
detector=cv2.CascadeClassifier('/home/pi/facedetection/haarcascade_frontalface_default.xml')

def getImagesAndLabels(path):
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
    faceSamples=[]
    ids=[]
    for imagePath in imagePaths:
        PIL_img=Image.open(imagePath).convert('L')
        img_numpy=np.array(PIL_img,'uint8')
        id=int(os.path.split(imagePath)[-1].split(".")[1])
        faces=detector.detectMultiScale(img_numpy)
        for (x,y,w,h) in faces:
            faceSamples.append(img_numpy[y:y+h,x:x+w])
            ids.append(id)
    return faceSamples,ids

print("Training...")
faces,ids=getImagesAndLabels(path)

recognizer.train(faces,np.array(ids))
recognizer.save('trainer.yml')

print("\n{0}".format(len(np.unique(ids))))