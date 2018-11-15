# Face-Eye-Detection-Haar-Cascade-Classifier
Face and Eye Detection Technique using Raspberry Pi with Pi camera. 
# Goals
-To introduce with OpenCV </br>
-Interface Pi camera with Raspberry Pi and test the camera</br>
-Detect human face and eye using Haar Cascade classifier
# Description 
Here, this project is done using OpenCV with python, Raspberry Pi and Pi camera. I used Haar features based cascade classifier where a cascade function is trained from a lot of positive and negative images. 
### Negative Images: 
Actually, negative images/background samples/background images are the image that doesn't contain the 'desired object'. And these samples will be used to train the machine, what not to look for when searching for the desired object.
### Positive images: 
Actually, these are images we are looking for. 
# Creating own classifier
As we know OpenCV can be used as a trainer as well as a detector. So, we can train our own classifier for any object using OpenCV by following the steps from here: [Cascade Classifier Training](https://docs.opencv.org/3.3.0/dc/d88/tutorial_traincascade.html). 
#### OR
By following these steps from here: [Creating a Cascade of Haar-Like Classifier: Step by Step](https://www.cs.auckland.ac.nz/~m.rezaei/Tutorials/Creating_a_Cascade_of_Haar-Like_Classifiers_Step_by_Step.pdf)

But as OpenCv conatains many pre-trained classifier, I have used form those pre-trained. 
# Procedures
## Camera Test
At first we have to test is our ready to perform. I imported OpenCv in python. Then capture video by using this command: </br>
-vdo = cv2.VideoCapture(0) #here indexing 0 indicates my first camera</br>
-retu, img_frame = vdo.read()#it's return boolean true and false</br>
We can convert our real image into gray scale by using this command: </br>
-gray = cv2.cvtColor(img_frame, cv2.COLOR_BGR2GRAY)</br>
then to show our original and gray scale image :</br>
-cv2.imshow('img_frame', img_frame) #original image </br>
-cv2.imshow('gray', gray)# gray image</br>
## Face and Eye Detection
Now, as our camera is okay so we are ready for face and eye detetction. Here we have used building cascade classifier form OpenCv. </br>

-face_c = cv2.CascadeClassifier('Cascades/haarcascade_frontalface_default.xml')</br>
eye_c = cv2.CascadeClassifier('haarcascade_eye.xml')</br>

#we may create our own classifier but here I have used trained classifier from OpenCv </br>
Then We have to call our classifier function, passing to some very important parameters like scale factor, number of neighbours and minimum size of the detected face. </br>
- faces = face_c.detectMultiScale(gray, 1.3, 5)</br>
- eyes = eye_c.detectMultiScale(roi_gray)</br>
        

Whenever, a face is detected a rectecngular box indicates the face region.</br> 
-for (x,y,w,h) in faces:     # (x,y) coordinate of the left upper position to draw the rectangle</br> 
        cv2.rectangle(img_flim,(x,y),(x+w,y+h),(255,0,0),2) # draw a rectangle indicating face</br>
        roi_gray = gray[y:y+h, x:x+w]</br>
        roi_color = img_flim[y:y+h, x:x+w]</br> 
         
and Whenevr, eye is detected .........
-for (ex,ey,ew,eh) in eyes:</br>
-cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
