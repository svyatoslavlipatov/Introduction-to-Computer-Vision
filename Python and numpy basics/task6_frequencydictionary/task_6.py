import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import label, regionprops

def filling_factor(region):
    return np.mean(region.image)

def check_fill_factor(factor):
    return factor == 1

def preprocess_image(image):
    tmp = image.copy()
    tmp[[0, -1], :] = 1
    return label(tmp)

def get_tmp_regions(tmp):
    tmp_labeled = label(tmp)
    return regionprops(tmp_labeled)

def process_euler(region):
    image = region.image
    mean_row = image.mean(0)

    if np.any(mean_row == 1):
        return "*" if region.eccentricity < 0.5 else "1"

    tmp = preprocess_image(image)
    tmp_regions = regionprops(tmp)

    if tmp_regions:
        euler = tmp_regions[0].euler_number
        return 'X' if euler == -1 else 'W' if euler == -2 else '/' if region.eccentricity > 0.5 else '*'
    
    return '/'

def recognize(region):
    euler = region.euler_number
    image = region.image
    mean_row = image.mean(0)
    mean_col = image.mean(1)

    if check_fill_factor(filling_factor(region)):
        return '-'

    if euler == -1:
        return 'B' if np.any(mean_row[:1] == 1) else '8'

    elif euler == 0:
        tmp = image.copy()
        tmp[-1, :] = 1
        tmp_regions = get_tmp_regions(tmp)

        if np.any(mean_row[:1] == 1):
            tmp[:, -len(tmp[0]) // 2:] = 1
            tmp_regions = get_tmp_regions(tmp)

            if tmp_regions:
                e = tmp_regions[0].euler_number
                return 'P' if e == -1 else 'D' if e == 0 else '_'

        if np.any(mean_col == 1):
            return '*'

        return 'A' if tmp_regions and tmp_regions[0].euler_number == -1 else '0'

    elif euler == 1:
        return process_euler(region)

    return '_'

def analyze_symbols(image_path='Python and numpy basics/task6_frequencydictionary/images/symbols.png'):
    image = plt.imread(image_path).min(2)
    image[image > 0] = 1
    labeled = label(image)
    regions = regionprops(labeled)

    symbols = ['A', 'B', '8', '0', '1', 'W', 'X', '*', '-', '/', 'P', 'D']
    counts = {}

    for region in regions:
        symbol = recognize(region)
        counts[symbol] = counts.get(symbol, 0) + 1

    total_symbols = np.max(labeled)
    print(f"Всего символов: {total_symbols}")

    for symbol in symbols:
        count = counts.get(symbol, 0)
        percentage = (count / total_symbols) * 100
        print(f"{symbol}: {count} ({percentage:.2f}%)")

analyze_symbols()