a="sheen !!!!!"
print(a)
# length
print(len(a))
# upper
print(a.upper())
# lower
print(a.lower())
# strip end terms only
print(a.rstrip("!"))
# replace words
print(a.replace("sheen","sean"))
# split 
print(a.split(" "))
# capitalize
heading="sheen is my name"   
print(heading.capitalize()) 
# center
print(heading.center(50))
# count
print(a.count("sheen"))
# to check ending
print(a.endswith("!"))
# to check starting
print(a.startswith("!"))
# find a word
n=("hey i am still learning")
print(n.find("learning"))
# to check if string is alphanumeric
print(a.isalnum())
# to check if string is alpha
print(a.isalpha())
# to check if string is lower
print(a.islower())
# to check if string is printable, \n is  not printable
print(a.isprintable())
# to check if string has space
print(a.isspace())
# to check if string is title
print(a.istitle())
# swap case lower to upper and vice versa
print(a.swapcase())
# to make first letter of everyword capital
print(a.title())