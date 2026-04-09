# Análise de Dados - Olist E-commerce Brasileiro

## Descrição
Este projeto tem como objetivo realizar uma análise descritiva dos dados do e-commerce brasileiro da Olist, buscando identificar padrões de vendas, comportamento dos clientes e fatores que impactam o desempenho do negócio. A análise foi conduzida a partir de perguntas orientadas aos dados disponíveis no dataset.

## Dataset
O projeto utiliza o dataset público da Olist, disponibilizado no Kaggle.
Principais colunas utilizadas:  
order_id → Identificação do pedido  
product_id → Identificação do produto  
product_category_name → Categoria do produto  
customer_id → Identificação do cliente  
customer_state → Estado do cliente  
price → Preço do pedido  
review_score → Nota dada pelo cliente  
seller_id → Identificação do vendedor  
order_approved_at → Data de aprovação do pedido  
order_delivered_carrier_date → Data de envio do pedido  
order_delivered_customer_date → Data de entrega  
order_estimated_delivery_date → Data estimada de entrega  

## Tecnologias Utilizadas
Python  
Pandas  
NumPy  
Matplotlib  
Jupyter Notebook  

## Estrutura do Projeto
data -> Dados (não versionados)  
notebooks -> Análises exploratórias  
src -> Funções de análise e funções de visualização  

## Análises Realizadas
Análise de vendas por categoria e região  
Cálculo de ticket médio por estado  
Correlação entre preço e avaliação dos pedidos  
Ranking de vendedores por volume de vendas  
Análise de tempo de entrega por região  

## Principais Insights
Diferenças relevantes de consumo entre estados  
Concentração de vendas em categorias específicas  
Prazo de entrega em cada região  
Identificação dos vendedores com maior volume de pedidos  

## Melhorias Futuras
Desenvolvimento de dashboard interativo(web)  
Automatização do pipeline de análise  
Tratamento mais avançado dos dados  

## Executar o Projeto
Clonar repositorio: git clone <seu-repositorio>  
Baixar o dataset: https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce  
Colocar os arquivos na pasta `data/`  
Instale as dependências: pip install -r requirements.txt  

## Autor
João Pedro