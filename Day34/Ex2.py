def calculate_conditional_probability(p_a_and_b, p_a):
  return p_a_and_b / p_a

def main():
  p_a_and_b = 0.2
  P_A = 0.5
  p_b_given_a = calculate_conditional_probability(p_a_and_b, P_A)
  print(f"Xác suất có điều kiện P(B|A) là: {p_b_given_a}")


if __name__ == "__main__":
  main()
