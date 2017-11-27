# Use python3
import sys
import numpy as np
import matplotlib.image as mpimg
from PIL import Image

# Method 1: use matplotlib
# Will generate 512 * 512 * 4 which is RGBA!!!! not RGB
#img1 = mpimg.imread('lena.png')
#print(img1.shape)
#print(img1)
#print(type(img1))

# Method 3: use cv2
#Didnt success to use cv2
#import cv2
#img3 = cv2.imread("lena.png")
#print(type(img3))
#print(img3.shape)

# Method 2: Use PIL's image
img_org = Image.open('lena.png').convert('RGBA')
arr_org = np.array(img_org)
img_mod = Image.open('lena_modified.png').convert('RGBA')
arr_mod = np.array(img_mod)
arr_diff= np.zeros_like(arr_mod)

for i in range(arr_mod.shape[0]) :
    for j in range(arr_mod.shape[1]) :
            #if np.all(arr_mod[i,j]) == np.all(arr_org[i,j]) :
            #if np.all(arr_mod[i, j]) == np.all(arr_org[i, j]):
            #    arr_diff[i,j] = (0,0,0,0)
            #else :
            #    #arr_diff[i,j] = arr_mod[i,j]
            #    arr_diff[i, j] = arr_mod[i, j]

            if np.array_equal(arr_mod[i, j], arr_org[i, j]):
                arr_diff[i, j] = (0, 0, 0, 0)
            else:
                arr_diff[i, j] = arr_mod[i, j]

#print(arr_org[0,0])
#print(arr_mod[0,0])

#arr_diff= arr_mod - arr_org # this is wrong!
print(arr_diff.shape)
#print(arr_diff)
img_diff = Image.fromarray(arr_diff, 'RGBA')
img_diff.save('ans_two.png')
