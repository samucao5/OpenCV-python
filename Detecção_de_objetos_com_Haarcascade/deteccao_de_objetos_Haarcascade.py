import cv2

# inicia a webcam
camera = cv2.VideoCapture(0)

# carrega o classificador de olhos
classificador = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_eye.xml'
)

classificador_2 = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

classificador_3 = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_smile.xml'
)

# verifica se o XML foi carregado
if classificador.empty():
    print("Erro ao carregar XML")
    exit()

# loop infinito da câmera
while True:

    # captura um frame da webcam
    check, img = camera.read()

    # verifica se a câmera está funcionando
    if not check:
        print("Erro ao acessar câmera")
        break

    # converte a imagem para escala de cinza
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # detecta objetos (olhos)
    objetos = classificador.detectMultiScale(
        imgGray,
        #controla o fator de escala do objeto
        scaleFactor=1.1,
        #controla a escala da busca
        minNeighbors=5,
        #limita o tamanho minimo para o haas procurar o objeto
        minSize=(30,30)
    )

    objetos_2 = classificador_2.detectMultiScale(
        imgGray,
        scaleFactor=1.5,
        minNeighbors=5,
        minSize=(50,50)
    )

    objeto_3 = classificador_3.detectMultiScale(
        imgGray,
        scaleFactor=1.5,
        minNeighbors=20,
        minSize=(20,20)
    )

    # mostra coordenadas dos objetos encontrados
    print(objetos_2)

    # percorre cada objeto detectado
    for (x, y, w, h) in objetos:

        # desenha retângulo no objeto detectado
        cv2.rectangle(
            img,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

    for (x,y, w, h) in objetos_2:
        cv2.rectangle(
            img, 
            (x,y),
            (x + w, y + h),
            (255,0,0),
            2
        )

    for (x, y, w, h) in objeto_3:
        cv2.rectangle(
            img,
            (x,y),
            (x + w, y + h),
            (0,0,200),
            2
        )


    # mostra imagem colorida
    cv2.imshow('webcam', img)

    # mostra imagem em cinza
    cv2.imshow('webcam cinza', imgGray)

    # fecha ao apertar S
    if cv2.waitKey(1) & 0xFF == ord('s'):
        print("camera desligada")
        break 

# libera a câmera
camera.release()

# fecha todas as janelas
cv2.destroyAllWindows()