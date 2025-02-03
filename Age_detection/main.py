import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Load the pre-trained modelC:\Users\hp\Desktop\cam
model = load_model("C:\\Users\\hp\\Desktop\\cam\\model.h5")

# Open a connection to the laptop camera (0 corresponds to the default camera)
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Resize the frame to the input size expected by the model
    input_size = (224, 224)
    resized_frame = cv2.resize(frame, input_size)

    # Preprocess the frame for the model
    input_data = np.expand_dims(resized_frame, axis=0)
    input_data = input_data / 255.0  # Normalize pixel values to be between 0 and 1

    # Make a prediction using the model
    predictions = model.predict(input_data)

    # Get the index with the highest predicted probability
    predicted_class = np.argmax(predictions)

    # Display the results on the frame
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, f"Predicted Class: {predicted_class}", (10, 30), font, 1, (0, 255, 0), 2, cv2.LINE_AA)

    # Display the frame
    cv2.imshow('Sign Language Detection', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
