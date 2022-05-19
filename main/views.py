import datetime
import json
from django.shortcuts import render

from main.forms import UserForm
from main.serializers import AppTransactionsSerializer, ClientSerializer
from .models import AppTransactions, ToDoList, Item, Client
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse, HttpResponseRedirect 
# import knn algorithm classification libraries
# import matplotlib as pl
# import numpy as np
from django.db.models import Sum
 


#  an example view
def index(response): 
     
    return render(response, 'main/base.html',{"name":"Desmond"})

@csrf_exempt 
def signIn(response):
    print("===> response")
    print(response.body)
    return HttpResponse(json.dumps({"message":"success", "header":"transaction successful", "status":200}), status=200, content_type="text/plain")

 
@csrf_exempt 
def signUp(response):
    print("===> response")
    print(response.body)
    try:
        data = json.loads(response.body)
        # deserialize the json data as client object
        client = Client(
            name=data["name"],
            email=data["email"],
            password=data["password"],
            created_at=datetime.datetime.now(),
            id_front=data["id_front"],
            id_back=data["id_back"],
            phone=data["phone"],
            lat=data["lat"],
            lng=data["lng"],
            city=data["city"],
            country=data["country"],
            photo=data["photo"]
        )
    #  save client data
        client.save()
    except Exception as e:
        print(e)
        return HttpResponse(json.dumps({"message":"error", "header":"transaction failed", "status":400}), status=400, content_type="application/json")

    return HttpResponse(json.dumps({"message":"success", "header":"transaction successful", "status":200}), status=200, content_type="application/json")


@csrf_exempt 
def payment(request):
    print("===> requ")
    print(requ.body)
    # add column to user model
    
    return HttpResponse(json.dumps({"message":"success", "header":"transaction successful", "status":200}), status=200, content_type="application/json")


@csrf_exempt 
def getUser(request):
    # print get request parameers
    print("===> requ")
    data = json.loads(request.body)
    # get user data from database
    try:
        client = Client.objects.get(email=data["email"])
        print(client)
    except Exception as e:
        print(e)
        return HttpResponse(json.dumps({"message":"error", "header":"transaction failed", "status":400}), status=400, content_type="application/json")
    # serialize the user data
    serializer = ClientSerializer(client)
    #  return the serialized user data with message and header
    return HttpResponse(json.dumps({"message":"success", "header":"transaction successful", "status":200, "data":serializer.data}), status=200, content_type="application/json")
   

# get transactions for the last 10 days
@csrf_exempt
def getTransactions(request):
    # client email from POST request
    data = json.loads(request.body)
    email = data["email"]
    # get transactions from Apptranscations table where sender_id or receiver_id is equal to the client email
    try:
        transactions = AppTransactions.objects.filter(sender_id=email) | AppTransactions.objects.filter(receiver_id=email)
    except Exception as e:
        print(e)
        return HttpResponse(json.dumps({"message":"error", "header":"transaction failed", "status":400}), status=400, content_type="application/json")
    # serialize the transactions data
    serializer = AppTransactionsSerializer(transactions, many=True)
    #  return the serialized transactions data with message and header
    return HttpResponse(json.dumps({"message":"success", "header":"transaction successful", "status":200, "data":serializer.data}), status=200, content_type="application/json")


# get account balance
@csrf_exempt
def getBalance(request):
    # client email from POST request
    data = json.loads(request.body)
    email = data["email"]
    # sum amount column from transaction table where receiver_id is equal to the client email
    try:
        deposits = AppTransactions.objects.filter(receiver_id=email).aggregate(Sum('amount'))
        # sum amount column from transaction table where sender_id is equal to the client email
        deficites = AppTransactions.objects.filter(sender_id=email).aggregate(Sum('amount'))
        finalCompution= (deposits['amount__sum'] or 0) -( deficites['amount__sum'] or 0)
        # return the serialized transactions data with message and header
        return HttpResponse(json.dumps({"message":"success", "header":"transaction successful", "status":200, "data":finalCompution}), status=200, content_type="application/json")
    except Exception as e:
        print(e)
        return HttpResponse(json.dumps({"message":"error", "header":"transaction failed", "status":400}), status=200, content_type="application/json")
    
   


# record a transaction to database
@csrf_exempt
def recordTransaction(request):
    # client email from POST request
    data = json.loads(request.body)
    
    # create a new transaction object
    transaction = AppTransactions(
        sender_id=data["sender_id"],
        receiver_id=data["receiver_id"],
        amount=data["amount"],
        created_at=data["created_at"],
        ref=data["ref"],
        type=data["type"],
        category=data["category"],
        sender_photo=data["sender_photo"],
        receiver_photo=data["receiver_photo"],
        sender_name=data["sender_name"],
        receiver_name=data["receiver_name"], 
         )
    # save the transaction object
    transaction.save()
    # return the serialized transaction data with message and header
    return HttpResponse(json.dumps({"message":"success", "header":"transaction successful", "status":200}), status=200, content_type="application/json")
