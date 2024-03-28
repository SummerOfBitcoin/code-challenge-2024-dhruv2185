import json
import os
from .classes import Transaction


def load_transaction_data():
    # load all the transaction data in a list
    transaction_list = []
    script_dir = os.path.dirname(os.path.abspath(__file__))
    mempool_dir = os.path.join(script_dir, '..', 'mempool')
    print("Loading Transaction data...")
    for file in os.listdir(mempool_dir):

        if file.endswith('.json'):
            with open(os.path.join(mempool_dir, file)) as f:
                data = json.load(f)
                transaction = Transaction.from_dict(data)
                transaction_list.append(transaction)
    return transaction_list
