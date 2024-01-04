import graphene
from graphene_django import DjangoObjectType

from customers.models import Customer, Order

class CustomerType(DjangoObjectType):
  class Meta:
    model = Customer
    fields = "__all__"

class OrderType(DjangoObjectType):
  class Meta:
    model = Order
    fields = "__all__"

class CreateCustomer(graphene.Mutation):
  #data expected in order to create a new customer
  class Arguments:
    name = graphene.String()
    industry = graphene.String()

  #field
  customer = graphene.Field(CustomerType)

  #functions paired with field
  def mutate(root, info, name, industry):
    #define customer object and save to db
    customer = Customer(name=name, industry=industry)
    customer.save()
    return CreateCustomer(customer=customer)


class Query(graphene.ObjectType):
  customers = graphene.List(CustomerType)
  orders = graphene.List(OrderType)

  customer_by_name = graphene.List(CustomerType, name=graphene.String(required=True))

  def resolve_customers(root, info):
    return Customer.objects.all()
  
  def resolve_orders(root, info):
    #get all orders related to customer
    return Order.objects.select_related("customer").all()

  #get a single element by name
  def resolve_customer_by_name(root, info, name):
    try:
      return Customer.objects.filter(name=name)
    except Customer.DoesNotExist:
      return None 


#crud operations
class Mutations(graphene.ObjectType):
  createCustomer = CreateCustomer.Field()

schema = graphene.Schema(query=Query, mutation=Mutations)