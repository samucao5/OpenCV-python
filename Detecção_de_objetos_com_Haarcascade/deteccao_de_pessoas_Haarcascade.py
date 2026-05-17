import cv2

camera = cv2.VideoCapture(r"openCV_conceitos basicos\conteudos\video.mp4")

classificador = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_fullbody.xml'
)

if not camera.isOpened():
    print("video não encontrado")
    exit()

if classificador.empty():
    print("conteudo não encontrado")
    exit()

while True:
    check, img = camera.read()

    if not check:
        print("fim do video")
        break

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    objetos = classificador.detectMultiScale(imgGray,minSize=(50,50),scaleFactor=1.5,minNeighbors=1)

    for x,y,l,a in objetos:
        cv2.rectangle(img, (x, y), (x+l, y+a), (0,255,0), 2)

    cv2.imshow("camera", img)
    if cv2.waitKey(10) & 0xFF == ord('s'):
        break

camera.release()
cv2.destroyAllWindows()
