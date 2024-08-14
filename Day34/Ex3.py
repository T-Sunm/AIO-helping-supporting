import numpy as np

def calculate_covariance(x: np.ndarray, y: np.ndarray):

  mean_x = np.mean(x)
  mean_y = np.mean(y)
  N = len(x)

  return np.sum((x - mean_x) * (y - mean_y)) / N


def calculate_correlation(x: np.ndarray, y: np.ndarray):
  mean_x = np.mean(x)
  mean_y = np.mean(y)
  N = len(x)

  cov = calculate_covariance(x, y)
  var_x = np.sqrt(np.sum((x - mean_x)**2) / N)
  var_y = np.sqrt(np.sum((y - mean_y)**2) / N)

  return cov / (var_x * var_y)


def main():
  X = [2, 4, 6, 8, 10]
  Y = [1, 3, 5, 7, 9]

  covariance = calculate_covariance(np.array(X), np.array(Y))
  correlation = calculate_correlation(np.array(X), np.array(Y))

  print(f" Covariance giữa X và Y là: {covariance}")
  print(f" Correlation giữa X và Y là: {correlation:.2f}")


if __name__ == "__main__":
  main()
