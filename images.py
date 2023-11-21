import matplotlib
matplotlib.use("TkAgg")
import numpy as np
import cv2
import matplotlib.pyplot as plt
# читаем изображение
img = cv2.imread("cat.jpg")
# конвертируем в RGB для pyplot
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# обрезка изображения
trans_img = img[150:500, 150:500]

plt.axis('off')
plt.imshow(trans_img)
plt.show()
