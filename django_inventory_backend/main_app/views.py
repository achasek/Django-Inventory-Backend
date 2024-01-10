from django.http import HttpResponse
from .models import Item, Profile
from django.contrib.auth.models import User
from .serializers import ItemSerializer, ProfileSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


def base_url(request):
    return HttpResponse("This is the base url for the entire server -- delete later")

# @csrf_exempt

@api_view(['GET', 'POST'])
def items_index(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    # WHEN MAKING POST REQS, MUST ADD TRAILING BACKSLASH
    # I.E. /items/
    elif request.method == 'POST':
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def items_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        item = Item.objects.get(pk=pk)
    except Item.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ItemSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def users_index(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        users = Profile.objects.all()
        serializer = ProfileSerializer(users, many=True)
        return Response(serializer.data)

    # WHEN MAKING POST REQS, MUST ADD TRAILING BACKSLASH
    # I.E. /users/
    elif request.method == 'POST':
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def users_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        user = Profile.objects.get(pk=pk)
    except Profile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProfileSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProfileSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def users_login(request, username):
    try:
        user = Profile.objects.get(username=username)
    except Profile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProfileSerializer(user)
        return Response(serializer.data)

@api_view(['GET', 'PUT'])    
def view_cart(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        user = Profile.objects.get(pk=pk)
    except Profile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # user = user.items.prefetch_related("cart")
        user_items = user.items.all()
        serializer = ProfileSerializer(user, context={'request': request})
        return Response(serializer.data)
        # serializer = ProfileSerializer(user, many=True)
    
    
    # elif request.method == 'PUT':
    #     serializer = ProfileSerializer(user, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])        
def edit_cart(request, removeOrAdd,userpk, itempk):
    try:
        profile = Profile.objects.get(pk=userpk)
        item = Item.objects.get(pk=itempk)
    except Profile.DoesNotExist:
        return Response("Profile cannot be found", status=status.HTTP_404_NOT_FOUND)
    except Item.DoesNotExist:
        return Response("Item cannot be found", status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'PUT':
        if removeOrAdd == "add":
            profile.items.add(item)
            profile.save()
            return Response("Successfully added to cart", status=status.HTTP_202_ACCEPTED)
        else:
            profile.items.remove(item)
            profile.save()
            return Response("Successfully removed from cart", status=status.HTTP_202_ACCEPTED)
        # serializer = ProfileSerializer(profile, data=request.data)
        # if serializer.is_valid():
        #     # print(serializer.data.items, "---------------------------------------")
        #     # profile.items.add(item)
        #     serializer.save()
        #     return Response(serializer.data)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)