# %% [markdown] 
# Importando Bibliotecas

# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# %% [markdown]
# Importando Dados

# %%
df = pd.read_csv('data/olist_customers_dataset.csv')
print(f'{df.isna().count()}, {df.shape}')



# %%
