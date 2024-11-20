from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/transactions/', views.create_transaction, name='create_transaction'),  # For POST request
    path('api/transactions/all/', views.get_transactions, name='get_transactions'), 
    # path('api/transactions/all', views.get_transactions, name='get_transactions'),  # For GET request (user_id query parameter)
    path('api/transactions/<int:transaction_id>/', views.get_transaction, name='get_transaction'),
    path('api/transactions/<int:transaction_id>/update/', views.update_transaction_status, name='update_transaction_status'),
]
