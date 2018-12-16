"""
exercise 9-7-9-2
"""

fname = raw_input("Enter file name: ")
filehandle = open(fname)
d = dict()
for line in filehandle:
 newline = line.split()
 if newline != [] and newline[0] == 'From':
  mail = newline[1]
  if mail not in d:
   d[mail] = 1
  else:
   d[mail] += 1
print d    
  