from customers.models import Customer
from django.http import JsonResponse
from customers.serializers import CustomerSerializer

def customers(request):
  data = Customer.objects.all()
  serializer = CustomerSerializer(data, many=True)
  #get serialized version, passing json compatible data as response
  return JsonResponse({"customers": serializer.data})


def customer(request, id):
  data = Customer.objects.get(pk=id)
  serializer = CustomerSerializer(data)
  #get serialized version, passing json compatible data as response
  return JsonResponse({"customer": serializer.data})