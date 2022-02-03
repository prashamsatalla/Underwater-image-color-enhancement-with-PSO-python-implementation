import os
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from utility import *


dir_path = "./images/"

original_images =[]
NUCE_images =[]

img_w = 350 #image width
img_h = 350 #image height

for im in os.listdir(dir_path):

	img = cv.imread(dir_path+im,1)
	# img = cv.resize(img,(img_w,img_h))
	original_images.append(img)

	nuce_img = NUCE(img)  
	NUCE_images.append(nuce_img)

	cv.imwrite("./results/"+im.split('/')[-1], nuce_img)


fig, ax = plt.subplots(4,2,figsize=(6, 9), constrained_layout = False)
ax[0][0].set_title("Original Image")
ax[0][1].set_title("NUCE Image")

for i in range(4):

	ax[i][0].imshow(cv.cvtColor(original_images[i], cv.COLOR_BGR2RGB),cmap='gray')
	ax[i][0].axis('off')

	ax[i][1].imshow(cv.cvtColor(NUCE_images[i], cv.COLOR_BGR2RGB), cmap='gray')
	ax[i][1].axis('off')

fig.tight_layout()
plt.savefig("./results/output.jpg")
# plt.show()
