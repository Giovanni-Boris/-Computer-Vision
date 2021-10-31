#Importación de recursos
import cv2
import numpy as np

#Iniciamos camara
vc = cv2.VideoCapture(0)

while True:
  #Capturamos video frame a frame
  ret, frame = vc.read()
  if ret==True:
    #Convertimos a escala de grises
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frameHSV=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    #Mostramos el frame capturado
    cv2.imshow('Video', frame)

    #Si pulsamos q finalizamos'
    if  cv2.waitKey(1) & 0xFF==ord("q"):
      break;
#Finalizamos camara  y cerramos ventana
vc.release()
cv2.destroyAllWindows()

