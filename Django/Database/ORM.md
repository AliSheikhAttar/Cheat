# ORM

- each model has attribute objects
- objects is manager object, db interface
- return query_set
- query_set => object encapsulate query except the count() & get() method (returns actual objects)
- django evalutes query_set when the latter is behaved like list & send right sql statement to db & get result
- ex : 
```python
#1
list(query_set)
#2
for item in quer_set:
#3
query_set[0]
```
## filter by primary_key
```python
Product = Product.objects.get(pk=1)
```
## exception
```python
from django.core.exceptions import ObjectDoesNotExist

try:
    Product = Product.objects.get(pk=1)
except ObjectDoesNotExist:
    pass
# Equivalent
Product = Product.objects.filter(pk=1).first() # none if not exists
```
## existance
```python
exists = Product.objects.filter(pk=1).exists()
```

## field lookups
```python
#keyword => pk = 1 
Product = Product.objects.filter(unit_price=1).first() # none if not exists
#inequality => unit_price__lte=1 => keyword for expression (less than or equal) => unit_price <= 1, lt, lte, gt, gte,
Product = Product.objects.filter(unit_price__lte=1).first() # none if not exists
#range => unit_price__range(20,30)
#relationship => collection__<filed_of_collection>__<look up field or none>=<something>
#relationship => collection__id__range=(1,2,3) => all of products in any of the 1 2 3 collections
# string
## contains => title__contains='coffee' => case sensitive
## contains => title__icontains='coffee' => case insensitive
## contains => title__startswith='coffee' => case insensitive
# date
## last_update__year=2002,  date, year, month,minute, second
# null
## description__isnull=True => all fields without descriptions
```
### exercise
```python
# Order items for products in collection 3
query_set = OrderItem.objects.filter(product__collection__id=3)
```
## Complex query using Q
```python
# unitprice.id==3 and title.contains('as')
query_set = OrderItem.objects.filter(unitprice__id=3, title__contains='as')
# Equal
query_set = OrderItem.objects.filter(unitprice__id=3).filter(title__contains='as')
# unitprice.id==3 or not(title.contains('as'))
from django.db.models import Q
query_set = OrderItem.objects.filter(Q(unitprice__id=3) | ~Q(title__contains='as'))
```

## reference field using F
```python
from django.db.models import F
# fields on same table
query_set = OrderItem.objects.filter(inventory=F('price'))
# fields on related tables
query_set = OrderItem.objects.filter(inventory=F('collection__id'))

query_set = orderItem.objects.values('product_id').distinct() # it doesnt have product_id => creates it and set it as foreign key to product, same as product__id
```

## sorting
```python
# sort on field ascending
order_by('price')
# sort on field descending
order_by('-price')
# sort on multiple fields
order_by('unit_price', '-price')
# reverse the ordering => first descending , second ascending
order_by('unit_price', '-price').reverse()

# earliest
order_by('unit_price')[0]
# Equal
earliest('unit_price')

# latest
order_by('-unit_price')[0]

# Equal
latest('unit_price')
```

## limit
```python
LIMIT = 5
OFFSET = 3
query_set = OrderItem.objects.order_by('price')[OFFSET:LIMIT]
```

## Selection fields
- output = dictionary , key = column
```python
query_set = OrderItem.objects.values('id', 'title', 'colllection__title')
```
- output = tupple
```python
query_set = OrderItem.objects.values('id', 'title', 'colllection__title')
```
- output = instance
```python
query_set = OrderItem.objects.only('id', 'title', 'colllection__title')
```

- exclude fields
```python
query_set = OrderItem.objects.defer('description')
```

### Loading joins 
- each have 1 foreign key instance
```python
.select_related('table')
```
- each have multiple foreign key instances
```python
.prefetch_related('table')
```

## Aggregation
```python
.aggregate(Count('id'))
.aggregate(Count('id'), min_price=Min('Unit_Price'))
```

## Anotation 
- Add columns to table
```python
.annotate(<field>=(Value(True)/F('<other filed>'))
```
## Functions
- call sql functions
```python
.annoatate(full_name=Func(F('first_name'), Value(' '), F('last_name'), function='CONCAT')))
# or
from django.db.models.functions import Concat

.annoatate(full_name=Concat('first_name', Value(' '), 'last_name'))
```

## Grouping
- count of field for primary , group by primary
```python
.annotate(orders_count=Count('order')) # dont use django defualt converstion <table>_set just use <table>
```
## Expression wrapper
- set output type
```python
x = ExpressionWrapper(F('field')*0.3,output_field=DecimalField())
```

## Quering generic relations

- tags of a product
```python
content_type = ContentType.objects.get_for_model(Product)
query =  TaggedItem.objects \ 
    .select_related('tag') \ 
    .filter(
        content_type=content_type,
        object_id=1
    )

# find content_type id for product model
#  preload tag table because its related by foreing key to TaggedItem
# filter by object_id which is product_id
```

## Custom Manager 
```python
# in models.py
class custom_manager(models.Manager):
    def custom_func():
        pass
    
class mymodel(models.Model):
    objects = custom_manager()

# view
def view_fun(request):
    query_set = mymodel.objects.custom_func()

```

## Create Object
```python
# first approach -> better
obj = myModel()
obj.field = value
obj.foreignkey = related_model(pk=2)
obj.save()
obj.id

# second approach
obj = myModel.objects.create(field=value, foreignkey_id=2)
```
- ex.
```python
cart = Cart()
cart.save()

item1 = CartItem()
item1.cart = cart
item1.product_id = 1
item1.quantity = 1
item1.save()
```

## Update Object
```python
# first approach
obj = myModel.objects.get(pk=11)
obj.field = newvalue
obj.save()

# second approach-> this updates the field for every record
myModel.objects.update(field=newvalue)

# for specified record
myModel.objects.filter(pk=11).update(field=newvalue)
```

## Delete Object
```python
# single
obj = myModel.objects.get(pk=11) # myModel(pk=2)
obj.delete()

# multiple
myModel.objects.filter(field__gt=5).delete()
```

## Transaction
- run codes atomic, if one fails, changes will be rolled back
```python
def view_func():
    # other codes

    with transaction.atomic():
        obj1 = Model1()
        obj.field = value
        obj.save()
    
        obj2 = Model2()
        obj2.field = value
        obj2.foreign_key = obj1
        obj2.save()

```

## Raw Query
```python
query_set = Model1.objects.raw('SELECT * FROM table')

# Doesnt map to model object, accesess database directly, bypass model layer
cursor = connection.cursor()
cursor.execute('SELECT column FROM table')
cursor.close()

# its gonna close even when exceptions happen
with connection.cursor() as cursor:
    cursor.execute('SELECT column FROM table')

# executing stored procedures
with connection.cursor() as cursor:
    cursor.callproc('get_customer', [param, param2, param3])

```