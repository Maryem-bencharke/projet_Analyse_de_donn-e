from PIL import Image
import numpy.linalg as alg
import numpy as np
from matplotlib.image import imread
import matplotlib.pyplot as plt
import os #The OS module in Python provides functions for creating and removing a directory (folder), fetching its contents, changing and identifying the current directory,
'''im=Image.open("lena_gris.png") 
T=np.array(im)
h,l =T.shape #hauteur, largeur de l'image
'''
    
def compression(M):
    U , S , VT = np.linalg.svd(M, full_matrices = False)
    S = np.diag(S)
    j= 0
    for r in (20,30,180):
        Xapprox = U[:,:r] @ S[0:r,:r] @ VT[:r,:]
        plt.figure(j+1)
        j+=1
        img = plt.imshow(Xapprox -256)
        img.set_cmap('gray')
        plt.axis('off')
        plt.title('r =' +str(r))
        plt.show()
    plt.figure(1)
    plt.semilogy(np.diag(S))
    plt.title('singular values')
    plt.show()  
    plt.figure(2)
    plt.plot(np.cumsum(np.diag(S))/np.sum(np.diag(S))) 
    plt.title('singular values : cumulative sum')
    plt.show() 
    return U , S , VT
im=Image.open("lena_gris.png") 
M=np.array(im)    
h,l =M.shape
print(compression(M))
#pour la valeur de k permettant de capter 95% de la variance c'est 
#on va faire une projection sur la 2eme figure pour 0,95 ensuite on peut avoir la valeur de k

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        