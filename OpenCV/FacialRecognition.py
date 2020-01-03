import cv2

#img = cv2.imread('ellen-page.jpg', 1)
img = cv2.imread('group-photo.png', 1)
resized = cv2.resize(img, (600, 600))
#cv2.imshow('Resized Group Photo', resized)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#gray_img = cv2.imread('ellen-page.jpg', cv2.COLOR_BGR2GRAY)
# print(img)
print(img.shape)

#cv2.imshow('Ellen Page', img)
#cv2.imshow('Ellen Page Resized', resized)
faces = face_cascade.detectMultiScale(resized, scaleFactor=1.05, minNeighbors=5)
# print(faces)
#cv2.imshow('Ellen Page detected', faces)
#for x, y, w, h in faces:
    #img_detection = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
#cv2.imshow('Ellen Page Detected', img_detection)
for x, y, w, h in faces:
    img_detection = cv2.rectangle(resized, (x, y), (x+w, y+h), (0, 255, 0), 3)
cv2.imshow('Group Photo', img_detection)
cv2.waitKey(0)
cv2.destroyAllWindows()


