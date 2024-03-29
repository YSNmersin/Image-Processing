#Logaritmik Donusum
import cv2
import numpy as np
import matplotlib.pyplot as plt

fpath = "Sources\Dessert.jpg"

np.seterr(divide='ignore')

# Read an image
image = cv2.imread(fpath)

# Apply log transformation method

c = 255 / np.log(1 + np.max(image))
log_image = c * (np.log(image + 1))

# Specify the data type so that
# float value will be converted to int

log_image = np.array(log_image, dtype=np.uint8)

# Display both images
res = np.hstack((image, log_image))
plt.imshow(cv2.cvtColor(res, cv2.COLOR_BGR2RGB))
plt.show()
