import cv2
import numpy as np

def highlight_colors(video_path, lower_bound_blue, upper_bound_blue, lower_bound_green, upper_bound_green, lower_bound_red, upper_bound_red, lower_bound_pink, upper_bound_pink):
    cap = cv2.VideoCapture(video_path)
    my_pic_count = 0
    all_pics = 0
    if not cap.isOpened():
        print("Ошибка при открытии видеофайла")
        return

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Конец видеофайла")
            break

        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        mask_blue = cv2.inRange(hsv_frame, lower_bound_blue, upper_bound_blue)
        mask_green = cv2.inRange(hsv_frame, lower_bound_green, upper_bound_green)
        mask_red = cv2.inRange(hsv_frame, lower_bound_red, upper_bound_red)
        mask_pink = cv2.inRange(hsv_frame, lower_bound_pink, upper_bound_pink)

        combined_mask = cv2.bitwise_or(cv2.bitwise_or(cv2.bitwise_or(mask_blue, mask_green), mask_red), mask_pink)
        highlighted_frame = cv2.bitwise_and(frame, frame, mask=combined_mask)

        if cv2.countNonZero(mask_blue) > 0 and cv2.countNonZero(mask_green) > 0 and cv2.countNonZero(mask_red) > 0 and cv2.countNonZero(mask_pink) > 500:
            # print("Все цвета в сборе")
            my_pic_count += 1
            
        all_pics += 1

        # cv2.imshow("Выделение цветов", highlighted_frame)
        # cv2.waitKey()

    print(f"Количество всех изображений: {all_pics}")
    print(f"Количество 'моих' изображений: {my_pic_count}")
    cap.release()
    cv2.destroyAllWindows()


video_path = 'Python and numpy basics/task11_findmypicture/video/output.avi'

lower_blue = np.array([100, 50, 50])
upper_blue = np.array([130, 255, 255])

lower_green = np.array([40, 50, 50])
upper_green = np.array([80, 255, 255])

lower_red = np.array([0, 100, 100])
upper_red = np.array([10, 255, 255])

lower_pink = np.array([140, 50, 50])
upper_pink = np.array([170, 255, 255])
highlight_colors(video_path, lower_blue, upper_blue, lower_green, upper_green, lower_red, upper_red, lower_pink, upper_pink)