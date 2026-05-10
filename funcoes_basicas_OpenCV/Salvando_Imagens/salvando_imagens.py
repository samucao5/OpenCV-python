import cv2

img = cv2.imread(r'openCV_conceitos basicos\conteudos\floresta.jpg')
imgredin = cv2.resize(img, (1200,800))

# Abre uma janela para selecionar uma área da imagem
# O usuário arrasta o mouse para escolher o recorte
dim = cv2.selectROI("selecione a janela de recorte", imgredin, False)
cv2.destroyAllWindows()

# Mostra no terminal as dimensões selecionadas
print(dim)

# Coordenada X inicial
v1 = int(dim[0])

# Coordenada Y inicial
v2 = int(dim[1])

# Largura da área selecionada
v3 = int(dim[2])

# Altura da área selecionada
v4 = int(dim[3])

# Faz o recorte da imagem
# [linha inicial : linha final, coluna inicial : coluna final]
recorte = imgredin[v2:v2+v4, v1:v1+v3]

# Caminho da pasta onde a imagem será salva
diretorio = r"openCV_conceitos basicos\Salvando_Imagens\recortes"
# Pede o nome do arquivo ao usuário
nome_arquivo = input("digite o nome do arquivo: ")
# Salva a imagem recortada
cv2.imwrite(f'{diretorio}\\{nome_arquivo}.jpg',recorte)
print('Imagem salva com sucesso')

cv2.imshow("imagem", imgredin)
cv2.imshow("imagem recortada", recorte)
cv2.waitKey(0)

cv2.destroyAllWindows()