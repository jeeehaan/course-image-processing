import cv2
import numpy
from matplotlib import pyplot as plt

color = ('b','g','r') 

img = cv2.imread('image/5.jpg')
img_to_yuv = cv2.cvtColor(img,cv2.COLOR_BGR2YUV)
img_to_yuv[:,:,0] = cv2.equalizeHist(img_to_yuv[:,:,0])
hist_equalization_result = cv2.cvtColor(img_to_yuv, cv2.COLOR_YUV2BGR)
 
cv2.imwrite('image/5_histo_equal.jpg',hist_equalization_result)


# for i, col in enumerate(color):
histr =cv2.calcHist([hist_equalization_result],[0],None,[256],[0,256])
plt.plot(histr,color='b')
plt.xlim([0,256])

plt.savefig(f'image/5_histo_equal_histo_b.jpg')
plt.show()

histr =cv2.calcHist([hist_equalization_result],[1],None,[256],[0,256])
plt.plot(histr,color='g')
plt.xlim([0,256])

plt.savefig(f'image/5_histo_equal_histo_g.jpg')
plt.show()

histr =cv2.calcHist([hist_equalization_result],[2],None,[256],[0,256])
plt.plot(histr,color='r')
plt.xlim([0,256])

plt.savefig(f'image/5_histo_equal_histo_r.jpg')
plt.show()