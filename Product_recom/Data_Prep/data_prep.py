# -*- coding: utf-8 -*-
"""Untitled24.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TDbsOm5SzA8-P6hSp7So03xefwGF7cNv
"""

#Importing Libraray
import numpy as np
import pandas as pd

print('Preparing Data for transformation......')


#Read Data
orders = pd.read_csv("https://raw.githubusercontent.com/ashwinkadam/DigitalMarketing-Algorithms-Project/main/Data/order_items.csv")
products = pd.read_csv("https://raw.githubusercontent.com/ashwinkadam/DigitalMarketing-Algorithms-Project/main/Data/products.csv")
users = pd.read_csv("https://raw.githubusercontent.com/ashwinkadam/DigitalMarketing-Algorithms-Project/main/Product_recom/users.csv")


#Product Data formatting
products = products.dropna(subset=['name'])
products = products.rename(columns={'id': 'product_id', 'name': 'product_name'})
products = products[['product_id', 'category','product_name', 'brand', 'department']]

#orders aggregation
orders = orders.groupby(['user_id', 'product_id']).size().reset_index(name="Quantity")

#city_item Data
users = users.dropna(subset=['city'])
users = users.rename(columns={'id': 'user_id'})

#master data
master_data = users.merge(orders, on = 'user_id', how = 'inner')[['user_id','city','age','product_id','Quantity']]

# Save the DataFrame to a CSV file
master_data.to_csv('master_data.csv', index=False)

print('Data Transformation Done, Master Data file created')

