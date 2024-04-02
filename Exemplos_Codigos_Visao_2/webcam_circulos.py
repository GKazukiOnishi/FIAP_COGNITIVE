import cv2
import numpy as np

def detectar_circulos(img):
    """
    Detecta círculos na imagem usando a transformada de Hough
    """
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Aplicar um desfoque para reduzir o ruído
    gray_blurred = cv2.medianBlur(gray, 5)
    
    # Detectar círculos
    circles = cv2.HoughCircles(gray_blurred, cv2.HOUGH_GRADIENT, dp=1, minDist=20,
                               param1=50, param2=30, minRadius=80, maxRadius=150)
    
    if circles is not None:
        # Converter para inteiros
        circles = np.uint16(np.around(circles))
        
        # Desenhar os círculos detectados e o centro de massa
        for circle in circles[0, :]:
            center = (circle[0], circle[1])
            radius = circle[2]
            cv2.circle(img, center, radius, (0, 255, 0), 3)  # Desenhar círculo
            cv2.circle(img, center, 2, (0, 0, 255), 3)  # Marcar o centro

    return img

def main():
    cv2.namedWindow("preview")
    vc = cv2.VideoCapture(0)

    if not vc.isOpened():  # Tenta obter o primeiro quadro
        print("Erro ao abrir a câmera.")
        return

    while True:
        rval, frame = vc.read()
        if not rval:
            print("Erro ao capturar a imagem.")
            break

        img_com_circulos = detectar_circulos(frame)

        cv2.imshow("Detecção de círculos", img_com_circulos)

        key = cv2.waitKey(20)
        if key == 27:  # Sai ao pressionar ESC
            break

    cv2.destroyWindow("preview")
    vc.release()

if __name__ == "__main__":
    main()
