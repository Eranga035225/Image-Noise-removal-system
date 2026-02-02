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


    


        
    

