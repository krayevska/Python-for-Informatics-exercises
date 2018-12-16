"""
exercise 10-1
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
l = list()
for key, val in d.items():
 l.append ((val, key))
l.sort(reverse=True)
print l[0]
 

  