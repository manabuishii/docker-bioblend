#!/usr/bin/python
# coding: utf-8
import os
from bioblend import toolshed

#
ts = toolshed.ToolShedInstance(url='https://toolshed.g2.bx.psu.edu')
# testtoolshed
# ts = toolshed.ToolShedInstance(url='https://testtoolshed.g2.bx.psu.edu')

rl = ts.repositories.get_repository_revision_install_info('freebayes','devteam','99684adf84de')

print(rl)
