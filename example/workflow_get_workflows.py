#!/usr/bin/python
# coding: utf-8
"""
Install toolshed tool list into your Galaxy
"""
import os
from bioblend import galaxy

galaxy_url = os.getenv("GALAXY_URL", "http://dockergalaxy/")
api_key=os.getenv("GALAXY_API_KEY", "admin")

#
install_tool_dependencies=True
install_repository_dependencies=True

gi = galaxy.GalaxyInstance(url=galaxy_url, key=api_key)


wl = gi.workflows.get_workflows()

print wl
