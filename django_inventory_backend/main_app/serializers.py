from rest_framework import serializers
from .models import Item, Profile
# from django.contrib.auth.models import User

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

# to move to Django User model, fix this to include all predefined Django user fields as seen on lines 8-14 and do include profile line as well
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