# QRCode Dataset Generation

This project generates a dataset of QR code images overlaid on various desert background images. The dataset consists of images and corresponding labels in **YOLO** format for training object detection models. It utilizes Python libraries such as **OpenCV**, **cvzone**, and **SciPy** to manipulate and create realistic images with QR codes placed in random positions and orientations.

## Table of Contents

1. [Overview](#overview)
2. [Installation](#installation)
3. [How It Works](#how-it-works)
4. [Dataset Generation](#dataset-generation)
5. [Technologies Used](#technologies-used)
6. [License](#license)

---

## Overview

The goal of this project is to generate a dataset for object detection, specifically for detecting **QR codes** placed on desert images. The QR code image is randomly resized, rotated, and placed at a random position on different desert backgrounds. For each generated image, a corresponding label is saved in YOLO format, which contains the normalized bounding box coordinates of the QR code.

---

## Installation

### 1. Prerequisites

Before running the project, make sure you have the following libraries installed:

- **OpenCV**: For image manipulation and object detection.
- **cvzone**: For overlaying images (QR code on background).
- **SciPy**: For rotating the QR code.
- **UUID**: For unique file naming.

You can install the required dependencies using `pip`:

```bash
pip install opencv-python
pip install cvzone
pip install scipy
```

---

## How It Works

1. **Prepare QR code and Desert Backgrounds**: 
   - The QR code image (`qr.png`) is loaded into the program.
   - A set of desert background images is loaded from a specified directory.
   
2. **Randomized Image Generation**: 
   - The QR code is resized randomly.
   - It is rotated by a random angle (0-360 degrees).
   - The QR code is randomly positioned on the desert background.
   
3. **Bounding Box Calculation**: 
   - For each generated image, the program calculates the normalized bounding box coordinates of the QR code, which are required for YOLO-based object detection models.
   
4. **Image and Label Saving**: 
   - The final image (QR code overlaid on desert background) is saved in the output directory.
   - A corresponding `.txt` label file is generated containing the normalized bounding box coordinates for YOLO training.

5. **File Renaming**: 
   - The files in the flags directory are renamed alphabetically (from `a.png` to `z.png`), ensuring that the names are unique and consistent for labeling purposes.

---

## Dataset Generation

To generate the dataset, follow these steps:

1. **Set the Source and Output Directories**:
   - **QR Code Image**: Place your QR code image (e.g., `qr.png`) in the specified path.
   - **Desert Background Images**: Place the desert background images in the specified directory.
   - **Output Directories**: The generated images will be saved to an output folder, and the corresponding label files will be saved to a separate folder.
   
2. **Running the Script**:
   Run the script using the following command:

```bash
python dataset_generator.py
```

This will generate the dataset with the desired number of images and labels.

3. **Renaming Flag Images**:
   You can also run the renaming script for flag images located in the `flags` directory. This will rename all `.png` files alphabetically:

```bash
python rename_flags.py
```

---

## Technologies Used

- **OpenCV**: 
  - For reading and manipulating images.
  - For overlaying the QR code image on the desert background.
- **cvzone**: 
  - For overlaying the QR code image onto the desert background in a simple and efficient way.
- **SciPy**: 
  - For rotating the QR code image randomly to simulate realistic placement.
- **UUID**: 
  - For generating unique filenames for each image to ensure no overwriting of files.

---

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

