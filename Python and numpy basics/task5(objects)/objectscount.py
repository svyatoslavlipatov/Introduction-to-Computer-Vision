import numpy as np
from scipy.ndimage import binary_opening
from skimage.measure import label

area = np.load("Python and numpy basics/task5(objects)/area/ps.npy.txt")
labeled = label(area)

object1 = np.array([[1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1]])

object2 = np.array([[1, 1, 0, 0, 1, 1],
                    [1, 1, 0, 0, 1, 1],
                    [1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1]])

object3 = np.array([[1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1],
                    [1, 1, 0, 0, 1, 1],
                    [1, 1, 0, 0, 1, 1]])

object4 = np.array([[1, 1, 1, 1],
                    [1, 1, 1, 1],
                    [1, 1, 0, 0],
                    [1, 1, 0, 0],
                    [1, 1, 1, 1],
                    [1, 1, 1, 1]])

object5 = np.array([[1, 1, 1, 1],
                    [1, 1, 1, 1],
                    [0, 0, 1, 1],
                    [0, 0, 1, 1],
                    [1, 1, 1, 1],
                    [1, 1, 1, 1]])

count_all_objects = np.max(labeled)
count_object1 = label(binary_opening(area, object1)).max()
count_object2 = label(binary_opening(area, object2)).max() - count_object1
count_object3 = label(binary_opening(area, object3)).max() - count_object1
count_object4 = label(binary_opening(area, object4)).max()
count_object5 = label(binary_opening(area, object5)).max()

print(f"Количество всех объектов вместе: {count_all_objects}\n"
      f"Количество объектов (▬): {count_object1}\n"
      f"Количество объектов (﹈): {count_object2}\n"
      f"Количество объектов (﹇): {count_object3}\n"
      f"Количество объектов ([): {count_object4}\n"
      f"Количество объектов (]): {count_object5}")

# Ответ:
# Количество объектов (▬): 92
# Количество объектов (﹈): 187
# Количество объектов (﹇): 188
# Количество объектов ([): 94
# Количество объектов (]): 123
# Количество всех объектов вместе: 500