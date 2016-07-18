#!/usr/bin/env python

import sys
from ConiteDB import ConiteDB


def printUsage():
    print "Usage: %s <ciname> ..." % sys.argv[0]
    sys.exit(1)


def getArgs():
    if len(sys.argv) <= 1:
        printUsage()

    cinames = []
    for arg in sys.argv[1:]:
        cinames.append(arg)

    return cinames


def printResults(cinamesfound):
    for ciname in cinamesfound:
        print ciname
        for cinamekey in sorted(cinamesfound[ciname].keys()):
            if not cinamekey.startswith("_") and cinamekey != "ciname":
                if type(cinamesfound[ciname][cinamekey]) == type([]):
                    cinamesfound[ciname][cinamekey] = ",".join(cinamesfound[ciname][cinamekey])
                print "\t%s: %s" % (cinamekey, cinamesfound[ciname][cinamekey])


def main():
    cinames = getArgs()
    coniteobj = ConiteDB()
    cinamesfound = coniteobj.desc(cinames)
    printResults(cinamesfound)

if __name__ == "__main__":
        main()
