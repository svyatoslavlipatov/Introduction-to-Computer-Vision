import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import label

def area(labeled, label=1):
    return (labeled[labeled == label] / label).sum()

coins = np.load("Python and numpy basics/task4(coins)/coins.npy")
labeled = label(coins)

count_areas = {69:0, 145:0, 305:0, 609:0}
nominals = [1, 2, 5, 10]
sum_list = []
c = 0

for i in range(1, np.max(labeled) + 1):
    n = area(labeled, i)
    if n in count_areas:
        count_areas[n] += 1

for key in count_areas:
    sum_of_nominal = count_areas[key] * nominals[c] 
    sum_list.append(sum_of_nominal)
    c += 1
    
print(f"Общая сумма: {sum(sum_list)}")
plt.imshow(coins)
plt.show()
