import numpy as np

random_values = [-3.5, -1.2, 0, 2.8, -4.1, 1.5, -0.7, 3.2, -2.4, 4.6]

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

for value in random_values:
    print(f"Sigmoid of {value}: {sigmoid(value)}")