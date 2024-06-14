# Database
- make migrations
create or modify tables in database base on our models and create respective migrations file
```bash
python manage.py makemigrations <App name>
```
- sql code sent to database at runtime for <app> forn <n>th migrations
```bash
python manage.py sqlmigrate <app> <000n>
```

- migrate and update database
create database schema bassed on migrations
```bash
python manage.py migrate 
```
- revert to specific migrations
```bash
python manage.py migrate <app> <000n>
```
- connect to mysql
```bash
pipenv install mysqlclient
```
- check mysql
```bash
mysql -u root -p <pass>
```
- add config to setting
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'storefront',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'MyPassword'
    }
}
```
- migrate to new database
```bash
python manage.py migrate
```
## Running custom SQL
- create empty migration
```bash
python manage.py makemigrations <app> --empty
```
- inside migration file write sql code
- first argument of RunSQL is for upgrading database
- second arg is for downgrading database (when reverting)
```python
operations = [
    migrations.RunSQL("""
        INSERT INTO store_collection (title)
        VALUES ('collection1')
    """, """
        DELETE FROM store_collection 
        WHERE title='collection1'
    """)
]
```
- generate dummy data
> (mockaroo.com)