"""
7-11-7-3
"""
fname = raw_input("Enter file name: ")
if fname == 'na na boo boo':
 print 'NA NA BOO BOO TO YOU - you have been punk"d'
 exit() 
filehandle = open(fname)
countLines = 0
for line in filehandle:
 countLines+=1  
print   'There were ', countLines, 'lines in ', fname 
  
  
