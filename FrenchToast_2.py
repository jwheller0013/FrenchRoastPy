import csv
import json

transaction_template = {
    "account_number": 0,
    "balance": 0,
}

customer = {
}

with open('resources/transactions.csv', 'r', newline='') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)

    lines  = 0
    for line in csv_reader:

        cus = line[1]
        cusID = int(line[2])
        transType = line[3].strip().lower()
        amount = float(line[4])
        if customer.get(cus) is None:
            customer[cus] = []

        account_exists = False
        for account_info in customer[cus]:
            if account_info["account_number"] == cusID:
                account_exists = True
                if transType == 'withdrawal':
                    account_info["balance"] -= amount
                elif transType == 'deposit':
                    account_info["balance"] += amount

        if not account_exists:
            new_account = transaction_template.copy()
            new_account["account_number"] = cusID
            if transType == 'withdrawal':
                new_account["balance"] -= amount
            elif transType == 'deposit':
                new_account["balance"] += amount
            customer[cus].append(new_account)

    # print(customer)

sorted_customer = dict(sorted(customer.items()))

for customer_key in sorted_customer:
    sorted_customer[customer_key] = sorted(sorted_customer[customer_key], key=lambda x: x['account_number'])

with open('customers.json', 'w') as json_file:
    json.dump(sorted_customer, json_file, indent=4)
