from products.models import *
from rest_framework import serializers
from users.models import *

class UserRegistrationSerializer(serializers.ModelSerializer):
 
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password', 'password2']
        extra_kwargs = {
            'password' : { 'write_only':True }
        }

    
    def save(self, *args, **kwargs):
        password  = self.validated_data.get('password')
        password2 = self.validated_data.get('password2')
        email     = self.validated_data.get('email')
        username  = self.validated_data.get('username')

        if password != password2:
            raise serializers.ValidationError({ "password": "password didn't match."})

        result = CustomUser(email=email, username=username, password=password)
        result.save()
        return result 


        





    
   