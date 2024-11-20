from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Transaction
from .serializers import TransactionSerializer
from django.http import HttpResponse

# Home view, returns a simple HTTP response as a welcome message
def home(request):
    return HttpResponse("Welcome to the Transaction Management System!")

# Create a new transaction using POST request
@api_view(['POST'])
def create_transaction(request):
    if request.method == 'POST':
        # Validate the incoming data using the TransactionSerializer
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            # If data is valid, save the transaction to the database
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Return created transaction data
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return error if validation fails

# Get all transactions for a specific user using GET request
@api_view(['GET'])
def get_transactions(request):
    # Check if 'user_id' is provided in query parameters
    if 'user_id' in request.query_params:
        user_id = request.query_params['user_id']
        # Fetch transactions from the database for the specified user
        transactions = Transaction.objects.filter(user_id=user_id)
        # Serialize the transaction data
        serializer = TransactionSerializer(transactions, many=True)
        return Response({'transactions': serializer.data})  # Return the serialized transaction data
    return Response({'error': 'user_id is required'}, status=status.HTTP_400_BAD_REQUEST)  # Return error if 'user_id' is not found

# Get a specific transaction by its ID using GET request
@api_view(['GET'])
def get_transaction(request, transaction_id):
    try:
        # Fetch the transaction by its ID
        transaction = Transaction.objects.get(id=transaction_id)
    except Transaction.DoesNotExist:
        # If the transaction is not found, return a 404 error
        return Response({'error': 'Transaction not found'}, status=status.HTTP_404_NOT_FOUND)

    # Serialize and return the transaction data
    serializer = TransactionSerializer(transaction)
    return Response(serializer.data)

# Update the status of an existing transaction using PUT request
@api_view(['PUT'])
def update_transaction_status(request, transaction_id):
    try:
        # Fetch the transaction by its ID
        transaction = Transaction.objects.get(id=transaction_id)
    except Transaction.DoesNotExist:
        # If the transaction is not found, return a 404 error
        return Response({'error': 'Transaction not found'}, status=status.HTTP_404_NOT_FOUND)

    # Check if the 'status' is provided in the request data
    if 'status' in request.data:
        transaction.status = request.data['status']  # Update the status of the transaction
        transaction.save()  # Save the changes to the database
        # Serialize and return the updated transaction data
        serializer = TransactionSerializer(transaction)
        return Response(serializer.data)
    # If 'status' is not provided, return an error
    return Response({'error': 'status is required'}, status=status.HTTP_400_BAD_REQUEST)
