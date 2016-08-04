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

# Running locally
The script can be run without supervisor for testing.
```bash
python main.py
```

# Creating Tasks
Tasks can be created with a POST request.
The following will create a task that will display a reminder when I arrive home.
```bash
curl -X POST http://localhost:5000/todo/remind/me -d "I will be reminded when I get home"
```
Tasks can be created with a reminder at alternative locations.
```bash
curl -X POST http://localhost:5000/todo/remind/me/at/station -d "I will be reminded when I arrive at the station"
curl -X POST http://localhost:5000/todo/remind/me/at/city -d "I will be reminded when I arrive at home in the city"
curl -X POST http://localhost:5000/todo/remind/me/at/country -d "I will be reminded when I arrive at home in the country"
```