from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage.io import imread, imshow
from skimage import exposure
import numpy.linalg as alg


#im=plt.imread("lena_couleur.png") 
im=Image.open("lena_couleur.png") 
M=np.array(im)
imr = M[:,:,0]#picks out the red/first number in each RGB triple
img = M[:,:,1]#picks out the green/second number in each RGB triple
imb = M[:,:,2]#picks out the blue/third number in each RGB triple
U_red , S_red , VT_red = np.linalg.svd(imr)#here we compute SVD of the matrix of the 435 X 395  matrix of red weights

U_blue , S_blue, VT_blue = np.linalg.svd(imb)#here we compute SVD of the matrix of the 435 X 395  matrix of blue weights

U_green , S_green , VT_green = np.linalg.svd(img)#here we compute SVD of the matrix of the 435 X 395  matrix of green weights



def compress_color(M):    
    j= 0
    m = M.shape[0]
    n = M.shape[1]
    for r in (20,60,180):# here the r is the number of singular values we use to compress our image
       comp_red = U_red[:,:r] @ np.diag(S_red[:r])  @ VT_red[:r,:]#use @ instead of * for matrix multiplication in Python!
       comp_red = comp_red.astype(int)#transform the values of our data to intiger instead of float.
        
       comp_green = U_green[:,:r] @np.diag(S_green[:r]) @ VT_green[:r,:]
       comp_green = comp_green.astype(int)

       comp_blue = U_blue[:,:r] @ np.diag(S_green[:r]) @ VT_blue[:r,:]
       comp_blue = comp_blue.astype(int)
       compress_array = np.stack((comp_red , comp_green  , comp_blue) , axis = 2)#here we join the three  arrays along a new axis.
       plt.figure(j+1)
       j+=1
       plt.axis('off')
       plt.title('r =' +str(r))
       plt.imshow(compress_array)
       taux_de_compression = (r*(m+n+1))/(m*n)
    print(taux_de_compression)
       
    
    




  
compress_color(M)
im2 = imread("lena_couleur.png")

def imageHist(im2):
    _, axis = plt.subplots(ncols=2, figsize=(12, 3))
    axis[0].imshow(im2)
    axis[1].set_title('Histogram')
    axis[0].set_title('Colored Image')
    rgbcolors = ['red', 'green', 'blue']
    for i, mycolor in enumerate(rgbcolors):
        axis[1].plot(exposure.histogram(im2[...,i])[0], color=mycolor)




imageHist(im2)











