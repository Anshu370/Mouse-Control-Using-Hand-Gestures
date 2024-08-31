import cv2
import pyautogui
import mediapipe as mp

cap = cv2.VideoCapture(0)

hand_capture = mp.solutions.hands.Hands()

drawing_utilities = mp.solutions.drawing_utils

screen_width, screen_height = pyautogui.size()

index_y = 0

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output_hands = hand_capture.process(rgb_frame)
    hands = output_hands.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utilities.draw_landmarks(frame, hand, mp.solutions.hands.HAND_CONNECTIONS)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)
                # print(x, y)
                if id == 8:
                    cv2.circle(img=frame, center=(x, y), radius=30, color=(255, 0, 0))
                    index_x = (screen_width/frame_width) * x
                    index_y = (screen_height/frame_height) * y

                if id == 12:
                    cv2.circle(img=frame, center=(x, y), radius=30, color=(0, 0, 0))
                    middle_x = (screen_width/frame_width) * x
                    middle_y = (screen_height/frame_height) * y
                    pyautogui.moveTo(middle_x, middle_y)

                if id == 4:
                    cv2.circle(img=frame, center=(x, y), radius=30, color=(255, 255, 255))
                    thumb_x = (screen_width/frame_width) * x
                    thumb_y = (screen_height/frame_height) * y
                    # print(abs(index_y-thumb_y))
                    if abs(index_y-thumb_y) < 35:
                        print(f"click, {abs(index_y-thumb_y)}")
                        pyautogui.click()
                        # pyautogui.sleep(0.2)

    cv2.imshow('Mouse', frame)
    cv2.waitKey(1)