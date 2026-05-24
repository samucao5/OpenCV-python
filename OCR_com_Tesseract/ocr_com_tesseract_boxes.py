import cv2
import pytesseract as pt

pt.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

img = cv2.imread(r"OCR_com_Tesseract\conteudo\imgteste.JPG")

#pegar a img e transforma em texto os caracteres da img
#print(pt.pytesseract.image_to_string(img,lang='por'))
#mostra a localização de cada letra da img 
boxes = pt.pytesseract.image_to_boxes(img,lang='por')

imH, imW,_ = img.shape

for b in boxes.splitlines():
    b = b.split(' ')
    letra,x,y,w,h = b[0], int(b[1]), int(b[2]), int(b[3]), int(b[4])
    cv2.rectangle(img, (x, imH - y),(w,imH - h),(0,255,0),1)
    cv2.putText(img,letra,(x,imH-y+25),cv2.FONT_HERSHEY_SIMPLEX,1,(0,245,0),2)

cv2.imshow('imagem', img)
cv2.waitKey(0)