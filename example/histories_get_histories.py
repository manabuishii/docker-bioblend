#!/usr/bin/python
# coding: utf-8
import os
from bioblend import galaxy

galaxy_url = os.getenv("GALAXY_URL", "http://dockergalaxy/")
api_key=os.getenv("GALAXY_API_KEY", "admin")

gi = galaxy.GalaxyInstance(url=galaxy_url, key=api_key)

hl = gi.histories.get_histories()

print(hl)
