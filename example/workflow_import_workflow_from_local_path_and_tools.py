#!/usr/bin/python
# coding: utf-8
"""
Import workflow
"""
import json
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
f = open(workflow_filename)

tools = {}
workflow_json = json.load(f)
for key in workflow_json['steps']:
  item = workflow_json['steps'][key]
  if item is not None:
    if item.has_key('tool_shed_repository'):
      tool_shed_repository=item['tool_shed_repository']
      # {u'owner': u'devteam', u'changeset_revision': u'952059348a30', u'name': u'vcffilter', u'tool_shed': u'toolshed.g2.bx.psu.edu'}
      str=tool_shed_repository['owner'] \
          +tool_shed_repository['changeset_revision'] \
          +tool_shed_repository['name'] \
          +tool_shed_repository['tool_shed']
      tools[str]=tool_shed_repository

#
install_tool_dependencies=True
install_repository_dependencies=True


gi = galaxy.GalaxyInstance(url=galaxy_url, key=api_key)

for k in tools:
  item = tools[k]

  toolshed_url='https://'+item['tool_shed']+'/'
  name=item['name']
  owner=item['owner']
  changeset_revision=item['changeset_revision']
  gi.toolShed.install_repository_revision(toolshed_url,
                                        name,owner,changeset_revision,
                                        install_tool_dependencies=install_tool_dependencies,
                                        install_repository_dependencies=install_repository_dependencies)
     
ej = gi.workflows.import_workflow_from_local_path(workflow_filename)

