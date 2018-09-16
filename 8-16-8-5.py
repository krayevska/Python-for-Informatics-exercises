"""
8-16-8-5
"""
fname = raw_input("Enter file name: ")
filehandle = open(fname)
count = 0
for line in filehandle:
 if line.startswith("From"):
  newline = line.split()
  print newline[1]
  count+=1
print "there are ", count, " lines in the file with From as the first word"  
  
  
