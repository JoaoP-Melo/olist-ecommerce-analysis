# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


custumers = pd.read_csv("data\olist_customers_dataset.csv")
orders = pd.read_csv("data\olist_orders_dataset.csv")
order_items = pd.read_csv("data\olist_order_items_dataset.csv")
order_payments = pd.read_csv("data\olist_order_payments_dataset.csv")
order_review = pd.read_csv("data\olist_order_reviews_dataset.csv")
products = pd.read_csv("data\olist_products_dataset.csv")
sellers = pd.read_csv("data\olist_sellers_dataset.csv")
category_name = pd.read_csv("data\product_category_name_translation.csv")


# %%
#Pergunta 01
order_items_analise = order_items[["order_id", "product_id"]]
products_analise = products[["product_id","product_category_name"]]
orders_analise = orders[["order_id", "customer_id"]]
custumers_analise = custumers[["customer_id", "customer_state"]]

df_analise = orders_analise.merge(right=custumers_analise, on="customer_id", )
df_analise = df_analise.merge(right= order_items_analise, on = "order_id")
df_analise = df_analise.merge(right=products_analise, on="product_id")

df_analise = (df_analise[["customer_state", "product_category_name", "product_id"]]
              .groupby(["customer_state", "product_category_name"], as_index=False)
              .size())


def maior(row : pd.DataFrame):
    return row[['product_category_name', 'size']].sort_values('size', ascending=False).iloc[0]

df_analise = df_analise.groupby(["customer_state"], as_index=False).apply(maior)

df_analise

# %%
#Pergunta 02

order_items_analise = order_items[["order_id", "product_id"]]
products_analise = products[["product_id","product_category_name"]]

df_analise = order_items_analise.merge(right=products_analise, on='product_id')

df_analise = (df_analise[["product_category_name", "order_id"]]
              .groupby("product_category_name", as_index=False)
              .size())

df_analise["percentual"] = df_analise["size"] / df_analise["size"].sum() * 100

df_analise = df_analise.sort_values("size", ascending=False).iloc[0:3]


plt.figure(figsize=(8,5))
plt.barh(df_analise["product_category_name"], df_analise["size"])
plt.ylabel("Categorias")
plt.xlabel("Quantidade de Vendas")
plt.title("Quantidade de Venda das Categorias")
plt.gca().invert_yaxis()



# %%
# Pergunta 03

order_items_analise = order_items[["order_id", "product_id"]]
products_analise = products[["product_id","product_category_name"]]

df_analise = order_items_analise.merge(right=products_analise, on='product_id')

df_analise = (df_analise[["product_category_name", "order_id"]]
              .groupby("product_category_name", as_index=False)
              .size())

df_analise["percentual"] = df_analise["size"] / df_analise["size"].sum() * 100

df_analise = df_analise.sort_values("size", ascending=False).iloc[0:10]


plt.figure(figsize=(8,5))
plt.barh(df_analise["product_category_name"], df_analise["size"])
plt.ylabel("Categorias")
plt.xlabel("Quantidade de Vendas")
plt.title("Quantidade de Venda das Categorias")
plt.gca().invert_yaxis()

# %%

#Pergunta 04

order_items_analise = order_items[["order_id", "product_id", "price"]]
orders_analise = orders[["order_id", "customer_id"]]
custumers_analise = custumers[["customer_id", "customer_state"]]

df_analise = order_items_analise.merge(right=orders_analise, on='order_id')
df_analise = df_analise.merge(right=custumers_analise, on='customer_id')


df_analise = df_analise.groupby('customer_state', as_index=False).agg({'price' : 'median'}).sort_values('customer_state')
df_analise

plt.figure(figsize=(8,5))
plt.barh(df_analise["customer_state"], df_analise["price"])
plt.ylabel("Estado do cliente")
plt.xlabel("Preco")
plt.title("Preco medio por estado")
plt.gca().invert_yaxis()

# %%
#Pergunta 05
orders_review_analise = order_review[['order_id','review_score']]
order_items_analise = order_items[['order_id', 'price']]

