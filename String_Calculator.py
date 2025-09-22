def add(numbers):
  if numbers == "":
    return 0
  if numbers.startswith("//"):
    delimiter_line, numbers = numbers.split("\n", 1)
    delimiter = delimiter_line[2:]
    numbers = numbers.replace(delimiter, ",")
  else:
    numbers = numbers.replace("\n", ",")
  return sum(int(x) for x in numbers.split(","))

