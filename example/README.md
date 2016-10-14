# DEBUG TIPS and CHECKLIST

* Check your galaxy intance url is valid
* Check toolshed url is that you want
 * Released [https://toolshed.g2.bx.psu.edu/](https://toolshed.g2.bx.psu.edu/)
 * Test [https://testtoolshed.g2.bx.psu.edu/](https://testtoolshed.g2.bx.psu.edu/)
# Start Galaxy


## Using Docker Galaxy Stable

```
docker run -d --name dockergalaxy -p 20080:80 bgruening/galaxy-stable:latest
```

# Connect to Galaxy by using Bioblend

[See official document](http://bioblend.readthedocs.io/en/latest/api_docs/galaxy/all.html)

```
#!/usr/bin/env python

from bioblend import galaxy

gi = galaxy.GalaxyInstance(url='http://127.0.0.1:8000', key='your_api_key')

hl = gi.histories.get_histories()
```

## example

### first start docker galaxy

```
docker run -d --name dockergalaxy -p 20080:80 bgruening/galaxy-stable:latest
```

### second

```
docker run --link dockergalaxy:dockergalaxy \
           -v $PWD:/work \
           --rm \
           manabuishii/docker-bioblend:0.8.0 \
           python /work/histories_get_histories.py
```

result

```
[]
```

# error messages

## toolshed URL is invalid

```
$ docker run --link dockergalaxy:dockergalaxy  -v $PWD:/work --rm manabuishii/docker-bioblend:0.8.0 python /work/to
olshed_tool_install_to_your_galaxy.py
Traceback (most recent call last):
  File "/work/toolshed_tool_install_to_your_galaxy.py", line 19, in <module>
    gi.toolShed.install_repository_revision(toolshed_url,name,owner,changeset_revision)
  File "/usr/local/lib/python2.7/site-packages/bioblend/galaxy/toolshed/__init__.py", line 146, in install_repository_revision
    return Client._post(self, url=url, payload=payload)
  File "/usr/local/lib/python2.7/site-packages/bioblend/galaxy/client.py", line 157, in _post
    files_attached=files_attached)
  File "/usr/local/lib/python2.7/site-packages/bioblend/galaxyclient.py", line 134, in make_post_request
    body=r.text, status_code=r.status_code)
bioblend.ConnectionError: Unexpected HTTP status code: 500: {"err_msg": "Error attempting to retrieve installation information from tool shed https://toolshed.g2.bx.psu.edu2/ for revision 5:93f27bdc08cd of repository fastqc owned by devteam: <urlopen error [Errno -2] Name or service not known>", "err_code": 500001}

```

## name , owner, changeset_revision is invalid

Same error message

Owner is ```devteam222``` (no such a owner)

```
$ docker run --link dockergalaxy:dockergalaxy  -v $PWD:/work --rm manabuishii/docker-bioblend:0.8.0 python /work/to
olshed_tool_install_to_your_galaxy.py
Traceback (most recent call last):
  File "/work/toolshed_tool_install_to_your_galaxy.py", line 28, in <module>
    name,owner,changeset_revision)
  File "/usr/local/lib/python2.7/site-packages/bioblend/galaxy/toolshed/__init__.py", line 146, in install_repository_revision
    return Client._post(self, url=url, payload=payload)
  File "/usr/local/lib/python2.7/site-packages/bioblend/galaxy/client.py", line 157, in _post
    files_attached=files_attached)
  File "/usr/local/lib/python2.7/site-packages/bioblend/galaxyclient.py", line 134, in make_post_request
    body=r.text, status_code=r.status_code)
bioblend.ConnectionError: Unexpected HTTP status code: 400: {"err_msg": "No information is available for the requested repository revision.\nOne or more of the following parameter values is likely invalid:\ntool_shed_url: https://toolshed.g2.bx.psu.edu/\nname: fastqc\nowner: devteam222\nchangeset_revision: 3fdc1a74d866\n", "err_code": 400008}
```

## success

```
$ docker run --link dockergalaxy:dockergalaxy  -v $PWD:/work --rm manabuishii/docker-bioblend:0.8.0 python /work/to
olshed_tool_install_to_your_galaxy.py
[{u'tool_shed_status': {u'latest_installable_revision': u'True', u'revision_update': u'False', u'revision_upgrade': u'False', u'repository_deprecated': u'False'}, u'status': u'Installed', u'name': u'fastqc', u'deleted': False, u'ctx_rev': u'7', u'error_message': u'', u'installed_changeset_revision': u'3fdc1a74d866', u'tool_shed': u'toolshed.g2.bx.psu.edu', u'dist_to_shed': False, u'url': u'/api/tool_shed_repositories/f2db41e1fa331b3e', u'id': u'f2db41e1fa331b3e', u'owner': u'devteam', u'uninstalled': False, u'changeset_revision': u'3fdc1a74d866', u'includes_datatypes': False}, {u'tool_shed_status': None, u'status': u'New', u'name': u'package_fastqc_0_11_4', u'deleted': False, u'ctx_rev': u'2', u'error_message': u'', u'installed_changeset_revision': u'a8f485b2efd9', u'tool_shed': u'toolshed.g2.bx.psu.edu', u'dist_to_shed': False, u'url': u'/api/tool_shed_repositories/f597429621d6eb2b', u'id': u'f597429621d6eb2b', u'owner': u'iuc', u'uninstalled': False, u'changeset_revision': u'a8f485b2efd9', u'includes_datatypes': False}]
```


# Workflow

## Workflow list

Get workflow list in your container

```
$ docker run  --link dockergalaxy:dockergalaxy  -v $PWD:/work --rm manabuishii/docker-bioblend:0.8.0 python /work/workflow_get_workflows.py
[{u'name': u'Testworkflow', u'tags': [], u'deleted': False, u'latest_workflow_uuid': u'809c768a-59f1-4d9d-90c8-701ddf43b536', u'url': u'/api/workflows/f2db41e1fa331b3e', u'published': False, u'owner': u'admin', u'model_class': u'StoredWorkflow', u'id': u'f2db41e1fa331b3e'}]
```

## Export workflow as json


```
docker run  --link dockergalaxy:dockergalaxy  -v $PWD:/work --rm manabuishii/docker-bioblend:0.8.0 python /work/workflow_export_workflow_json.py
```

### Pretty Print

```
$ docker run -e PRETTY_PRINT=True --link dockergalaxy:dockergalaxy  -v $PWD:/work --rm manabuishii/docker-bioblend:0.8.0 python /work/workflow_export_workflow_json.py
```

```
{
  "a_galaxy_workflow": "true", 
  "format-version": "0.1", 
  "name": "Testworkflow", 
  "steps": {
    "0": {
      "tool_id": "toolshed.g2.bx.psu.edu/repos/devteam/fastqc/fastqc/0.65", 
      "content_id": "toolshed.g2.bx.psu.edu/repos/devteam/fastqc/fastqc/0.65", 
      "uuid": "19ac4c29-bf33-4420-8630-1aa8f2bc8f41", 
      "tool_version": "0.65", 
      "outputs": [
        {
          "type": "html", 
          "name": "html_file"
        }, 
        {
          "type": "txt", 
          "name": "text_file"
        }
      ], 
      "post_job_actions": {}, 
      "workflow_outputs": [], 
      "annotation": "", 
      "input_connections": {}, 
      "inputs": [
        {
          "name": "contaminants", 
          "description": "runtime parameter for tool FastQC"
        }, 
        {
          "name": "limits", 
          "description": "runtime parameter for tool FastQC"
        }, 
        {
          "name": "input_file", 
          "description": "runtime parameter for tool FastQC"
        }
      ], 
      "tool_errors": null, 
      "position": {
        "top": 248.5, 
        "left": 253.5
      }, 
      "tool_state": "{\"__page__\": 0, \"contaminants\": \"{\\\"__class__\\\": \\\"RuntimeValue\\\"}\", \"__rerun_remap_job_id__\": null, \"limits\": \"{\\\"__class__\\\": \\\"RuntimeValue\\\"}\", \"input_file\": \"{\\\"__class__\\\": \\\"RuntimeValue\\\"}\"}", 
      "label": null, 
      "type": "tool", 
      "id": 0, 
      "tool_shed_repository": {
        "owner": "devteam", 
        "changeset_revision": "3fdc1a74d866", 
        "name": "fastqc", 
        "tool_shed": "toolshed.g2.bx.psu.edu"
      }, 
      "name": "FastQC"
    }
  }, 
  "annotation": "", 
  "uuid": "809c768a-59f1-4d9d-90c8-701ddf43b536"
}
```
