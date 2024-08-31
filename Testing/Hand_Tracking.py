import cv2
import mediapipe as mp
import time
from google.protobuf.json_format import MessageToDict

capture = cv2.VideoCapture(0)

hand = mp.solutions.hands
hands = hand.Hands()
draw = mp.solutions.drawing_utils

previousTime = 0
currentTime = 0

while True:
    ret, frame = capture.read()

    frame = cv2.flip(frame, 1)
    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:

        handcount = len(results.multi_handedness)
        # print(results.multi_hand_landmarks)
        cv2.putText(frame, "handcount "+str(handcount), (230, 50),
                    cv2.FONT_HERSHEY_COMPLEX, 0.9,
                    (0, 255, 0), 2)

        for handLandmarks in results.multi_hand_landmarks:
            for id, lm in enumerate(handLandmarks.landmark):

                # Return Dict in handedsness
                handedness = results.multi_handedness[0]

                # Return whether it is Right or Left Hand
                label = MessageToDict(handedness)['classification'][0]['label']

                if handcount == 2:
                    cv2.putText(frame, label + ' Hand', (20, 50),
                                cv2.FONT_HERSHEY_COMPLEX, 0.9,
                                (0, 255, 0), 2)
                    cv2.putText(frame, label + ' Hand', (460, 50),
                                cv2.FONT_HERSHEY_COMPLEX,
                                0.9, (0, 255, 0), 2)
                if label == 'Left':
                    # Display 'Left Hand' on left side of window
                    cv2.putText(frame, label + ' Hand', (20, 50),
                                cv2.FONT_HERSHEY_COMPLEX, 0.9,
                                (0, 255, 0), 2)

                if label == 'Right':
                    # Display 'Right Hand' on right side of window
                    cv2.putText(frame, label + ' Hand', (460, 50),
                                cv2.FONT_HERSHEY_COMPLEX,
                                0.9, (0, 255, 0), 2)

                print(id, lm)
            draw.draw_landmarks(frame, handLandmarks, hand.HAND_CONNECTIONS)

    currentTime = time.time()
    fps = 1 / (currentTime - previousTime)
    previousTime = currentTime

    cv2.putText(frame, "FPS: {:.2f}".format(fps), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    cv2.imshow('Hand Tracking', frame)
    cv2.waitKey(1)
