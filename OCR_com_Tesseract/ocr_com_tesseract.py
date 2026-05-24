import cv2
import pytesseract as pt

pt.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

img = cv2.imread(r"OCR_com_Tesseract\conteudo\imgteste.JPG")

#pegar a img e transforma em texto os caracteres da img
#print(pt.pytesseract.image_to_string(img,lang='por'))
#identifica palavras ao inves de caracteres da img
dados = pt.pytesseract.image_to_data(img,lang='por')
print(dados)


for x,linha in enumerate(dados.splitlines()):
    if x !=0:
        linha = linha.split()
        print(linha)
        if len(linha)==12:
            x,y,w,h = int(linha[6]), int(linha[7]), int(linha[8]), int(linha[9])
            palavra = linha[11]
            cv2.rectangle(img, (x, y),(w+x,h+y),(0,255,0),1)
            cv2.putText(img,palavra,(x,y+10),cv2.FONT_HERSHEY_SIMPLEX,1,(0,245,0),2)

cv2.imshow('imagem', img)
cv2.waitKey(0)
