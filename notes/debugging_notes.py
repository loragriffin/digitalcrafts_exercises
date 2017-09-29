#debugging notes

#Common exceptions: SyntaxError, RuntimeError, KeyError, NameError
#SyntaxError: possible tpyo, something typed it doesn't understand - look at line indicated and line before it
#RuntimeError: generic error "something is wrong" - have to dig into to find
#KeyError: same as IndexError - this particualar key or index doesn't exist - usually related to lists and dictionaries
#NameError: tried to use something that wasn't defined
#MemoryError: maybe ran out of memory - need to optimize
#FileExistError: file doesn't exist
#ImportError: importing something that doesn't exist
#KeyboardInterrupt: force quitting program

#Warnings
#don't usually stop program, but should be fixed

#can program to produce result with certain error
while True:
    try:
        x = int(input("Please enter a number: "))
except ValueError:
    print("Oops! That was not a valid number. Try again...")
#can catch multiple errors
except MemoryError:
    print("Sorry, this computer sucks.")
#except:
#print("Oops! That was not a valid number. Try again...")
#pass
#Catching all errors - beware of doing this, don't always want it to ignore all errors and catch major ones
#better to catch expected errors
    else:
        x = x + 10
        print(x)
        break
    finally:
        print("always executed")

#Raise statement - create custom error message
raise NameError('hi error')
raise MemoryError("Close your Facebook. It\'s eating all my memory.")

#creating your own error - more often used in web
class MyError(Exception):
    pass
raise MyError('hello')

#process of debugging
#throw in print statement and run code - enables you to see what's happening especially with loops

#python debugger - built in
import pdb
pdb.run('1 + 1')
#s - steps through code
#interact - open interactive terminal
#^D - exit interactive module
#c - continue command
#exit - get out

import pdb
import mymodule #program name
pdb.run('mymodule.test()')
#display - show variables or elements

python -m pdb mymodule.py
#syntax to run straight in terminal - shortcut
