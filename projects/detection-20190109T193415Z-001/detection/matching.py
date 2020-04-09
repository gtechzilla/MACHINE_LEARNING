import cv2
import pickle
#import mysql.connector
#from mysql.connector import errorcode


def match():

    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

    # face recognizer module
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    # face trained file
    recognizer.read("./recognizers/face-trainer.yml")

    # create label dictionary from pickle labels
    labels = {"person": 1}
    with open("pickles/labels.pickle", "rb") as f:
        first_labels = pickle.load(f)
        # we invert to use id_ as our call out value
        # noinspection PyRedeclaration
        labels = {v: k for k, v in first_labels.items()}

    cap = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        # if we are viewing a video and we did not grab a frame,
        # then we have reached the end of the video
        if frame is None:
           break
  
        faces = face_cascade.detectMultiScale(frame)
        for (x, y, w, h) in faces:
            # print(x,y,w,h)
            # (ycord_start, ycord_end)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w]

            # recognizing
            id, conf = recognizer.predict(roi_gray)
            if conf <= 70:
                # print(conf)
                # print(id)
                # print(labels[id])
                font = cv2.FONT_HERSHEY_SIMPLEX
                name = labels[id]
                color = (255, 255, 255)
                stroke = 2
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                cv2.putText(frame, name, (x, y), font, 1, color, stroke, cv2.LINE_AA)
                cv2.putText(frame, "ID: " + str(id), (10, 23), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
                cv2.putText(frame, "NAME: " + str(name), (10, 46), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)

                #  sending data to db
                cnx = mysql.connector.connect(database='detection',
                                              user='root', )
                mycursor = cnx.cursor()
                mycursor.execute("INSERT INTO logs(StudentID, Name) VALUES(%s,%s)", (id, name))
                cnx.commit()
                print(mycursor.rowcount, "record inserted.")

                eyes = eye_cascade.detectMultiScale(roi_gray)
                for (ex, ey, ew, eh) in eyes:
                    cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

                cv2.imshow('frame', frame)

            # else:
            #     cv2.putText(frame, "Not Authorised", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)
            #     # cv2.putText(frame, "Not Authorised", (10, 23), (255, 255, 255), 1)
            #
            #     cv2.imshow('frame', frame)

            if cv2.waitKey(20) & 0xFF == ord('q'):
                break

    # When everything done, release the capture

        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    match()

