import datetime
import json
from django.shortcuts import render
from main.detectionTrainer import getAnormally

from main.forms import UserForm
from main.serializers import AppTransactionsSerializer, ClientSerializer,  ReportedTransactionSerializer
from .models import AppTransactions, ReportedTransactions, ToDoList, Item, Client
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse, HttpResponseRedirect
# import knn algorithm classification libraries
# import matplotlib as pl
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import NearestNeighbors

from django.db.models import Sum


#  an example view
def index(response):

    return render(response, 'main/base.html', {"name": "Desmond"})


@csrf_exempt
def signIn(response):
    print("===> response")
    print(response.body)
    return HttpResponse(json.dumps({"message": "success", "header": "transaction successful", "status": 200}), status=200, content_type="text/plain")


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
        return HttpResponse(json.dumps({"message": "error", "header": "transaction failed", "status": 400}), status=400, content_type="application/json")

    return HttpResponse(json.dumps({"message": "success", "header": "transaction successful", "status": 200}), status=200, content_type="application/json")


@csrf_exempt
def payment(request):
    print("===> requ")
    print(requ.body)
    # add column to user model

    return HttpResponse(json.dumps({"message": "success", "header": "transaction successful", "status": 200}), status=200, content_type="application/json")


@csrf_exempt
def getUser(request):
    # print get request parameers
    print("===> requ")
    data = json.loads(request.body)
    print(data)
    # get user data from database
    try:
        client = Client.objects.get(email=data["email"])
        print(client)
    except Exception as e:
        print(e)
        return HttpResponse(json.dumps({"message": "error", "header": "transaction failed", "status": 400}), status=200, content_type="application/json")
    # serialize the user data
    serializer = ClientSerializer(client)
    #  return the serialized user data with message and header
    return HttpResponse(json.dumps({"message": "success", "header": "transaction successful", "status": 200, "data": serializer.data}), status=200, content_type="application/json")


# admin summary
@csrf_exempt
def adminGetSummary(request):

    users = []
    transactions = []
    reports = []
    try:
        users1 = list(Client.objects.all())
        for user in users1:
            users.append(ClientSerializer(user).data)

        print(users)

        transaction1 = list(AppTransactions.objects.all())
        for transaction in transaction1:
            transactions.append(AppTransactionsSerializer(transaction).data)

        reports1 = list(ReportedTransactions.objects.all())

        for report in reports1:
            reports.append(ReportedTransactionSerializer(report).data)

    except Exception as e:
        print(e)
        return HttpResponse(json.dumps({"message": "error", "header": "transaction failed", "status": 400}), status=200, content_type="application/json")

    # return httpresponse with data on users, transactions, and reports
    return HttpResponse(json.dumps({"message": "success", "header": "transaction successful", "status": 200, "data": {"users": users, "transactions": transactions, "reports": reports}}), status=200, content_type="application/json")


# get transactions for the last 10 days
@csrf_exempt
def getTransactions(request):
    # client email from POST request
    data = json.loads(request.body)
    email = data["email"]
    # get transactions from Apptranscations table where sender_id or receiver_id is equal to the client email
    try:
        transactions = AppTransactions.objects.filter(
            sender_id=email) | AppTransactions.objects.filter(receiver_id=email)
    except Exception as e:
        print(e)
        return HttpResponse(json.dumps({"message": "error", "header": "transaction failed", "status": 400}), status=400, content_type="application/json")
    # serialize the transactions data
    serializer = AppTransactionsSerializer(transactions, many=True)
    #  return the serialized transactions data with message and header
    return HttpResponse(json.dumps({"message": "success", "header": "transaction successful", "status": 200, "data": serializer.data}), status=200, content_type="application/json")


# get account balance
@csrf_exempt
def getBalance(request):
    # client email from POST request
    data = json.loads(request.body)
    email = data["email"]
    # sum amount column from transaction table where receiver_id is equal to the client email
    try:
        deposits = AppTransactions.objects.filter(
            receiver_id=email).aggregate(Sum('amount'))
        # sum amount column from transaction table where sender_id is equal to the client email
        deficites = AppTransactions.objects.filter(
            sender_id=email).aggregate(Sum('amount'))
        finalCompution = (deposits['amount__sum'] or 0) - \
            (deficites['amount__sum'] or 0)
        # return the serialized transactions data with message and header
        return HttpResponse(json.dumps({"message": "success", "header": "transaction successful", "status": 200, "data": finalCompution}), status=200, content_type="application/json")
    except Exception as e:
        print(e)
        return HttpResponse(json.dumps({"message": "error", "header": "transaction failed", "status": 400}), status=200, content_type="application/json")


