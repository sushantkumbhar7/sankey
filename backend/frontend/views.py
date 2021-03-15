from .models import registration,addfurniture
from .serializers import registerSerializer,showSerializer,addfurnitureSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import HttpResponse
from rest_framework.response import Response
from django.http import JsonResponse
@api_view(['POST'])
def signup(request):
    if request.method=='POST':
        serializer = registerSerializer(registration(),request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response({'status':200})
        return Response({'Data Is Not Accepted':406,'error':serializer.errors})   
          
    

@api_view(['GET'])
def Show_data(request):
    if request.method=='GET':
        ress=registration.objects.all()
        print(ress)
        serializer=showSerializer(ress,many=True)
        return Response({'status':200,'Details':serializer.data})
    

@api_view(['POST'])
def login(request):
    try:
        email=request.data['email']
        password=request.data['password']
        store=registration.objects.get(email=email,password=password)
        serializer=registerSerializer(store,many=False)
        return Response({'status':202,'Data':serializer.data})
    except:
        return Response({'Enter Valid Credentials':401})



@api_view(['POST'])
def addf(request):
    if request.method=='POST':
        serializer = addfurnitureSerializer(addfurniture(),request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response({'status':202})
 
        return Response({'Data Is Not Accepted':406,'error':serializer.errors})  

@api_view(['GET'])
def Show_fur(request):
    if request.method=='GET':
        ress=addfurniture.objects.all()
        print(ress)
        serializer=addfurnitureSerializer(ress,many=True)
        return Response({'status':200,'Details':serializer.data})