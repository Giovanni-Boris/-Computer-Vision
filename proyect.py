import cv2

#Iniciamos camara
vc = cv2.VideoCapture(0)
# Creating the cascade objects
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye_tree_eyeglasses.xml")
while True:
  #Capturamos video frame a frame
  ret, frame = vc.read()
  if ret==False:
    break 
  if frame is not None:
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
      cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
      roi_gray = gray[y:y + h, x:x + w]
      roi_color = frame[y:y + h, x:x + w]
      eyes = eye_cascade.detectMultiScale(roi_gray)
      for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

  #Convertimos a escala de grises
  #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  #Mostramos el frame capturado
  cv2.imshow('Video', frame)

  #Si pulsamos q finalizamos'
  if  cv2.waitKey(1) & 0xFF==ord("q"):
    break;
#Finalizamos camara  y cerramos ventana
vc.release()
cv2.destroyAllWindows()

