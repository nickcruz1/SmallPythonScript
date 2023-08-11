# This will print the message below
print("Hi, This is a small Python Script")

# Python File Handling 

# Opening a file 
pyth = open("findme.txt")
# alternative way to write the above code:
pyth - open("findme.txt", "rt")

# Reading File (If located in same location)
# (If opening in a different location then specify the file path within the double quotes "" )
pyth = open("findme.txt", "r")
print(pyth.read())

# Reading File (How to read a specific number of characters.. in this case 8 characters)
pyth = open("findme.txt", "r")
print(f.read(8))

# Creating a for loop with 4 string values 
theList = ['n', 'i', 'c','k']
for list in theList:
   print(theList)

# Input Validation With Python
cyberArray = ['OSCP', 'CEH', 'CYSA']

cyberCert = str(input("Enter your certification"))

if cyberCert == cyberArray[0]:
   print "That is the gold standard"
else:
  print("I don't know that one")

# Included strings and numbers 
theContainer = ['1', 2, '3']

# Created a for loop showing what would happen with 2 strings (the beginning and the end) and then a number in between. 
for x in theContainer:
  print x * 5


numContainer = [-5, -8, 10]
unknownVar = 2

def calculate():
  print(numContainer[0] + numContainer[1])
  print(numContainer[1] + numContainer[2])
  print(numContainer[1] - numContainer[2])

print(calculate())
