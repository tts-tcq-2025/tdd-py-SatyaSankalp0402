def add(numbers):
  if numbers == "":
    return 0
  if "," in numbers:
    for parts in numbers.split(","):
      return sum(int(parts))
  return int(numbers)
