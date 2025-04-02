import csv
import pandas as pd
import os
import json

#Your code should be able to adapt to a different file of transactions,
# with different data entirely, and produce a clean JSON file

#CSV has {customer_number, account_number, transaction_type, date/time}
# 20,000 transactions in total, customers can have multiple accounts

#need to handle transaction_type withdrawl(minus) and deposit(add)
#accounts can be negative and do not need to worry about "overdraft" aspects
#need to handle customer_number being assigned to multiple account_numbers

class Bank():

    def __init__(self, filename):
        file_path = os.path.dirname(os.path.abspath(__file__))
        self.file = os.path.join(file_path, filename)
        self.transactions = self.read_CSV()

    transaction_template = {
        "customer": None,
        "account_number": None,
        "transaction": None,
        "amount": None,
        "date_time": None
        }


    def read_CSV(self):
        try:
            df = pd.read_csv(self.file)
            return df
        except FileNotFoundError:
            return f"File '{self.file}' not found."
        except IOError as e:
            return f"Error reading file: {e}"


    def formating(self, file):
        test_data = Bank.transaction_template.copy()
        test_data["customer"] = file["customerId"]
        test_data["account_number"] = file["accountId"]
        test_data["transaction"] = file["transactionType"]
        test_data["amount"] = file["amount"]
        test_data["date_time"] = file["timestamp"]
        return test_data

    print(test_data)

if __name__ == "__main__":
    bank = Bank("transactions.csv")









