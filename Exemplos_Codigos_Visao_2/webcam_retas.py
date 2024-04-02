import cv2
import numpy as np
import matplotlib.pyplot as plt

def detectar_linhas(img):
    """
    Detecta linhas na imagem usando a transformada de Hough
    """
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 50, minLineLength=30, maxLineGap=5)
    
    if lines is not None:
        hough_img = np.zeros_like(img)
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(hough_img, (x1, y1), (x2, y2), (255, 0, 255), 5)
        
        return hough_img
    
    else:
        return np.zeros_like(img)

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

        img_com_linhas = detectar_linhas(frame)

        cv2.imshow("Detecção de linhas", img_com_linhas)

        key = cv2.waitKey(20)
        if key == 27:  # Sai ao pressionar ESC
            break

    cv2.destroyWindow("preview")
    vc.release()

if __name__ == "__main__":
    main()
