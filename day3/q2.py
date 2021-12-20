def readInput(input_file):
  with open(input_file) as f:
    signals = [line.rstrip() for line in f]
  
  return signals

def binaryToDecimal(binary):
  return int(binary,2)

def scrapOxygen(signals):

  oxygen_nominee = signals.copy()
  oxygen_rating = 0

  for i in range(len(signals[0])):
    counter = {"0":0, "1":0}

    for nominee in oxygen_nominee:
      counter[nominee[i]] += 1

    if counter['1'] >= counter['0']:
      most_common = "1"
    else:
      most_common = "0"

    oxygen_nominee = [n for n in oxygen_nominee if n[i] == most_common]

    if len(oxygen_nominee) == 1:
      oxygen_rating = binaryToDecimal(oxygen_nominee[0])
    
  return oxygen_rating


def scrapCo2(signals):

  co2_nominee = signals.copy()
  co2_rating = 0

  for i in range(len(signals[0])):
    counter = {"0":0, "1":0}

    for nominee in co2_nominee:
      counter[nominee[i]] += 1

    if counter['1'] >= counter['0']:
      most_common = "0"
    else:
      most_common = "1"

    co2_nominee = [n for n in co2_nominee if n[i] == most_common]

    if len(co2_nominee) == 1:
      co2_rating = binaryToDecimal(co2_nominee[0])
    
  return co2_rating

def binary_diagnostic_two(signals):

  #signals = readInput(file)

  oxygen = scrapOxygen(signals)
  co2 = scrapCo2(signals)

  return co2*oxygen

  


sample_arr = ["00100","11110","10110","10111","10101","01111","00111","11100","10000","11001","00010","01010"]
print(binary_diagnostic_two(sample_arr))