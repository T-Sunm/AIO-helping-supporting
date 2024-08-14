def calculate_probability(event_occurrences, total_trials):
  return event_occurrences / total_trials

def main():
  event_occurrences = 5
  total_trials = 20
  probability = calculate_probability(event_occurrences, total_trials)
  print(f"Xác suất của sự kiện là: {probability}")


if __name__ == "__main__":
  main()
