def add(numbers):
  if numbers == "":
    return 0
  if numbers.startswith("//"):
    delimiter_line, numbers = numbers.split("\n", 1)
    delimiter = delimiter_line[2:]
    numbers = numbers.replace(delimiter, ",")
  else:
    numbers = numbers.replace("\n", ",")
  parts=[int(x) for x in numbers.split(",") if x]
  if negatives:
    raise ValueError(f"negatives not allowed:{negatives}")
  return sum(x for x in parts if x<=1000)

