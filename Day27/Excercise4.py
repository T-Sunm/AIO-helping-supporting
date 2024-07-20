import numpy as np

def main():

  # Tạo bộ sinh ngẫu nhiên
  rng = np.random.default_rng(7)

  matrix = rng.random((3, 3))
  print("Ma trận trước khi chuyển vị:\n", matrix)

  matrix_transpose = np.einsum('ij->ji', matrix)
  print("Ma trận sau khi chuyển vị:\n", matrix_transpose)


if __name__ == "__main__":
  main()
