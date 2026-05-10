import cv2

video = cv2.VideoCapture(r'openCV_conceitos basicos\conteudos\Twelve Dance.mp4')
while True:
    check, img = video.read()

    # redimenciona o tamanho da tela, quando exibido
    imgredin = cv2.resize(img,(480,240))
    # mostra o tamanho da tela
    print(img.shape)
    cv2.imshow("Dance",imgredin)
    cv2.waitKey(10)