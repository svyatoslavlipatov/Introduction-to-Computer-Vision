import numpy as np

def read_image(filename):
    with open(filename, 'r') as file:
        file.readline()
        image_data = np.loadtxt(file, dtype=int)
        return image_data

def find_object_coordinates(image):
    object_indices = np.argwhere(image == 1)
    min_y, min_x = object_indices.min(axis=0)
    return min_y, min_x

def load_images(read_image, find_object_coordinates):
    img1 = read_image('task1/files/img1.txt')
    img2 = read_image('task1/files/img2.txt')
    min_y1, min_x1= find_object_coordinates(img1)
    min_y2, min_x2 = find_object_coordinates(img2)
    # print(f"Координаты первого изображения {min_y1}, {min_x1}")
    # print(f"Координаты второго изображения {min_y2}, {min_x2}")
    offset_y = min_y1 - min_y2
    offset_x = min_x2 - min_x1
    return offset_y, offset_x

offset_y, offset_x = load_images(read_image, find_object_coordinates)
print(f"Смещение img2 относительного img1: y = {offset_y}, x = {offset_x}")
