## Virtual env
- Create virtual env
```bash
python -m venv <env_name> 
virtualenv <env_name>
```
- activate
```bash
source <env>/bin/activate
deactivate 
```

- ready the pip
```bash
python3 -m pip install --upgrade pip
python3 -m pip --version 
```

- installed packages
```bash
python3 -m pip freeze
pip list 
```
- create vitualenv & install django inside 
```bash
 pipenv django
```
- activate virtualenv
 ```bash
 pipenv shell
```
- virtualenv path
```bash
pipenv --venv
```

- Start project
```bash 
django-admin startproject <Project name> . # . -> current dir for proj dir
``` 

- Start app
```bash
python manage.py startapp <App name>
```
- resiter app
```python
INSTALLED_APPS = [
    ...
    'django_extensions',
]
```

- run web server
```bash
python manage.py runserver <port(default:8000)> # instead of django-admin which doesnt take the settings of proj into account 
```

## frontend
```bash
mkdir templates
touch temlplates/<index.html>
```
- render html page
```python
return render(request, '<index.html>')
```

## debug
### VSCODE
- create launch.json
- add port "9000" to args in configurations so it doesnt clash with the deafult 8000 port
- set breakpoint
- run debug
- go to debug port <9000> of the url

### Dubug_toolbar
- ` python -m pip install django-debug-toolbar `
- add to `debug_toolbar` to apps
- add to main url pattern
```python
import debug_toolbar
path('__debug__/', include(debug_toolbar.urls)),
```
- add to middleware
```python
MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]
```
- add ip
INTERNAL_IPS = [
    '127.0.0.1',
]