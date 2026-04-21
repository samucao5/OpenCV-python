import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# Leitura da imagem
img = cv.imread(r"C:\Users\samue\Music\OpenCv\Pre-Processamento\Histograma de cores\cinza.jpg", 0)

# Verificação (ESSENCIAL)
if img is None:
    print("Erro: imagem não encontrada!")
    exit()

# Mostrar imagem
plt.imshow(img, cmap='gray')
plt.title("Imagem em tons de cinza")
plt.axis('off')

# Histograma
plt.figure()
plt.hist(img.ravel(), 256, [0,256])
plt.title("Histograma da imagem")
plt.show()