# DEBUG TIPS and CHECKLIST

* Check your galaxy intance url is valid
* Check toolshed url is that you want
 * Released [https://toolshed.g2.bx.psu.edu/](https://toolshed.g2.bx.psu.edu/)
 * Test [https://testtoolshed.g2.bx.psu.edu/](https://testtoolshed.g2.bx.psu.edu/)
# Start Galaxy


## Using Docker Galaxy Stable

```
docker run -d -p 20080:80 bgruening/galaxy-stable:latest
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

# success

```
$ docker run --link dockergalaxy:dockergalaxy  -v $PWD:/work --rm manabuishii/docker-bioblend:0.8.0 python /work/to
olshed_tool_install_to_your_galaxy.py
[{u'tool_shed_status': {u'latest_installable_revision': u'True', u'revision_update': u'False', u'revision_upgrade': u'False', u'repository_deprecated': u'False'}, u'status': u'Installed', u'name': u'fastqc', u'deleted': False, u'ctx_rev': u'7', u'error_message': u'', u'installed_changeset_revision': u'3fdc1a74d866', u'tool_shed': u'toolshed.g2.bx.psu.edu', u'dist_to_shed': False, u'url': u'/api/tool_shed_repositories/f2db41e1fa331b3e', u'id': u'f2db41e1fa331b3e', u'owner': u'devteam', u'uninstalled': False, u'changeset_revision': u'3fdc1a74d866', u'includes_datatypes': False}, {u'tool_shed_status': None, u'status': u'New', u'name': u'package_fastqc_0_11_4', u'deleted': False, u'ctx_rev': u'2', u'error_message': u'', u'installed_changeset_revision': u'a8f485b2efd9', u'tool_shed': u'toolshed.g2.bx.psu.edu', u'dist_to_shed': False, u'url': u'/api/tool_shed_repositories/f597429621d6eb2b', u'id': u'f597429621d6eb2b', u'owner': u'iuc', u'uninstalled': False, u'changeset_revision': u'a8f485b2efd9', u'includes_datatypes': False}]
```
