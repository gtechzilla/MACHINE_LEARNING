import cv2,os
import numpy as np
from PIL import Image
import sqlite3
import urllib
recognizer =  cv2.face.LBPHFaceRecognizer_create()
detector= cv2.CascadeClassifier('cascades_/haarcascade_frontalface_default.xml')
#url="http://192.168.0.19:8080/shot.jpg"

def getImagesAndLabels(path):
    #get the path of all the files in the folder
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
    #create empth face list
    faceSamples=[]
    #create empty ID list
    Ids=[]
    #now looping through all the image paths and loading the Ids and the images
    for imagePath in imagePaths:
        #loading the image and converting it to gray scale
        pilImage=Image.open(imagePath).convert('L')
        #Now we are converting the PIL image into numpy array
        imageNp=np.array(pilImage,'uint8')
        #getting the Id from the image
        Id=int(os.path.split(imagePath)[-1].split(".")[1])
        # extract the face from the training image sample
        faces=detector.detectMultiScale(imageNp)
        #If a face is there then append that in the list as well as Id of it
        for (x,y,w,h) in faces:
            faceSamples.append(imageNp[y:y+h,x:x+w])
            Ids.append(Id)
    return faceSamples,Ids


faces,Ids = getImagesAndLabels('dataset')
recognizer.train(faces, np.array(Ids))
#recognizer.save('trainner.yml')

def get_profile(id):
    conn=sqlite3.connect("my_users.db")
    cmd="SELECT * FROM people WHERE ID=" + str(id)

    cursor=conn.execute(cmd)
    profile=None
    for row in cursor:
        profile=row
    conn.close()
    return profile



def face_detector(img, size=0.5):
    #convert image to grayscale
    gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    faces=detector.detectMultiScale(gray,1.3,5)
    if faces is ():
        return img,[]

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        roi=img[y:y+h,x:x+w]
        roi=cv2.resize(roi,(200,200))
    return img,roi

cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    #imgRSP=urllib.urlopen(url)
    #imgNP=np.array(bytearray(imgRSP.read()),dtype=np.uint8)
    #frame=cv2.imdecode(imgNP,-1)
    #frame=cv2.resize(frame,None,fx=2,fy=1.5,interpolation=cv2.INTER_LINEAR)


    frame=cv2.flip(frame,1)
    cv2.rectangle(frame,(0,0),(635,112),(0,0,0),-2)

    image,face=face_detector(frame)

    try:
        face=cv2.cvtColor(face,cv2.COLOR_RGB2GRAY)

        #pass face to prediction model
        #"result comprises of a tuple containing the label and the confidence value"
        iden,result=recognizer.predict(face)
        ID=iden

        data=get_profile(ID)
        #print(profile)

        if (data!= None):
            cv2.putText(image,"NAME: "+str(data[1]),(10,46),cv2.FONT_HERSHEY_COMPLEX,0.4,(255,255,255),1)
            cv2.putText(image,"SEX :"+str(data[3]),(10,86),cv2.FONT_HERSHEY_COMPLEX,0.4,(255,255,255),1)
            cv2.putText(image,"ID : "+str(data[0]),(211,46),cv2.FONT_HERSHEY_COMPLEX,0.4,(255,255,255),1)
            cv2.putText(image,"AGE : "+str(data[2]),(375,86),cv2.FONT_HERSHEY_COMPLEX,0.4,(255,255,255),1)
            cv2.putText(image,"STATUS : FACE DETECTED",(336,46),cv2.FONT_HERSHEY_COMPLEX,0.4,(255,255,255),1)





        if result < 500:
            confidence=int(100*(1-(result)/300))
            display_string="CONFIDENCE : "+ str(confidence) +"%"
            cv2.putText(image,display_string,(165,86),cv2.FONT_HERSHEY_COMPLEX,0.4,(255,255,255),1)
            #cv2.putText(image,str(data[1]),(30,46),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
            #cv2.putText(image,str(data[3]),(70,46),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)


        if confidence>75:
            cv2.putText(image,"UNLOCKED",(10,16),cv2.FONT_HERSHEY_COMPLEX,0.7,(255,255,255),1)

            cv2.putText(image,"NAME: "+str(data[1]),(10,46),cv2.FONT_HERSHEY_COMPLEX,0.4,(255,255,255),1)
            cv2.putText(image,"SEX :"+str(data[3]),(10,86),cv2.FONT_HERSHEY_COMPLEX,0.4,(255,255,255),1)
            cv2.putText(image,"ID : "+str(data[0]),(211,46),cv2.FONT_HERSHEY_COMPLEX,0.4,(255,255,255),1)
            cv2.putText(image,"AGE : "+str(data[2]),(375,86),cv2.FONT_HERSHEY_COMPLEX,0.4,(255,255,255),1)
            cv2.putText(image,"STATUS : UNKNOWN",(336,46),cv2.FONT_HERSHEY_COMPLEX,0.4,(255,255,255),1)





            #cv2.imshow("face cropper",image)





        else:
            cv2.putText(image,"LOCKED",(10,16),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0),1)


        cv2.imshow("Face cropped",image)
        print(result)


    except:
        cv2.putText(image,"STATUS : NO FACE FOUND",(336,46),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
        cv2.putText(image,"LOCKED",(10,16),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0),1)
        cv2.putText(image,"NAME: ",(10,46),cv2.FONT_HERSHEY_COMPLEX,0.4,(255,255,255),1)
        cv2.putText(image,"SEX :",(10,86),cv2.FONT_HERSHEY_COMPLEX,0.4,(255,255,255),1)
        cv2.putText(image,"ID : ",(211,46),cv2.FONT_HERSHEY_COMPLEX,0.4,(255,255,255),1)
        cv2.putText(image,"AGE : ",(375,86),cv2.FONT_HERSHEY_COMPLEX,0.4,(255,255,255),1)

        cv2.imshow("Face cropped",image)

    if cv2.waitKey(1)==13:
        break

cap.release()
cv2.destroyAllWindows()
