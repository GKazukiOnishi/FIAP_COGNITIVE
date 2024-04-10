import cv2
import mediapipe as mp

# Inicializar o detector de mãos
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Inicializar o vídeo
vs = cv2.VideoCapture(0)

# Loop sobre os frames do vídeo
while True:
    ret, frame = vs.read()
    if not ret:
        break

    # Converter a imagem para RGB (MediaPipe Hands requer entrada RGB)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detectar mãos na imagem
    results = hands.process(rgb_frame)

    # Verificar se mãos foram detectadas
    if results.multi_hand_landmarks:
        # Loop sobre cada mão detectada
        for hand_landmarks in results.multi_hand_landmarks:
            # Desenhar pontos de referência das mãos na imagem
            for landmark in hand_landmarks.landmark:
                x, y = int(landmark.x * frame.shape[1]), int(landmark.y * frame.shape[0])
                cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)

    # Exibir o resultado
    cv2.imshow("Hand Tracking", frame)

    # Tecla para sair do script "q"
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Limpar
cv2.destroyAllWindows()
vs.release()
