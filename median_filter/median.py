import cv2

img = cv2.imread('./../decode_rgb/secret2.jpg')  # Load image
median_radius = int(input('Enter the radius for Median Filter: '))
img_median = cv2.medianBlur(img, median_radius)  # Add median filter to image

cv2.imwrite('result.jpg', img_median)