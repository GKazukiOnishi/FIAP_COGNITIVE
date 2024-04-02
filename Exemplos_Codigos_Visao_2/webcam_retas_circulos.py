import cv2
import numpy as np

def detectar_formas(img):
    """
    Detecta formas (círculos e retas) na imagem usando a transformada de Hough
    """
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)

    # Detectar círculos
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=40, minRadius=50, maxRadius=100)
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for circle in circles[0, :]:
            center = (circle[0], circle[1])
            radius = circle[2]
            cv2.circle(img, center, radius, (0, 255, 0), 3)

    # Detectar retas
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 50, minLineLength=30, maxLineGap=5)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 5)

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

        img_com_formas = detectar_formas(frame)

        cv2.imshow("Detecção de formas", img_com_formas)

        key = cv2.waitKey(20)
        if key == 27:  # Sai ao pressionar ESC
            break

    cv2.destroyWindow("preview")
    vc.release()

if __name__ == "__main__":
    main()
