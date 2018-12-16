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
  dom = mail.split('@')
  domain = dom[1]
  if domain not in d:
   d[domain] = 1
  else:
   d[domain] += 1
print d
