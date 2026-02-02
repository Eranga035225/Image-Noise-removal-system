import cv2
from processing.filters import apply_filter

img = cv2.imread("assets/samples/test1.png")  # put any image here
out = apply_filter(img, "median", k=5)

cv2.imwrite("output/test_median.png", out)
print("Saved output/test_median.png")
