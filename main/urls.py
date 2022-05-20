from unicodedata import name
from django.urls import path


from . import views


urlpatterns=[
    path('', views.index, name='index'), 
    path("api/sign_up/", views.signUp, name="home"),
    path("api/sign_in/",  views.signIn, name="processRequest"),
    path("api/payment/",  views.payment, name="payment"),
    path("api/user/",  views.getUser, name="getUser"),
    path("api/transactions/",  views.getTransactions, name="transactions"),
    path("api/balance/",  views.getBalance, name="balance"),
    path("api/record-transaction/",  views.recordTransaction, name="recordTransaction"),
    path("api/ml", views.machineLearner, name="ml"),
    path("api/record-transaction/detect", views.verifyPossibleAnormally, name="transact-detect")
    

]