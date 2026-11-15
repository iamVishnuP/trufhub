from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.serializers import AdminSerializer,UserSerializer
# Create your views here.

class AdminCreateView(APIView):

    def post(self,request):

        form_data=request.data

        serializer_instance= AdminSerializer(data=form_data)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(serializer_instance.data)

        else:

            return Response(serializer_instance.errors)


class UserCreateView(APIView):

    def post(self,request):
        form_data=request.data
        serilaizer_instance= UserSerializer(data=form_data)
        if serilaizer_instance.is_valid():
            serilaizer_instance.save()
            return Response(serilaizer_instance.data)
        else:
            return Response(serilaizer_instance.errors)


