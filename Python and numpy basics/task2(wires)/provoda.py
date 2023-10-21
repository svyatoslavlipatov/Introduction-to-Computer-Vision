import os
import numpy as np
import matplotlib.pyplot as plt
from skimage.morphology import binary_erosion
from skimage.measure import label

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "wires", "wires6.npy")

wires = np.load(file_path)
struct = np.ones((3, 1))
labeled = label(wires)

for lb in range(1, np.max(labeled) + 1):
    new_image = np.zeros_like(wires)
    new_image[labeled == lb] = 1
    chopped = binary_erosion(new_image, struct)
    n_components = np.max(label(chopped))

    print(f"провод № {lb}:")
    if n_components == 0:
        print("а это какой-то неправильный провод")
    elif n_components == 1:
        print("целый")
    else:
        print(f"порван на {n_components} частей")

plt.subplot(121)
plt.imshow(label(wires))
plt.subplot(122)
plt.imshow(binary_erosion(wires,struct))
plt.show()