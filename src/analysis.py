import pandas as pd
import numpy as np

def top_category_state(order_items, products, orders, customers):
    #Seleção de colunas
    order_items_analyses = order_items[["order_id", "product_id"]]
    products_analyses = products[["product_id","product_category_name"]]
    orders_analyses = orders[["order_id", "customer_id"]]
    customers_analyses = customers[["customer_id", "customer_state"]]

    #Merges
    categories_by_state = orders_analyses.merge(customers_analyses, on="customer_id")
    categories_by_state = categories_by_state.merge(order_items_analyses, on="order_id")
    categories_by_state = categories_by_state.merge(products_analyses, on="product_id")

    #Agrupamento
    categories_by_state = (
        categories_by_state[["customer_state", "product_category_name", "product_id"]]
        .groupby(["customer_state", "product_category_name"], as_index=False)
        .size()
    )

    #Função interna
    def maior(row):
        return row.sort_values('size', ascending=False).iloc[0]

    #Resultado final
    categories_by_state = (categories_by_state.groupby("customer_state", as_index=False)
                           .apply(maior)
                           .reset_index(drop=True)
                           .rename(columns={'size' : 'number_of_sales'}))
    categories_by_state = categories_by_state.sort_values('number_of_sales', ascending=False)

    return categories_by_state

def top_category_country(order_items, products):
    # Seleção de colunas
    order_items_analyses = order_items[["order_id", "product_id"]]
    products_analyses = products[["product_id","product_category_name"]]

    # Merges
    top_sales_categories = order_items_analyses.merge(right=products_analyses, on='product_id')

    # Agrupamento
    top_sales_categories = (top_sales_categories[["product_category_name", "order_id"]]
                .groupby("product_category_name", as_index=False)
                .size()
                .rename(columns={'size' : 'number_of_sales'}))

    # Resultado final
    top_sales_categories["percent"] = top_sales_categories["number_of_sales"] / top_sales_categories["number_of_sales"].sum() * 100
    top_sales_categories = top_sales_categories.sort_values("number_of_sales", ascending=False).iloc[0:5]

    return top_sales_categories

def ticket_by_state(order_items, orders, customers):
    #Seleção de colunas
    order_items_analyses = order_items[["order_id", "product_id", "price"]]
    orders_analyses = orders[["order_id", "customer_id"]]
    custumers_analyses = customers[["customer_id", "customer_state"]]

    #Merges
    ticket_mean = order_items_analyses.merge(right=orders_analyses, on='order_id')
    ticket_mean = ticket_mean.merge(right=custumers_analyses, on='customer_id')

    #Agrupamento
    ticket_mean = ticket_mean.groupby('customer_state', as_index=False).agg({'price' : 'median', 'customer_id': 'size'}).sort_values('customer_state')

    #Resultado final
    ticket_mean = ticket_mean.rename(columns={'price' : 'mean', 'customer_id' : 'qty_sales'}).sort_values('qty_sales', ascending=False)

    return ticket_mean

def correlation(column1, column2):
    return np.corrcoef(column1,column2)

def value_valuation(orders_review, order_items):
    #Seleção de colunas
    orders_review_analyses = orders_review[['order_id','review_score']]
    order_items_analyses = order_items[['order_id', 'price']]

    #Merges
    price_and_evaluation = orders_review_analyses.merge(right=order_items_analyses, on='order_id')

    #Agrupamento
    price_and_evaluation = price_and_evaluation.groupby('order_id').agg({
        'price': 'sum',
        'review_score': 'first'
    })

    #Filtro
    filter_outliar = price_and_evaluation["price"] < 5000

    #Resultado final
    price_and_evaluation = price_and_evaluation[filter_outliar]

    return price_and_evaluation


def price_ranges(evaluation_analysis):

    #Filtro
    range_evaluation = evaluation_analysis[evaluation_analysis["price"] <= 5000]

    #Resultado final
    range_evaluation['faixa_preco'] = pd.qcut(range_evaluation['price'], 5)
    range_evaluation = range_evaluation.groupby('faixa_preco')['review_score'].mean()

    return range_evaluation

def top_sellers(order_items, sellers):
    #Seleção de colunas
    order_items_analise = order_items[["product_id","seller_id"]]

    #Merges
    sellers_analise = order_items_analise.merge(right=sellers, on="seller_id")

    #Agrupamento
    sellers_analise = sellers_analise.groupby("seller_id").agg({
        "product_id" : "size",
        "seller_state" : "first",
        "seller_zip_code_prefix" : "first"})
    
    #Resultado final
    sellers_analise["seller_zip_code_prefix"] = sellers_analise["seller_zip_code_prefix"].astype("str")
    sellers_analise = sellers_analise.sort_values("product_id", ascending=False).iloc[0:10]

    return sellers_analise

def formata_data(data_completa : str):
    data_completa = str(data_completa)
    data = data_completa.split(' ')

    return data[0]

def pega_dias(n_dias):
    n_dias = str(n_dias)
    dias = n_dias.split(' ')
    dias = int(dias[0])
    return dias

def average_transport(orders, customers):
    #Seleção de colunas
    orders_analise  = orders[[ "order_id","customer_id", "order_delivered_carrier_date","order_delivered_customer_date"]]
    custumers_analise = customers[["customer_id", "customer_state"]]

    #Merges
    average_number_days = orders_analise.merge(right=custumers_analise, on="customer_id")
    average_number_days = average_number_days.dropna()

    #Aplicação da formula
    average_number_days["order_delivered_carrier_date"] = average_number_days["order_delivered_carrier_date"].apply(formata_data)
    average_number_days["order_delivered_customer_date"] = average_number_days["order_delivered_customer_date"]. apply(formata_data)

    #Mudando tipo
    average_number_days["order_delivered_carrier_date"] = pd.to_datetime(average_number_days["order_delivered_carrier_date"])
    average_number_days["order_delivered_customer_date"] = pd.to_datetime(average_number_days["order_delivered_customer_date"])

    #Subtraindo datas
    average_number_days['total_delivery_time'] = average_number_days["order_delivered_customer_date"] - average_number_days["order_delivered_carrier_date"]

    #Pegando numero de dias
    average_number_days['total_delivery_time'] = average_number_days['total_delivery_time'].astype(str)
    average_number_days['total_delivery_time'] = average_number_days['total_delivery_time'].apply(pega_dias)

    #Resultado final
    average_number_days = average_number_days.groupby('customer_state',as_index=False).agg({'total_delivery_time' : 'mean'}).sort_values('total_delivery_time')

    return average_number_days

