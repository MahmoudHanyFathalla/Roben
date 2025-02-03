# Shape Detection with Template Matching using OpenCV

This project demonstrates how to use **template matching** with OpenCV to detect specific objects or patterns in an image. The code matches predefined templates (images of objects) to a target image and highlights the locations where the templates are found. It then counts how many times each template appears in the image and outputs the result.

The project is particularly useful for applications where predefined patterns or objects need to be identified within a larger image, such as in image processing, quality control, or object recognition tasks.

## Table of Contents

1. [Overview](#overview)
2. [Installation](#installation)
3. [How It Works](#how-it-works)
4. [Running the Project](#running-the-project)
5. [Technologies Used](#technologies-used)
6. [License](#license)

---

## Overview

This script uses **OpenCV**'s **`matchTemplate`** function to perform template matching. It compares a predefined template image with a target image and finds areas that match the template. The code works with multiple templates, detects all occurrences of each template, counts how many times each template appears, and draws rectangles around the detected objects.

The project works with grayscale images and uses the **`cv.TM_CCOEFF_NORMED`** method for template matching. When the match exceeds a set threshold, it identifies the object and draws a red rectangle around it.

---

## Installation

Before running the project, ensure you have the required libraries installed:

- **OpenCV**: For handling image processing and template matching.
- **NumPy**: For numerical operations on images.
- **Matplotlib**: For displaying images (optional, if you want to visualize the results directly).

You can install the required libraries using `pip`:

```bash
pip install opencv-python numpy matplotlib
```

---

## How It Works

1. **Loading Images**:
   - The script loads a target image (`img.jpg`) and several template images (`cr.jpg`, `rec.jpg`, `tr.jpg`, `line.jpg`) using OpenCV's **`imread`** function. These templates represent the objects you want to detect.

2. **Template Matching**:
   - The **`matchTemplate`** function compares each template image with the target image using the **`cv.TM_CCOEFF_NORMED`** method, which computes a normalized correlation score between the template and each part of the target image.

3. **Thresholding**:
   - A threshold is set at `0.98`. Only regions of the target image that have a matching score greater than or equal to this threshold are considered as a match for the template.

4. **Counting Matches**:
   - The script counts how many times each template is detected by checking the locations where the score exceeds the threshold. The `zip(*loc[::-1])` function is used to iterate over these matching locations.

5. **Drawing Rectangles**:
   - The code draws red rectangles around the detected objects in the target image using **`cv.rectangle`** to visually highlight the regions where the templates match.

6. **Saving Results**:
   - The processed image with rectangles drawn around detected objects is saved as `res.png`.

7. **Displaying Results**:
   - The script prints the count of detected objects for each template (cr, rec, tr, line) in the console.

---

## Running the Project

1. **Prepare Your Files**:
   Ensure you have the following files in the specified paths:

   - `img.jpg`: The target image where object detection will be performed.
   - `cr.jpg`, `rec.jpg`, `tr.jpg`, `line.jpg`: The template images representing the objects to detect.
   
   You can replace these files with your own images, but ensure the paths are updated accordingly in the script.

2. **Run the Script**:
   After preparing the files, you can run the script using:

   ```bash
   python main.py
   ```

3. **View Results**:
   - The processed image will be saved as `res.png` in the working directory.
   - The terminal will print the count of detected objects for each template, like so:

     ```
     5
     3
     2
     4
     ```

   This means the template `cr.jpg` was found 5 times, `rec.jpg` was found 3 times, and so on.

---

## Technologies Used

- **OpenCV**: For image processing, template matching, and drawing rectangles around detected objects.
- **NumPy**: For handling array manipulations and image operations.
- **Matplotlib (optional)**: For visualizing images in the notebook or console.

---

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
