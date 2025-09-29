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
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('/content/closeup-shot-colorful-loriini-blurred-background.jpg')  # Replace with your image path
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Original Image
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')
plt.show()
```
### SOBEL EDGE DETECTOR

```python
sobel_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=5)  # Sobel in x direction
sobel_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=5)  # Sobel in y direction
sobel_combined = cv2.magnitude(sobel_x, sobel_y)  # Combine both directions
plt.imshow(sobel_combined, cmap='gray')
plt.title('Sobel Edge Detection')
plt.axis('off')
plt.show()
```

### LAPLACIAN EDGE DETECTOR
```python
aplacian = cv2.Laplacian(gray_image, cv2.CV_64F)

# Convert to uint8
laplacian_uint8 = cv2.convertScaleAbs(laplacian)

plt.imshow(laplacian_uint8, cmap='gray')
plt.title('Laplacian Edge Detection')
plt.axis('off')
plt.show()
```

### CANNY EDGE DETECTOR
```python
canny_edges = cv2.Canny(gray_image, 50, 150)
plt.imshow(canny_edges, cmap='gray')
plt.title('Canny Edge Detection')
plt.axis('off')  
```
## Output:

### ORIGINAL IMAGE
<br>
<img width="500" height="400" alt="Screenshot 2025-09-29 111952" src="https://github.com/user-attachments/assets/1f6fe619-074e-4f09-9cc5-a99aea3b7c31" />

<br>

### SOBEL EDGE DETECTOR
<br>
<img width="500" height="400" alt="Screenshot 2025-09-29 111958" src="https://github.com/user-attachments/assets/57074d0b-0b10-4130-9c2c-89b44e00ba8d" />

<br>

### LAPLACIAN EDGE DETECTOR
<br>
<img width="500" height="400" alt="Screenshot 2025-09-29 112004" src="https://github.com/user-attachments/assets/f1e5a02f-ae11-463f-9820-2ce963800ae7" />

<br>

### CANNY EDGE DETECTOR
<br>
<img width="500" height="400" alt="Screenshot 2025-09-29 112015" src="https://github.com/user-attachments/assets/4bca03ff-94a0-4476-9a5e-314e7386840a" />

<br>

## Result:
Thus the edges are detected using Sobel, Laplacian, and Canny edge detectors.
