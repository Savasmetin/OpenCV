import cv2
import numpy as np
from matplotlib import pyplot as plt

resim = cv2.imread("bee.jpg")

kenarlar = cv2.Canny(resim,100, 200)
print(resim.shape)
resimrgb = cv2.cvtColor(resim,cv2.COLOR_BGR2RGB)


plt.subplot(221),plt.imshow(resimrgb)
plt.title("orjinal"),plt.xticks([]),plt.yticks([])
plt.subplot(223),plt.imshow(resim)
plt.title("çevirilmemiş"),plt.xticks([]),plt.yticks([])
plt.subplot(222),plt.imshow(kenarlar,cmap = "gray")
plt.title("kenarlar"),plt.xticks([]),plt.yticks([])
plt.show()

