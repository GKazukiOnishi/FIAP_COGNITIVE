import cv2
import mediapipe as mp

# Inicializar o detector de rostos
mp_face_detection = mp.solutions.face_detection
face_detection = mp_face_detection.FaceDetection()

# Inicializar o vídeo a partir de um arquivo MP4
video_path = 'caminho/do/seu/video.mp4'
vs = cv2.VideoCapture(video_path)

# Loop sobre os frames do vídeo
while True:
    ret, frame = vs.read()
    if not ret:
        break

    # Converter a imagem para RGB (MediaPipe Face Detection requer entrada RGB)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detectar rostos na imagem
    results = face_detection.process(rgb_frame)

    # Desenhar as caixas delimitadoras dos rostos na imagem
    if results.detections:
        for detection in results.detections:
            bboxC = detection.location_data.relative_bounding_box
            ih, iw, _ = frame.shape
            bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
                   int(bboxC.width * iw), int(bboxC.height * ih)
            cv2.rectangle(frame, bbox, (0, 255, 0), 2)

    # Exibir o resultado
    cv2.imshow("Face Detection", frame)

    # Tecla para sair do script "q"
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Limpar
cv2.destroyAllWindows()
vs.release()
