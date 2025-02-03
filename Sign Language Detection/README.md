# Sign Language Detection using TensorFlow and OpenCV

This project uses a pre-trained deep learning model to detect and classify **sign language gestures** from live video input using **OpenCV** and **TensorFlow**. The model predicts the sign language gesture from a frame captured by the laptop camera and displays the corresponding class label in real-time.

## Table of Contents

1. [Overview](#overview)
2. [Installation](#installation)
3. [How It Works](#how-it-works)
4. [Usage](#usage)
5. [Technologies Used](#technologies-used)
6. [Model Information](#model-information)
7. [License](#license)

---

## Overview

The **Sign Language Detection** project is designed to recognize hand gestures in sign language using a webcam feed. The pre-trained model processes each frame and outputs the predicted sign language class. The project leverages **OpenCV** for image capture and display, and **TensorFlow** for the model inference. This is a useful application in improving communication with hearing-impaired individuals by translating their hand gestures into text.

---

## Installation

### 1. Prerequisites

Before running the project, make sure you have the following libraries installed:

- **OpenCV**: For real-time video capture and image processing.
- **TensorFlow**: For loading the pre-trained model and making predictions.
- **NumPy**: For array manipulations.

You can install the required dependencies using `pip`:

```bash
pip install opencv-python
pip install tensorflow
pip install numpy
```

### 2. Pre-trained Model

You must have a pre-trained model (`model.h5`) to run this project. Ensure that you have the model file in the correct directory or modify the path accordingly in the code.

---

## How It Works

1. **Capture Webcam Feed**: The program opens a connection to the laptop camera using OpenCV. Each frame from the webcam is captured and processed in real-time.
2. **Preprocess Frame**: The frame is resized to the input size expected by the model (224x224 pixels), and the pixel values are normalized to range from 0 to 1.
3. **Prediction**: The pre-trained model is used to predict the class label based on the processed frame.
4. **Display Results**: The predicted class is displayed on the frame using OpenCV's `putText` function, and the frame is shown in a separate window.
5. **Exit Condition**: The program will continue running until the user presses the 'q' key, at which point it will release the camera and close the OpenCV window.

---

## Usage

1. **Place the model**: Ensure you have the pre-trained model (`model.h5`) in the correct directory (as specified in the code or modify the path accordingly).
2. **Run the Script**: Execute the Python script:

```bash
python sign_language_detection.py
```

3. **View the Output**: The program will start the webcam and display the video feed with predictions in real-time. The predicted class (sign language gesture) will appear in the top-left corner.
4. **Exit the Program**: Press the 'q' key to stop the detection and close the webcam window.

---

## Technologies Used

- **OpenCV**: 
  - For capturing webcam frames.
  - For real-time image processing and displaying results.
- **TensorFlow**: 
  - For loading the pre-trained model and making predictions.
- **NumPy**: 
  - For array manipulation and data preprocessing.

---

## Model Information

- **Model Type**: Convolutional Neural Network (CNN)
- **Input Size**: 224x224 pixels (RGB images)
- **Output**: Predicted class of the hand gesture.

This model was pre-trained on a dataset of sign language gestures and is capable of classifying the most common hand gestures. You can modify the code to use any custom-trained model by adjusting the input dimensions and class labels.

---

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
