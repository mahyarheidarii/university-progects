import numpy as np

code_meli = "0025096583"
unique_digits = sorted(set(code_meli))
vector = np.array([int(d) for d in unique_digits])
matrix = np.random.choice(vector, size=(10, 10), replace=True)

print(vector)
print(matrix)