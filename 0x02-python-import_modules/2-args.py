#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":

    n=len(sys.argv)
    if((len(sys.argv)-1)==1):
        print((len(sys.argv)-1)," argument:")
    elif((len(sys.argv)-1)==0):
        print((len(sys.argv)-1)," arguments.")
    else:
        print((len(sys.argv)-1)," arguments:")
    for i in range(1,n):
        print(i,":",str(sys.argv[i]))
