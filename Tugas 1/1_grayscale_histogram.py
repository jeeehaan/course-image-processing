# Import modul yang dibutuhkan
import cv2
from matplotlib import pyplot as plt

# Import gambar yang ingin dibaca
image = cv2.imread('image/5.jpg')

# Mengubah gambar ke grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# membuat histogram dari gambar grayscale
# mengkalkulasikan warna dari gambar grayscale
histr = cv2.calcHist([gray_image], [0], None, [256], [0,256])

# hasil kalkulasi menjadi plot
plt.plot(histr)

# simpan hasil histogram ke nama dan ekstensi yang diinginkan dan
# jangan lupa untuk menambahakan format gambar seperti .jpg .png dll
plt.savefig(f'image/5_gray_histo.jpg')

# simpan gambar yang telah dijadikan grayscale
cv2.imwrite(f'image/5_gray_image.jpg', gray_image)