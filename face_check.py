import cv2
import mediapipe as mp
import time
from screenshot import click_screenshot
import pyautogui 
import numpy as np

def count_faces_in_video():
    # Initialize MediaPipe face detection
    mp_face_detection = mp.solutions.face_detection
    face_detection = mp_face_detection.FaceDetection(min_detection_confidence=0.5)

    # Open the webcam
    cap = cv2.VideoCapture(0)

    # Initialize face count
    

    while cap.isOpened():
        # Read a frame from the webcam
        total_faces = 0
        ret, frame = cap.read()
        if not ret:
            break

        # Convert the frame to RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Detect faces in the frame
        results = face_detection.process(frame_rgb)

        # Count the number of faces
        if results.detections:
            total_faces += len(results.detections)

        # Display the frame with face detections
        for detection in results.detections:
            bboxC = detection.location_data.relative_bounding_box
            ih, iw, _ = frame.shape
            x, y, w, h = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
                         int(bboxC.width * iw), int(bboxC.height * ih)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Display the frame
        if total_faces>1:
            print(total_faces)
            # current_time_tuple = time.localtime()
            # current_hour = current_time_tuple.tm_hour
            # current_minute = current_time_tuple.tm_min
            # current_second = current_time_tuple.tm_sec
            cv2.putText(frame, f"Warning: Multiple Faces", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            click_screenshot("multi_face")

        cv2.imshow('Face Detection', frame)
        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    # Release the webcam and close all windows
    cap.release()
    cv2.destroyAllWindows()

    return total_faces

# Count the number of faces from the webcam
count_faces_in_video()
