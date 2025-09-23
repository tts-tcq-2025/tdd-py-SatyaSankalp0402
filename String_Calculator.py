def add(numbers):
  if numbers == "":
    return 0
  numbers, delimeter = extract_delimeter(numbers)
  tokens= split_numbers(numbers,delimeter)
  values= integer_converter(tokens)
  check_negatives(values)
  return sum(values)

def extract_delimeter(numbers):
  if numbers.startswith("//"):
    delimiter_line, numbers = numbers.split("\n", 1)
    return numbers, delimiter_line[2:]
  return numbers, ","

def split_numbers(numbers,delimeter):
  numbers = numbers.replace("\n", ",")
  if delimeter != ",":
    numbers = numbers.replace(delimeter, ",")
  return [x for x in numbers.split(",") if x]

def integer_converter(tokens):
  return [int(x) for x in tokens]

def check_negatives(values):
  negatives = [x for x in values if x<0]
  if negatives:
    raise ValueError(f"negatives not allowed:{negatives}")

def sum(values):
  return sum(x for x in values if x<=1000)
  
