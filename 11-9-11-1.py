import re
usersReg = input('Enter a regular expression: ')
count = 0;
file = open('mbox.txt')
for line in file:
 line = line.rstrip()
 if re.search(usersReg, line):
   count += 1
print ('mbox.txt had ', count, 'lines that matches', usersReg)
    
