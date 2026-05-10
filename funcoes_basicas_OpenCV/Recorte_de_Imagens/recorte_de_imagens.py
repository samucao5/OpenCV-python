import cv2

img = cv2.imread(r'openCV_conceitos basicos\conteudos\floresta.jpg')
imgredin = cv2.resize(img, (1200,800))
dim = cv2.selectROI("selecione a janela de recorte", imgredin, False)
print(dim)
v1 = int(dim[0])
v2 = int(dim[1])
v3 = int(dim[2])
v4 = int(dim[3])

recorte = imgredin[v2:v2+v4, v1:v1+v3]

cv2.imshow("imagem", imgredin)
cv2.imshow("imagem recortada", recorte)
cv2.waitKey(0)

cv2.destroyAllWindows()