import os
import cv2
import numpy as np
from PIL import Image
import pickle


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, "images")


def train():

    face_cascade = cv2.CascadeClassifier('C:/Python36/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('C:/Python36/Lib/site-packages/cv2/data/haarcascade_eye.xml')

    # face recognizer module
    recognizer = cv2.face.LBPHFaceRecognizer_create()

    label_ids = {}
    y_labels = []
    x_train = []

    for root, dirs, files in os.walk(image_dir):
        for file in files:
            if file.endswith("png") or file.endswith("jpg") or file.endswith("jpeg"):
                # get path to images
                path = os.path.join(root, file)
                # get path to folders in images which are labels to the respective images
                label = os.path.basename(os.path.dirname(path)).lower()
                # print(label, path)
                labelid = os.path.basename(path)
                # print(labelid)
                # getting the ID
                Id = int(os.path.split(labelid)[1].split(".")[0])
                # print(Id)

                if label not in label_ids:
                    label_ids[label] = Id
                id = label_ids[label]

                # to grayscale
                pil_image = Image.open(path).convert("L")

                # resizing image to increase accuracy
                size = (550, 550)
                final_image = pil_image.resize(size, Image.ANTIALIAS)

                # convert image to numpy array values
                image_array = np.array(pil_image, "uint8")
                # print(image_array)
                faces = face_cascade.detectMultiScale(image_array, scaleFactor=1.3, minNeighbors=5)

                for (x, y, w, h) in faces:
                    roi = image_array[y:y + h, x:x + w]
                    x_train.append(roi)
                    y_labels.append(id)
                    cv2.namedWindow('Faces training', cv2.WINDOW_NORMAL)
                    cv2.resizeWindow('Faces training', 300, 300)
                    cv2.imshow("Faces training", roi)
                    cv2.waitKey(1)

                with open("pickles/labels.pickle", "wb") as f:
                    pickle.dump(label_ids, f)

    recognizer.train(x_train, np.array(y_labels))
    recognizer.save("recognizers/face-trainer.yml")

    cv2.destroyAllWindows()


if __name__ == "__main__":
    train()
