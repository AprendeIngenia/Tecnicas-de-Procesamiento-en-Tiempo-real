# Importamos las librerias
import cv2
import numpy as np

# Modos de ejecucion
#vc = 0 --> 48  # Captura de video
#fd = 1 --> 49  # Filtro desenfoque
#fe = 2 --> 50  # Filtro detector de esquinas
#fb = 3 --> 51  # Filtro de Bordes


# Parametros para detector de esquinas
esquinas_param = dict(maxCorners = 500,    # Maximo numero de esquinas a detectar
                      qualityLevel = 0.2,  # Umbral minimo para la deteccion de esquinas
                      minDistance = 15,    # Distacia entre pixeles
                      blockSize = 9)       # Area de pixeles

# Modo
mood = 48

# Creamos la Video Captura
cap = cv2.VideoCapture(0)

# Creamos un ciclo para ejecutar nuestros Frames
while True:
    # Leemos los fotogramas
    ret, frame = cap.read()

    # Decidimos el mood
    # Normal
    if mood == 48:
        # Mostramos los frames
        resultado = frame

    # Desenfoque
    elif mood == 49:
        # Modificamos frames
        resultado = cv2.blur(frame, (13, 13))

    # Bordes
    elif mood == 51:
        # Modificamos frames
        resultado = cv2.Canny(frame, 135, 150)  # Umbral superior y umbral inferior

    # Esquinas
    elif mood == 50:
        # Obtenemos los frames
        resultado = frame
        # Conversion a escala de grises
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Calculamos las caracteristicas de las esquinas
        esquinas = cv2.goodFeaturesToTrack(gray, **esquinas_param)

        # Preguntamos si detectamos esquinas con esas caracteristicas
        if esquinas is not None:
            # Iteramos
            for x, y in np.float32(esquinas).reshape(-1,2):
                # Convertimos en enteros
                x,y = int(x), int(y)
                # Dibujamos la ubicacion de las esquinas
                cv2.circle(resultado, (x,y), 10, (255,0,0), 1)

    # Si presionamos otra tecla
    elif mood != 48 or mood != 49 or mood != 50 or mood != 51 or mood != -1:
        # No hacemos nada
        resultado = frame

        # Imprimimos mensaje
        print('TECLA INCORRECTA')


    # Mostramos los Frames
    cv2.imshow("VIDEO CAPTURA", resultado)

    # Cerramos con lectura de teclado
    t = cv2.waitKey(1)
    # Salimos
    if t == 27:
        break
    # Modificamos Mood
    elif t != -1:
        mood = t

# Liberamos la VideoCaptura
cap.release()
# Cerramos la ventana
cv2.destroyAllWindows()
