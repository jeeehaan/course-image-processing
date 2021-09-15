#import modul yang dibutuhkan
import cv2
from matplotlib import pyplot as plt 

#import gambar yang ingin dibaca
image = cv2.imread('image/5.jpg')

#membuat histogram dari gambar rgb
#mengkalkulasikan warna dari gambar rgb
color = ('b', 'g', 'r')
for i, col in enumerate(color):
    histr = cv2.calcHist([image], [i], None, [256], [0, 256])
    plt.plot(histr, color=col)
    plt.xlim([0,256])

#simpan hasil histogram ke nama dan ekstensi yang diinginkan dan
#jangan lupa untuk menambahkan format gambar seperti .jpg .png dll
plt.savefig(f'image/5_rgb_histo.jpg')
 
#menampilkan histogram
plt.show()