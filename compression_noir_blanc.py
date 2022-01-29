from PIL import Image , ImageFilter , ImageOps 
import numpy.linalg as alg
import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread
from skimage import exposure

    
def compression(M):
    U , S , VT = np.linalg.svd(M, full_matrices = False)
    S = np.diag(S)
    j= 0
    m , n = M.shape
    for r in (10,20,30,40,50):
        Mapprox = U[:,:r] @ S[0:r,:r] @ VT[:r,:]
        plt.figure(j+1)
        j+=1
        img = plt.imshow(Mapprox -256)
        img.set_cmap('gray')
        plt.axis('off')
        plt.title('r =' +str(r))
        plt.show() 
        taux_de_compression = (r*(m+n+1))/(m*n)
    print(taux_de_compression)
    plt.figure(1)
    plt.semilogy(np.diag(S))
    plt.plot(np.diag(S))
    plt.title('singular values')
    plt.show()  
    plt.figure(2)
    plt.plot(np.cumsum(np.diag(S))/np.sum(np.diag(S))) 
    plt.title('singular values : cumulative sum')
    plt.show()
     
    
    return U , S , VT
  
im=Image.open("lena_gris.png")
M=np.array(im)
# Generate Gaussian noise with zero mean and standard deviation 7
noise = np.random.normal(0, 7, M.shape)

# Create the noisy image and display it
noisy_img = Image.fromarray(M + noise).convert('L')
noisy_img.show()
noisy_img.filter(ImageFilter.BoxBlur(1)).show() 
    
# To normalize it: argument density=True in plt.hist
# To get the cumulative histogram: argument cumulative=True
n, bins, patches = plt.hist(M.flatten(), bins=range(256))
plt.xlabel('shades of grey')
plt.ylabel('number of pixels')
plt.show()

im2 = ImageOps.equalize(im, mask = None)
  
im2.show() 
B = np.array(im2)

n, bins, patches = plt.hist(B.flatten(), bins=range(256))
plt.xlabel('shades of grey')
plt.ylabel('number of pixels')
plt.show()


print(compression(M))
im2 = imread("lena_gris.png", as_gray=True)
def imageHist(im2):
    _, axis = plt.subplots(ncols=2, figsize=(12, 3))
    axis[0].imshow(im, cmap=plt.get_cmap('gray'))
    axis[1].set_title('Histogram')
    axis[0].set_title('Grayscale Image')
    hist = exposure.histogram(im2)
    axis[1].plot(hist[0])
    
imageHist(im2)
def variance():
    D = alg.svd(M)[1]
    sumSV = sum(D)**2
    for s in range(len(D)):
        if(sum(D[:s])**2 / sumSV)>0.95:
            print('the value of the variance is:{}'.format(s))
            Msvd = compression(M)
            Image.fromarray(Msvd).show()
    return
        
        
        
        
        
  
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        