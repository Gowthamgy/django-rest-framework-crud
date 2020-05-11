# from rest_framework import viewsets
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from .serializers import ArticleSerializer
from .models import Hero


@api_view(['GET'])
def apioverview(request):
    api_urls = {
        'List':'/list/',
        'Detail':'/detail/<str-pk>/',
        'create':'/create/',
        'update':'/update/<str:pk>/',
        'delete':'/delete/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def taskList(request):
    tasks = Hero.objects.all()
    serializer = ArticleSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request, pk):
    tasks = Hero.objects.get(id=pk)
    serializer = ArticleSerializer(tasks, many=False)
   
    return Response(serializer.data)
 
    

@api_view(['POST'])
def taskcreate(request):
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def taskupdate(request,pk):
    tasks = Hero.objects.get(id=pk)
    serializer = ArticleSerializer(instance=tasks ,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def taskdelete(request,pk):
    tasks = Hero.objects.get(id=pk)
    tasks.delete()
    return Response("Item sucessful delete")