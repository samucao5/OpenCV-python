import cv2

img = cv2.imread(r'processamento_morfologico\conteudos\pag_1.jpg')
cv2.imshow('imagem original', img)
img_cinza = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

_,th1 = cv2.threshold(img_cinza,127,255,cv2.THRESH_BINARY)
cv2.imshow('th1', th1)


img_2 = cv2.imread(r'processamento_morfologico\conteudos\img02.jpg')
img_2 = cv2.resize(img_2, (500,200))
img_cinza_2 = cv2.cvtColor(img_2,cv2.COLOR_BGR2GRAY)

_,th2 = cv2.threshold(img_cinza_2,127,255,cv2.THRESH_BINARY_INV)
cv2.imshow('th2', th2)

th3 = cv2.adaptiveThreshold(img_cinza_2,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,25,16
)
cv2.imshow('th3', th3)

th4 = cv2.adaptiveThreshold(img_cinza_2,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,25,16)
cv2.imshow('th4', th4)
cv2.waitKey(0)