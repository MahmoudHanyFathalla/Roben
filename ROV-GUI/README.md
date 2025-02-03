# Multi-Camera Video Stream with Tkinter

This project demonstrates how to display live video streams from multiple cameras using the **Tkinter** GUI framework and **OpenCV**. The application captures video from three different cameras (USB or internal), displays the video frames in real-time, and rotates through the camera feeds to show them on a Tkinter-based interface. The program uses multithreading and queues to manage the video feeds and ensure smooth frame updates.

## Table of Contents

1. [Overview](#overview)
2. [Installation](#installation)
3. [How It Works](#how-it-works)
4. [Running the Project](#running-the-project)
5. [Technologies Used](#technologies-used)
6. [License](#license)

---

## Overview

This project allows you to view live video feeds from three cameras simultaneously in a single window. It uses the **Tkinter** library for the graphical user interface and **OpenCV** to capture and display video streams from the connected cameras. Each camera feed is displayed in a separate section of the Tkinter window, and the program switches between cameras every frame to display the latest video feed.

The program utilizes multithreading to manage the frames coming from multiple cameras, ensuring smooth video streaming without any delay or lag.

---

## Installation

### 1. Prerequisites

Before running the project, you need to install the following libraries:

- **Tkinter**: The standard Python interface to the Tk GUI toolkit.
- **Pillow (PIL)**: To handle image processing for displaying the video frames.
- **OpenCV**: For capturing video from the cameras.
  
You can install the required libraries using `pip`:

```bash
pip install opencv-python
pip install pillow
```

*Note: Tkinter is usually included by default in most Python installations. If not, you can install it using your package manager (for example, `sudo apt-get install python3-tk` on Linux).*

---

## How It Works

1. **Capture Video Feeds**:
   - The program uses **OpenCV** to capture video from three cameras (`camera_caps[0]`, `camera_caps[1]`, and `camera_caps[2]`).
   - It retrieves frames continuously from the cameras and processes them to update the GUI.

2. **Displaying Frames in Tkinter**:
   - Each camera feed is displayed in its own `Label` widget within the Tkinter window.
   - The frames are updated continuously by converting the frames from OpenCV into images that can be displayed using Tkinter.

3. **Multithreading**:
   - The video capture loop runs on a single thread, but the GUI (Tkinter) is updated within the same loop using `win.update()` to avoid lag.
   - The program cycles through the three camera feeds by switching between them in a round-robin fashion.

4. **Error Handling**:
   - If there’s an issue with any of the cameras (such as if one camera disconnects), the program will reset the corresponding camera.

---

## Running the Project

1. **Prepare Your Cameras**:
   Ensure that you have three cameras connected to your system. These can be USB webcams, internal webcams, or other compatible devices. The script assumes the default video devices (0, 1, and 2) for the cameras.

2. **Running the Script**:
   After the required libraries are installed, run the script using:

```bash
python ROV_GUI.py
```

This will open a Tkinter window displaying the live feeds from the cameras. Each feed will appear in a different position on the window, and the program will switch between them every frame.

---

## Technologies Used

- **Tkinter**:
  - Provides the graphical user interface (GUI) for displaying video frames from the cameras.
- **OpenCV**:
  - Used for capturing video from multiple cameras.
  - Handles image conversion and processing to update the Tkinter interface.
- **Pillow (PIL)**:
  - Used to handle image conversion from OpenCV format to Tkinter format for display.
- **Threading**:
  - While not explicitly implemented here, the project structure could be enhanced with multithreading to manage camera feeds asynchronously.

---

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

---

Feel free to modify the code to suit your needs, including handling more than three cameras or adding more advanced features like camera switching or frame rate adjustments.
