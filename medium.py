def CountingMinutes(str): 
  """Not working for all test cases
  Need to finish."""
  
  # clean up the time string a bit
  times = str.replace(":"," ").replace("-"," ").split()
  # extract min/hour values
  t1_hr = int(times[0])
  t1_min = times[1]
  t2_hr = int(times[2])
  t2_min = times[3]
  
  # add 12 hrs if time is in pm
  if t1_min[2] == "p":
    t1_hr += 12
    print "t1_hr is", t1_hr 
  if t2_min[2] == "p":
    t2_hr += 12
    print "t2_hr is", t2_hr 
  
  tot_min_t1 = 60 * t1_hr + int(t1_min[0:2])
  print "t1_min is", t1_min[0:2]
  tot_min_t2 = 60 * t2_hr + int(t2_min[0:2])
  print "t2_min is", t2_min[0:2]
  
  if tot_min_t2 > tot_min_t1:
    print "t2 > t1"
    return tot_min_t2 - tot_min_t1
  else:
    print "t1 > t2"
    return 24 * 60 - tot_min_t2 + tot_min_t1

def RunLength(someString): 
  """Take the str parameter being passed 
  and return a compressed version of the string 
  using the Run-length encoding algorithm. 
  This algorithm works by taking the occurrence 
  of each repeating character and outputting that number 
  along with a single character of the repeating sequence. 
  For example: "wwwggopp" would return 3w2g1o2p."""

  counter = 0
  final_str = ""
  i = 0
  while i < len(someString):
    letter = someString[i]
    while i < len(someString) and someString[i] == letter:
      counter += 1
      i += 1
    final_str += str(counter)
    final_str += letter
    counter = 0
  return final_str


