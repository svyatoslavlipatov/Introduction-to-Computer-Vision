import cv2
import matplotlib.pyplot as plt
import os

def process_image(image_path):
    img = cv2.imread(image_path)
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    lower_orange = (120, 40, 20)
    upper_orange = (225, 85, 55)
    orange_mask = cv2.inRange(hsv_img, lower_orange, upper_orange)
    orange_objects = cv2.bitwise_and(img, img, mask=orange_mask)

    lower_green = (25, 75, 10)
    upper_green = (85, 190, 60)
    green_mask = cv2.inRange(hsv_img, lower_green, upper_green)
    green_objects = cv2.bitwise_and(img, img, mask=green_mask)

    lower_blue = (25, 50, 75)
    upper_blue = (55, 110, 135)
    blue_mask = cv2.inRange(hsv_img, lower_blue, upper_blue)
    blue_objects = cv2.bitwise_and(img, img, mask=blue_mask)

    def count_contours(mask):
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        valid_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > 30000]  # Фильтрация по площади
        return len(valid_contours)
    
    orange_count = count_contours(orange_mask)
    green_count = count_contours(green_mask)
    blue_count = count_contours(blue_mask)

    # plt.figure(figsize=(15, 5))
    # plt.subplot(141), plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)), plt.title('Изображение')
    # plt.subplot(142), plt.imshow(cv2.cvtColor(orange_objects, cv2.COLOR_BGR2RGB)), plt.title(f'Оранжевые: {orange_count}')
    # plt.subplot(143), plt.imshow(cv2.cvtColor(green_objects, cv2.COLOR_BGR2RGB)), plt.title(f'Зеленые: {green_count}')
    # plt.subplot(144), plt.imshow(cv2.cvtColor(blue_objects, cv2.COLOR_BGR2RGB)), plt.title(f'Синие: {blue_count}')
    # plt.show()

    return orange_count, green_count, blue_count

image_folder = "Python and numpy basics/task7(pencils)/images/"

if not os.path.exists(image_folder):
    print(f"Путь {image_folder} не найден!")
    exit()
    
total_orange = 0
total_green = 0
total_blue = 0

image_files = os.listdir(image_folder)
total_images = len(image_files)
processed_images = 0
print(f"Изображения обрабатываются. Пожалуйста, подождите...")
for i in range(1, 13):
    image_path = os.path.join(image_folder, f"img ({i}).jpg")
    if os.path.exists(image_path):
        counts = process_image(image_path)
        total_orange += counts[0]
        total_green += counts[1]
        total_blue += counts[2]

        processed_images += 1
        percentage_processed = (processed_images / total_images) * 100
        print(f"Обработка изображения: img ({i}).jpg. {percentage_processed:.0f}%")

    else:
        print(f"Изображение {image_path} не найдено.")

total_count = total_orange + total_green + total_blue
print(f"Всего карандашиков: {total_count}\n"
      f"Оранжевых карандашиков: {total_orange}\n"
      f"Зеленых карандашиков: {total_green}\n"
      f"Синих карандашиков: {total_blue}")