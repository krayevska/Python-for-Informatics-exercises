"""
exercise 10-2
"""

fname = raw_input("Enter file name: ")
filehandle = open(fname)
d = dict()
for line in filehandle:
 newline = line.split()
 if newline != [] and newline[0] == 'From':
  time = newline[5].split(':')
  hour = time[0]
  if hour not in d:
   d[hour] = 1
  else:
   d[hour] += 1
print d

l = list()
for key, val in d.items():
 l.append ((key, val))
l.sort(reverse=False) 

for i in l:
 print i
  