import cv2
from fer import FER
import numpy as np

# Load face detector
face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

# Load emoji images
emoji_dict = {
    'happy': cv2.imread('emojis/happy.png', -1),
    'sad': cv2.imread('emojis/sad.png', -1),
    'angry': cv2.imread('emojis/angry.png', -1),
    'surprise': cv2.imread('emojis/surprise.png', -1)
}

# Initialize emotion detector
detector = FER()

# Start webcam
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break

    frame = cv2.flip(frame, 1)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        roi_color = frame[y:y+h, x:x+w]
        emotion, score = detector.top_emotion(roi_color) or (None, None)

        if emotion:
            if emotion in emoji_dict:
                emoji = emoji_dict[emotion]
                emoji = cv2.resize(emoji, (100, 100))  # Fixed size for top-left display

                # Display emoji in top-left corner
                x_offset, y_offset = 10, 10
                y1, y2 = y_offset, y_offset + emoji.shape[0]
                x1, x2 = x_offset, x_offset + emoji.shape[1]

                # Handle transparency
                if emoji.shape[2] == 4:  # Ensure emoji has alpha channel
                    alpha_emoji = emoji[:, :, 3] / 255.0
                    alpha_frame = 1.0 - alpha_emoji

                    for c in range(0, 3):
                        frame[y1:y2, x1:x2, c] = (alpha_emoji * emoji[:, :, c] +
                                                  alpha_frame * frame[y1:y2, x1:x2, c])

                cv2.putText(frame, emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_AA)
            else:
                cv2.putText(frame, "Emotion not found", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow('Emoji Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
