#!/usr/bin/python
# coding: utf-8
"""
Install toolshed tool list into your Galaxy
"""
import os
from bioblend import galaxy

galaxy_url = os.getenv("GALAXY_URL", "http://dockergalaxy/")
api_key=os.getenv("GALAXY_API_KEY", "admin")
toolshed_url = os.getenv("TOOLSHED_URL", "https://toolshed.g2.bx.psu.edu/")
name=os.getenv("TOOL_NAME", "fastqc")
owner=os.getenv("TOOL_OWNER", "devteam")
changeset_revision=os.getenv("TOOL_CHANGESET_REVISION", "3fdc1a74d866")

#
install_tool_dependencies=True
install_repository_dependencies=True

gi = galaxy.GalaxyInstance(url=galaxy_url, key=api_key)


gi.toolShed.install_repository_revision(toolshed_url,
                                        name,owner,changeset_revision,
                                        install_tool_dependencies=install_tool_dependencies,
                                        install_repository_dependencies=install_repository_dependencies)

hl = gi.toolShed.get_repositories()

print hl
