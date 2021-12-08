def dive(input):
  x,y,aim = 0,0,0

  with open(input) as f:
    movements = [line.rstrip() for line in f]
  
  for direction in movements:
    if direction.split()[0] == "forward":
      x += int(direction.split()[1])
      y += aim*int(direction.split()[1])
    else:
      if direction.split()[0] == "up":
        aim -= int(direction.split()[1])
      else:
        aim += int(direction.split()[1])

  return x*y