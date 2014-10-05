import string

# Using the Python language, have the function FirstReverse(str) 
# take the str parameter being passed and return the string in reversed order. 

def FirstReverse(str): 
    new_string = ""
    for i in range(len(str)):
      new_string = str[i] + new_string 
    return new_string

print FirstReverse("I Love Code")

# return the factorial of num (ie. if num = 4, return (4 * 3 * 2 * 1)).

def FirstFactorial(num):
    total = 1
    for i in range(1,num + 1):
        total = total * i
    return total

print FirstFactorial(4) #24
print FirstFactorial(8) # 40320

# Return the largest word in the string. 
# If there are two or more words that are the same length, 
# return the first word from the string with that length.

def LongestWord(sen):
    words = sen.split()
    print words
    longest_word = ""
    for word in words:
        count = ""
        for char in word:
            if char in string.ascii_letters:
                count += char
        if len(count) > len(longest_word):
            longest_word = count
    return longest_word

print LongestWord("fun&!! time") #time

# Replace every letter in the string with the letter following it in the alphabet 
# (ie. c becomes d, z becomes a). Then capitalize every vowel in this new string 
# (a, e, i, o, u) and finally return this modified string. 

def LetterChanges(str):
    new_sen = ""
    for char in str:
        if char in "aeiouAEIOU":
            char = char.upper()
        if char in string.ascii_letters:
            new_sen = new_sen + chr(ord(char)+1)
        else:
            new_sen = new_sen + char
    return new_sen

print LetterChanges("hello*3") #"Ifmmp*3"
print LetterChanges("fun times!") #gvO Ujnft!

# add up all the numbers from 1 to num. 

def SimpleAdding(num):
    total = 0
    for num in range(num + 1):
        total = total + num
    return total

print SimpleAdding(12) #78
print SimpleAdding(140) #9870

# Capitalize the first letter of each word

def LetterCapitalize(str):
    words = str.split()
    for i in range(len(words)):
        firstletter = words[i][0]
        words[i] = firstletter.upper() + words[i][1:]
    words = " ".join(words)
    return words

print LetterCapitalize("hello world") #Hello World
print LetterCapitalize("i ran there") #I Ran There

#  for the string to be true each letter must be surrounded by a + symbol

def SimpleSymbols(aString):
    if aString[0].isalpha() or aString[-1].isalpha():
        return False
    for i in range(len(aString)):
        if aString[i].isalpha():
            if aString[i-1] != "+" or aString[i+1] != "+":
                return False
    return True

print SimpleSymbols("+d+=3=+s+") # True 
print SimpleSymbols("f++d+") # False
print SimpleSymbols("++d+===+c++==a")#False

# Return True if num2 is greater than num1, -1 if they're equal, and False if it's less

def CheckNums(num1,num2):
    if num2 > num1:
        return True
    elif num1 == num2:
        return "-1"
    else:
        return False

print CheckNums(3,122) # True
print CheckNums(67, 67) # -1

# eturn the number of hours and minutes the parameter converts to 
# (ie. if num = 63 then the output should be 1:3). 
#Separate the number of hours and minutes with a colon. 

def TimeConvert(num):
    hours = num / 60
    minimum = num % 60
    return "%d:%d" % (hours, minimum)

print TimeConvert(126) # 2:6
print TimeConvert(45) # 0:45

# Return string with letters in alphabetical order

def AlphabetSoup(aString):
    chars = list(aString)
    chars.sort()
    return ''.join(chars)

print AlphabetSoup("coderbyte") # bcdeeorty
print AlphabetSoup("hooplah") # ahhloop

# return the string true if the characters a and b are separated 
# by exactly 3 places anywhere in the string at least once 
# (ie. "lane borrowed" would result in true because there is 
# exactly three characters between a and b). Otherwise return the string false. 

def ABCheck(aString):
    for i in range(len(aString)):
        if aString[i] == "a":
            if aString[i-3] == "b" or aString[i+3] == "b":
                return "true"
    return "false"

print ABCheck("after badly") # false
print ABCheck("Laura sobs") # true

# return number of vowels string contains

def vowelCount(str):
    count = 0
    for char in str:
        if char in "aeiouAEIOU":
            count += 1
    return count

print vowelCount("hello") # 2
print vowelCount("coderbyte") #3
