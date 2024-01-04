from rest_framework import serializers
from .models import Item, Profile
from django.contrib.auth.models import User

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         fields = (
#             'id',
#             'username',
#             'password',
#             'email',
#             'first_name',
#             'last_name',
#             'profile'
#         )
#         model = User

class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'id',
            'name',
            'price',
            'description',
            'category',
            'image'
        )
        model = Item

class ProfileSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = (
            'id',
            'username',
            'password',
            'items'
        )