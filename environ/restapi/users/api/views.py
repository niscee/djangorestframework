from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from users.api.serializers import UserRegistrationSerializer
from users.models import *


@api_view(['GET'])
def index(request):
    api_urls = {
        'login': 'api/login/',
        'register': 'api/register',
    }
    return Response(api_urls)



@api_view(['POST'])
def register(request):
    
    if request.method == "POST":
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Registered Successfully!!"})
        else:
            data = serializer.errors
            return Response(data)    
