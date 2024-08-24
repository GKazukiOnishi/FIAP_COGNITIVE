import cv2
from matplotlib import pyplot as plt
import numpy as np
import mediapipe as mp
import math
from pynput.keyboard import Key, Controller
import cvzone 

NOME_JANELA = 'Frame'
NOME_JANELA_MAO = 'FrameMao'
LARGURA_JANELA = 640
ALTURA_JANELA = 480
LARGURA_FRAME_MAO = 150
ALTURA_FRAME_MAO = 300

COR_PONTO = (0, 0, 255)
COR_LINHA = (0, 255, 0)

mediaPipeHands = mp.solutions.hands.Hands()
teclado = Controller()
distanciaEmPixels = [300, 245, 200, 170, 145, 130, 112, 103, 93, 87, 80, 75, 70, 67, 62, 59, 57]
distanciaEmCM = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
coeficienteAngular = np.polyfit(distanciaEmPixels, distanciaEmCM, 2)

camera = cv2.VideoCapture(0)
camera.set(3, LARGURA_JANELA)
camera.set(4, ALTURA_JANELA)

def mountLandmarksList(landmarks):
  landmarksList = []

  for landmark in landmarks:
    x, y = int(landmark.x * frame.shape[1]), int(landmark.y * frame.shape[0])
    landmarksList.append((x, y, landmark.z))

  return landmarksList

def conectarPontos(imagem, pontos, idx1, idx2):
  cv2.line(imagem, (pontos[idx1][0], pontos[idx1][1]), (pontos[idx2][0], pontos[idx2][1]), COR_LINHA, 1)

def desenharLandmarks(imagem, pontos):
  contador = 0

  for ponto in pontos:
    x, y, z = ponto

    cv2.circle(imagem, (x, y), 5, COR_PONTO, -1)
    cv2.putText(imagem, str(contador), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.2, (0, 255, 0), 2)
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

def getFrameMao(landmarks, direitaEsquerda):
  inferior = landmarks[8][1] - 20
  superior = landmarks[0][1] + 20
  if direitaEsquerda == 'Right':
    esquerda = landmarks[4][0] - 20
    direita = landmarks[20][0] + 20
  else:
    esquerda = landmarks[20][0] - 20
    direita = landmarks[4][0] + 20
  
  if inferior >= 0 and esquerda >= 0 and direita <= LARGURA_JANELA and superior <= ALTURA_JANELA and inferior < superior and esquerda < direita:
    frameMao = frame[inferior:superior, esquerda:direita]
    frameMao = cv2.resize(frameMao, (LARGURA_FRAME_MAO, ALTURA_FRAME_MAO), cv2.INTER_CUBIC)
  else:
    frameMao = None

  return frameMao

escalaFixaVolume = [0, 100]
escalaFixaDistanciaDedos = [20, 300]
zFixoDaEscalaDistanciaDedos = 2

while True:
  leuOFrame, frame = camera.read()
  frameMao = None

  if not leuOFrame:
    break

  frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
  resultado = mediaPipeHands.process(frameRGB)

  if resultado.multi_hand_landmarks:
    for hand_index, hand_landmarks in enumerate(resultado.multi_hand_landmarks):
      direitaEsquerda = resultado.multi_handedness[hand_index].classification[0].label

      landmarksList = mountLandmarksList(hand_landmarks.landmark)
      desenharLandmarks(frame, landmarksList)

      conectarPontos(frame, landmarksList, 4, 8)

      frameMao = getFrameMao(landmarksList, direitaEsquerda)

      distanciaDedaoIndicador = distanciaPontos(landmarksList, 4, 8)
      volumeXDist = np.interp(distanciaDedaoIndicador, escalaFixaDistanciaDedos, escalaFixaVolume)

      #print(f"Distância {distanciaDedaoIndicador}, Volume {volumeXDist}")

       
      if resultado:
        
        A,B,C = coeficienteAngular
        distRealCMT = (A*distanciaDedaoIndicador**2)+(B*distanciaDedaoIndicador)+C

        print(distanciaDedaoIndicador,distRealCMT)
        cvzone.putTextRect(frame,f'{int(distRealCMT)} cm',(10,30))

      if distanciaDedaoIndicador > 70.00:
        teclado.press(Key.media_volume_up)
        teclado.release(Key.media_volume_up)

      if distanciaDedaoIndicador < 20.00:
        teclado.press(Key.media_volume_down)
        teclado.release(Key.media_volume_down)
  
  if frameMao is not None:
    cv2.imshow(NOME_JANELA_MAO, frameMao)
  
  cv2.imshow(NOME_JANELA, frame)
  
  if cv2.waitKey(200) & 0xFF == ord('q'):
    break

camera.release()
cv2.destroyAllWindows()