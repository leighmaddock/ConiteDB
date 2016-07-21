ConiteDB
============
Configuration management tool to assist with automation and categorisation of systems.

A python library that can be imported into existing code, or called via pre-built api's via shell.

Uses a combination of python, pymongo and mongodb.

Requirements
============
* Tested on Ubuntu LTS 16.04
* Tested on pymongo 3.2
* Tested on mongodb 2.6.10
* Tested on Python 2.7.12

Installation
============
Ubuntu LTS 16.04:
```BASH
 # sudo apt-get install mongodb
 # sudo apt-get install python-pymongo
```
You can then copy the library into where you want to use it (site-packages, local cli, new environment etc.)

How To Use
============
CI below refers to a "configuration item". This is typically server/vm/aws hostname. It's a unique name identifer that makes sense to you.

The below commands have been provided based on personal preference of interface, you can import ConiteDB and create your own interface if you wish.

Add a CI
```
 # ./conitedb_add.py ci1
```

Add multiple CI's
```
 # ./conitedb_add.py ci1 ci2 ci3
```

Add a CI with attributes
```
 # ./conitedb_add.py ci1 attr1=abc attr2=xyz
```

Add multiple CI's with attributes
```
 # ./conitedb_add.py ci1 ci2 ci3 attr1=abc attr2=xyz
```

Updating CI's is similar to adding, except you can also update based on a query

Update a CI
```
 # ./conitedb_update.py ci1 attr3=abcxyz
```

Update a CI based on query - query uses same syntax conitedb_search.py below
```
 # ./conitedb_update.py attr3=abcxyz --query="attr1=abc"
```
Update CI's based on both
```
 # ./conitedb_update.py attr5=blahblah ci1 --query="attr2=xyz"
```

Removing an attribute is done by passing an empty value
```
 # ./conitedb_update.py attr5= ci1
```

Remove a CI
```
 # ./conitedb_remove.py ci3
```

Remove multiple CI's
```
 # ./conitedb_remove.py ci1 ci2
```

Report on all CI's and their attributes
```
 # ./conitedb_report.py
```
Report on all CI's and a specific attribute
```
 # ./conitedb_report.py attr1
```

Report on all CI's and specific attributes
```
 # ./conitedb_report.py attr1 attr2
```

Report on CI's matching attributes and specific attributes
```
 # ./conitedb_report.py attr1=abc attr2 attr3 attr4
```

You can usually pass any combination of CI name and keys, in any order, in the above CLI interfaces to get the behavior you want.


conitedb_desc.py has similar behavior to report, except it is more designed for when a CI name is known, and you want to know all attributes it has.

Describe a CI (all attributes)
```
 # ./conitedb_desc.py ci1
```

Describe multiple CI's (all attributes)
```
 # ./conitedb_desc.py ci1 ci2 ci3
```

conitedb_search.py is the opposite to desc, it is when you want a list of CI names based on known attributes
```
 # ./conitedb_search.py attr1=abc attr2=xyz
```

Warnings
============
This project is a work in progress.
None of the data is protected (at this point in time) by passwords, finger slips etc. Use with caution.


Feature Requests
============
* Secure Mongo transactions
* Transaction logging/auditing
* REST api
* JSON output support in calling scripts (or new script)
* Support items inside of an attribute (instead of replacing with update flag, simply append/pop items)
* better arg support (switch to using argparser, instead of funky string manipulation)

About
============
This is a project I worked on a few years ago, but shelved it as I wasn't happy with my append/pop item implementation. I have decided to ditch that support altogether and release as is for now to get a starting base. Some code had to be re-written/worked around due to newer versions of pymongo (original conitedb was developed on Ubuntu LTS 12.04!).

Testing
=========

Automated testing is provided by http://travis-ci.org configured by the .travis.yml.
The test runner is powered by py.test.
Coverage is provided by http://coveralls.io

Running the tests

```
  docker run -dP -p 27017:27017 mongo
  pip install -r requirements.txt
  pip install -r requirements-dev.txt
  PYTHONPATH=. py.test -vv --cov-report term-missing --cov=.
```
