from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import  Response
from rest_framework import authentication,permissions


from turf_management.models import Turf
from turf_management.serializers import TurfSerializer 

# Create your views here.

class TurfListCreateView(APIView):

    authentication_classes= [authentication.BasicAuthentication] # basic authentication
    permission_classes=[permissions.IsAdminUser] #  permission for admin

    def get(self,request):
        qs= Turf.objects.all()
        serializer_instance= TurfSerializer(qs,many=True) #conversion of QS --> PYNT
        return Response(serializer_instance.data)

    def post(self,request):
        form_data=request.data
        serializer_instance=TurfSerializer(data=form_data) # conversion from PYNT --> QS
        if serializer_instance.is_valid():
            # cleaned_data= serializer_instance.validated_data
            # Turf.objects.create(**cleaned_data)

            serializer_instance.save() # will call create() method in serializers

            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)

class TurfRetrieveUpdateDeleteView(APIView):

    authentication_classes= [authentication.BasicAuthentication] # basic authentication
    permission_classes=[permissions.IsAdminUser] #  permission for admin

    def get(self,request,pk=None):
        qs=Turf.objects.get(id=pk)
        serializer_instance=TurfSerializer(qs)
        return Response(serializer_instance.data)

    def put(self,request,pk=None):
        form_data=request.data

        turf_object= Turf.objects.get(id=pk)

        serializer_instance= TurfSerializer(data=form_data,instance=turf_object)
        if serializer_instance.is_valid():
            # cleaned_data=serializer_instance.validated_data
            # Turf.objects.filter(id=pk).update(**cleaned_data)

            serializer_instance.save() # will call update()

            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)

    def delete(self,request,pk=None):
        Turf.objects.filter(id=pk).delete()
        response_data={"message":"deleted"}
        return Response(response_data)
    
