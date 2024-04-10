import cv2
import dlib


def draw_text_info():
    """Função para escrever na tela as instruções de uso"""

    menu_pos = (10, 20)
    menu_pos_2 = (10, 40)
    menu_pos_3 = (10, 60)
    info_1 = "Selecione com o mouse o objeto para rastreamento"
    info_2 = "Use '1' para start, '2' para reset"

    cv2.putText(frame, info_1, menu_pos, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255))
    cv2.putText(frame, info_2, menu_pos_2, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255))
    if tracking_state:
        cv2.putText(frame, "Rastreando...", menu_pos_3, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0))
    else:
        cv2.putText(frame, "Não rastreando", menu_pos_3, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255))



points = []


# Função de callback do mouse
def mouse_click(event, x, y, flags, param):
    global points

    if event == cv2.EVENT_LBUTTONDOWN:
        points = [(x, y)]

    elif event == cv2.EVENT_LBUTTONUP:
        points.append((x, y))



capture = cv2.VideoCapture(0)


window_name = "tracking"
cv2.namedWindow(window_name)
cv2.setMouseCallback(window_name, mouse_click)

# Inicializa metodo de correlação de rastreamento
tracker = dlib.correlation_tracker()

# Variavel de estado
tracking_state = False

while True:
    ret, frame = capture.read()

    draw_text_info()

    # Se objeto esta selecionado
    if len(points) == 2:
        cv2.rectangle(frame, points[0], points[1], (0, 0, 255), 3)
        dlib_rectangle = dlib.rectangle(points[0][0], points[0][1], points[1][0], points[1][1])

    # Se é pra rastrear
    if tracking_state == True:
        tracker.update(frame)
        pos = tracker.get_position()
        cv2.rectangle(frame, (int(pos.left()), int(pos.top())), (int(pos.right()), int(pos.bottom())), (0, 255, 0), 3)

    # lê teclado
    key = 0xFF & cv2.waitKey(1)

    # '1' start
    if key == ord("1"):
        if len(points) == 2:
            # Start tracking:
            tracker.start_track(frame, dlib_rectangle)
            tracking_state = True
            points = []

    # '2' reset
    if key == ord("2"):
        points = []
        tracking_state = False

    if key == ord('q'):
        break

    cv2.imshow(window_name, frame)

# Release everything:
capture.release()
cv2.destroyAllWindows()