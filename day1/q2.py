def check(input):
  count = 0
  with open(input) as f:
    numbers = [int(line.rstrip()) for line in f]

    for i in range(len(numbers)-3):
      first_three = numbers[i] + numbers[i+1] + numbers[i+2]
      second_three = numbers[i+1] + numbers[i+2] + numbers[i+3]

      if second_three > first_three:
        count += 1

  return count