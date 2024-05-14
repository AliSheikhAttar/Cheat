from decimal import Decimal
from store.models import Product, Collection
from rest_framework import serializers


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:#instead of defining each field again (inheriting ModelSerializer instead of Serializer)
        model = Collection
        fields = ['id', 'title', 'products_count']#if not exists here look in body of the class, '__all__' for all, dont expose the database by interface

    products_count = serializers.IntegerField()

 

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'slug', 'inventory', 'unit_price', 'price_with_tax', 'collection']

    price_with_tax = serializers.SerializerMethodField(
        method_name='calculate_tax')

    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)
    
    def validate(self, data):#overwriting validate function
        if data['password'] != data['confirmed_pass']:
            return serializers.ValidationError('passwords don\'t match')
        return data#return either error or data

    #Serializers relation
    #1 primary key
    Collection = serializers.PrimaryKeyRelatedField(
        query_set = Collection.objects.all())
    #2 str
    Collection = serializers.StringRelatedField()
    #3 nested (object)
    Collection = CollectionSerializer()
    #4 hyperlink
    Collection = serializers.HyperlinkedRelatedField(
        query_set = Collection.objects.all(),
        view_name='collection-detail' #name for its specific url 
    )