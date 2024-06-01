from django.db.models.aggregates import Count
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Collection, Product
from .serializers import CollectionSerializer, ProductSerializer


@api_view(['GET', 'POST']) 
def product_list(request): #request will be instance of request in Django rest
    if request.method == 'GET':
        queryset = Product.objects.select_related('collection').all() #also load colloction model as related with foreign key for better performance
        serializer = ProductSerializer(
            queryset, many=True, context={'request': request}) #many=true => multi objects as input, context = ...=> for hyperlinkedrelatedfiled because request contains info about urls
        return Response(serializer.data)#retrieve serialized data
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)#by passing the data as data parameter, it deserialize it
        serializer.is_valid(raise_exception=True)#should be validated before save, validation in model fields not object-level
        serializer.save()#save the serialize.data into database
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])#PUT = update partialy
def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)#equal to try and expect with returning 404 error
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)#passing product instance, it update the data
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        if product.orderitems.count() > 0:#other models related to this model using foreign key
            return Response({'error': 'Product cannot be deleted because it is associated with an order item.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)#body of error message
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def collection_list(request):
    if request.method == 'GET':
        queryset = Collection.objects.annotate(products_count=Count('products')).all()#assign the related name to result
        serializer = CollectionSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CollectionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def collection_detail(request, pk):
    collection = get_object_or_404(
        Collection.objects.annotate(
            products_count=Count('products')), pk=pk) # annotate add fields to the model existing fields, the new field for each collection object is product_count which is count of products referenced to the collection object
    if request.method == 'GET': #get object
        serializer = CollectionSerializer(collection)
        return Response(serializer.data)
    elif request.method == 'PUT': #update object
        serializer = CollectionSerializer(collection, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE': #delete object
        if collection.products.count() > 0:
            return Response({'error': 'Collection cannot be deleted because it includes one or more products.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view()
def collection_detail(request, pk):#for hyperlink to related colloction object
    return Response('ok')