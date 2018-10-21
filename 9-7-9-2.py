"""
exercise 9-7-9-2

"""

fname = raw_input("Enter file name: ")
filehandle = open(fname)
d = dict()
for line in filehandle:
 newline = line.split()
 if newline != [] and newline[0] == 'From':
  day = newline[2]
  if day not in d:
   d[day] = 1
  else:
   d[day] += 1
print d    
  