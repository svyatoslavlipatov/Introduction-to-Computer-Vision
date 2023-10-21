import numpy as np

def calculate_nominal_resolution(filename):
    with open(filename, 'r') as file:
        max_size_mm = int(file.readline())
        file.readline()
        image_data = np.loadtxt(file, dtype=int)
        resolution = max_size_mm / image_data.shape[1]
        return resolution
    
<<<<<<< HEAD
filenames = ["Python and numpy basics/task1/files/figure1.txt", 
             "Python and numpy basics/task1/files/figure2.txt",
             "Python and numpy basics/task1/files/figure4.txt",
             "Python and numpy basics/task1/files/figure5.txt",
             "Python and numpy basics/task1/files/figure6.txt"]
=======
filenames = ["task1/files/figure1.txt", 
             "task1/files/figure2.txt",
             "task1/files/figure4.txt",
             "task1/files/figure5.txt",
             "task1/files/figure6.txt"]
>>>>>>> 1eb5ffa53a2a733d7abc44c7068bfaec074e2494

for filename in filenames:
    resolution = calculate_nominal_resolution(filename)
    print(f"Номинальное разрешение для {filename}: {resolution} мм/пиксель")
