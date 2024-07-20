import numpy as np

# Tạo ma trận 3x3
matrix = np.array([[1, 2, 3],
                   [0, 1, 4],
                   [5, 6, 0]])

# Tìm ma trận nghịch đảo
try:
  matrix_inverse = np.linalg.inv(matrix)
  print("Ma trận nghịch đảo:\n", matrix_inverse)
except np.linalg.LinAlgError:
  print("Ma trận không khả nghịch")
