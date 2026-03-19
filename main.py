# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

custumers = pd.read_csv("data\olist_customers_dataset.csv")
orders = pd.read_csv("data\olist_orders_dataset.csv")
order_items = pd.read_csv("data\olist_order_items_dataset.csv")
order_payments = pd.read_csv("data\olist_order_payments_dataset.csv")
order_review = pd.read_csv("data\olist_order_reviews_dataset.csv")
products = pd.read_csv("data\olist_products_dataset.csv")
sellers = pd.read_csv("data\olist_sellers_dataset.csv")
category_name = pd.read_csv("data\product_category_name_translation.csv")


# %%

order_items_analise = order_items[["order_id", "product_id"]]
products_analise = products[["product_id","product_category_name"]]
orders_analise = orders[["order_id", "customer_id"]]
custumers_analise = custumers[["customer_id", "customer_state"]]

df_analise = orders_analise.merge(right=custumers_analise, on="customer_id", )
df_analise = df_analise.merge(right= order_items_analise, on = "order_id")
df_analise = df_analise.merge(right=products_analise, on="product_id")

df_analise = (df_analise[["customer_state", "product_category_name", "product_id"]]
              .groupby(["customer_state", "product_category_name"], as_index=False)
              .count())

df_analise = df_analise.rename(columns={"product_id" : "qtd"})

def maior(row):
    return row[['product_category_name', 'qtd']].max()

df_analise.groupby(["customer_state"]).apply(maior)
# %%
