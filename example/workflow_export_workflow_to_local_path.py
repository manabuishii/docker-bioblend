#!/usr/bin/python
# coding: utf-8
"""
Get workflow as json format
"""
import os
import json
from bioblend import galaxy


galaxy_url = os.getenv("GALAXY_URL", "http://dockergalaxy/")
api_key=os.getenv("GALAXY_API_KEY", "admin")
workflow_id=os.getenv("WORKFLOW_ID", "f2db41e1fa331b3e")
pretty_print_str=os.getenv("PRETTY_PRINT" , False)
pretty_print= pretty_print_str=="True"
indent=int(os.getenv("INDENT", 2))

#
install_tool_dependencies=True
install_repository_dependencies=True

gi = galaxy.GalaxyInstance(url=galaxy_url, key=api_key)

ej = gi.workflows.export_workflow_to_local_path(workflow_id, "/work/")

