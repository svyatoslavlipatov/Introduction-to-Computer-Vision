import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import label, regionprops
from skimage.morphology import binary_erosion

h_area_lst = []

for i in range(100):
    h_area = np.load("Python and numpy basics/task8(trajectory)/out/" + f"h_{i}.npy")
    h_area_lst.append(h_area)

plt.figure(figsize=(8, 8))

object_colors = {}

for i, h_area in enumerate(h_area_lst):
    eroded = binary_erosion(h_area)
    labeled = label(eroded)
    props = regionprops(labeled)

    for prop in props:
        label_value = prop.label
        y, x = prop.centroid
        
        color = object_colors.setdefault(label_value, 'purple' if len(object_colors) % 2 == 0 else 'red')
        
        color = object_colors[label_value]
        plt.scatter(x, y, color=color, s=20)

plt.title("Траектория движения")
# plt.imshow(labeled, cmap='viridis')
plt.show()