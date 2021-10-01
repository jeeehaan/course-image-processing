# mengimpor library
import numpy as np
import cv2
import matplotlib.pyplot as plt

# function untuk melakukan plotting terhadap gambar
def plotImages(img):
	plt.imshow(img, cmap="gray")
	plt.axis('off')
	plt.style.use('seaborn')
	plt.show()

# membaca gambar menggunakan OpenCV
# OpenCV membaca gambar secara default dalam format BGR
image = cv2.imread('img/1.jpg')

# mengonversi gambar BGR ke dalam format gambar RGB
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# melakukan plotting terhadap gambar asli
# plotImages(image)

face_detect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face_data = face_detect.detectMultiScale(image, 1.3, 5)

kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])

# membuat gambar persegi di sekitar wajah yang menjadi region of interest (ROI)
for (x, y, w, h) in face_data:
	cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
	roi = image[y:y+h, x:x+w]
	# menerapkan filter2d di atas area persegi yang baru
	roi = cv2.filter2D (roi, -1, kernel)
	# meng-impose gambar yang sudah disharpening pada gambar asli untuk mendapat final image
	image[y:y+roi.shape[0], x:x+roi.shape[1]] = roi

# menampilkan output
plotImages(image)

image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
cv2.imwrite(f'img/sharp1.jpg', image)