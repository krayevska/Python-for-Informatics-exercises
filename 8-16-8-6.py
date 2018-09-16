"""
8-16-8-6
"""
listOfNumbers = []
max = 0
min = 0
results = []
number = ""
while number != 'Done':
 number = input("Enter a number: ")
 if number != 'Done':
  listOfNumbers.append(number)
for i in listOfNumbers:
 if max == 0 or i>max:
  max = i
for ii in listOfNumbers:
 if min == 0 or i<min:
  min = ii
print "Maximum: ", max
print "Minimum: ", min  

 