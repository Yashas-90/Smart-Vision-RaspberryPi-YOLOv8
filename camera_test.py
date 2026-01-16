from picamera2 import Picamera2
import cv2

# Initialize PiCamera2
picam2 = Picamera2()

# Set preview configuration
picam2.preview_configuration.main.size = (640, 480)
picam2.preview_configuration.main.format = "RGB888"
picam2.configure("preview")

# Start the camera
picam2.start()

print("[INFO] Camera started. Press 'q' to quit.")

while True:
    # Capture a frame as numpy array
    frame = picam2.capture_array()

    # Display the frame
    cv2.imshow("PiCamera2 - Live Stream", frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("[INFO] Exiting...")
        break

# Cleanup
picam2.close()
cv2.destroyAllWindows()

