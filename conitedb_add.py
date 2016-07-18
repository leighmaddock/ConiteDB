#!/usr/bin/env python
import sys
from ConiteDB import ConiteDB


def printUsage():
    print "Usage: %s <ciname> [key=value] ..." % sys.argv[0]
    sys.exit(1)


def getArgs():
    if len(sys.argv) <= 1:
        printUsage()
    cinames = []
    updates = {}
    for arg in sys.argv[1:]:
        if "=" in arg:
            P1, I, P2 = arg.partition("=")
            updates[P1] = P2
        else:
            cinames.append(arg)
    # cinames is mandatory, updates is not
    if not cinames:
        printUsage()

    return cinames, updates


def main():
    cinames, updates = getArgs()
    coniteobj = ConiteDB()
    coniteobj.add(cinames, updates)

if __name__ == "__main__":
    main()
