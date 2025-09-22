def add(numbers):
  if numbers == "":
    return 0
  if "," in numbers:
    return sum(int(parts) for parts in numbers.split(","))
  return int(numbers)
