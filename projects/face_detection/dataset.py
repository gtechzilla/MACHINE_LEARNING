import cv2
import numpy as np 
import sqlite3
import urllib

<<<<<<< HEAD
url="http://10.42.0.145:8080/shot.jpg"
cam = cv2.VideoCapture(url)
detector=cv2.CascadeClassifier('cascades_/haarcascade_frontalface_default.xml')

=======
cam = cv2.VideoCapture(0)
detector=cv2.CascadeClassifier('cascades_/haarcascade_frontalface_default.xml')
#url="http://192.168.0.19:8080/shot.jpg"
>>>>>>> 785ddf862d473beadd8e6119082f6ce8aa02557c

def include_update(Id,name):
	conn=sqlite3.connect("my_users.db")
	cmd="SELECT * FROM people WHERE ID="+str(Id)
	cursor=conn.execute(cmd)
<<<<<<< HEAD
	recordExist=0
	for row in cursor:
		recordExist=1

	if (recordExist==1):
=======
	RecordExist=0
	for row in cursor:
		RecordExist=1

	if (RecordExist==1):
>>>>>>> 785ddf862d473beadd8e6119082f6ce8aa02557c
		cmd="UPDATE people SET Name="+ str(name)+"WHERE ID="+str(Id)

	else:
		cmd="INSERT INTO people(ID,Name) Values("+str(Id)+","+str(name)+")"

	conn.execute(cmd)
	conn.commit()
	conn.close()



Id=input("enter your id: ")
name=input("Enter Name: ")
include_update(Id,name)
count=0

while(True):
    ret, img = cam.read()
    #imgRSP=urllib.urlopen(url)
    #imgNP=np.array(bytearray(imgRSP.read()),dtype=np.uint8)
    #img=cv2.imdecode(imgNP,-1)
    img=cv2.flip(img,1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        
        #incrementing sample number 
        count=count+1
        gray1=gray[y:y+h,x:x+w]

        face1=cv2.resize(gray1,(200,200))
        #saving the captured face in the dataset folder
        cv2.imwrite("dataset/user."+Id+"."+str(count)+".jpg",face1) #

        cv2.imshow('frame',img)
    #wait for 100 miliseconds 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    # break if the sample number is morethan 20
    elif count>100:
        break

cam.release()
cv2.destroyAllWindows()


