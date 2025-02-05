from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import IndividualItems
from .serializers import IndividualItemSerializer, ItemTypeSerializer, ShoppingListSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the sample index.")
# Create your views here.

@api_view(['PUT'])
def add_item(request):
    serializer = IndividualItemSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Item added successfully"}, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def new_type(request):
    serializer = ItemTypeSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Item added successfully"}, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def add_to_shoppinglist(request):
    serializer = ShoppingListSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Item added successfully"}, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

