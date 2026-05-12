import cv2

img = cv2.imread(r"processamento_morfologico\conteudos\nuvem.jpg")
img = cv2.resize(img, (500,400))
cv2.imshow("img original", img)

# Converte a imagem para escala de cinza
# Isso facilita os processamentos posteriores
img_cinza = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
cv2.imshow("imagem cinza", img_cinza)

# Aplica um desfoque Gaussiano (Blur)
# Serve para reduzir ruídos na imagem
img_Blur = cv2.GaussianBlur(img_cinza, (7,7), 0)
cv2.imshow("imagem blur", img_Blur)

# Detecta bordas usando o algoritmo Canny
# 50 = limite mínimo
# 100 = limite máximo
img_canny = cv2.Canny(img, 50,100)
cv2.imshow("img canny", img_canny)

# DILATAÇÃO (Dilate)
# Aumenta as regiões brancas da imagem
# Muito usado para engrossar bordas e conectar partes quebradas
# iterations=5 -> aplica o efeito 5 vezes
img_dilate = cv2.dilate(img_canny, (5,5), iterations=5)
cv2.imshow("img dilate",img_dilate)

# EROSÃO (Erode)
# Faz o contrário da dilatação
# Diminui as regiões brancas da imagem
# Usado para remover pequenos ruídos
img_erode = cv2.erode(img_canny, (5,5), iterations=2)
cv2.imshow("img erode", img_erode)


# OPENING (Abertura)
# Primeiro aplica erosão e depois dilatação
# Remove pequenos ruídos sem aumentar os objetos
img_opening = cv2.morphologyEx(img_canny, cv2.MORPH_OPEN, (5,5))
cv2.imshow("img opening",img_opening)


# CLOSING (Fechamento)
# Primeiro aplica dilatação e depois erosão
# Fecha pequenos buracos e falhas nos objetos
img_closing = cv2.morphologyEx(img_canny, cv2.MORPH_CLOSE, (5,5))
cv2.imshow("img closing", img_closing)


cv2.waitKey(0)

