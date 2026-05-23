import cv2 
import mediapipe as mp
import pygame

video = cv2.VideoCapture(0)

pygame.mixer.init()
pygame.mixer.music.load(r'Deteccao_de_objetos_com_MediaPipe\projeto_contador_de_dedos\conteudo\music_meme.mp3')
img_2 = cv2.imread(r'Deteccao_de_objetos_com_MediaPipe\projeto_contador_de_dedos\conteudo\quarteto_fantastico.jpg')
img_2 = cv2.resize(img_2,(200,200))
hand = mp.solutions.hands
Hand = hand.Hands(max_num_hands=1)
mpDraw = mp.solutions.drawing_utils
while True:
    check, img = video.read()
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = Hand.process(img_rgb)
    handsPoints = result.multi_hand_landmarks
    h,w,_ = img.shape
    pontos = []
    if handsPoints:
        for points in handsPoints:
            mpDraw.draw_landmarks(img,points,hand.HAND_CONNECTIONS)
            for id,cord in enumerate(points.landmark):
                    cx, cy = int(cord.x*w), int(cord.y*h)
                    cv2.putText(img,str(id),(cx,cy+10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),2)
                    pontos.append((cx, cy))

              
        dedos = [8,12,16,20]
        contador = 0
        if points:
             if pontos[4][0] < pontos[2][0]:
                  contador =+ 1
                  
             for x in dedos:
                  if pontos[x][1] < pontos[x - 2][1]:
                       contador += 1
        
        texto = f"dedos levantados: {contador}"
        if contador == 4:
            img[50:250, 50:250] = img_2
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.play()
        else:
              pygame.mixer.music.stop()
             
             
        cv2.putText(img,texto,(40,200),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),5)
    cv2.imshow('webcam', img)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        print("camera desligada")
        print(f'voce fez {contador} polichinelos, parabens campeão')
        break