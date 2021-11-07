#Importación de recursos
import cv2
import numpy as np

#Iniciamos camara
vc = cv2.VideoCapture(0)
#Marcador 
azulBajo02 = np.array([110,100,20],np.uint8)   
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
x1 = None
y1 = None
#Espacio para dibujar
aux = None
while True:
  #Capturamos video frame a frame
  ret, frame = vc.read()
  if ret==True:
    #Efecto espejo
    frame = cv2.flip(frame,1)
    frameHSV=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #Creacion de matriz de ceros igual que el frame
    if aux is None:
      aux=np.zeros(frame.shape,dtype=np.uint8)
    #Creando rectangulos de colores
    cv2.rectangle(frame,(0,0),(50,50),verde,grosorVerde)
    cv2.rectangle(frame,(0,60),(50,100),rosa,grosorRosa)
    cv2.rectangle(frame,(0,110),(50,150),celeste,grosorCeleste)
    cv2.rectangle(frame,(0,160),(50,200),amarillo,grosorAmarillo)
    #Borrador
    cv2.rectangle(frame,(300,0),(400,50),borrador,1)
    cv2.putText(frame,"Borrador",(320,20),6,0.6,borrador,1,cv2.LINE_AA)
    #Grosores
    cv2.rectangle(frame,(1220,0),(1270,50),(0,0,0),litle)
    cv2.circle(frame,(1245,25),3,(0,0,0),-1)
    cv2.rectangle(frame,(1220,60),(1270,100),(0,0,0),midle)
    cv2.circle(frame,(1245,80),7,(0,0,0),-1)
    cv2.rectangle(frame,(1220,110),(1270,150),(0,0,0),big)
    cv2.circle(frame,(1245,130),11,(0,0,0),-1)
    #Deteccion de celeste
    mask = cv2.inRange(frameHSV,azulBajo02,azulAlto02)
    #Transformacione morfologicas para mejorar imagen binaria
    mask = cv2.erode(mask,None,iterations=1)
    mask = cv2.dilate(mask,None,iterations=2)
    #Suavizando colores
    mask = cv2.medianBlur(mask,13)
    #Deteccion de contornos
    contornos,_ = cv2.findContours(mask,cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)
    #Contorno mas grande segun su area
    contornos = sorted(contornos,key=cv2.contourArea,reverse=True)[:1]
    #Dibujar las contornos
    #cv2.drawContours (frame, contornos, -1, (255,0,0), 3)
    #Eliminado algunos contornos no deseados
    for i in contornos:
      area=cv2.contourArea(i)
      if area>1000:
        #Hace un rectangulo que rodea el area de la tapa
        x,y2,w,h = cv2.boundingRect(i)
        cv2.rectangle(frame,(x,y2),(x+w,y2+h),(0,255,0),2)
        #Realizar trazos para la parte superior
        x2= x + w//2 

        if x1 is not None:
          if 0 <x2 <50 and 0<y2<50:
            color = verde
            grosorVerde =  6
            grosorRosa = 2
            grosorAmarillo = 2
            grosorCeleste=2
          if 0 <x2 <50 and 60<y2<100:
            color = Rosa
            grosorVerde =  2
            grosorRosa = 6
            grosorAmarillo = 2
            grosorCeleste=2
          if 0 <x2 <50 and 110<y2<150:
            color = celeste 
            grosorVerde =  2
            grosorRosa = 2
            grosorAmarillo = 2
            grosorCeleste=6
          if 0 <x2 <50 and 160<y2<200:
            color = amarillo
            grosorVerde =  2
            grosorRosa = 2
            grosorAmarillo = 6
            grosorCeleste=2
          if 0 <x2 <50 and 160<y2<200:
            color = amarillo
            grosorVerde =  2
            grosorRosa = 2
            grosorAmarillo = 6
            grosorCeleste=2
            #Grosor de linea
        if 1220 <x2 <1270 and 0<y2<50:
            grosor = 3
            litle =  6
            midle = 1
            big= 1
        if 1220 <x2 <1270 and 60<y2<100:
            grosor = 7
            litle =  1
            midle = 6
            big= 1
        if 1220 <x2 <1270 and 110<y2<150:
            grosor = 11
            litle =  1
            midle = 1
            big= 6
        #borrador
        if 300 < x2 < 400 and 0 <y2 < 50:
          cv2.rectangle(frame,(300,0),(400,50),borrador,2)
          cv2.putText(frame,"Borrador",(320,20),6,0.6,borrador,2,cv2.LINE_AA)
     



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
      else:
        x1=None
        y1=None
    cv2.imshow('Video', frame)
    #cv2.imshow('aux', aux)
    cv2.imshow("azul",mask)

    #Si pulsamos q finalizamos'
    if  cv2.waitKey(1) & 0xFF==ord("q"):
      break;
#Finalizamos camara  y cerramos ventana
vc.release()
cv2.destroyAllWindows()

