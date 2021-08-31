import requests
import pandas as pd
from bs4 import BeautifulSoup

response = requests.get('https://g1.globo.com/')

content = response.content

site = BeautifulSoup(content, 'html.parser')

noticia = []

results = site.findAll('div', attrs={'class': 'feed-post-body'})

for result in results:

  data = result.find('div', attrs= {'class': 'feed-post-metadata'})

  título = result.find('a', attrs={'class': 'feed-post-link'})

  sub = result.find('div', attrs= {'class': 'feed-post-body-resumo'})


  noticia.append([data, título, sub])

tabela = pd.DataFrame(noticia, columns=['data','título','sub'])
print(tabela)

tabela

