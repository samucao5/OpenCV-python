import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread(r"C:\Users\samue\Music\OpenCv\Pre-Processamento\Histograma de cores\cores.jpg")

if img is None:
    print("Erro: imagem não encontrada")
    exit()

img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
plt.imshow(img_rgb)

azul, verde, vermelho = cv.split(img)

plt.imshow(img)
plt.title("Imagem colorida")
plt.axis('off')

fig = plt.figure(figsize=(15,5))

axl = fig.add_subplot(131)
axl.hist(azul.ravel(), 256, [0,256])
axl.set_title("Histograma do canal azul")

ax2 = fig.add_subplot(132)
ax2.hist(verde.ravel(), 256, [0,256])
ax2.set_title("Histograma do canal verde")

ax3 = fig.add_subplot(133)
ax3.hist(vermelho.ravel(), 256, [0,256])
ax3.set_title("Histograma do canal vermelho")

plt.show()