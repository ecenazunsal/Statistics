import numpy as np

def shifted(data):
    mean = np.mean(data)
    median = np.median(data)
    if mean == 0 and median == 0:
        return 0
    return abs(mean - median) / (abs(mean) + 1e-9) * 100
