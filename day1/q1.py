def check(input):
  with open(input) as input:
    numbers = [int(line.rstrip()) for line in input]

  return sum([1 for i in range(len(numbers)-1) if numbers[i] < numbers[i+1]])