@csrf_exempt
def getReportedTransactions(request):
    # client email from POST request
    data = json.loads(request.body)
    # verify is specific transaction_id was sent
    if "transaction_id" in data:
        # get specific report from database
        try:
            report = ReportedTransactions.objects.get(
                transaction_id=data["transaction_id"])
        except Exception as e:
            print(e)
            return HttpResponse(json.dumps({"message": "error", "header": "transaction failed", "status": 400}), status=400, content_type="application/json")
        # serialize the report data
        serializer = ReportedTransactionSerializer(report)
        #  return the serialized report data with message and header
        return HttpResponse(json.dumps({"message": "success", "header": "transaction successful", "status": 200, "data": serializer.data}), status=200, content_type="application/json")
    else:
        # get all reports from database
        try:
            reports = ReportedTransactions.objects.all()
        except Exception as e:
            print(e)
            return HttpResponse(json.dumps({"message": "error", "header": "transaction failed", "status": 400}), status=400, content_type="application/json")
        # serialize the report data
        serializer = ReportedTransactionSerializer(reports, many=True)
        #  return the serialized report data with message and header
        return HttpResponse(json.dumps({"message": "success", "header": "transaction successful", "status": 200, "data": serializer.data}), status=200, content_type="application/json")


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
        lng=data["lng"],
        lat=data["lat"],
        time=data["time"],
        month=data["month"],
        day=data["day"],
    )
    # save the transaction object
    transaction.save()
    # return the serialized transaction data with message and header
    return HttpResponse(json.dumps({"message": "success", "header": "transaction successful", "status": 200}), status=200, content_type="application/json")


def machineLearner(request):
    transactions = AppTransactions.objects.all().values(
        "amount", "created_at", "receiver_id", "sender_id", "type", "id")
    # transactions = AppTransactions.objects.all().values("amount","created_at","receiver_id")
    # df = pd.DataFrame(list(transactions))
    # df.add()

    # abnormalIds = getAnormally(df)

    # return response
    return HttpResponse(json.dumps({"message": ""}))

# function calculates


@csrf_exempt
def verifyPossibleAnormally(request):

    transactionData = AppTransactions.objects.all()
    last_id = AppTransactionsSerializer(
        transactionData[len(transactionData)-1])["id"].value+1

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
        lng=data["lng"],
        lat=data["lat"],
        time=data["time"],
        month=data["month"],
        day=data["day"],
        id=last_id
    ).save()

    # where sender_id or receiver_id is equal to the client email
    transactionData = AppTransactions.objects.filter(
        sender_id=data["sender_id"])

    transactions = list(transactionData.values("amount", "created_at", "receiver_id",
                        "sender_id", "lng", "lat", "time", "month", "day", "type", "id"))

    df = pd.DataFrame(list(transactions))

    abnormalIds = []

    try:
        abnormalIds = getAnormally(df)
    except Exception as e:
        print(e)
        AppTransactions.objects.filter(id=last_id).delete()
        return HttpResponse(json.dumps({"message": "error ocurred\n", "header": "transaction failed", "status": 400}), status=400, content_type="application/json")

    print(abnormalIds)
    try:
        if(abnormalIds.count(last_id) > 0):
            AppTransactions.objects.filter(id=last_id).delete()
            return HttpResponse(json.dumps({"message": "This transaction could be a fraud", "header": "transaction suspicious", "status": 205, "data": {"safe": False}}), status=200, content_type="application/json")
    except:
        print("error getting index")

    return HttpResponse(json.dumps({"message": "success", "header": "transaction successful", "status": 200, "data": {"safe": True}}))


@csrf_exempt
def getAnormalData(request):

    # get email from request
    data = json.loads(request.body)
    email = data["email"]

    transactionData = AppTransactions.objects.filter(sender_id=email)

    transactions = list(transactionData.values("amount", "created_at",
                        "receiver_id", "sender_id", "lng", "lat", "time", "month", "day", "id"))

    df = pd.DataFrame(list(transactions))

    abnormalIds = getAnormally(df)

    # get transactions with ids in abnormalIds list
    transactions = AppTransactions.objects.filter(id__in=abnormalIds)
    # serialize the transactions data
    serializer = AppTransactionsSerializer(transactions, many=True)
    #  return the serialized transactions data with message and header
    return HttpResponse(json.dumps({"message": "success", "header": "transaction successful", "status": 200, "data": serializer.data}), status=200, content_type="application/json")


# record a transaction to database
@csrf_exempt
def reportTransaction(request):
    # client email from POST request
    data = json.loads(request.body)

    # create a new transaction report
    report = ReportedTransactions(
        amount=data["amount"],
        created_at=data["created_at"],
        reported_at=data["reported_at"],
        reporter=data["reporter"],
        reported=data["reported"],
        type=data["type"],
        lng=data["lng"],
        lat=data["lat"],
        transaction_id=data["transaction_id"],
    )
    # save the report object
    report.save()
    # return the serialized transaction data with message and header
    return HttpResponse(json.dumps({"message": "success", "header": "Reported successfully", "status": 200}), status=200, content_type="application/json")
