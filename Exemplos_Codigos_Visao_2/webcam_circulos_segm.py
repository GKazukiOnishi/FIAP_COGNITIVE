import cv2
import numpy as np

def filtrar_imagem(img):
    """
    Filtra a imagem da webcam para destacar os círculos
    """
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Aplicar um desfoque para reduzir o ruído
    gray_blurred = cv2.medianBlur(gray, 5)
    
    # Detectar círculos
    circles = cv2.HoughCircles(gray_blurred, cv2.HOUGH_GRADIENT, dp=1, minDist=20,
                               param1=50, param2=50, minRadius=10, maxRadius=100)
    
    if circles is not None:
        # Converter para inteiros
        circles = np.uint16(np.around(circles))
        
        # Criar uma máscara para os círculos
        mask = np.zeros_like(gray)
        for circle in circles[0, :]:
            cv2.circle(mask, (circle[0], circle[1]), circle[2], 255, -1)

        # Segmentar os círculos
        segmented_circles = cv2.bitwise_and(img, img, mask=mask)

        # Contar a quantidade de círculos
        num_circles = len(circles[0])

        return segmented_circles, num_circles
    
    else:
        return None, 0

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

        segmented_circles, num_circles = filtrar_imagem(frame)

        if segmented_circles is not None:
            # Adicionar contador na tela
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(segmented_circles, f'Quantidade de circulos: {num_circles}', (10, 30), font, 0.8, (0, 255, 0), 2, cv2.LINE_AA)

            # Exibir os círculos segmentados
            cv2.imshow("Círculos Segmentados", segmented_circles)

        key = cv2.waitKey(20)
        if key == 27:  # Sai ao pressionar ESC
            break

    cv2.destroyWindow("preview")
    vc.release()

if __name__ == "__main__":
    main()
