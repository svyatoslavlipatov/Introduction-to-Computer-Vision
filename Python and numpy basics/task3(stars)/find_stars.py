import numpy as np
import matplotlib.pyplot as plt
from skimage.morphology import binary_erosion
from skimage.measure import label

sky = np.load("task3(stars)/stars/stars.npy")

mask_cross = np.array([[1, 0, 0, 0, 1],
                       [0, 1, 0, 1, 0],
                       [0, 0, 1, 0, 0],
                       [0, 1, 0, 1, 0],
                       [1, 0, 0, 0, 1]])

mask_plus = np.array([[0, 0, 1, 0, 0],
                      [0, 0, 1, 0, 0],
                      [1, 1, 1, 1, 1],
                      [0, 0, 1, 0, 0],
                      [0, 0, 1, 0, 0]])

labeled = label(sky)
plus = label(binary_erosion(labeled, mask_plus))
cross = label(binary_erosion(labeled, mask_cross))

stars_plus = len(np.unique(plus)) - 1
stars_cross = len(np.unique(cross)) - 1
all_stars = stars_plus + stars_cross

print(f"Количество звёздочек формой +: {stars_plus}")
print(f"Количество звёздочек формой х: {stars_cross}")
print(f"Всего звёздочек: {all_stars}")

plt.figure(figsize=(8, 8))  
plt.imshow(sky, cmap='viridis')
plt.show()