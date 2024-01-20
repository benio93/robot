import cv2
import numpy as np

# Open the default camera (usually the built-in webcam)
cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Define window name
window_name = "Camera Feed"

# Rotate angle in degrees
rotate_angle = 180

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Check if the frame was read successfully
    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Rotate the frame by 18 degrees
    height, width = frame.shape[:2]
    rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), rotate_angle, 1)
    rotated_frame = cv2.warpAffine(frame, rotation_matrix, (width, height))

    # Resize the frame to make it larger
    scale_factor = 1.5
    resized_frame = cv2.resize(rotated_frame, None, fx=scale_factor, fy=scale_factor)

    # Display the resized and rotated frame in a window
    cv2.imshow(window_name, resized_frame)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()
