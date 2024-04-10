import cv2
import mediapipe as mp

# Inicializar o detector de pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

# Inicializar o vídeo a partir de um arquivo MP4
video_path = 'caminho/do/seu/video.mp4'
vs = cv2.VideoCapture(video_path)

# Loop sobre os frames do vídeo
while True:
    ret, frame = vs.read()
    if not ret:
        break

    # Converter a imagem para RGB (MediaPipe Pose requer entrada RGB)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detectar pose na imagem
    results = pose.process(rgb_frame)

    # Desenhar os pontos-chave da pose na imagem
    if results.pose_landmarks:
        mp_drawing = mp.solutions.drawing_utils
        mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    # Exibir o resultado
    cv2.imshow("Pose Detection", frame)

    # Tecla para sair do script "q"
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Limpar
cv2.destroyAllWindows()
vs.release()
