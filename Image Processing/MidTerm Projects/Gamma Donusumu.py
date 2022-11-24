#Gamma Donusumu
import cv2
import numpy as np
from matplotlib import pyplot as plt

fpath = "Sources\Dessert.jpg"

def gammaCorrection(src, gamma):
    invGamma = 1 / gamma

    table = [((i / 255) ** invGamma) * 255 for i in range(256)]
    table = np.array(table, np.uint8)

    return cv2.LUT(src, table)


img = cv2.imread(fpath)
gammaImg = gammaCorrection(img, 3.0)

res = np.hstack((img, gammaImg))
plt.imshow(cv2.cvtColor(res, cv2.COLOR_BGR2RGB))
plt.show()

fpath = "Sources\Apple.jpg"
