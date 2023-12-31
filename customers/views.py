from customers.models import Customer
from django.http import JsonResponse
from customers.serializers import CustomerSerializer

def customers(request):
  #invoking serializer and returning client
  data = Customer.objects.all()
  serializer = CustomerSerializer(data, many=True)
  #get serialized version, passing json compatible data as response
  return JsonResponse({"customers": serializer.data})