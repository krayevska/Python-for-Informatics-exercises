"""
exercise 10-3
"""

fname = raw_input("Enter file name: ")
filehandle = open(fname)
d = dict()
for line in filehandle:
 newline = line.split()
 for word in newline:
  word = word.lower()
  for letter in word:
   if letter not in d:
    if letter.isalpha():
     d[letter] = 1
   else:
    d[letter] += 1
print d

l = list()
for key, val in d.items():
 l.append ((val, key))
l.sort(reverse=True) 

for i in l:
 print i[1], i[0]
  