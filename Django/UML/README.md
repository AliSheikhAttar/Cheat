
# UML

## gvz
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
## xml drawio
```bash
pyreverse -o dot -p <outputname> <app1> <app2> ...
```
- convert dot to xml
```bash
python dot2xml.py
```