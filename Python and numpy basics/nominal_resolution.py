import numpy as np

def calculate_nominal_resolution(filename):
    with open(filename, 'r') as file:
        max_size_mm = int(file.readline())
        file.readline()
        image_data = np.loadtxt(file, dtype=int)
        resolution = max_size_mm / image_data.shape[1]
        return resolution
    
filenames = ["files/figure1.txt", "files/figure2.txt", "files/figure4.txt", "files/figure5.txt", "files/figure6.txt"]
for filename in filenames:
    resolution = calculate_nominal_resolution(filename)
    print(f"Номинальное разрешение для {filename}: {resolution} мм/пиксель")