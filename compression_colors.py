from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

#im=plt.imread("lena_couleur.png") 
im=Image.open("lena_couleur.png") 
M=np.array(im)
imr = M[:,:,0]
img = M[:,:,1]
imb = M[:,:,2]
U_red , S_red , VT_red = np.linalg.svd(imr)
#S_red = np.diag(S_red) 

U_blue , S_blue, VT_blue = np.linalg.svd(imb)
#S_blue = np.diag(S_blue)

U_green , S_green , VT_green = np.linalg.svd(img)
#S_green = np.diag(S_green)



def compress_color(M):
    
    
    j= 0
    for r in (20,60,180):
       comp_red = U_red[:,:r] @ np.diag(S_red[:r])  @ VT_red[:r,:]
       comp_red = comp_red.astype(int)
        
       comp_green = U_green[:,:r] @np.diag(S_green[:r]) @ VT_green[:r,:]
       comp_green = comp_green.astype(int)

       comp_blue = U_blue[:,:r] @ np.diag(S_green[:r]) @ VT_blue[:r,:]
       comp_blue = comp_blue.astype(int)
       compress_array = np.stack((comp_red , comp_green  , comp_blue) , axis = 2)
       plt.figure(j+1)
       j+=1
       plt.axis('off')
       plt.title('r =' +str(r))
       plt.imshow(compress_array)
    

  
compress_color(M)



















