import random
import datetime
import csv
import sys

# def read_menu_from_csv(filename='order.csv'):
#     order = []
#     with open(filename, 'r') as file:
#         reader = csv.reader(file)
#         next(reader)  # Skip the header row
#         for row in reader:
#             # Adjust the condition to allow empty menu_type
#             if len(row) != 4 or row[0].strip() == '' or row[1].strip() == '' or row[3].strip() == '' or row[4].strip() == '':
#                 print(f"Skipping invalid or empty row: {row}")
#                 continue
#             try:
#                 name, order_list, price, order_date = row
#                 order.append(((name, order_list, price, order_date)))
#             except ValueError as e:
#                 print(f"Error converting row {row}: {e}")
#     print(order)
#     return order