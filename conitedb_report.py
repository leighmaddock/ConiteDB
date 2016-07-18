#!/usr/bin/env python

import sys
from ConiteDB import ConiteDB


def printUsage():
    print "Usage: %s <ciname> ..." % sys.argv[0]
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
                dispkeys.append(arg)

    return dispkeys, criteria


def printResults(cinamesfound, dispkeys):
    for ciname in sorted(cinamesfound):
        if not dispkeys:
            print ciname
            for cinamekey in sorted(cinamesfound[ciname].keys()):
                if not cinamekey.startswith("_") and cinamekey != "ciname":
                    if type(cinamesfound[ciname][cinamekey]) == type([]):
                        cinamesfound[ciname][cinamekey] = ",".join(cinamesfound[ciname][cinamekey])
                    print "\t%s: %s" % (cinamekey, cinamesfound[ciname][cinamekey])
        else:
            message = "%s" % ciname
            for cinamekey in sorted(cinamesfound[ciname].keys()):
                if cinamekey in dispkeys:
                    if type(cinamesfound[ciname][cinamekey]) == type([]):
                        cinamesfound[ciname][cinamekey] = ",".join(cinamesfound[ciname][cinamekey])
                    message = message + "\t%s=%s" % (cinamekey, cinamesfound[ciname][cinamekey])
            print message


def main():
    dispkeys, criteria = getArgs()
    coniteobj = ConiteDB()
    cinamesfound = coniteobj.find(criteria)
    printResults(cinamesfound, dispkeys)

if __name__ == "__main__":
    main()
