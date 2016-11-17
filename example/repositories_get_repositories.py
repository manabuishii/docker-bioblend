#!/usr/bin/python
# coding: utf-8
import os
from bioblend import toolshed

ts = toolshed.ToolShedInstance(url='https://testtoolshed.g2.bx.psu.edu')

rl = ts.repositories.get_repositories()

print(rl)
