# Dataframe
Cientistas de dados tem um problema de organizar muitos muitos dados e aplicar conceitos e modelos para aplicar Machine Learning.  
Ele precisa fazer essa etapa de organizar e pegar dados bons (se forem ruins não dá tão certo).  

## Pandas
Tabelas contendo informações para ajudar nisso.  
O Pandas consegue pegar uma matriz de informações e transforma em um Dataframe.  
  
Essas informações costumam vir de pesquisas, dados públicos etc. (não coisa aleatória, porque aí não tem muito o que extrair).  
  
Se formos usar o anaconda, precisaria dar o comando `pip3 install pandas`. No Colab não precisaria.  
  
Vamos usar as libs: Pandas e matplotlib  
  
### Exemplo
Análise das espécies de Iris, analisando as suas medidas sabendo da sua espécia, e partindo apenas das medidas para deduzir a sua espécie.  
https://archive.ics.uci.edu/dataset/53/iris
  
https://www.kaggle.com/datasets - Lugar com váris outros datasets  
  
## Cabeçalho do Dataframe
Antes de processar com o panda, é importante adicionar os atributos na primeira linha.  
Para isso, criamos o header como um array com os nomes de atributos.  
`df = pd.read_csv(url, header=None, names=header)` -> names seria esse tal de cabeçalho e o header=None seria para remover o cabeçalho atual e usar o names no lugar.  
  
* `df.info()` - Comando que ajuda a identificar mais informações do dataframe.
* `df.shape` - Dimensões do dataframe.
* `print(df.groupby('species').size())` - Agrupa informações por um campo
* `df.describe()`
* `df.species.unique()`
* `df['petal_length'].head()`
* `df[['petal_length']].head()`
* `df[['petal_length', 'petal_width']].head()`

## Gráficos
  
### Boxes
```
# box and whisker plots
df.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False, figsize=(15, 15))
plt.show()
```

### Histograma
```
# Lembra de histograma, que exibe uma gráfico de frequência.
df.hist(bins=100, figsize=(15, 15))
plt.show()
```

### Pandas
```
# scatter plot matrix
from pandas.plotting import scatter_matrix
scatter_matrix(df,figsize=(15, 15))
plt.show()
```

### Seaborn
```
import matplotlib.pyplot as plt
import seaborn as sns

# A cor vem do campo `species` do dataframe
sns.pairplot(df, hue='species', height=5)
plt.show()
```  
  
Esses permitem com que certas análises sejam feitas para chegar em certas conclusões  

### Forma de chegar em correlações entre informações  
```
cols = ['sepal_length', 'sepal_width', 'petal_length','petal_width']
corr_matx = df[cols].corr()
heatmap = sns.heatmap(corr_matx,cbar=True,annot=True,square=True,fmt='.2f',annot_kws={'size': 15},yticklabels=cols,xticklabels=cols,cmap='Dark2')
plt.show()
```
  
* 0.9 a 1 positivo ou negativo indica uma correlação muito forte.
* 0.7 a 0.9 positivo ou negativo indica uma correlação forte.
* 0.5 a 0.7 positivo ou negativo indica uma correlação moderada.
* 0.3 a 0.5 positivo ou negativo indica uma correlação fraca.
* 0 a 0.3 positivo ou negativo indica uma correlação desprezível.
* lembre-se* que: alta correlação não implica em causa. (causa e consequência). Para entender melhor vale a pena dar uma olhada nesse site que mostra correlações absurdas...'spurious correlations' (http://www.tylervigen.com/spurious-correlations) 
  
## Como aplicar
A ideia é saber utilizar essas ferramentas para encontrar conclusões, relações e dentre outras informações, permitindo identificar cenários, padrões, sobreposições e até mesmo modelos de predição com base em dados.  
