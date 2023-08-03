import cv2
import mediapipe
import pyautogui

face_mesh = mediapipe.solutions.face_mesh.FaceMesh(refine_landmarks=True)
cam = cv2.VideoCapture(0)
screen_w, screen_h = pyautogui.size()
while True:
    _, image = cam.read()
    image = cv2.flip(image, 1)
    window_h, window_w, window_d = image.shape
    rbg_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    processed_image = face_mesh.process(rbg_image)
    face_landmark_points = processed_image.multi_face_landmarks
    if face_landmark_points:
        landmark_points = face_landmark_points[0].landmark
        # for id,landmark_point in enumerate(landmark_points[474:478]):
        #     x = int(landmark_point.x * window_w)
        #     y = int(landmark_point.y * window_h)
        #     print(landmark_point.x, landmark_point.y)
        #     if id == 1:
        #         mouse_x = (screen_w/window_w*x)
        #         mouse_y = (screen_h/window_h*y)
        #         pyautogui.moveTo(mouse_x,mouse_y)
        #     cv2.circle(image, (x, y), 3, (0, 0, 255))
        left_eye = [landmark_points[145], landmark_points[159]]
        for landmark_point in left_eye:
            x = int(landmark_point.x * window_w)
            y = int(landmark_point.y * window_h)
            print(landmark_point.x, landmark_point.y)
            cv2.circle(image, (x, y), 3, (255, 0, 255))
        if (left_eye[0].y - left_eye[1].y < 0.01):
            pyautogui.click()
    cv2.imshow("eye", image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
