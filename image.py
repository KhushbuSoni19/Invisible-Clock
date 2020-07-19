import cv2
cap = cv2.VideoCapture(0) #this is my webcam
while cap.isOpened():#camera is open
    ret, back = cap.read()#this is simple reading from webcam
    if ret:
        #ret = what u r reading is successfull or not
        #back = what is camera reading
        cv2.imshow("image", back)
        if cv2.waitKey(5) == ord('q'):#press the key
            cv2.imwrite('img/khushbu.png', back)#save the image
            break
cap.release()
cv2.destroyAllWindows()
