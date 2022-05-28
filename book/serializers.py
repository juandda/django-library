import imp
from rest_framework import serializers
from .models import Book
from core.serializers import UserSerializer

class BookSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    class Meta:
        model = Book
        fields = "all"
        depth = 1