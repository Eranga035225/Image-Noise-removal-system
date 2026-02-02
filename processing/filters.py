from __future__ import annotations
import cv2
import numpy as np


def _validate_kernel_size(k: int) -> int:
    if not isinstance(k, int):
        raise TypeError("Kernel size must be an integer")
    
    if k<=0:
        raise ValueError("Kernel size must be positive")
    

    if k % 2 == 0:
        raise ValueError("Kernel size must be odd")
    


    return k




def mean_filter(image: np.ndarray, k: int = 3)-> np.ndarray:
    k = _validate_kernel_size(k)
    return cv2.blur(image, (k,k))


def gaussian_filter(image: np.ndarray, k: int = 5, sigma: float = 1.0)-> np.ndarray:
    k = _validate_kernel_size(k)

    if not isinstance(sigma, (int,float)):
        raise TypeError("Sigma must be a number")
    
    if sigma <= 0 :
        raise ValueError("Sigma must be positive")
    
    return cv2.GaussianBlur(image, (k,k), sigmaX=float(sigma), sigmaY=float(sigma))
    


def median_filter(image: np.ndarray, k: int = 3)-> np.ndarray:
    k = _validate_kernel_size(k)
    if k == 1 :
        return image.copy()
    
    return cv2.medianBlur(image,k)



def apply_filter(image: np.ndarray, filter : str, k : int = 5 , sigma: float = 1.0 )-> np.ndarray:
    if image is None:
        raise ValueError("Input image is None")
    
    if not isinstance(filter, str):
        raise TypeError("Filter type must be a string")
    
    name = filter.strip().lower()

    if name == "mean":
        return mean_filter(image, k=k)
    
    elif name == "gaussian":
        return gaussian_filter(image, k=k, sigma=sigma)
    

    elif name == "median":
        return median_filter(image, k=k)
    
    
    

  
        

        
    

