from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class Credential_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Credentials
        fields="__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password']
        
           
            

        
