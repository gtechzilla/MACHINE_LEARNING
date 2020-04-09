import numpy as np
import cv2
import os
import sys

face_cascade = cv2.CascadeClassifier('C:/Python36/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('C:/Python36/Lib/site-packages/cv2/data/haarcascade_eye.xml')


def faceID(StudentID, Name):
    # StudentID = input("Enter Student ID: ")
    # Name = input("Enter Name: ")

    # if request.method == "POST":
    # StudentID = request.form["studentid"]
    # Name = request.form["name"]

    count = 0
    cap = cv2.VideoCapture(0)

    while True:
        # capture video frame
        ret, img = cap.read()

        # create gray filter and map rectangle to faces
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
        # print("Found {0} faces!".format(len(faces)))

        # faces
        for (x, y, w, h) in faces:
            print(x, y, w, h)
            # (ycord_start, ycord_end) (xcord_start, xcord_end)
            roi_gray = gray[y:y + h, x:x + w]
            # use frame or img
            roi_color = img[y:y + h, x:x + w]
            # resizing the gray image
            face1 = cv2.resize(roi_gray, (200, 200))
            # resizing the color image
            face2 = cv2.resize(roi_color, (200, 200))

            # incrementing sample number
            count = count + 1

            # creating folder from input
            FolderPath = "C:/Users/MUGWE/Documents/FALL 2018/APT4900/detection/images/" + Name
            while FolderPath:
                if not os.path.exists(FolderPath):
                    os.makedirs(FolderPath)
                    for root, dirs, files in os.walk("images"):
                        for file in files:
                            if file.endswith("png") or file.endswith("jpg") or file.endswith("jpeg"):
                                # img_item = (StudentID + "." + str(count) + ".jpg")
                                newpath = os.path.join(FolderPath, file)
                                # print(newpath)
                                cv2.imwrite(newpath, face2)
                                # + StudentID + "." + str(count) + ".jpg"

            # cv2.imwrite("C:/Users/MUGWE/Documents/FALL 2018/APT4900/project/detection/images/newton/" + StudentID +
            #             "." + str(count) + ".jpg", face2)

            # end_cord y and x, color, thickness of rectangle
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        # else:
        #     print("Keep your head facing the camera")

        # eyes
        eyes = eye_cascade.detectMultiScale(gray)
        for (ex, ey, ew, eh) in eyes:
            # end_cord y and x, color, thickness of rectangle
            cv2.rectangle(img, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

        # display the frame
        cv2.imshow('frame', img)
        cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
        cv2.putText(img, "TAKING IMAGES!!", (10, 16), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
        cv2.imshow('frame', img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        # break if the sample number is more than 10
        elif count > 10:
            break

    # When finished or if stopped release the captures
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    faceID()
