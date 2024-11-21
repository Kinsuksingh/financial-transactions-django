import { useState } from 'react';
import axios from 'axios';
import './App.css';

const App = () => {
  const [amount, setAmount] = useState('');
  const [transactionType, setTransactionType] = useState('WITHDRAWAL');
  const [userId, setUserId] = useState(1);
  const [transactions, setTransactions] = useState([]);
  const [error, setError] = useState('');

  // Create Transaction
  const handleCreateTransaction = async () => {
    const transactionData = {
      amount: parseFloat(amount),
      transaction_type: transactionType,
      user: userId,
    };

    try {
      await axios.post('http://127.0.0.1:8000/api/transactions/', transactionData, {
        headers: {
          'Content-Type': 'application/json',
        },
      });
      alert('Transaction Created');
      fetchTransactions(); // Refresh transactions list after creating a new one
    } catch (error) {
      console.error('Error creating transaction:', error);
      setError('Error creating transaction. Please fill in the amount value.');
    }
  };

  // Fetch All Transactions for a User
  const fetchTransactions = async () => {
    try {
      const response = await axios.get(`http://127.0.0.1:8000/api/transactions/all/?user_id=${userId}`);
      const { transactions } = response.data; // Assuming response.data contains a transactions key
      if (transactions) {
        setTransactions(transactions);
      } else {
        setError('Error fetching transactions. Please check the data.');
      }
    } catch (error) {
      console.error('Error fetching transactions:', error);
      setError('Error fetching transactions. Please try again.');
    }
  };

  // Update Transaction Status
  const handleUpdateStatus = async (transactionId, newStatus) => {
    try {
      await axios.put(
        `http://127.0.0.1:8000/api/transactions/${transactionId}/update/`,
        { status: newStatus },
        { headers: { 'Content-Type': 'application/json' } }
      );
      alert('Transaction Status Updated');
      fetchTransactions(); // Refresh transactions after status update
    } catch (error) {
      console.error('Error updating transaction:', error);
      setError('Error updating transaction. Please try again.');
    }
  };

  return (
    <div className="app">
      <h1>Transaction Management</h1>

      {/* Error Message */}
      {error && <p className="error">{error}</p>}

      {/* Create Transaction Form */}
      <div className="form-container">
        <h2>Create a Transaction</h2>
        <div className="form-group">
          <label>User Id</label>
          <input
            type="number"
            value={userId}
            onChange={(e) => setUserId(e.target.value)}
            placeholder="Enter user ID"
          />
        </div>
        <div className="form-group">
          <label>Amount</label>
          <input
            type="number"
            value={amount}
            onChange={(e) => setAmount(e.target.value)}
            placeholder="Enter amount"
          />
        </div>
        <div className="form-group">
          <label>Transaction Type</label>
          <select
            value={transactionType}
            onChange={(e) => setTransactionType(e.target.value)}
          >
            <option value="WITHDRAWAL">Withdrawal</option>
            <option value="DEPOSIT">Deposit</option>
          </select>
        </div>
        <button onClick={handleCreateTransaction}>Create Transaction</button>
      </div>

      {/* Transactions List */}
      <div className="transaction-list">
        <h2>Transactions</h2>
        <button onClick={fetchTransactions}>Get Transactions</button>
        <div className="transactions">
          {transactions && transactions.length > 0 ? (
            transactions.map((transaction) => (
              <div key={transaction.id} className="transaction-item">
                <p><strong>ID:</strong> {transaction.id}</p>
                <p><strong>Amount:</strong> ${transaction.amount}</p>
                <p><strong>Type:</strong> {transaction.transaction_type}</p>
                <p><strong>Status:</strong> {transaction.status}</p>
                <button
                  className={transaction.status === 'PENDING' ? 'btnCOLOR' : 'completed'}
                  onClick={() => handleUpdateStatus(transaction.id, 'COMPLETED')}
                >
                  {transaction.status === 'PENDING' ? 'Pending' : 'Completed'}
                </button>
              </div>
            ))
          ) : (
            <p>No transactions available.</p>
          )}
        </div>
      </div>
    </div>
  );
};

export default App;
