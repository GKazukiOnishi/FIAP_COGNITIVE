import numpy as np
import cv2
from keras.preprocessing import image
from keras.models import load_model

# Carregando o modelo treinado
modelo_carregado = load_model("modelo_treinado.h5")

# Lista de classes do CIFAR-10
classes_cifar10 = ['aviao', 'automovel', 'passaro', 'gato', 'veado', 'cachorro', 'sapo', 'cavalo', 'navio', 'caminhao']

# Função para fazer a predição e mostrar o resultado na imagem
def prever_e_mostrar(frame):
    # Redimensionar o frame para 32x32
    img = cv2.resize(frame, (32, 32))
    img_array = image.img_to_array(img)
    img_array = img_array.reshape((1, 32, 32, 3))

    # Normalizando a escala para ficar entre 0 e 1
    img_array = img_array / 255.0

    # Avaliando a imagem usando o modelo carregado
    predicao = modelo_carregado.predict(img_array)

    # Obtendo a classe predita
    classe_predita = np.argmax(predicao)
    nome_classe_predita = classes_cifar10[classe_predita]

    # Exibir a classe prevista na janela
    cv2.putText(frame, f'Classe: {nome_classe_predita}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

# Capturando vídeo da webcam em tempo real
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Fazer a predição e mostrar o resultado na imagem
    prever_e_mostrar(frame)

    # Mostrar o frame com a classe prevista
    cv2.imshow('Webcam - Pressione "q" para sair', frame)

    # Sair do loop ao pressionar 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
