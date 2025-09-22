def add(numbers):
  if numbers == "":
    return 0
  newnumbers = numbers.replace("\n", ",")
  parts = newnumbers.split(",")
  return sum(int(x) for x in parts)
  

