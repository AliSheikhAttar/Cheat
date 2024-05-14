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