import cv2
from matplotlib import pyplot as plt
import numpy as np
import mediapipe as mp
import math

NOME_JANELA = 'Frame'
LARGURA_JANELA = 640
ALTURA_JANELA = 480

COR_PONTO = (0, 0, 255)
COR_LINHA = (0, 255, 0)

mediaPipeHands = mp.solutions.hands.Hands()

frame = cv2.imread('./img/mao.jpg')
frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
resultado = mediaPipeHands.process(frameRGB)

def mountLandmarksList(landmarks):
  landmarksList = []

  for landmark in landmarks:
    x, y = int(landmark.x * frame.shape[1]), int(landmark.y * frame.shape[0])
    landmarksList.append((x, y, landmark.z))

  return landmarksList

def conectarPontos(imagem, pontos, idx1, idx2):
  cv2.line(imagem, (pontos[idx1][0], pontos[idx1][1]), (pontos[idx2][0], pontos[idx2][1]), COR_LINHA, 5)

def desenharLandmarks(imagem, pontos):
  contador = 0

  for ponto in pontos:
    x, y, z = ponto

    cv2.circle(imagem, (x, y), 15, COR_PONTO, -1)
    cv2.putText(imagem, str(contador), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    contador += 1

  conectarPontos(imagem, pontos, 0, 1)
  conectarPontos(imagem, pontos, 1, 2)
  conectarPontos(imagem, pontos, 2, 3)
  conectarPontos(imagem, pontos, 3, 4)
  conectarPontos(imagem, pontos, 0, 5)
  conectarPontos(imagem, pontos, 5, 6)
  conectarPontos(imagem, pontos, 6, 7)
  conectarPontos(imagem, pontos, 7, 8)
  conectarPontos(imagem, pontos, 5, 9)
  conectarPontos(imagem, pontos, 9, 10)
  conectarPontos(imagem, pontos, 10, 11)
  conectarPontos(imagem, pontos, 11, 12)
  conectarPontos(imagem, pontos, 9, 13)
  conectarPontos(imagem, pontos, 13, 14)
  conectarPontos(imagem, pontos, 14, 15)
  conectarPontos(imagem, pontos, 15, 16)
  conectarPontos(imagem, pontos, 13, 17)
  conectarPontos(imagem, pontos, 17, 18)
  conectarPontos(imagem, pontos, 18, 19)
  conectarPontos(imagem, pontos, 19, 20)
  conectarPontos(imagem, pontos, 0, 17)

def distanciaPontos(pontos, idx1, idx2):
  x1, y1, z1 = pontos[idx1]
  x2, y2, z2 = pontos[idx2]

  return math.hypot(x2 - x1, y2 - y1)

while True:
  if resultado.multi_hand_landmarks:
    for hand_index, hand_landmarks in enumerate(resultado.multi_hand_landmarks):
      handedness = resultado.multi_handedness[hand_index].classification[0].label
      print(f"Hand {handedness} - Index {hand_index}")

      landmarksList = mountLandmarksList(hand_landmarks.landmark)
      desenharLandmarks(frame, landmarksList)

      conectarPontos(frame, landmarksList, 4, 8)

      inferior = landmarksList[0][1]
      superior = landmarksList[12][1]
      esquerda = landmarksList[4][0]
      direita = landmarksList[20][0]

      # print(f"Inferior {inferior}, Superior {superior}, Esquerda {esquerda}, Direita {direita}")
      # print(distanciaPontos(landmarksList, 4, 8))

  
  frameR = cv2.resize(frame, (ALTURA_JANELA, LARGURA_JANELA), cv2.INTER_CUBIC)
  cv2.imshow(NOME_JANELA, frameR)

  if cv2.waitKey(25) & 0xFF == ord('q'):
    break
