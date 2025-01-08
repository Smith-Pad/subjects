import cv2
import mediapipe as mp

# Initialize the MediaPipe hands module
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Set up the hand detector with parameters (you can tweak these)
hands = mp_hands.Hands(
    static_image_mode=False,  # set to False for live video
    max_num_hands=2,         # Detect up to two hands
    min_detection_confidence=0.5,  # Confidence threshold for detection
    min_tracking_confidence=0.5   # Confidence threshold for tracking
)



cap = cv2.VideoCapture(0)  # Open the camera

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    ret, frame = cap.read()  # Capture frame-by-frame
    
    if not ret:
        print("Error: Failed to capture image.")
        break

    # Flip the frame horizontally for a more natural user experience
    frame = cv2.flip(frame, 1)
    
    # Convert the frame to RGB (Mediapipe uses RGB format)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame to detect hands
    results = hands.process(rgb_frame)

    # Check if any hands are detected
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw landmarks and connections on the hand
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Show the resulting frame with detected hands (if any)
    cv2.imshow('Hand Detection', frame)  # Display the resulting frame
    
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Exit loop if 'q' is pressed
        break

cap.release()  # Release the capture object
cv2.destroyAllWindows()  # Close all OpenCV windows
