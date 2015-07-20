#!/bin/bash
description=$@
cp redmine.py python-redmine/.
cd python-redmine
/usr/bin/python redmine.py --description "${description}"
rm -rf python-redmine/redmine.py
