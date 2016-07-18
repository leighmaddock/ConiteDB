#!/usr/bin/env python
import sys
from ConiteDB import ConiteDB


def printUsage():
    print "Usage: %s <key=value> ..." % sys.argv[0]
    sys.exit(1)


def getArgs():
    dispkeys = []
    criteria = {}
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            if "=" in arg:
                P1, I, P2 = arg.partition("=")
                criteria[P1] = P2
            else:
                continue

    return criteria


def printResults(cinamesfound):
    for ciname in sorted(cinamesfound):
        print ciname


def main():
    criteria = getArgs()
    coniteobj = ConiteDB()
    cinamesfound = coniteobj.find(criteria)
    printResults(cinamesfound)

if __name__ == "__main__":
    main()
