import cv2

img = cv2.imread(r'processamento_morfologico\conteudos\objetos.jpg')
img = cv2.resize(img, (800,800))
imgcinza = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
imgcanny = cv2.Canny(imgcinza,30,200)
imgclose = cv2.morphologyEx(imgcanny, cv2.MORPH_CLOSE, (7,7))

contours, hierarchy = cv2.findContours(imgclose, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

numOb = 1
for cnt in contours:
    #cria o contorno do objeto
    # cv2.drawContours(img, cnt, -1,(0,200,0),2)
    x,y,w,h = cv2.boundingRect(cnt)
    objeto = img[y:y+h, x:x+w]
    cv2.imwrite(f'processamento_morfologico\projeto_separando_objetos\objetos\objeto{numOb}.jpg',objeto)
    cv2.rectangle(img,(x,y),(x+w, y+h),(0,200,0),2)
    numOb += 1

cv2.imshow("objetos_cinza", imgcinza)
cv2.imshow("objetos", img)
cv2.imshow("contornos dos objetos", imgcanny)

cv2.waitKey(0)

