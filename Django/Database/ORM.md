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
```

## sorting
```python
# sort on field ascending
query_set = OrderItem.objects.order_by('price')
# sort on field descending
query_set = OrderItem.objects.order_by('-price')
# sort on multiple fields
query_set = OrderItem.objects.order_by('unit_price', '-price')
# reverse the ordering => first descending , second ascending
query_set = OrderItem.objects.order_by('unit_price', '-price').reverse()

# earliest
query_set = OrderItem.objects.order_by('unit_price')[0]
# Equal
query_set = OrderItem.objects.earliest('unit_price')

# latest
query_set = OrderItem.objects.order_by('-unit_price')[0]
# Equal
query_set = OrderItem.objects.latest('unit_price')
```

## limit
```python
LIMIT = 5
query_set = OrderItem.objects.order_by('price')[:LIMIT]
```

## Selection
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
### ordered products
```python
query_set = orderItem.objects.values('product_id').distinct() # it doesnt have product_id => creates it and set it as foreign key to product, same as product__id
# answer
query_set = Product.objects.filter(
        id__in=orderItem.objects.values('product_id').distinct()).order_by('title')# id field in ...

```
