import cv2

# Load the cascade classifiers
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_smile.xml")
body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_fullbody.xml")

# Open the camera
cap = cv2.VideoCapture(0)

while True:
    # Capture the video frame by frame
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    bodies = body_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        face_gray = gray[y:y+h, x:x+w]
        face_color = frame[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(face_gray, scaleFactor=1.1, minNeighbors=5)
        smiles = smile_cascade.detectMultiScale(face_gray, scaleFactor=1.8, minNeighbors=20, minSize=(25, 25))

        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(face_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(face_color, (sx, sy), (sx + sw, sy + sh), (0, 0, 255), 2)

    # Draw rectangles around detected bodies
    for (bx, by, bw, bh) in bodies:
        cv2.rectangle(frame, (bx, by), (bx + bw, by + bh), (255, 255, 0), 2)

    # Display the frame
    cv2.imshow("Camera", frame)

    # Exit the camera view if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the camera
cap.release()

# Close the window
cv2.destroyAllWindows()
