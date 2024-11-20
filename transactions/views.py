from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Transaction
from .serializers import TransactionSerializer

from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Transaction Management System!")

@api_view(['POST'])
def create_transaction(request):
    if request.method == 'POST':
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_transactions(request):
    if 'user_id' in request.query_params:  # Checking if 'user_id' is passed in query params
        user_id = request.query_params['user_id']
        transactions = Transaction.objects.filter(user_id=user_id)  # Filtering transactions by user_id
        serializer = TransactionSerializer(transactions, many=True)  # Serializing the filtered transactions
        return Response({'transactions': serializer.data})  # Returning the serialized data in the response
    return Response({'error': 'user_id is required'}, status=status.HTTP_400_BAD_REQUEST)  # If 'user_id' is not found, return an error

@api_view(['GET'])
def get_transaction(request, transaction_id):
    try:
        transaction = Transaction.objects.get(id=transaction_id)
    except Transaction.DoesNotExist:
        return Response({'error': 'Transaction not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = TransactionSerializer(transaction)
    return Response(serializer.data)

@api_view(['PUT'])
def update_transaction_status(request, transaction_id):
    try:
        transaction = Transaction.objects.get(id=transaction_id)
    except Transaction.DoesNotExist:
        return Response({'error': 'Transaction not found'}, status=status.HTTP_404_NOT_FOUND)

    if 'status' in request.data:
        transaction.status = request.data['status']
        transaction.save()
        serializer = TransactionSerializer(transaction)
        return Response(serializer.data)
    return Response({'error': 'status is required'}, status=status.HTTP_400_BAD_REQUEST)
