#!/usr/bin/env python
import sys
from ConiteDB import ConiteDB


def printUsage():
    print "Usage: %s [ciname]|[--query='key=value'] <key=value> ..." % sys.argv[0]
    sys.exit(1)


def getArgs():
    if len(sys.argv) <= 1:
        printUsage()
    cinames = []
    updates = {}
    criteria = {}
    for arg in sys.argv[1:]:
        if arg.startswith("--query="):
            P1, I, P2 = arg.partition("=")
            if "=" in P2:
                for queryarg in P2.split(" "):
                    A1, I, A2 = queryarg.partition("=")
                    criteria[A1] = A2
            else:
                printUsage()

        elif "=" in arg:
            P1, I, P2 = arg.partition("=")
            updates[P1] = P2
        else:
            cinames.append(arg)
    # cinames OR --query is mandatory, updates is also
    if not (cinames or criteria) and not updates:
        printUsage()

    return cinames, updates, criteria


def main():
    cinames, updates, criteria = getArgs()
    coniteobj = ConiteDB()
    coniteobj.update(cinames, updates, criteria)

if __name__ == "__main__":
    main()
