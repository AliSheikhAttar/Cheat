# admin


- create admin user
```bash
python3 manage.py createsuperuser
```
- change admin password
```bash
python manage.py changepassword admin
```
- Register object model in admin
```bash
    admin.site.register(ObjectModel)
```

## customize presentation

-> project.urls
- chage header & title
```python
admin.site.site_header = '<any>'
admin.site.index_title = '<any>'
```
- register model to admin
-> admin.py of app
```python
admin.site.register(models.<model>)
```
- change presentation on admin
-> models -> model
```python 
def __str__(self) -> str:
    return <self.title>
```
- sort presentation on admin
-> models -> model
```python
class Meta
    ordering = ['<field>']
```
- customize list display
-> models -> admin
```python 
# show fields
@admin.register(models.Product)# approach 1
class <model>Admin(admin.ModelAdmin):
    list_display = ['field','field']

admin.site.register(models.Product, <model>Admin)# approach 2
# editables
list_editables = ['unit_price']# can be edited in admin panel
# objects per page
list_per_page = <n>
```
## computed columns
-> models -> admin
```python

class <model>Admin(admin.ModelAdmin):
    list_display = ['field','field', <func>]

@admin.display(ordering='inventory')# how to sort
def <func>(self, product):
    if product.inventory < 10 :
        return  'Low'
    return 'ok'
```

## related objects
```python
list_display = [collection_title]
list_selected_related = ['collection']

def collection_title(self, product):
    return product.collection.title
```

## overriding queryset

```python
list_display = [products_count]
@admin.display(ordering='products_count')
def product_count(self, collection):
    return collection.products_count

def get_queryset(self,request):
    return super().get_queryset(request).annotate(products_count=Count('product'))
```

## links to other pages
```python
@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    autocomplete_fields = ['featured_product']
    list_display = ['title', 'products_count']
    search_fields = ['title']

    @admin.display(ordering='products_count')
    def products_count(self, collection):
        url = (
            reverse('admin:store_product_changelist')
            + '?'
            + urlencode({
                'collection__id': str(collection.id)
            }))
        return format_html('<a href="{}">{} Products</a>', url, collection.products_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            products_count=Count('product')
        )
```