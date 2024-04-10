import cv2
import mediapipe as mp

# Inicializar o detector de objetos 3D
mp_objectron = mp.solutions.objectron
objectron = mp_objectron.Objectron(static_image_mode=False)

# Inicializar o vídeo
vs = cv2.VideoCapture(0)

# Loop sobre os frames do vídeo
while True:
    ret, frame = vs.read()
    if not ret:
        break

    # Converter a imagem para RGB (MediaPipe Objectron requer entrada RGB)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detectar objetos 3D na imagem
    results = objectron.process(rgb_frame)

    # Desenhar os objetos 3D na imagem
    if results.detected_objects:
        for detected_object in results.detected_objects:
            mp_drawing = mp.solutions.drawing_utils
            mp_drawing.draw_landmarks(frame, detected_object.landmarks_2d, mp_objectron.BOX_CONNECTIONS)

    # Exibir o resultado
    cv2.imshow("Objectron", frame)

    # Tecla para sair do script "q"
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Limpar
cv2.destroyAllWindows()
vs.release()
