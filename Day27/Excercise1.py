import numpy as np

def main():

  # Tạo bộ sinh ngẫu nhiên
  rng = np.random.default_rng(7)

  matrix = rng.random((3, 3))
  print("Ma trận 3x3 với các phần tử ngẫu nhi ên:\n", matrix)


if __name__ == "__main__":
  main()
