from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *
from django.contrib.auth.models import User



class Register(APIView):
    
    def post(self,request):
        user_data=request.data.get("user_data",{})
        cred_data=request.data.get("credential",{})
        user_serializer=UserSerializer(data=user_data)
        if user_serializer.is_valid():
           user_instance=user_serializer.save()
           cred_data['user']=user_instance.id
           cred_seiralizer=Credential_Serializer(data=cred_data)
           if cred_seiralizer.is_valid():
                cred_seiralizer.save()
                return Response("data added successfully")
           else:
                return Response(cred_seiralizer.errors)
               
        else:

            return Response(user_serializer.errors)
        
    