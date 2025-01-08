import cv2
import mediapipe
import mediapipe.tasks import python

cap = cv2.VideoCapture(0)  # Open the camera

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    ret, frame = cap.read()  # Capture frame-by-frame
    
    if not ret:
        print("Error: Failed to capture image.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert to grayscale

    cv2.imshow('Video', gray)  # Display the resulting frame
    
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Exit loop if 'q' is pressed
        break

cap.release()  # Release the capture object
cv2.destroyAllWindows()  # Close all OpenCV windows
