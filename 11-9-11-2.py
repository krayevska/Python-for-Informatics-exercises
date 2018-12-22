import re
fileName = input('Enter a file name: ')
count = 0;
sumOfAll = 0;
file = open(fileName)
for line in file:
 line = line.rstrip()
 x = re.findall('New Revision: (\d+)', line)
 if len(x) > 0:
  sumOfAll += float(x[0].strip('"'))
  count += 1
print (sumOfAll/count)
    
