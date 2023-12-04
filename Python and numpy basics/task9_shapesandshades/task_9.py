import cv2
import numpy as np

def process_color(image, lower, upper, color):
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_image, lower, upper)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    total_shapes = 0
    rectangles = 0
    circles = 0

    color_dict = {
        'red': (0, 0, 255),
        'blue': (255, 0, 0),
        'green': (0, 255, 0),
        'pink': (255, 0, 255),
        'yellow': (0, 255, 255)
    }

    for contour in contours:
        epsilon = 0.02 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)

        if len(approx) == 4:
            rectangles += 1
            cv2.drawContours(image, [contour], -1, color_dict[color], 2)
        elif len(approx) >= 6:
            circles += 1
            cv2.drawContours(image, [contour], -1, color_dict[color], 2)

        total_shapes += 1

    return total_shapes, rectangles, circles

image = cv2.imread('Python and numpy basics/task9_shapesandshades/pic/balls_and_rects.png')

color_ranges = {
    'red': ([0, 100, 100], [10, 255, 255]),
    'green': ([40, 50, 50], [80, 255, 255]),
    'blue': ([110, 50, 50], [130, 255, 255]),
    'pink': ([140, 100, 100], [170, 255, 255]),
    'yellow': ([20, 100, 100], [40, 255, 255])
}

total_shapes_all = 0

for color, (lower, upper) in color_ranges.items():
    total_shapes, rectangles, circles = process_color(image, np.array(lower), np.array(upper), color)
    total_shapes_all += total_shapes

    print(f"{color.capitalize()} объекты:")
    print(f"Всего фигур: {total_shapes}")
    print(f"Кругов: {circles}")
    print(f"Прямоугольников: {rectangles}\n")

print(f"Общее количество всех фигур: {total_shapes_all}")

height, width = image.shape[:2]
resized_image = cv2.resize(image, (800, 800))

cv2.imshow('Shapes Detection', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()