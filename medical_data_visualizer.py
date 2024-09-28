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
#     # o método(?) count() repara e retora valores nulos e NAN, enquanto size() não.


#     # 7 - Você terá que renomear uma das colunas para que o gráfico funcione corretamente.
    fig = sns.catplot(x='variable', y='total', hue='value', col='cardio', data=df_cat, kind='bar')
    


#     # 8 - - Converta os dados para o formato longo e crie um gráfico que mostre as contagens de valores dos recursos categóricos 
#     # Usando o método fornecido pela biblioteca seaborn: sns.catplot().
    fig = sns.catplot(x='variable', y='total', hue='value', col='cardio', data=df_cat, kind='bar')


#     # 9 - Obtenha a figura para a saída e armazene-a na variável fig.
    fig.savefig('catplot.png')
    
    return fig


# # 10 - Não modifique as duas linhas seguintes.

def draw_heat_map():
#     # 11 - Desenhe o Mapa de Calor na função draw_heat_map.
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) &
                 (df['height'] >= df['height'].quantile(0.025)) &
                 (df['height'] <= df['height'].quantile(0.975)) &
                 (df['weight'] >= df['weight'].quantile(0.025)) &
                 (df['weight'] <= df['weight'].quantile(0.975))]

#     # 12 - Limpe os dados na variável df_heat filtrando os seguintes segmentos de pacientes que representam dados incorretos: [abrir read.me]
    corr = df_heat.corr()


#     # 13 - Calcule a matriz de correlação e armazene-a na variável corr.
    mask = np.triu(np.ones_like(corr, dtype=bool))


#     # 14 - Gere uma máscara para o triângulo superior e armazene-a na variável mask.
    fig, ax = plt.subplots(figsize=(12, 8))


#     # 15 - Configure a figura do matplotlib.
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', ax=ax, cmap='BrBG', linewidths=0.5)


#     # 16 - Plote a matriz de correlação usando o método fornecido pela biblioteca seaborn: sns.heatmap().
    fig.savefig('heatmap.png')
    
    return fig # oba acabou :)
