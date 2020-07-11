import cv2
import matplotlib.pyplot as plt
fs = open('../encodedImg.bin', 'w')

img = cv2.imread('secret_img2.jpg')

shape = img.shape

rgba_data = []

data = ""
for i in range(shape[0]):
    for j in range(shape[1]):
        for k in range(shape[2]):
            data += chr(img[i][j][k]//2)

print(shape)
fs.write(data)
fs.close()

