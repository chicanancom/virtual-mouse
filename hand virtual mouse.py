import cv2
import mediapipe
import pyautogui

hand_detector = mediapipe.solutions.hands.Hands()
cam = cv2.VideoCapture(0)
screen_w, screen_h = pyautogui.size()
drawing_util = mediapipe.solutions.drawing_utils
index1 = 0
index2 = 0
while True:
    _, image = cam.read()
    image = cv2.flip(image, 1)
    window_h, window_w, window_d = image.shape
    rbg_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    processed_image = hand_detector.process(rbg_image)
    hand_landmark_points = processed_image.multi_hand_landmarks
    if hand_landmark_points:
        for hand in hand_landmark_points:
            # drawing_util.draw_landmarks(image,hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x * window_w)
                y = int(landmark.y * window_h)
                print(x,y)
                if id == 8:
                    cv2.circle(image, (x, y), 10, (0, 0, 255))
                    mouse_x = 1.2*screen_w / window_w * x
                    mouse_y = 1.2*screen_h / window_h * y
                    index1 = mouse_y
                    if abs(index1 - index2) >= 100:
                        pyautogui.moveTo(mouse_x, mouse_y)
                if id == 4:
                    cv2.circle(image, (x, y), 10, (0, 0, 255))
                    click_y = screen_h / window_h * y
                    index2 = click_y
                    print(abs(index1 - index2))
                    if abs(index1 - click_y) < 100:
                        pyautogui.dragTo(mouse_x, mouse_y,button="left")
    cv2.imshow("eye", image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
