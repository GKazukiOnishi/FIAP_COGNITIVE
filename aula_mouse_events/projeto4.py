import cv2
import numpy as np
 
# Carrega uma imagem
# Neste caso estamos criando uma imagem RGB preta de tamanho 480x640
img = np.zeros((480, 640, 3), dtype="uint8")
  
# Exibe a imagem
cv2.imshow('image', img)

points = []

# Função de callback, quando ocorre um evento do mouse, essa função é chamada
def mouse_click(event, x, y, flags, param): 
    global points

    if event == cv2.EVENT_LBUTTONDOWN:
        points = [(x, y)]

    elif event == cv2.EVENT_LBUTTONUP:
        points.append((x, y))
        p1 = tuple(points[0]) 
        p2 = tuple(points[1])

        cv2.rectangle(img, p1 , p2, (0, 255, 0), 3)
        cv2.imshow('image', img)

# Seta a função de callback que será chamada 
# Evento 'image', função callback mouse_click  
cv2.setMouseCallback('image', mouse_click)
   
cv2.waitKey(0)
  
# fecha a janela.
cv2.destroyAllWindows()