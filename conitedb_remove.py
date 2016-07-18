#!/usr/bin/env python
import sys
from ConiteDB import ConiteDB


def printUsage():
    print "Usage: %s <ciname1> <ciname2> ..." % sys.argv[0]
    sys.exit(1)


def getArgs():
    if len(sys.argv) <= 1:
        printUsage()
    cinames = []
    for arg in sys.argv[1:]:
        if "=" in arg:
            print "Queries not allowed in remove, too dangerous (use search to pipe into remove if you must)"
            printUsage()
        else:
            cinames.append(arg)
    # cinames is mandatory, updates is not
    if not cinames:
        printUsage()

    return cinames


def main():
    cinames = getArgs()
    coniteobj = ConiteDB()
    coniteobj.remove(cinames)

if __name__ == "__main__":
    main()
