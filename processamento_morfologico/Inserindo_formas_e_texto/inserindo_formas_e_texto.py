import cv2

#imagem

img = cv2.imread(r"processamento_morfologico\conteudos\nuvem.jpg")
#caso voce coloque a espesura negativa ele e preenchido


# OBS:
# Se a espessura for negativa (-1),
# a forma geométrica será preenchida

# rectangle(
# imagem,
# ponto inicial (x,y),
# ponto final (x,y),
# cor BGR,
# espessura
# )
cv2.rectangle(img, (25,25),(50,50), (0, 128, 0), -5)

# circle(
# imagem,
# centro,
# raio,
# cor BGR,
# espessura
# )

cv2.circle(img, (200,200), 50, (0,100,200),-1)

# line(
# imagem,
# ponto inicial,
# ponto final,
# cor,
# espessura
# )
cv2.line(img,(100,100), (300,300), (44,20,100), 3)

texto = "nuvem"
# putText(
# imagem,
# texto,
# posição,
# fonte,
# tamanho,
# cor,
# espessura
# )
cv2.putText(img,texto,(100,400),cv2.FONT_HERSHEY_SIMPLEX,2,(0, 128, 0),2)


cv2.imshow("imagem", img)
cv2.waitKey(0)

#video
video = cv2.VideoCapture(r"C:\Users\samue\Music\OpenCv\processamento_morfologico\conteudos\Twelve Dance.mp4")

while True:
    check, img = video.read()
    
    cv2.rectangle(img, (25,25),(50,50), (0, 128, 0), -5)

    cv2.circle(img, (200,200), 50, (0,100,200),-1)

    cv2.line(img,(100,100), (300,300), (44,20,100), 3)

    texto = "dance"

    cv2.putText(img,texto,(0,200),cv2.FONT_HERSHEY_SIMPLEX,2,(0, 128, 0),2)
    cv2.imshow('dance',img)

# Se apertar ESC (27), fecha o vídeo
    if cv2.waitKey(10) == 27:
        break

video.release()
cv2.destroyAllWindows()

