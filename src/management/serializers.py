from django.db import models
from rest_framework import serializers
from rest_framework import fields
from rest_framework.fields import CreateOnlyDefault

from accounts.serializers import UserSerializer
from accounts.models import User

from .models import Catalogue, Book



class CatalogueSerializer(serializers.ModelSerializer):
    # user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset = User.objects.all())

    class Meta:
        model = Catalogue
        fields = ['id', 'name', 'description', 'created', 'user_id']

    def create(self, validated_data):
        user_id = validated_data.pop('user_id')
        user = User.objects.get(id=user_id)
        catalogue = Catalogue.objects.create(user=user, **validated_data)
        return catalogue



class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'name', 'description', 'created','catalogue_id' 'user']
    
    # def create(self, validated_data):
    #     book = Book(**validated_data)
    #     book.save()
    #     return book
