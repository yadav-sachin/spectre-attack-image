import numpy as np
import matplotlib.pyplot as plt
import time
import cv2
prev_data = [0]
shape = (1130, 928, 3)
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
    time.sleep(2)
    if(prev_data == img_data): 
        break
    prev_data = img_data
