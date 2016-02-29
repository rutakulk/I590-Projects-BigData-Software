import sys

inputNumber  = int(input('Enter a number: '))


def fizzbuzz(inputNumber):
    for i in range (1,inputNumber):
        if (i % 2 == 0) and (i % 3 == 0):
           print ("fizzbuzz")
        elif i % 2 == 0:
            print ("fizz")
        elif i % 3 == 0:
            print ("buzz")
        else:
            print (i)

fizzbuzz(inputNumber)
