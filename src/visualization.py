import pandas as pd
import matplotlib.pyplot as plt

def plot_top_categgory_state(df):
    plt.figure(figsize=(8,5))
    plt.barh(df["customer_state"], df["number_of_sales"])
    plt.ylabel("Estado")
    plt.xlabel("Quantidade de vendas")
    plt.title("Numero de vendas da categoria lider de cada estado")
    plt.gca().invert_yaxis()
    plt.show()

def plot_top_category_country(df):
    plt.barh(df['product_category_name'], df['number_of_sales'])
    plt.title("Categgorias com maior numero de vendas no pais")
    plt.ylabel("Categorias")
    plt.xlabel("Numero de vendas")
    plt.gca().invert_yaxis()
    plt.show()


def plot_ticket_by_state(df):
    plt.scatter( df['qty_sales'], df['mean'])
    plt.ylabel("Ticket medio")
    plt.xlabel("Quantidade de vendas")
    plt.title("Ticket Medio x Numero de Vendas")
    plt.show()

def plot_value_valuation(df):

    plt.scatter(df['price'], df['review_score'])
    plt.yticks(range(1, 6, 1))
    plt.xlabel("Preço Total do Pedido")
    plt.ylabel("Nota")
    plt.title("Relação entre Preço e Avaliação")

def plot_average_transport(df):

    plt.figure(figsize=(8,5))
    plt.barh(df["customer_state"], df["total_delivery_time"])
    plt.ylabel("Estado")
    plt.xlabel("Tempo medio de entregas")
    plt.title("Tempo medio de entregas por regiao(Em dias)")

