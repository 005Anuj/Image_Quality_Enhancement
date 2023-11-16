# Image Quality Enhancement with Python

## Introduction

This Python program utilizes the OpenCV library to enhance the quality of an image. The input image file is named "test.jpeg," and the enhanced image is saved as "hd_output.jpeg."

## Requirements

- Python 3.x
- OpenCV library
- Matplotlib
- NumPy

## Installation

To install the required libraries, run the following command:

```bash
pip install opencv-python matplotlib numpy
```

## Code Explanation

```python
import cv2
import matplotlib.pyplot as plt
import numpy as np

# Read the input image
input_image_file = cv2.imread('./test.jpeg')

# Function to expand a 2D array
def expand2darray(arr):
    row_added = []
    for row in range(1, arr.shape[0]):
        temp = (arr[row-1] + arr[row]) / 2
        row_added.append(arr[row-1].tolist())
        row_added.append(temp.tolist())
    
    row_added.append(arr[arr.shape[0]-1].tolist())
    row_added = np.array(row_added)
    arr = row_added
    
    column_added = []
    for column in range(1, arr.shape[1]):
        temp = (arr[:, column-1] + arr[:, column]) / 2
        column_added.append(arr[:, column-1].tolist())
        column_added.append(temp.tolist())
    
    column_added.append(arr[:, arr.shape[1]-1].tolist())
    column_added = np.array(column_added)
    column_added = column_added.transpose()
    
    return column_added

# Splitting channels and normalizing values
r, g, b = cv2.split(input_image_file)
r, g, b = r/255, g/255, b/255

# Expanding 2D arrays for each channel
r_new = expand2darray(r)
g_new = expand2darray(g)
b_new = expand2darray(b)

# Rescaling values to the original range
r_new, g_new, b_new = r_new * 255, g_new * 255, b_new * 255

# Merging channels to create the enhanced image
new_img = cv2.merge((r_new, g_new, b_new))

# Save the enhanced image
cv2.imwrite("hd_output.jpeg", new_img)
```

## Usage

1. Ensure the input image file ("test.jpeg") is in the same directory as the script.
2. Run the script, and the enhanced image will be saved as "hd_output.jpeg" in the same directory.

Feel free to adjust the script according to your specific needs and experiment with different parameters for further enhancements.
