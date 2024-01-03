from customers.models import Customer
from django.http import JsonResponse, Http404
from customers.serializers import CustomerSerializer, UserSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken


#DEFINFING: an api that can take get, post requests using API decorator
@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def customers(request):
  if request.method == "GET":
    data = Customer.objects.all()
    serializer = CustomerSerializer(data, many=True)
    #get serialized version, passing json compatible data as response
    return Response({"customers": serializer.data})
  
  #creating a new customer
  elif request.method == "POST":
    serializer = CustomerSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response({"customer": serializer.data}, status=status.HTTP_201_CREATED)
    
    #if serializer is not valid
    return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


#DEFINFING: an api that can take get, post, delete requests using API decorator
@api_view(["GET", "POST", "DELETE"])
@permission_classes([IsAuthenticated])
def customer(request, id):
  try:
    data = Customer.objects.get(pk=id)
  except Customer.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  #check complete
  if request.method == "GET":
    serializer = CustomerSerializer(data)
    #get serialized version, passing json compatible data as response
    return Response({"customer": serializer.data}, status=status.HTTP_200_OK)
  
  elif request.method == "DELETE":
    data.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  
  #UPDATING customer
  elif request.method == "POST":
    serializer = CustomerSerializer(data, data=request.data)

    #quality check to ensure serialisation is valid
    if serializer.is_valid():
      serializer.save()
      return Response({"customer":serializer.data})
    
    # not serializedsomething that was sent is bad
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def register(request):
  serializer = UserSerializer(data=request.data)
  if serializer.is_valid():
    # creating refresh and access tokens for when user registers
    user = serializer.save()
    refresh = RefreshToken.for_user(user)
    tokens = {
      "refresh": str(refresh),
      "access": str(refresh.access_token)
    }
    return Response(tokens, status=status.HTTP_201_CREATED)
  
  #if serializer not valid
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)