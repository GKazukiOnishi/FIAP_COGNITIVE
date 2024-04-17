import cv2
import numpy as np
 
# Carrega uma imagem
# Neste caso estamos criando uma imagem RGB preta de tamanho 480x640
img = np.zeros((480, 640, 3), dtype="uint8")
  
# Exibe a imagem
cv2.imshow('image', img)

# Cria duas variaveis globais
clicks = 0      # conta a quantidade de clicks dada
coordinates = [] # salva as coordenadas de cada click


# Função de callback, quando ocorre um evento do mouse, essa função é chamada
def mouse_click(event, x, y, flags, param):
    global clicks, coordinates, image
    # Se foi movimento do mouse  

    if clicks < 2:
        if event == cv2.EVENT_LBUTTONDBLCLK:
            clicks += 1        
            coordinates.append([x, y])
            cv2.circle(img, (x,y), 2,(0,255,0), -1)
            cv2.imshow('image', img)
            print(clicks, coordinates)

    # Se foi o botão esquerdo do mouse  
    else:
        if event == cv2.EVENT_RBUTTONDOWN:
            img[:,:,] = 0
            img[:,:,1] = 0
            img[:,:,2] = 0
            clicks = 0
            coordinates = []
            cv2.imshow('image', img)
        else:
            start_point = tuple(coordinates[0]) 
            end_point = tuple(coordinates[1])
            print(start_point,end_point)
            cv2.line(img, start_point, end_point, (0,255,0), 2)
            cv2.imshow('image', img)


# Seta a função de callback que será chamada 
# Evento 'image', função callback mouse_click  
cv2.setMouseCallback('image', mouse_click)
   
cv2.waitKey(0)
  
# fecha a janela.
cv2.destroyAllWindows()