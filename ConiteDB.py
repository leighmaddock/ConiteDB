#!/usr/bin/env python
from pymongo import mongo_client
import time

# VERSION - 0.5.0

class ConiteDB:
    def __init__(self, dbname="conitedb", host="localhost", port=27017):
        self.dbname = dbname
        self.conn = mongo_client.MongoClient(host, port)
        self.db = self.conn[dbname]
        self.items = self.db.configitems

    def add(self, cinames, updates={}):
        if updates:
            updates = self.splitUpdates(updates)
        # Track update time stamp, also workaround for pymongo empty set bug
        updates["_updatetime"] = int(time.time())
        for ciname in cinames:
            self.items.find_and_modify({'ciname': ciname}, {"$set": updates}, upsert=True)

    def desc(self, cinames):
        cinamesfound = {}
        for ciname in cinames:
            results = self.items.find_one({'ciname': ciname})
            if results:
                cinamesfound[ciname] = results
        return cinamesfound

    def remove(self, cinames):
        for ciname in cinames:
            self.items.find_and_modify({'ciname': ciname}, remove=True)

    def find(self, criteria):
        cinamesfound = {}
        results = self.items.find(criteria)
        if results:
            for result in results:
                if result.get("ciname", ""):
                    cinamesfound[result["ciname"]] = result
        return cinamesfound

    def update(self, cinames, updates, criteria=""):
        if updates:
            updates = self.splitUpdates(updates)
        # Track update time stamp, also workaround for pymongo empty set bug
        updates["_updatetime"] = int(time.time())
        # run the udpate against cinames manually passed
        if cinames:
            for ciname in cinames:
                self.items.find_and_modify({'ciname': ciname}, {"$set": updates}, Upsert=True)
        # run through the query updates
        if criteria:
            self.items.update(criteria, {"$set": updates}, multi=True)

    def splitUpdates(self, updates):
        for key in updates.keys():
            if "," in updates[key]:
                updates[key] = updates[key].split(",")
        return updates

if __name__ == "__main__":
    pass
