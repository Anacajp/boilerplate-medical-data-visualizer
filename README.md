# Medical Data Visualizer

This is the boilerplate for the Medical Data Visualizer project. Instructions for building your project can be found at https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/medical-data-visualizer


>>> Crie um gráfico semelhante ao "examples/Figure_1.png", onde mostramos as contagens de resultados bons e ruins para as variáveis cholesterol, gluc, alco, active e smoke para pacientes com cardio=1 e cardio=0 em painéis diferentes.

>>> Use os dados para concluir as seguintes tarefas em medical_data_visualizer.py:

    - Adicione uma coluna chamada overweight (acima do peso) aos dados. Para determinar se uma pessoa está acima do peso, primeiro calcule o IMC (Índice de Massa Corporal) dividindo o peso da pessoa em quilogramas pelo quadrado de sua altura em metros. Se o valor for maior que 25, a pessoa está acima do peso. Use o valor 0 para NÃO acima do peso e o valor 1 para acima do peso.

    - Normalize os dados, fazendo com que 0 sempre seja considerado bom e 1 seja considerado ruim. Se o valor de colesterol ou glicose for 1, transforme o valor em 0. Se o valor for maior que 1, transforme o valor em 1.

    - Converta os dados para o formato "long" (long format) e crie um gráfico que mostre a contagem de valores das características categóricas usando o catplot() do Seaborn. O conjunto de dados deve ser dividido por Cardio, então haverá um gráfico para cada valor de Cardio. O gráfico deve se parecer com examples/Figure_1.png.

    - Limpe os dados. Filtre os seguintes segmentos de pacientes que representam dados incorretos:

            - A pressão diastólica é maior que a sistólica (Mantenha os dados corretos com (df['ap_lo'] <= df['ap_hi']))
        
            - A altura é menor que o percentil 2.5 (Mantenha os dados corretos com (df['height'] >= df['height'].quantile(0.025)))

            - A altura é maior que o percentil 97.5
        
            - O peso é menor que o percentil 2.5

            - O peso é maior que o percentil 97.5

            - Crie uma matriz de correlação usando o conjunto de dados. Plote a matriz de correlação usando o heatmap() do Seaborn. Masque o triângulo superior. O gráfico deve se parecer com examples/Figure_2.png.


    - Sempre que uma variável for definida como None, certifique-se de substituí-la pelo código correto.


Testes unitários estão escritos para você no arquivo test_module.py.

________________________________

**Instruções**
Por cada número no arquivo medical_data_visualizer.py, adicione o código da instrução associada abaixo.


1 - Importe os dados do medical_examination.csv e atribua-os à variável df.

2 - Crie a coluna overweight na variável df.
    
3 - Normalize os dados, fazendo com que 0 seja sempre bom e 1 seja sempre ruim. Se o valor de cholesterol ou gluc for 1, defina o valor como 0. Se o valor for superior a 1, defina o valor como 1.

4 - Desenhe o Gráfico Categórico na função draw_cat_plot.

5 - Crie um DataFrame para o gráfico categórico usando pd.melt com valores de cholesterol, gluc, smoke, alco, active e overweight na variável df_cat.

6 - Agrupe e reformate os dados em df_cat para dividi-los por cardio. Mostre as contagens de cada recurso. 7 

7 - Você terá que renomear uma das colunas para que o gráfico funcione corretamente.

8 - Converta os dados para o formato longo e crie um gráfico que mostre as contagens de valores dos recursos categóricos usando o método fornecido pela biblioteca seaborn: sns.catplot().

9 - Obtenha a figura para a saída e armazene-a na variável fig.

10 - Não modifique as duas linhas seguintes.

11 - Desenhe o Mapa de Calor na função draw_heat_map.

12 - Limpe os dados na variável df_heat filtrando os seguintes segmentos de pacientes que representam dados incorretos:
    - altura inferior ao percentil de 2,5 (Mantenha os dados corretos com (df['height'] >= df['height'].quantile(0.025)))
    - altura superior ao percentil de 97,5
    - peso inferior ao percentil de 2,5
    - peso superior ao percentil de 97,5

13 - Calcule a matriz de correlação e armazene-a na variável corr.

14 - Gere uma máscara para o triângulo superior e armazene-a na variável mask.

15 - Configure a figura do matplotlib.

16 - Plote a matriz de correlação usando o método fornecido pela biblioteca seaborn: sns.heatmap().


*Não modifique as duas linhas seguintes.*