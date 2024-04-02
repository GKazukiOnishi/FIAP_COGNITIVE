import cv2
import numpy as np
from scipy.spatial import distance as dist

def ordenar_pontos(pts):
    x_ordenado = pts[np.argsort(pts[:, 0]), :]
    mais_a_esquerda = x_ordenado[:2, :]
    mais_a_direita = x_ordenado[2:, :]
    mais_a_esquerda = mais_a_esquerda[np.argsort(mais_a_esquerda[:, 1]), :]
    (tl, bl) = mais_a_esquerda
    D = dist.cdist(tl[np.newaxis], mais_a_direita, "euclidean")[0]
    (br, tr) = mais_a_direita[np.argsort(D)[::-1], :]
    return np.array([tl, tr, br, bl], dtype="float32")

def ponto_medio(ptA, ptB):
    return ((ptA[0] + ptB[0]) * 0.5, (ptA[1] + ptB[1]) * 0.5)

def desenhar_dimensao(imagem, dimensao, pt1, pt2):
    cv2.putText(imagem, "{:.2f}cm".format(dimensao), (int(pt1[0]), int(pt1[1] - 7)), cv2.FONT_HERSHEY_SIMPLEX, 0.50, (0, 0, 255), 1)

def processar_frame(frame, largura=15.00, pixels_por_metrica=None):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    azul_baixo = np.array([100, 50, 50])  # Limiar inferior para a cor azul em HSV
    azul_alto = np.array([130, 255, 255])  # Limiar superior para a cor azul em HSV
    mascara = cv2.inRange(hsv, azul_baixo, azul_alto)
    res = cv2.bitwise_and(frame, frame, mask=mascara)

    cinza = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
    cinza = cv2.GaussianBlur(cinza, (7, 7), 0)
    bordas = cv2.Canny(cinza, 50, 150)
    dilatar = cv2.dilate(bordas, None, iterations=2)
    erodir = cv2.erode(dilatar, None, iterations=1)

    contornos, _ = cv2.findContours(erodir.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    min_area = 1000  # Área mínima em pixels quadrados
    max_area = 3000  # Área máxima em pixels quadrados

    contornos = [c for c in contornos if min_area < cv2.contourArea(c) < max_area]  # Filtra contornos dentro da faixa de área

    original = frame.copy()
    for c in contornos:
        caixa = cv2.minAreaRect(c)
        caixa = cv2.boxPoints(caixa)
        caixa = ordenar_pontos(caixa)
        cv2.drawContours(original, [caixa.astype("int")], -1, (0, 255, 0), 2)
        for (x, y) in caixa:
            cv2.circle(original, (int(x), int(y)), 5, (25, 0, 0), -1)

        (tl, tr, br, bl) = caixa
        (tltrX, tltrY) = ponto_medio(tl, tr)
        (blbrX, blbrY) = ponto_medio(bl, br)
        (tlblX, tlblY) = ponto_medio(tl, bl)
        (trbrX, trbrY) = ponto_medio(tr, br)

        cv2.circle(original, (int(tltrX), int(tltrY)), 5, (255, 0, 0), -1)
        cv2.circle(original, (int(blbrX), int(blbrY)), 5, (255, 0, 0), -1)
        cv2.circle(original, (int(tlblX), int(tlblY)), 5, (255, 0, 0), -1)
        cv2.circle(original, (int(trbrX), int(trbrY)), 5, (255, 0, 0), -1)

        cv2.line(original, (int(tltrX), int(tltrY)), (int(blbrX), int(blbrY)), (255, 0, 255), 2)
        cv2.line(original, (int(tlblX), int(tlblY)), (int(trbrX), int(trbrY)), (255, 0, 255), 2)

        dA = dist.euclidean((tltrX, tltrY), (blbrX, blbrY))
        dB = dist.euclidean((tlblX, tlblY), (trbrX, trbrY))

        if pixels_por_metrica is None:
            pixels_por_metrica = dB / largura

        dimA = dA / pixels_por_metrica
        dimB = dB / pixels_por_metrica

        desenhar_dimensao(original, dimB, (tltrX, tltrY), (blbrX, blbrY))
        desenhar_dimensao(original, dimA, (trbrX, trbrY), (tlblX, tlblY))

    cv2.imshow("Dimensões", original)

# Inicialização da webcam
cap = cv2.VideoCapture(0)

# Loop para capturar frames da webcam
while True:
    ret, frame = cap.read()
    if not ret:

        break

    processar_frame(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

