def binary_diagnostic(input):

  with open(input) as f:
    signals = [line.rstrip() for line in f]

  i,j = 0,0
  gamma = ""
  epsilon = ""
  
  # for gamma
  while(i <= len(signals[0])-1):
    arr = ""

    for signal in signals:
      arr += signal[i]

    if arr.count("0") > arr.count("1"):
      gamma += "0"
    else:
      gamma += "1"

    i += 1
  
  #for epsilon
  while(j <= len(signals[0])-1):
    arr = ""

    for signal in signals:
      arr += signal[j]

    if arr.count("0") > arr.count("1"):
      epsilon += "1"
    else:
      epsilon += "0"

    j += 1

  # convert to binary 
  gamma = int(gamma,2)
  epsilon = int(epsilon,2)


  return gamma*epsilon