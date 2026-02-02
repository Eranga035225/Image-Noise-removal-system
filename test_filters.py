import cv2
from processing.filters import apply_filter

img = cv2.imread("assets/samples/test1.png")  # put any image here
out = apply_filter(img, "gaussian", k=5, sigma=1.0)

cv2.imwrite("output/test_gaussian.png", out)
print("Saved output/test_gaussian.png")




