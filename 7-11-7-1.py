"""
7-11-7-1
"""
fname = raw_input("Enter file name: ")
filehandle = open(fname)
for line in filehandle:
  print line.rstrip().upper()
  
  
