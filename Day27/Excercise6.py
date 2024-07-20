import numpy as np

# Tạo ma trận 3x3
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Tính định thức
det = np.linalg.det(matrix)
print("Định thức của ma trận:\n", det)
