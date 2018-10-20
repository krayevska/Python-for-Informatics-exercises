"""
7-11-7-2
"""
fname = raw_input("Enter file name: ")
filehandle = open(fname)
countLines = 0
total = 0
startLine = 'X-DSPAM-Confidence:'
for line in filehandle:
 if line.startswith (startLine):
  countLines+=1
  total += float(line[len(startLine):])
print   'Average spam confidence:', total/countLines 
  
  
