from picamera2 import Picamera2
import cv2
from ultralytics import YOLO
from gtts import gTTS
import os
import time

# ---------------- CONFIGURATION ----------------
MODEL_PATH = "Models/yolov8n.pt"  # Keep model inside Models folder
PRIORITY_OBJECTS = {"person", "cell phone", "bottle", "book"}
ANNOUNCEMENT_INTERVAL = 8  # seconds
AUDIO_FILE = "output.mp3"

# ---------------- HELPER FUNCTION ----------------
def get_direction(x1, x2, frame_width):
    """
    Estimate direction (left / ahead / right) based on object's horizontal position.
    """
    center_x = (x1 + x2) / 2

    if center_x < frame_width / 3:
        return "to your left"
    elif center_x > 2 * frame_width / 3:
        return "to your right"
    else:
        return "ahead"

# ---------------- LOAD YOLO MODEL ----------------
print("[INFO] Loading YOLOv8 model...")
model = YOLO(MODEL_PATH)
print("[INFO] YOLOv8 model loaded successfully.")

# ---------------- INITIALIZE CAMERA ----------------
picam2 = Picamera2()

preview_config = picam2.create_preview_configuration(
    main={"size": (640, 480), "format": "RGB888"}
)

picam2.configure(preview_config)
picam2.start()

time.sleep(1)
print("[INFO] Camera started. Press 'q' to quit.")

# ---------------- TTS TIMER ----------------
last_announcement_time = time.time()

# ---------------- MAIN LOOP ----------------
while True:
    frame = picam2.capture_array()
    frame_height, frame_width = frame.shape[:2]

    # YOLO inference
    results = model(frame)

    detected_objects_info = []

    # Process detections
    for box in results[0].boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        conf = box.conf.item()
        label = int(box.cls.item())
        label_name = model.names[label]

        # Only announce priority objects
        if label_name in PRIORITY_OBJECTS:
            # Distance estimation (basic)
            distance = "near" if (y2 - y1) > frame_height / 2 else "far"

            # Direction estimation
            direction = get_direction(x1, x2, frame_width)

            object_info = f"{label_name} {direction}, {distance}"
            detected_objects_info.append(object_info)

        # Draw bounding box + label text
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, f"{label_name} {conf:.2f}",
                    (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (0, 255, 0), 2)

    # ---------------- TEXT-TO-SPEECH ----------------
    current_time = time.time()

    if detected_objects_info and (current_time - last_announcement_time > ANNOUNCEMENT_INTERVAL):
        speech_text = "I have detected " + ", ".join(set(detected_objects_info))
        print("[INFO] Announcing:", speech_text)

        # Remove previous mp3 if exists
        if os.path.exists(AUDIO_FILE):
            os.remove(AUDIO_FILE)

        # Generate new voice
        tts = gTTS(text=speech_text, lang="en")
        tts.save(AUDIO_FILE)

        last_announcement_time = current_time

        # Play audio (non-blocking)
        os.system(f"mpg123 {AUDIO_FILE} &")

    # ---------------- DISPLAY FRAME ----------------
    cv2.imshow("Smart Vision - YOLOv8 + PiCamera2", frame)

    # Quit on 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("[INFO] Quitting program...")
        break

# ---------------- CLEANUP ----------------
picam2.close()
cv2.destroyAllWindows()
