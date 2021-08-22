# Chương trình giúp nhận diện khuôn mặt cơ bản

import dlib   
import cv2
from google.colab.patches import cv2_imshow     #load ảnh trong collab

!curl -o face_recognition.jpg https://static1.dienanh.net/upload/202108/2x1_987bb697-5c03-4ec6-9f09-85b08a08c4f0.jpg
#read the image
img = cv2.imread("face_recognition.jpg", cv2.IMREAD_UNCHANGED)

#covert image to Grayscale
gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)

#dlib: Load Face Recognition Ditector
face_ditector = dlib.get_frontal_face_detector()     #module nhận diện khuôn mặt

#use ditector to find the face landmarks (điểm nổi trên mặt)
faces = face_ditector(gray)
print(f"To have {len(faces)} faces")

#Sử dụng tọa độ trên mặt để vẽ các đường chấm (AI)
for face in faces:
  x1 = face.left()    #left point
  y1 = face.top()     #top point
  x2 = face.right()   #right point
  y2 = face.bottom()  #bottom point

  #Draw a rectangle (đương viền)
  cv2.rectangle(img = img, pt1=(x1, y1), pt2=(x2, y2), color=(0, 255, 0), thickness=2)


#show the image
#cv2_imshow(winname="Face Recognition App", mat=img)    #bị lỗi trong collab
cv2_imshow(img)

#wait for a key press to quit (nhấn bất cứ phím nào để log out)
cv2.waitKey(delay=0)

#close on the window
cv2.destroyAllWindows()