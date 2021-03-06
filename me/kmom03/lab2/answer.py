#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""                                               
4603064a1dbd86df0e96e21868f97217 generated for miis15 at 2015-02-21 08:21:09 
"""

from Dbwebb import Dbwebb

dbwebb = Dbwebb()
print("Ready to begin.")


"""
==========================================================================
Lab 2 - python 
 
Strings and files 
"""

"""
--------------------------------------------------------------------------
Section 1. Strings 
 
The basics of strings 
"""

"""
Exercise 1.1 
 
Assign the word: 'lollipop' to a variable and put your variable as the
answer. 

Write your code below and put the answer into the variable ANSWER.
"""

text = "lollipop"
ANSWER = text


# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.1", ANSWER, False))

"""
Exercise 1.2 
 
Assign the word 'lollipop' to a variable. Create another variable where you
put the first and the last letter in the word. Answer with the second
variable. 

Write your code below and put the answer into the variable ANSWER.
"""

text = "lollipop"
ANSWER = text[:1] + text[-1:]

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.2", ANSWER, False))

"""
Exercise 1.3 
 
Assign the word: banana to a variable. Answer with the length of the word
as an integer. 

Write your code below and put the answer into the variable ANSWER.
"""
text = "banana"

ANSWER = len(text)

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.3", ANSWER, False))

"""
Exercise 1.4 
 
Use the 'in-operator' to see if the word: 'melon' contains the letter 'a'.
Answer with a boolean result. 

Write your code below and put the answer into the variable ANSWER.
"""
word = "melon"
ANSWER = 'a' in word

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.4", ANSWER, False))

"""
Exercise 1.5 
 
Make all the letters in the word 'banana' capitalized. Answer with the
capitalized word. 

Write your code below and put the answer into the variable ANSWER.
"""
text = "banana"

ANSWER = text.upper()

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.5", ANSWER, False))

"""
Exercise 1.6 
 
Use the built-in function 'startswith()' to see if the word 'orange' starts
with the letter 'n'. Answer with the boolean value. 

Write your code below and put the answer into the variable ANSWER.
"""
word = "orange"
ANSWER = word.startswith("n")

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.6", ANSWER, False))

"""
Exercise 1.7 
 
Assign the words: 'car' and 'apple' to two different variables. Create a
function and pass the two words as arguments to it. Your function should
return them as a single word. Answer with the result. 

Write your code below and put the answer into the variable ANSWER.
"""
word1 = "car"
word2 = "apple"

def conWords(var1, var2):
    """
    Concatenate words
    """
    return var1 + var2

ANSWER = conWords(word1, word2)

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.7", ANSWER, False))

"""
Exercise 1.8 
 
Create a function and pass the word: 'lollipop' to it. Your function should
return the sentence: 'This word was: lollipop'. Answer with the result. 

Write your code below and put the answer into the variable ANSWER.
"""
word = "lollipop"

def makeSentence(var):
    """
    Concatenate variable and string
    """

    return "This word was: " + var

ANSWER = makeSentence(word)

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.8", ANSWER, False))

"""
Exercise 1.9 
 
Create a function and pass the word: 'apple' to it. Your function should
return the string 'yes' if the word is longer than 5 characters. Else
return 'no'. Answer with the result. 

Write your code below and put the answer into the variable ANSWER.
"""
word = "apple"

def checkLen(var):
    """
    Check the length of string
    """

    if len(var) > 5:
        return "yes"
    else:
        return "no"

ANSWER = checkLen(word)

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.9", ANSWER, False))

"""
Exercise 1.10 
 
Create a function and pass the word: 'banana' to it. Your function should
return a string with the word backwards. Answer with the result. 

Write your code below and put the answer into the variable ANSWER.
"""
word = "banana"

def backwards(var):
    """
    Return a word reversed
    """
    return var[::-1]

ANSWER = backwards(word)

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.10", ANSWER, False))

"""
Exercise 1.11 
 
Create a function and pass the word: 'car' to it. Your function should
exclude the first and the last letter of the word and return it. Answer
with the result. 

Write your code below and put the answer into the variable ANSWER.
"""
def excludeFirstAndLastLetter(var):
    """
    Return a given string without the first and last letter
    """
    return str.strip(var[1:-1])

ANSWER = excludeFirstAndLastLetter("car")

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.11", ANSWER, False))

"""
Exercise 1.12 
 
Use the format operator to print out: 'My 'string' has 'integer' 'string''.
Use the values: 'grandma', '42' and 'cows'. Answer with the result. 

Write your code below and put the answer into the variable ANSWER.
"""

def formatOperator(string1, integer, string2):
    """
    Use format operators in string
    """
    return "My %s has %s %s" % (string1, integer, string2)

ANSWER = formatOperator("grandma", 42, "cows")

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.12", ANSWER, False))

"""
Exercise 1.13 
 
