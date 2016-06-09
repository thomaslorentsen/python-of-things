# Python of things
A Python based http server that integrates to the Internet of Things

This script can be used in conjunction with IFTTT to perform various tasks.

# Installation
Install Pip
```bash
apt-get install python-pip
```

Install Python Tornado
```bash
apt-get install python-tornado
```

Install Todoist
```bash
pip install todoist
```

Install Tox
```bash
pip install tox
```

# Supervisor Installation
Install supervisor
```bash
apt-get install supervisor
```
Copy the config to ```/etc/supervisord/conf.d/pyhttp.conf``` and then restart supervisor
```bash
supervisorctl
reload
status
```

# Creating Tasks
Tasks can be created with a POST request
```bash
curl -X POST http://localhost:5000/todo/remind/me/at/station -d "Test add reminder"
```