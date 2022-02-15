#BT19ECE033 VISHAL YADAV
#Assignment 1-DIP:
# 1) Read and dispaly a color image
# 2) Convert color image to grayscale and binary
# 3) Add constant value to it

# Importing required libraries
import math                                               
import numpy as np
import cv2
image = cv2.imread('vishal.jpeg')       

path = r"C:\Users\USER\Desktop\images\vishal.jpeg" #declaring path of image
image = cv2.imread(path)                                  #Reading the image   
m,n,v = image.shape                                      
gray_image = np.zeros((m,n),np.uint8)                   
binary = np.zeros((m,n),np.uint8)  
binary_image = np.zeros((m,n),np.uint8)  
added_const = np.zeros((m,n),np.uint8)
print("Dimensions of Image is {}x{}x{}".format(m,n,v))

Sum = 0
for i in range(m):
    for j in range(n):                            
for i in range(m):        #Converting color Image to Grayscale by averaging
    for j in range(n): 
        k=0;                           
        for k in range(v):
            Sum = Sum + image[i][j][k]
        gray_image[i][j] = math.floor(Sum/3)
        Sum = 0
            k += math.floor(image[i][j][k]/3)

cv2.imwrite("gray_image.png",gray_image)
        gray_image[i][j] = k

for x in range(m):
for x in range(m):        #Converting gray Image to binary, Threshold = 50
    for y in range(n):
        if gray_image[x][y]%2==0 :
          binary[x][y]=0
        if gray_image[x][y]>=50 :
          binary_image[x][y]=0
        else:
          binary[x][y]=255
          binary_image[x][y]=255

cv2.imwrite("binary_image.png",binary)

for x in range(m):
for x in range(m):        #Adding a constant value '34' to image
    for y in range(n):
        k=min(gray_image[x][y]+34,255)
        added_const[x][y]=k

cv2.imwrite("Const_image.png",added_const)
#Dispalying the Images
cv2.imshow("original Image",image)
cv2.waitKey(0)
cv2.imshow('Grayscale Image',gray_image)
cv2.waitKey(0)
cv2.imshow('Bianry Image',binary_image)
cv2.waitKey(0)
cv2.imshow('Grayscale Image + constant value ',added_const) 
cv2.waitKey(0)
cv2.destroyAllWindows()