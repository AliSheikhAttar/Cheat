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
- make migrations
```bash
python manage.py makemigrations <App name>
```
- migrate and update database
```bash
python manage.py migrate <App name>
```

- create admin user
```bash
python3 manage.py createsuperuser
```

- Register object model in admin
```bash
    admin.site.register(ObjectModel)
```

- run web server
```bash
python manage.py runserver <port(default:8000)> # instead of django-admin which doesnt take the settings of proj into account 
```

## Create Classes UML
### gvz
- install req.
```bash
pip install django-extensions
sudo apt-get install graphviz
```
- install app inside django
```python
INSTALLED_APPS = [
    ...
    'django_extensions',
]
```
- create dot file
```bash
python manage.py graph_models -a --dot -o -g <output>.dot
python manage.py graph_models your_app_1 your_app_2 -o my_project_uml.png
```
- create png
```bash
dot -Tpng my_project.dot -o my_project.png
```
### xml drawio
```bash
pyreverse -o dot -p <outputname> <app1> <app2> ...
```
- convert dot to xml
```bash
python dot2xml.py
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