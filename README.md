# EXP 06 : EDGE-DETECTION
### NAME : HARI PRIYA M
### REG NO : 212224240047
## Aim:
To perform edge detection using Sobel, Laplacian, and Canny edge detectors.

## Software Required:
Anaconda - Python 3.7

## Algorithm:
### Step1:
Import all the necessary modules for the program.

### Step2:
Load a image using imread() from cv2 module.

### Step3:
Convert the image to grayscale

### Step4:
Using Sobel operator from cv2,detect the edges of the image.

### Step5:

Using Laplacian operator from cv2,detect the edges of the image and Using Canny operator from cv2,detect the edges of the image.

## Program

```python
# DEVELOPED BY :
# NAME : HARI PRIYA M
# REG NO : 212224240047

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
```
## Outputs:

### ORIGINAL IMAGE VS 

### i)SOBEL EDGE DETECTOR
### ii)LAPLACIAN EDGE DETECTOR
### iii)CANNY EDGE DETECTOR

<br>
<img width="600" height="800" alt="Screenshot 2025-11-04 222022" src="https://github.com/user-attachments/assets/95f87013-64b2-4c58-838b-58b8d90b43f4" />
<img width="600" height="800" alt="Screenshot 2025-11-04 222037" src="https://github.com/user-attachments/assets/9531751a-25bf-423f-972e-fca3ce78bf06" />

<img width="600" height="400" alt="Screenshot 2025-11-04 222045" src="https://github.com/user-attachments/assets/01fe6767-07a4-403c-a5b4-e51ed223d88c" />

<br>

<br>


## Result:
Thus the edges are detected using Sobel, Laplacian, and Canny edge detectors.
