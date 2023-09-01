from django.shortcuts import render
from base.serializers import UrlSerializer,TodoSerializer
# Create your views here.
from .models import Url,Todo
from rest_framework.views import  APIView
from rest_framework.response import Response
from rest_framework import status


class UrlView(APIView):
    
    def post(self,request):
        data = request.data;
        serializer = UrlSerializer(data=data)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.data)
    

class TodoAll(APIView):
    def get(self,request):
        objs = Todo.objects.all()
        serialiser = TodoSerializer(objs,many=True)
        return Response(serialiser.data)
    
    def post(self,request):
        # objs = Todo.objects.all()
        data = request.data 
        serialiser = TodoSerializer(data=data)
        if serialiser.is_valid():
            serialiser.save()
            
            return Response(serialiser.data)
        return Response(serialiser.errors)       
        
     

class TodoView(APIView):
    
   
    def get(self,request,t_id):
        try:
            objs = Todo.objects.get(id=t_id)
            serialiser = TodoSerializer(objs,many=False)
            return Response(serialiser.data)
        except Todo.DoesNotExist:
             return Response({"message": f"Todo with ID {t_id} does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        
       
    def patch(self,request,t_id):
        data  = request.data
        objs = Todo.objects.get(id=t_id)
        serialiser = TodoSerializer(objs,data=data,partial=True) 
        if serialiser.is_valid():
            serialiser.save()
            return Response(serialiser.data)
        return Response(serialiser.errors)
    
    def delete(self,request,t_id):
        data = request.data
        objs = Todo.objects.get(id=t_id)
        objs.delete()
        return Response({'Message':"Todo Deleted Successfully"})
