import numpy as np
import matplotlib.pyplot as plt
import time
import cv2

prev_data = [0]
shp = [int(i) for i in input('Enter the dimensions of the Image: ').split()]
assert(len(shp) == 2)
shape = (shp[0], shp[1], 3)

while True:
    tot_len = shape[0]*shape[1]*shape[2]
    fs = open('../spectre_output.txt', 'r')
    img_arr = np.zeros(shape)
    img_data = fs.read()
    len_img_data = len(img_data)
    img_data = [int(i)*2 for i in img_data.split()]
    img_data = img_data + (tot_len - len(img_data))*[0]

    counter = 0
    for i in range(shape[0]):
        for j in range(shape[1]):
            for k in range(shape[2]):
                img_arr[i][j][k] = img_data[counter]
                counter+=1

    cv2.imwrite('secret.jpg', img_arr)
    time.sleep(20)
    if(prev_data == img_data): 
        break
    prev_data = img_data
