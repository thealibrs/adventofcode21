def dive(input):
  x,y = 0,0

  with open(input) as f:
    movements = [line.rstrip() for line in f]
  
  for direction in movements:
    if direction.split()[0] == "forward":
      x += int(direction.split()[1])
    else:
      if direction.split()[0] == "up":
        y -= int(direction.split()[1])
      else:
        y += int(direction.split()[1])

  return x*y