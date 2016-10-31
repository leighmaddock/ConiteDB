#!/usr/bin/env python

from flask import Flask, jsonify, request
from ConiteDB import ConiteDB

app = Flask(__name__)

@app.route('/search', methods=['GET'])
def conitedb_search():
    criteria = request.args
    coniteobj = ConiteDB()
    cinamesfound = coniteobj.find(criteria)
    return jsonify({'cinames': cinamesfound.keys()})

@app.route('/report', methods=['GET'])
def conitedb_report():
    dispkeys = []
    # request.args is immutable, this allows us to manipulate input
    criteria = {key: value for key, value in request.args.items()}
    if "_fields" in criteria:
        dispkeys = criteria["_fields"].split(",")
        criteria.pop("_fields")
    coniteobj = ConiteDB()
    cinamesfound = coniteobj.find(criteria)
    # We search based on criteria, and filter out fields not wanted.
    for ciname in sorted(cinamesfound):
        for cinamekey in sorted(cinamesfound[ciname].keys()):
            if dispkeys:
                if cinamekey not in dispkeys:
                    cinamesfound[ciname].pop(cinamekey)
            else:
                if cinamekey.startswith("_") or cinamekey == "ciname":
                    cinamesfound[ciname].pop(cinamekey)
    return jsonify({'cinames': cinamesfound})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

