#Importación de recursos
import cv2
import numpy as np

#Iniciamos camara
vc = cv2.VideoCapture(0)
#Marcador 
azulBajo02 = np.array([100,100,20],np.uint8)   
azulAlto02 = np.array([125,255,255],np.uint8) 
#Colores para pintar
verde = (0,255,36)
rosa = (128,0,255)
celeste = (255,113,82)
amarillo  = (89,222,255)
borrador = (29,112,246)
#Grosor de las  lineas de recuadros de color
grosorVerde =5
grosorAmarillo=2
grosorCeleste=2
grosorRosa=2
#Grosor de recuadros para el grosor del marcador
litle = 7
midle = 1
big = 1
#Valores por defecto cuando se prende la camara
color = verde  #Color de entrada
grosor = 4 #Grosor del marcador
#Coordenadas
x = None
y = None
#Espacio para dibujar
aux = None
while True:
  #Capturamos video frame a frame
  ret, frame = vc.read()
  if ret==True:
    frame = cv2.flip(frame,1)
    frameHSV=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(frameHSV,azulBajo02,azulAlto02)
    #Deteccion de contornos
    contornos,_ = cv2.findContours(mask,cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)
    #Dibujar las contornos
    #cv2.drawContours (frame, contornos, -1, (255,0,0), 3)
    #Eliminado algunos contornos no deseados
    for i in contornos:
      area=cv2.contourArea(i)
      if area>3000:
        M=cv2.moments(i)
        if(M["m00"]==0): M["m00"]=1
        x=int(M["m10"]/M["m00"])
        y=int(M["m01"]/M["m00"])
        cv2.circle(frame,(x,y),7,(0,255,0),-1)
        font=cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame,'{},{}'.format(x,y),(x+10,y),font,0.75,
            (0,225,0),1,cv2.LINE_AA)
        nuevoContorno=cv2.convexHull(i)

        cv2.drawContours(frame,[nuevoContorno],0,(125,0,0),3)
    #En la imagen frameHSV vamos a encontrar los rango bajo01 y alto 1 los mismo para 2
    #firstRed1=cv2.inRange(frameHSV,redBajo01,redAlto01)
    #secondRed2=cv2.inRange(frameHSV,redBajo02,redAlto02)
    #Adicionar las dos para convertirla en una solo y me detecte el rojo
    #unity=cv2.add(firstRed1,secondRed2)
    #En vez de blanco mostrar el color real 
    #unityOriginal=cv2.bitwise_and(frame,frame,mask=unity)
    #cv2.imshow("unityOriginal",unityOriginal)
    #Visualiazacion detección de los colores
    #cv2.imshow("Mascara",mask)
    #Mostramos el frame capturado
    cv2.imshow('Video', frame)

    #Si pulsamos q finalizamos'
    if  cv2.waitKey(1) & 0xFF==ord("q"):
      break;
#Finalizamos camara  y cerramos ventana
vc.release()
cv2.destroyAllWindows()

