# Program developed by
# NAME : HARI PRIYA M
# REGISTER NO : 212224240047

import cv2
import matplotlib.pyplot as plt

# READ THE IMAGE USING imread()
img = cv2.imread("/content/Screenshot 2025-11-04 220203.png")      

# Convert BGR to RGB for displaying colors correctly
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Convert to GRAYSCALE
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Gaussian smoothing to reduce noise
gray = cv2.GaussianBlur(gray, (3, 3), 0)

# SOBEL EDGE DETECTION - X AXIS
sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=5)

plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.imshow(img_rgb)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(sobelx, cmap='gray')
plt.title("Sobel X axis")
plt.axis("off")
plt.show()

# SOBEL EDGE DETECTION - Y AXIS
sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=5)   
plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.imshow(img_rgb)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(sobely, cmap='gray')
plt.title("Sobel Y axis")
plt.axis("off")
plt.show()

# SOBEL EDGE DETECTION - XY (Combined)
sobelxy = cv2.Sobel(gray, cv2.CV_64F, 1, 1, ksize=5)

plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.imshow(img_rgb)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(sobelxy, cmap='gray')    
plt.title("Sobel XY axis")
plt.axis("off")
plt.show()

# LAPLACIAN EDGE DETECTION
lap = cv2.Laplacian(gray, cv2.CV_64F)

plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.imshow(img_rgb)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(lap, cmap='gray')      
plt.title("Laplacian Edge Detector")
plt.axis("off")
plt.show()


# CANNY EDGE DETECTION
canny = cv2.Canny(gray, 120, 150)

plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.imshow(img_rgb)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(canny, cmap='gray')
plt.title("Canny Edge Detector")   
plt.axis("off")
plt.show()
