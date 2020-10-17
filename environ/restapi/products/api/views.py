from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import Author
from products.api.serializers import AuthorSerializer
from products.models import *

@api_view(['GET'])
def index(request):
    api_urls = {
        'list': 'products/api/list/',
        'detail': 'products/api/detail/<int:pk>',
        'create': 'products/api/create/',
        'update': 'products/api/udpate/<int:pk>',
        'delete': 'products/api/delete/<int:pk>',
    }
    return Response(api_urls)


@api_view(['GET'])
def productList(request):
    categories = Author.objects.all()

    """ 
    many=True by setting many=True you tell drf that queryset contains mutiple items (a list of items) 
    so drf needs to serialize each item with serializer class (and serializer.
    data will be a list). 
    """ 

    results = AuthorSerializer(categories, many=True)
    return Response(results.data)


@api_view(['GET'])
def productDetail(request, pk):
    try:
        categories = Author.objects.get(id=pk)
        results = AuthorSerializer(categories)
        return Response(results.data)

    except:    
        return Response({"message": "Id Not Found"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def productCreate(request):
    serializer = AuthorSerializer(data=request.data)
    if serializer.is_valid():
       serializer.save()

    return Response({"message": "New Data Inserted Succesfully!!"})



@api_view(['DELETE'])
def productDelete(request, pk):
    try:
        categories = Author.objects.get(id=pk)
        categories.delete()
        return Response({"message": "Deleted Succesfully!!"})

    except:    
        return Response({"message": "Id Not Found"}, status=status.HTTP_404_NOT_FOUND)

    

@api_view(['PUT'])
def productUpdate(request, pk):
    try:
        categories = Author.objects.get(id=pk)
        serializer = AuthorSerializer(data=request.data, instance=categories)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    except:    
        return Response({"message": "Id Not Found"}, status=status.HTTP_404_NOT_FOUND)

    