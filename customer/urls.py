from django.urls import path, include
from rest_framework import views

from .views import CustomerCreate, CustomerDelete, CustomerDetail, CustomerList, CustomerUpdate

urlpatterns = [
  path('create', CustomerCreate.as_view(), name='create-customer'),
  path('', CustomerList.as_view(), name='list-customer'),
  path('update/<int:pk>/', CustomerUpdate.as_view(), name='update-customer'),
  path('delete/<int:pk>/', CustomerDelete.as_view(), name='delete-customer')
]