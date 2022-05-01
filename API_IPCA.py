## importando bibliotecas

from selenium import webdriver
from time import sleep
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

## acessando o Chromedrive

driver = webdriver.Chrome()
driver.implicitly_wait(10)


## instanciando URL
URL_BC_IPCA = "https://www.ibge.gov.br/estatisticas/economicas/precos-e-custos/9256-indice-nacional-de-precos-ao-consumidor-amplo.html?=&t=series-historicas"

driver.get(URL_BC_IPCA)

## acessando classe para busca dos valores do IPCA

historico_ipca = driver.find_elements_by_class_name('conteudo__interna')
Ano = driver.find_elements_by_class_name('pvtRowLabel') # Coletando os Valores do Ano Através das Classes
Valores = driver.find_elements_by_class_name('pvtVal') # Coletando os Valores Numéricos Através das Classes

## loop para criar lista com dados coletados

Values_to_Work = [] 
Values = []
for l in Valores:
    Values_to_Work.append(l.text)
    
for h in Values_to_Work:
    res = h.replace("," , '.')
    Values.append(float(res))
    
Year = []
for j in Ano:
    Year.append(j.text)
    
## criando o dataset

data = {'Year': Year , 'Values': Values}
indice_ipca = pd.DataFrame(data)
indice_ipca.info()
indice_ipca

## gráfico para melhorar visualização

fig_dims = (20, 10)
fig, ax = plt.subplots(figsize=fig_dims)
sns.lineplot(data=indice_ipca, x="Year", y="Values" , ax = ax)