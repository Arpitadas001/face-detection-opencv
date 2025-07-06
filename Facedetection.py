import cv2

print("OpenCV version:", cv2.__version__)

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

webcam = cv2.VideoCapture(0)

while True:
    success, img = webcam.read()
    if not success:
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.6, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0),3)

    cv2.imshow("Face Detection", img)

    key = cv2.waitKey(10)
    if key == 27:  # Esc key to exit
        break

# ✅ After loop ends, cleanup
webcam.release()
cv2.destroyAllWindows()
#https://github.com/Arpitadas001/face-detection-opencv.git
