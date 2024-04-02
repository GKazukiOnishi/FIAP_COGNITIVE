import cv2

# Capturar vídeo da webcam
cap = cv2.VideoCapture(0)

while True:
    # Capturar frame da webcam
    ret, frame = cap.read()
    if not ret:
        break
    
    # Aplicar a operação bitwise NOT em cada canal de cor do frame
    frame_not = cv2.bitwise_not(frame)
    
    # Exibir o frame resultante
    cv2.imshow('Webcam com efeito negativo', frame_not)
    
    # Parar o loop quando a tecla 'q' for pressionada
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar os recursos
cap.release()
cv2.destroyAllWindows()
