import cv2
import pickle
import numpy as np

vagas = []

with open(r'projeto_contador_de_vagas_de_estacionamento\vagas.pkl', 'rb') as arquivo:
    vagas = pickle.load(arquivo)

video = cv2.VideoCapture(r'projeto_contador_de_vagas_de_estacionamento\conteudos\video.mp4')

while True:
    check,img = video.read()

    if not check:
        print("fim do video")
        break

    imgcinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    imgTh = cv2.adaptiveThreshold(imgcinza, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,25,16)
    imgMedian = cv2.medianBlur(imgTh,5)
    kernel = np.ones((3,3), np.uint8)
    imgDil = cv2.dilate(imgMedian, kernel)


    vagas_abertas = 0

    for x,y,w,h in vagas:
        vaga = imgDil[y:y+h, x:x+w]
        count = cv2.countNonZero(vaga)
        cv2.putText(img, str(count), (x,y+h - 10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),1)
        if count < 900:
            cv2.rectangle(img,(x,y), (x+w, y+h), (0,255,0), 2)
            vagas_abertas += 1
        else:
            cv2.rectangle(img,(x,y), (x+w, y+h), (0,0,255), 2)

    cv2.putText(img,f'vagas livres: {vagas_abertas}/69',(70,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2,cv2.LINE_AA)
    cv2.putText(img,f'vagas fechadas: {69 - vagas_abertas}/69',(500,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2,cv2.LINE_AA)

    cv2.imshow('video', img)
    #cv2.imshow('video th', imgDil)


    if cv2.waitKey(10) & 0xFF == ord('s'):
        break
