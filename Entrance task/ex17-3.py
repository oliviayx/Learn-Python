from sys import argv
from os.path import exists

script,from_file,to_file=argv




"""input=open(from_file)
indata=input.read()
"""

output=open(to_file,'w')
output.write(open(from_file).read())



output.close()
#input.close()
