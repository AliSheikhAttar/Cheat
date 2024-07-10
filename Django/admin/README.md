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

## links to other pages & Search
```python
@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    autocomplete_fields = ['featured_product']
    list_display = ['title', 'products_count']
    search_fields = ['title__istartswith'] # search fields, starts with given input case insensitive, used for autocompletion

    @admin.display(ordering='products_count') # orderظ
    def products_count(self, collection):
        url = (
            reverse('admin:store_product_changelist')# go to store app -> product model -> changelist
            + '?' # get argument
            + urlencode({
                'collection__id': str(collection.id) # filter by query
            }))
        return format_html('<a href="{}">{} Products</a>', url, collection.products_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            products_count=Count('product')
        )
```

# Filter & Custom action
```python
class InventoryFilter(admin.SimpleListFilter):
    title = 'inventory'
    parameter_name = 'inventory'

    def lookups(self, request, model_admin):# define lookup values for filtering
        return [
            ('<10', 'Low')
        ]

    def queryset(self, request, queryset: QuerySet):# implement filtering
        if self.value() == '<10':
            return queryset.filter(inventory__lt=10)

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    autocomplete_fields = ['collection'] # for creating new object
    prepopulated_fields = {# for creating new object
        'slug': ['title'] # slug will be populated by title
    }
    actions = ['clear_inventory'] # pass name of custom method
    list_display = ['title', 'unit_price',
                    'inventory_status', 'collection_title']
    list_editable = ['unit_price']
    list_filter = ['collection', 'last_update', InventoryFilter] # filter arguments
    list_per_page = 10
    list_select_related = ['collection']
    search_fields = ['title']

    def collection_title(self, product):
        return product.collection.title

    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory < 10:
            return 'Low'
        return 'OK'

    @admin.action(description='Clear inventory')# name for custom action in drop down 
    def clear_inventory(self, request, queryset): # custom action
        updated_count = queryset.update(inventory=0)
        self.message_user( # message to user
            request,
            f'{updated_count} products were successfully updated.',
            messages.ERROR # type of message
        )
```

## Validator
models -> <model> -> <field>
```python

description = models.TextField(null=True, blank=True)# blank=True -> can be null when creating object in admin
unit_price = models.DecimalField(
    max_digits=6,
    decimal_places=2,
    validators=[MinValueValidator(1, message="custom message")]) # min value
```

## Edit children using inline
-> admin.py
```python
class OrderItemInline(admin.TabularInline): # StackedInline
    autocomplete_fields = ['product']
    min_num = 1
    max_num = 10 # max number of children
    model = models.OrderItem
    extra = 0 # no placeholders


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    autocomplete_fields = ['customer'] # must implement the search fields in customeradmin model
    inlines = [OrderItemInline] # add the inline
    list_display = ['id', 'placed_at', 'customer']
```

## Generic relationships

```python
class TagInline(GenericTabularInline):
    model = TaggedItem


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [TagInline]
``` 