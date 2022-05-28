from rest_framework import serializers
from .models import AppTransactions, Client, ReportedTransactions

class ClientSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Client
        fields = '__all__'
        
class  AppTransactionsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AppTransactions
        fields = '__all__'

class  ReportedTransactionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ReportedTransactions
        fields = '__all__'