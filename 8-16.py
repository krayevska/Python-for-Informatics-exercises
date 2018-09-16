"""
exercise 8-16

"""

fname = raw_input("Enter file name: ")
filehandle = open(fname)
list = []
for line in filehandle:
 newline = line.split()
 for word in newline:
  if word not in list:
   list.append(word)
list.sort()
print  list  
  