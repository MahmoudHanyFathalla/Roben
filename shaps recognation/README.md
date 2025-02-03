# Shape Recognition using OpenCV

This project utilizes **OpenCV** to recognize and classify basic shapes in an image. It identifies **Triangles**, **Rectangles**, **Circles**, and **Lines** by detecting and analyzing the contours of the shapes. The project counts the number of each shape present in the image and visualizes the results by drawing the contours and labeling them accordingly.

---

## Table of Contents

1. [Overview](#overview)
2. [Installation](#installation)
3. [How It Works](#how-it-works)
4. [Running the Project](#running-the-project)
5. [Technologies Used](#technologies-used)
6. [License](#license)

---

## Overview

This project demonstrates shape recognition using **OpenCV's** contour detection and approximation algorithms. It can detect the following shapes:

- **Triangle**: A shape with 3 vertices.
- **Rectangle**: A shape with 4 vertices.
- **Circle**: A shape with more than 5 vertices.
- **Line**: A shape with 2 vertices.

### Key Features:

- Detects basic shapes in a grayscale image.
- Classifies shapes as **Triangle**, **Rectangle**, **Circle**, or **Line**.
- Counts the number of each shape in the image.
- Visualizes the results by drawing contours and labeling the detected shapes.
- Displays the shape counts on the image.

---

## Installation

To run this project, you need to install the necessary Python libraries:

- **OpenCV**: For image processing and contour detection.
- **NumPy**: For numerical operations.

You can install them with the following commands:

```bash
pip install opencv-python numpy
```

---

## How It Works

1. **Image Loading**:
   - The input image (`5.jpg`) is read in grayscale, while another image (`imgg.JPG`) is used for display purposes.
   - The images are resized to a fixed dimension for uniformity.

2. **Thresholding**:
   - The grayscale image is thresholded to create a binary image that isolates the shapes. The threshold value is set to 140.

3. **Contour Detection**:
   - **`cv2.findContours`** is used to find contours in the binary image. These contours represent the boundaries of the shapes.

4. **Shape Classification**:
   - The contours are approximated using **`cv2.approxPolyDP`**. Based on the number of vertices, shapes are classified as:
     - **Triangle**: 3 vertices
     - **Rectangle**: 4 vertices
     - **Circle**: More than 5 vertices
     - **Line**: 2 vertices

5. **Visualization**:
   - The project draws contours around the shapes and places labels (such as "Triangle", "Rectangle", etc.) next to the shapes.
   - The total count of each type of shape is also displayed on the image.

6. **Output**:
   - The processed image with shapes and labels is displayed in one window.
   - The count of each shape is displayed in a second window, both in the terminal and on the image itself.

---

## Running the Project

1. **Prepare Your Files**:
   - Ensure you have the following files in the specified locations:
     - `5.jpg`: The input image that contains the shapes.
     - `imgg.JPG`: The image used for displaying shape counts.

2. **Run the Script**:
   - Execute the Python script using the following command:

     ```bash
     python main.py
     ```

3. **View Results**:
   - The processed image with contours and shape labels will appear in a window called **"img"**.
   - The shape counts will be displayed in a second window called **"imgg"**.

4. **Output**:
   - The number of each detected shape is displayed both on the image and printed in the terminal.

---

## Technologies Used

- **OpenCV**: For image processing, contour detection, and drawing shapes.
- **NumPy**: For handling numerical operations on the image arrays.

---

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
