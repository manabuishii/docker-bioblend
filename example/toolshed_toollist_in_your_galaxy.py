#!/usr/bin/python
# coding: utf-8
"""
Display toolshed tool list in your Galaxy
"""
import os
from bioblend import galaxy

galaxy_url = os.getenv("GALAXY_URL", "http://dockergalaxy/")
api_key=os.getenv("GALAXY_API_KEY", "admin")

gi = galaxy.GalaxyInstance(url=galaxy_url, key=api_key)

hl = gi.toolShed.get_repositories()

print hl
