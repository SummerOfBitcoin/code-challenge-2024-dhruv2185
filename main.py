from utils.loadTransactionData import load_transaction_data
from utils.classes import Transaction
from utils.transactionValidation import getValidatedTransactions
import os
import sys


def main():
    transactions = load_transaction_data()
    print("Transaction data loaded successfully")
    print("Number of transactions: ", len(transactions))
    validatedTransactions = getValidatedTransactions(transactions)
    print("Number of validated transactions: ", len(validatedTransactions))


if __name__ == "__main__":
    main()
