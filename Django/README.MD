## Virtual env
- Create virtual env
```bash
python -m venv <env_name> 
virtualenv <env_name>
```
- activate

` source <env>/bin/activate`
` deactivate `

- ready the pip

` python3 -m pip install --upgrade pip `
` python3 -m pip --version `
- installed packages
` python3 -m pip freeze `
` pip list `
- Start project
```bash 
django-admin startproject <Project name>
``` 

- Start app
```bash
python manage.py startapp <App name>
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

