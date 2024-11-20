# Transaction Management API

## Introduction
This is a simple API to manage financial transactions using Django and Django REST Framework (DRF). It supports basic operations such as creating, viewing, and updating transactions.

## Setup Instructions

### Install Dependencies
1. First, ensure that you have Python and pip installed on your system.
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Set up the Database
- Configure the database in `settings.py` under the `DATABASES` section (default is SQLite).
- Run migrations to set up the database tables:

```bash
python manage.py migrate
```

### Run the Development Server
- Start the development server:

```bash
python manage.py runserver
```

Now the API should be running at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## API Endpoints

### 1. Create Transaction
- **URL**: `/transactions/`
- **Method**: `POST`
- **Request Body**:
```json
{
  "amount": 100.50,
  "description": "Payment for services",
  "status": "pending",
  "user": 1
}
```
- **Response**:
```json
{
  "id": 1,
  "amount": 100.50,
  "description": "Payment for services",
  "status": "pending",
  "user": 1,
  "created_at": "2024-11-21T12:00:00Z"
}
```

### 2. Get All Transactions
- **URL**: `/transactions/`
- **Method**: `GET`
- **Response**:
```json
[
  {
    "id": 1,
    "amount": 100.50,
    "description": "Payment for services",
    "status": "pending",
    "user": 1,
    "created_at": "2024-11-21T12:00:00Z"
  },
  {
    "id": 2,
    "amount": 50.75,
    "description": "Refund for product",
    "status": "completed",
    "user": 1,
    "created_at": "2024-11-20T11:30:00Z"
  }
]
```

### 3. Get Specific Transaction
- **URL**: `/transactions/{id}/`
- **Method**: `GET`
- **Response**:
```json
{
  "id": 1,
  "amount": 100.50,
  "description": "Payment for services",
  "status": "pending",
  "user": 1,
  "created_at": "2024-11-21T12:00:00Z"
}
```

### 4. Update Transaction Status
- **URL**: `/transactions/{id}/`
- **Method**: `PUT`
- **Request Body**:
```json
{
  "status": "completed"
}
```
- **Response**:
```json
{
  "id": 1,
  "amount": 100.50,
  "description": "Payment for services",
  "status": "completed",
  "user": 1,
  "created_at": "2024-11-21T12:00:00Z"
}
```

## Testing the API

To test the API, you can use tools like **Postman**, **.http file**, and the **requests_test.py** script.

In this guide, we will focus on using the **requests_test.py** file to test the API.

### Step 1: Install the Required Package

To run the `requests_test.py` file, you need to install the **requests** library if you haven't already. You can do this using pip:

```bash
pip install requests
```

After installing the package, you can run the `requests_test.py` script to test the API. This script will create a `responses` folder where all the API responses will be stored.

```bash
python requests_test.py
```



## Conclusion
This API provides a simple and effective solution for managing financial transactions, built with Django and Django REST Framework. It supports the basic CRUD operations required for transaction management.
