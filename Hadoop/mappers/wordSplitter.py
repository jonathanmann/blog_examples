#!/usr/bin/python
import sys 
import re 

def main(argv): 
    print argv
    pattern = re.compile("[a-zA-Z][a-zA-Z0-9]*") 
    print sys.stdin
    """
    for line in sys.stdin.readlines(): 
        for word in pattern.findall(line): 
            print "LongValueSum:" + word.lower() + "\t" + "1" 
    """


if __name__ == "__main__": 
    main(sys.argv) 
