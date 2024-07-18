import numpy as np

def main():

  # Tạo bộ sinh ngẫu nhiên
  rng = np.random.default_rng(7)

  matrix1 = rng.random((3, 3))
  matrix2 = rng.random((3, 3))

  matrix_product_2 = np.einsum('ij,ij->ij', matrix1, matrix2)

  print("Tích của hai ma trận:\n", matrix_product_2)


if __name__ == "__main__":
  main()
