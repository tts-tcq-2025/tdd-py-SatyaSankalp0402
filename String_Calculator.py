def add(numbers):
  if numbers == "":
    return 0
  delimiters = [",", "\n"]
  if numbers.startswith("//"):
    delimiter_line, newnumbers = numbers.split("\n", 1)
    custom_delimiter = delimiter_line[2:]  # skip //
    delimiters = [custom_delimiter]
  for index in delimeters:
    actualnumbers=newnumbers.replace(index,",")
  parts = actualnumbers.split(",")
  return sum(int(x) for x in parts)
  

