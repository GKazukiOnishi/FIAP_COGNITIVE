import cv2

def aplicar_filtros(img):
    """
    Aplica filtros Gaussianos e Canny na imagem
    """
    # Aplicar filtro Gaussiano para suavizar e reduzir ruído
    img_suavizada = cv2.GaussianBlur(img, (5, 5), 0)
    # Detectar bordas usando o algoritmo Canny
    img_bordas = cv2.Canny(img_suavizada, 50, 200)  # Você pode ajustar os limiares conforme necessário

    return img_bordas

def main():
    cv2.namedWindow("preview")
    vc = cv2.VideoCapture('Livro.mp4')  # Altere 'seu_video.mp4' para o nome do seu arquivo de vídeo

    if not vc.isOpened():
        print("Erro ao abrir o vídeo.")
        return

    while True:
        rval, frame = vc.read()
        if not rval:
            print("Fim do vídeo.")
            break

        img_filtrada = aplicar_filtros(frame)

        cv2.imshow("Original", frame)
        cv2.imshow("Filtrada", img_filtrada)

        key = cv2.waitKey(5)
        if key == 27: # Sai ao pressionar ESC
            break

    cv2.destroyWindow("preview")
    vc.release()

if __name__ == "__main__":
    main()
