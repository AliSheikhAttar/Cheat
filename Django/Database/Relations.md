# Relations
## one to one relation
> models.oneToone
> parent = customer (customer should exists before adddress), child = address
> create foreign key in child
> on_delete (how to react to deletion of parent(customer)):
>  CASCADE => delete child , SET_NULL => set customer field in address null,
> SET_DEFAULT => customer field set to default value, PROTECT => first child should be deleted
> primary key = true => prevent duplicate address for one customer (because django would create id primary key)
> django will automatically create reverse relationship in parent

## one to many relation
> models.ForeignKey
> remove primary_key = true => allow duplicate values for customer column
> if parent class not defined above child just put the parent class in string

## many to many relation
> models.ManyToManyField
> related_name => the name used to create reverse relation in other model

## Circular
> models.ForeignKey('namce of dependant class', related_name=(X))
> X = anything other than the name other class already using for relationship or '+' => tells django dont create
reverse relationship in other class

## Generic relation
### taged items
```python
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Tag(models.Model):
    label = models.CharField(max_length=255)

class TaggedItem(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE) # which table
    object_id = models.PositiveIntegerField() # which record (only tables with positive int primary key)
    content_object = GenericForeignKey() # actual object 
```
###  user likes
```python
from django.contrib.auth.models import User

class LikedItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # foreign key to user class defined in django for auth
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
```
