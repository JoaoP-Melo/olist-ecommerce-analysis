# %% [markdown] 
## Importando Bibliotecas

# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# %% [markdown]
## Importando Dados

# %%
custumers = pd.read_csv("data\olist_customers_dataset.csv")
orders = pd.read_csv("data\olist_orders_dataset.csv")
order_items = pd.read_csv("data\olist_order_items_dataset.csv")
order_payments = pd.read_csv("data\olist_order_payments_dataset.csv")
order_review = pd.read_csv("data\olist_order_reviews_dataset.csv")
products = pd.read_csv("data\olist_products_dataset.csv")
sellers = pd.read_csv("data\olist_sellers_dataset.csv")
category_name = pd.read_csv("data\product_category_name_translation.csv")


# %%

custumers[['customer_city', 
           'customer_state']] = custumers[['customer_city', 
                                           'customer_state']].astype('category')

# %%

# nao mechi em orders

# %%
order_items['order_item_id'] = order_items['order_item_id'].astype('category')

# %%

order_payments['payment_type'] = order_payments['payment_type'].astype('category')
order_payments['payment_sequential'] = order_payments['payment_sequential'].astype('category')
order_payments['payment_installments'] = order_payments['payment_installments'].astype('category')

# %%
# nao mechi em products
# %%

sellers['seller_city'] = sellers['seller_city'].astype('category')
sellers['seller_state'] = sellers['seller_state'].astype('category')

# %%

