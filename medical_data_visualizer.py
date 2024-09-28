import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1 - Importe os dados do medical_examination.csv e atribua-os à variável df.
df = pd.read_csv('medical_examination.csv')
print(df.head())

# # 2 - Crie a coluna overweight na variável df.
df['overweight'] = (df['weight'] / (df['height'] / 100) ** 2).apply(lambda x: 1 if x > 25 else 0)

# # 3 - Normalize os dados, fazendo com que 0 seja sempre bom e 1 seja sempre ruim. 
# # Se o valor de cholesterol ou gluc for 1, defina o valor como 0. 
# # Se o valor for superior a 1, defina o valor como 1.
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)

# # 4
def draw_cat_plot():
#   # 5 - Crie um DataFrame para o gráfico categórico usando pd.melt com valores de cholesterol, gluc, smoke, alco, active e overweight na variável df_cat.
    df_cat = pd.melt(df, id_vars = ['cardio'], value_vars = ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])



#     # 6 - Agrupe e reformate os dados em df_cat para dividi-los por cardio. 
#     # Mostre as contagens de cada recurso.
    df_cat = df_cat.groupby(by = ['cardio', 'variable', 'value']).size().reset_index(name='total')


#     # 7 - Você terá que renomear uma das colunas para que o gráfico funcione corretamente.
    


#     # 8
#     fig = None


#     # 9
#     fig.savefig('catplot.png')
#     return fig


# # 10
# def draw_heat_map():
#     # 11
#     df_heat = None

#     # 12
#     corr = None

#     # 13
#     mask = None



#     # 14
#     fig, ax = None

#     # 15



#     # 16
#     fig.savefig('heatmap.png')
#     return fig
