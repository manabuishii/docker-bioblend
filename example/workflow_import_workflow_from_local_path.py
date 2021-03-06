#!/usr/bin/python
# coding: utf-8
"""
Import workflow
"""
import os
import sys
from bioblend import galaxy

if (len(sys.argv) != 2):
    print 'Usage: %s workflow_filename' % sys.argv[0]
    sys.exit(1)


galaxy_url = os.getenv("GALAXY_URL", "http://dockergalaxy/")
api_key=os.getenv("GALAXY_API_KEY", "admin")
workflow_filename=sys.argv[1]

#

gi = galaxy.GalaxyInstance(url=galaxy_url, key=api_key)

ej = gi.workflows.import_workflow_from_local_path(workflow_filename)

