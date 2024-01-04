from django.urls import path

from . import views

urlpatterns = [
    path('', views.base_url, name='base'),  
    path('items/', views.items_index, name='items_index'),
    # old way
    # path('items/create/', views.ItemCreate.as_view(), name='items_create'),
    # new way of views with rest api
    path('items/<int:pk>', views.items_detail, name="items_detail"),
    path('users/', views.users_index, name="users_index"),
    path('users/<int:pk>', views.users_detail, name="users_detail"),
    path('users/<str:username>', views.users_login, name="users_detail"),
    path('users/cart/<int:pk>', views.view_cart, name="view_cart"),
    path('users/editCart/<str:removeOrAdd>/<int:userpk>/<int:itempk>', views.add_to_cart, name="add_to_cart")
]