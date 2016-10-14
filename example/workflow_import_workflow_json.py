#!/usr/bin/python
# coding: utf-8
"""
Workflow list into your Galaxy
"""
import os
import sys
from bioblend import galaxy

if (len(sys.argv) != 2):
    print 'Usage: %s workflow_json_filename' % sys.argv[0]
    sys.exit(1)

galaxy_url = os.getenv("GALAXY_URL", "http://dockergalaxy/")
api_key=os.getenv("GALAXY_API_KEY", "admin")

gi = galaxy.GalaxyInstance(url=galaxy_url, key=api_key)

f = open(sys.argv[1])
workflow_json = f.read()
f.close()

print workflow_json


gi.workflows.import_workflow_json(workflow_json)

