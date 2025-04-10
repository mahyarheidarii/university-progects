import numpy as np

code_meli = "0025096583"
unique_digits = sorted(set(code_meli))
vector = np.array([int(d) for d in unique_digits])
matrix = np.random.choice(vector, size=(10, 10), replace=True)

matrix_sum = np.sum(matrix)
matrix_product = np.prod(matrix)

print("Matrix:")
print(matrix)
print("Sum:", matrix_sum)
print("Product:", matrix_product)