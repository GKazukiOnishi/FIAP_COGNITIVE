import cv2
import mediapipe as mp
import math
import pyautogui
import time

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)  # Captura do dispositivo de câmera padrão

# Define os valores inicialmente máximos e mínimos de distância e volume
max_distance = 315
min_distance = 19
volumes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Flag para indicar se a escala máxima e mínima foi definida
max_scale_defined = False
min_scale_defined = False

# Variáveis para controlar o tempo que o mindinho permanece abaixado
pinky_down_start = 0
pinky_down_duration = 0

while True:
    success, img = cap.read()
    if not success:
        print("Erro ao capturar o quadro")
        break

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            for id, lm in enumerate(hand_landmarks.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                if id == 4:  # Dedão
                    cv2.circle(img, (cx, cy), 5, (0, 0, 255), cv2.FILLED)
                    cv2.putText(img, f'{id}', (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
                elif id == 8:  # Indicador
                    cv2.circle(img, (cx, cy), 5, (0, 0, 255), cv2.FILLED)
                    cv2.putText(img, f'{id}', (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
                else:
                    cv2.circle(img, (cx, cy), 5, (0, 0, 255), cv2.FILLED)
                    cv2.putText(img, f'{id}', (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

            mpDraw.draw_landmarks(img, hand_landmarks, mpHands.HAND_CONNECTIONS,
                                  landmark_drawing_spec=mpDraw.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2))

            thumb_tip = (hand_landmarks.landmark[4].x * w, hand_landmarks.landmark[4].y * h)
            index_tip = (hand_landmarks.landmark[8].x * w, hand_landmarks.landmark[8].y * h)
            pinky_tip = (hand_landmarks.landmark[20].x * w, hand_landmarks.landmark[20].y * h)
            pinky_base = (hand_landmarks.landmark[17].x * w, hand_landmarks.landmark[17].y * h)
            distance = math.sqrt((index_tip[0] - thumb_tip[0]) ** 2 + (index_tip[1] - thumb_tip[1]) ** 2)

            # Verifica se o mindinho está abaixado
            if pinky_tip[1] > pinky_base[1]:
                # Se o mindinho foi abaixado recentemente, atualiza o tempo inicial
                if pinky_down_start == 0:
                    pinky_down_start = time.time()
                # Calcula o tempo decorrido desde que o mindinho foi abaixado
                pinky_down_duration = time.time() - pinky_down_start
            else:
                # Reinicia o contador se o mindinho não estiver abaixado
                pinky_down_start = 0
                pinky_down_duration = 0

            # Se o mindinho permanecer abaixado por mais de 1 segundo, define a escala máxima e mínima
            if pinky_down_duration >= 1:
                if not max_scale_defined:
                    max_distance = distance
                    print("Escala máxima definida:", max_distance)
                    time.sleep(2)
                    max_scale_defined = True
                elif max_scale_defined and not min_scale_defined:
                    min_distance = distance
                    print("Escala mínima definida:", min_distance)
                    min_scale_defined = True
                    time.sleep(2)

            # Mapeia a distância para os volumes específicos
            if max_scale_defined and min_scale_defined:
                volume_index = int((distance - min_distance) / (max_distance - min_distance) * len(volumes))
                volume_index = max(min(volume_index, len(volumes) - 1), 0)
                volume = volumes[volume_index]

                # Ajusta o volume do computador
                pyautogui.press("volumedown", presses=100)
                pyautogui.press("volumeup", presses=volume)

                print("Distância entre o dedão e o indicador:", distance)
                print("Volume ajustado para:", volume)

            cv2.line(img, (int(thumb_tip[0]), int(thumb_tip[1])), (int(index_tip[0]), int(index_tip[1])), (0, 255, 0), 2)

    cv2.imshow("Hand Tracking", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Pressione 'q' para sair
        break

cap.release()
cv2.destroyAllWindows()