import cv2
import matplotlib.pyplot as plt
fs = open('../encodedImg.txt', 'w')

imgFileName = input('Enter the target Image file name: ').strip()
if len(imgFileName) == 0:
    imgFileName = 'secret_img.jpg'
    
img = cv2.imread(imgFileName)
print('Processing File ... \n')

shape = img.shape

rgba_data = []

data = ""
for i in range(shape[0]):
    for j in range(shape[1]):
        for k in range(shape[2]):
            data += chr(img[i][j][k]//2)

print(f'Image Dimensions : {shape[0]} x {shape[1]}')
print('Image Successfully Encoded in RGBA !!')
fs.write(data)
fs.close()
