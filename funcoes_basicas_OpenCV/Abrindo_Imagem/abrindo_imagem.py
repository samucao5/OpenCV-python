import cv2
#carrega a imagem do caminho informado
#este r no começo permite copiar o path de maneira original sem precisar reescrever as barras
img = cv2.imread(r'openCV_conceitos basicos\conteudos\floresta.jpg')

#retorna o tamanho da imagem
print("escala da imagem com rgb",img.shape)

#torna a imagem cinza ou dois tons
imgcinza = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

print("escala da imagem cinza",imgcinza.shape)

#como o computador observa a imagem
print(imgcinza)
#verifica se a imagem foi encontrada
if img is None:
    print("Imagem não encontrada")
else:
# Cria uma janela exibindo a imagem
    cv2.imshow('exibindo imagem', img)
    cv2.imshow('imagem cinza', imgcinza)
#define o tempo que a tela permanecera aberta
    cv2.waitKey(0)