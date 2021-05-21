from .models import Customer
from rest_framework import generics, serializers
from .serializers import CustomerSerializer

class CustomerCreate(generics.CreateAPIView):
  # Api endpoint that allows creation of new customer
  queryset = Customer.objects.all()
  serializer_class = CustomerSerializer

class CustomerList(generics.ListAPIView):
  # Api endpoint that allows customer to be viewed. 
  queryset = Customer.objects.all()
  serializer_class = CustomerSerializer

class CustomerDetail(generics.RetrieveAPIView):
  # Api endpoint that returns a single customer by pk.
  queryset = Customer.objects.all()
  serializer_class = CustomerSerializer

class CustomerUpdate(generics.RetrieveUpdateAPIView):
  queryset = Customer.objects.all()
  serializer_class = CustomerSerializer

class CustomerDelete(generics.RetrieveDestroyAPIView):
  queryset = Customer.objects.all()
  serializer_class = CustomerSerializer