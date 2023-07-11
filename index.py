# This will print the message below
print("Hi, This is a small Python Script")

# Python File Handling 

# Opening a file 
pyth = open("findme.txt")
# alternative way to write the above code:
pyth - open("findme.txt", "rt")

# Reading File (If located in same location)
pyth = open("findme.txt", "r")
print(pyth.read())
