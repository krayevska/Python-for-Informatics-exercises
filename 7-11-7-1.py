"""
8-16-8-5
"""
fname = raw_input("Enter file name: ")
filehandle = open(fname)
for line in filehandle:
  print line.upper() 
  
  
