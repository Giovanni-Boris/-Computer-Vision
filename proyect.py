import cv2

#Iniciamos camara
vc = cv2.VideoCapture(0)

while True:
  #Capturamos video frame a frame
  ret, frame = vc.read()
  if ret==False:
    break

  cv2.imshow('Video', frame)
  if  cv2.waitKey(1) & 0xFF==ord("q"):
    break;
#Finalizamos camarai,grabacion y cerramos ventana
vc.release()
cv2.destroyAllWindows()

