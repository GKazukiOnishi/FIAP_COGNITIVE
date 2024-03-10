import cv2
import numpy as np


def aplicar_limiarizacao_otsu(img):
    """
    Aplica o método de limiarização de Otsu na imagem em escala de cinza
    """
    # Converte a imagem para escala de cinza
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Aplica o método de limiarização de Otsu
    limiar, img_limiarizada = cv2.threshold(img_gray, 0, 255, cv2.THRESH_OTSU)
    
    return img_limiarizada

def main():
    cv2.namedWindow("preview")
    vc = cv2.VideoCapture(0)

    if not vc.isOpened(): # Tenta obter o primeiro quadro
        print("Erro ao abrir a câmera.")
        return

    while True:
        rval, frame = vc.read()
        if not rval:
            print("Erro ao capturar a imagem.")
            break

        img_limiarizada = aplicar_limiarizacao_otsu(frame)

        cv2.imshow("Original", frame)
        cv2.imshow("Limiarizada", img_limiarizada)

        key = cv2.waitKey(20)
        if key == 27: # Sai ao pressionar ESC
            break

    cv2.destroyWindow("preview")
    vc.release()

if __name__ == "__main__":
    main()