Use 'find' and 'slice' on the string: '984.45.6.65 : (wasp), boat' to get
the word inside the parenthesis. Answer with the word as a string. 

Write your code below and put the answer into the variable ANSWER.
"""

text = "984.45.6.65 : (wasp), boat"

def removeParanthesis(var):
    """
    Return string between paranthesis
    """
    return var[str.find(var, "(")+1:str.find(var, ")")]

ANSWER = removeParanthesis(text)

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("1.13", ANSWER, False))

"""
--------------------------------------------------------------------------
Section 2. Files 
 
This section uses the text file: 'httpd-access.txt' 
"""

"""
Exercise 2.1 
 
Open the file and count the number of times a line starts with '81'. Answer
with the result as an integer. 

Write your code below and put the answer into the variable ANSWER.
"""

def countLine(file, var):
    """
    Cound the number of lines in the file that start with certain characters
    """
    with open(file, "r") as f:
        count = 0
        for line in f:
            if line.startswith(var):
                count = count + 1
        return count

ANSWER = countLine("httpd-access.txt", "81")

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.1", ANSWER, False))

"""
Exercise 2.2 
 
Find out the last 4 digits on line 821 in the file. Answer with the result
as an integer. 

Write your code below and put the answer into the variable ANSWER.
"""
def findLine(file, integer):
    """
    Return the last 4 digits on a certain line in the file 
    """    
    with open(file, "r") as f:
        for i, line in enumerate(f):
            if i == integer -1:
                return int(line[-5:-1]) # return int(line[-5:-1])

"""
enumerate(iterable, start=0) 
Return an enumerate object. iterable must be a sequence, an iterator, or some other object which supports iteration.
"""

ANSWER = findLine("httpd-access.txt", 821)

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.2", ANSWER, False))

"""
Exercise 2.3 
 
Find out which of the ip adresses 81.226.253.26 and 95.19.133.73 that has
the highest amount of entries. Answer with the result as an integer. 

Write your code below and put the answer into the variable ANSWER.
"""
ip1 = "81.226.253.26"
ip2 = "95.19.133.73"

def coundAndCompare(file, var1, var2):
    """
    Find certain lines in the file containing certain ips and compare them 
    """
    with open(file, "r") as f:
        countVars = [0, 0]

        for line in f:
            if var1 in line:
                countVars[0] += 1
            if var2 in line:
                countVars[1] += 1

    if countVars[0] >= countVars[1]:
        return int(countVars[0])
    else:
        return int(countVars[1])

ANSWER = coundAndCompare("httpd-access.txt", ip1, ip2)

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.3", ANSWER, True))

"""
Exercise 2.4 
 
Count the number of periods (.) there are in the file. Use the built-in
function count() on the file after you have converted it to a string.
Answer with the result as an integer.  

Write your code below and put the answer into the variable ANSWER.
"""

def countChar(file, var): 
    """
    Count the number of a certain character in the file
    """   
    f = open(file, "r").read()
    return int(f.count(var))

ANSWER = countChar("httpd-access.txt", ".")

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.4", ANSWER, False))

"""
Exercise 2.5 
 
Find the characters on line 637 from index 65 to index 75. Make sure that
the character at index 75 also gets included. Answer with the piece of
string you found. 

Write your code below and put the answer into the variable ANSWER.
"""

def findChars(file, lineNumber, index1, index2):
    """
    Slice a certain line in the file
    """ 
    with open(file, 'r') as f:
        for i, line in enumerate(f):
            if i == lineNumber - 1:
                return line[index1:index2+1]

ANSWER = findChars("httpd-access.txt", 637, 65, 75)

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.5", ANSWER, False))

"""
Exercise 2.6 
 
Find the last element on each line and sum all that are even numbers.
Answer with the result as an integer. 

Write your code below and put the answer into the variable ANSWER.
"""

def sumLastElement(file):
    """
    Return the sum of the last element of each line ending with a even number
    """

    with open(file, 'r') as f:
        evenNumbers = []

        for line in f:
            lastElement = line.replace('\n', '')[-1]

            try:
                elementAsInt = int(lastElement)
                if elementAsInt % 2 == 0:
                    evenNumbers.append(elementAsInt)
            except ValueError:
                pass

        return sum(evenNumbers)

ANSWER = sumLastElement("httpd-access.txt")

# Is the answer as expected?
# When you get stu

# Is the answer as expected?
# When you get stuck - change False to True to get a hint.
print(dbwebb.assertEqual("2.6", ANSWER, False))


dbwebb.exitWithSummary()