df_analise = orders_review_analise.merge(right=order_items_analise, on='order_id')
df_analise = df_analise.groupby('order_id').agg({
    'price': 'sum',
    'review_score': 'first'
})

np.corrcoef(df_analise['review_score'],df_analise['price'])

df_analise[df_analise["price"] > 5000]

df_analise = df_analise[df_analise["price"] <= 5000]

plt.scatter(df_analise['price'], df_analise['review_score'])
plt.xlabel("Preço Total do Pedido")
plt.ylabel("Nota")
plt.title("Relação entre Preço e Avaliação")
plt.show()


# %%
# Pergunta 06

df_analise = orders_review_analise.merge(right=order_items_analise, on='order_id')
df_analise = df_analise.groupby('order_id').agg({
    'price': 'sum',
    'review_score': 'first'
})

df_analise = df_analise[df_analise["price"] <= 5000]

df_analise['faixa_preco'] = pd.qcut(df_analise['price'], 5)

df_analise.groupby('faixa_preco')['review_score'].mean()


# %%
#Pergunta 07

order_items_analise = order_items[["product_id","seller_id"]]
sellers_analise = sellers

df_analise = order_items_analise.merge(right=sellers_analise, on="seller_id")
df_analise = df_analise.groupby("seller_id").agg({
    "product_id" : "size",
    "seller_state" : "first",
    "seller_zip_code_prefix" : "first"})

df_analise["seller_zip_code_prefix"] = df_analise["seller_zip_code_prefix"].astype("str")
df_analise = df_analise.sort_values("product_id", ascending=False).iloc[0:10]

plt.figure(figsize=(8,5))
plt.barh(df_analise["seller_zip_code_prefix"], df_analise["product_id"])
plt.ylabel("Zip vendendor")
plt.xlabel("Quantidade de Vendas")
plt.title("Quantidade de vendas de casa vendedor")
plt.gca().invert_yaxis()

df_analise

# %%

orders_analise  = orders[["order_approved_at", "order_id","customer_id", "order_delivered_carrier_date","order_delivered_customer_date","order_estimated_delivery_date"]]

custumers_analise = custumers[["customer_id", "customer_state"]]

df_analise = orders_analise.merge(right=custumers_analise, on="customer_id")

df_analise = df_analise[df_analise["order_approved_at"].notnull()]
df_analise['order_delivered_carrier_date'] = df_analise['order_delivered_carrier_date'].fillna(df_analise['order_approved_at'])
df_analise['order_delivered_customer_date'] = df_analise['order_delivered_customer_date'].fillna(df_analise['order_estimated_delivery_date'])

df_analise
def formata_data(data_completa : str):
    data_completa = str(data_completa)
    data = data_completa.split(' ')

    return data[0]

df_analise["order_delivered_carrier_date"] = df_analise["order_delivered_carrier_date"].apply(formata_data)
df_analise["order_delivered_customer_date"] = df_analise["order_delivered_customer_date"]. apply(formata_data)


df_analise["order_delivered_carrier_date"] = pd.to_datetime(df_analise["order_delivered_carrier_date"])
df_analise["order_delivered_customer_date"] = pd.to_datetime(df_analise["order_delivered_customer_date"])


df_analise['tempo_de_entrega_total'] = df_analise["order_delivered_customer_date"] - df_analise["order_delivered_carrier_date"]

df_analise['tempo_de_entrega_total'] = df_analise['tempo_de_entrega_total'].astype(str)

def pega_dias(n_dias):
    n_dias = str(n_dias)
    dias = n_dias.split(' ')
    dias = int(dias[0])
    return dias

df_analise['tempo_de_entrega_total'] = df_analise['tempo_de_entrega_total'].apply(pega_dias)
df_analise = df_analise.groupby('customer_state',as_index=False).agg({'tempo_de_entrega_total' : 'mean'})


plt.figure(figsize=(8,5))
plt.barh(df_analise["Estado"], df_analise["tempo_de_entrega_total"])
plt.ylabel("customer_state")
plt.xlabel("Tempo medio de entregas")
plt.title("Tempo dmedio de entregas por regiao(Em dias)")


# %%
