import string

def CountingMinutes(str): 
  """ Return the total number of minutes between two times.
  if str is 9:00am-10:00am then the output should be 60. 
  If str is 1:00pm-11:00am the output should be 1320."""
  
  # take out colon and dash from time string
  times = str.replace(":"," ").replace("-"," ").split()
  # extract min/hour values and am/pm
  t1_hr = int(times[0])
  t1_min = times[1][0:2]
  t1_ap = times[1][-2]

  t2_hr = int(times[2])
  t2_min = times[3]
  t2_ap = times[3][-2]
  
  # add 12 hrs if time is in pm, unless it's 12 pm
  if t1_ap == "p" and t1_hr != 12:
    t1_hr += 12

  if t2_ap == "p" and t2_hr != 12:
    t2_hr += 12

  if t1_hr == 12 and t1_ap == "a":
    t1_hr = 0
  if t2_hr == 12 and t2_ap == "a":
    t2_hr = 0
  
  tot_min_t1 = 60 * t1_hr + int(t1_min[0:2])
  tot_min_t2 = 60 * t2_hr + int(t2_min[0:2])
  
  diff = tot_min_t2 - tot_min_t1
  if diff < 0: # if end time is earlier in the day than start time
    return abs(diff + 24 * 60)
  else:
    return diff


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

def PalindromeTwo(someString):
  """ Return True if the parameter is a palindrome 
  (the string is the same forward as it is backward) 
  otherwise return false. Punctuation should not be considered."""
  punct = set(string.punctuation)
  # strip punctuation and spaces + lowercase everything
  str_orig = ''.join(ch for ch in someString if ch not in punct and ch != ' ').lower()
  # break the string into a list of chars
  letters = list(str_orig)
  # reverse the list
  letters.reverse()
  # join it back into a string
  str_rev = ''.join(letters)
  # compare reversed string to original
  if str_rev == str_orig:
    return True
  else:
    return False


