from math import perm
from django.shortcuts import render
from .models import User
from rest_framework import viewsets
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import action
from book.models import Book
from book.serializers import BookSerializer
from rest_framework.response import Response
from rest_framework import status
from library.models import BookItem
from book.models import Book

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [] 

    def get_permissions(self):
        if self.action == "create":
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsOwnerOrReadOnly]
        
        return [permission() for permission in permission_classes]
    
    @action(detail=True)
    def my_boks(self, request, pk=None):
        queryset = Book.objects.filter(
            owner__id = pk
        )
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(detail=True)
    def my_books_rented(self, request, pk=None):
        queryset = BookItem.objects.filter(
            book__owner__id=pk
        ).values_list("book__id", flat=True)
        books = Book.objects.filter(
            id__in=queryset
        )
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)