import requests
import json
url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
response = requests.get(url)

print(response)
if response.status_code == 200:
  dados_json = response.json()
  dados_restaurante = {}
  for item in dados_json:
    nome_restaurante = item['Company']
    if nome_restaurante not in dados_restaurante:
      dados_restaurante[nome_restaurante] = []
    dados_restaurante[nome_restaurante].append({
      'item': item['Item'],
      'price': item['price'],
      'description': item['description']
    })

else:
  print(f'Dados não encontrados')



for nome_restaurante, dados in dados_restaurante.items():
  nome_arquivo = f'{nome_restaurante}.json'
  with open(nome_arquivo,'w') as arquivo_json:
    json.dump(dados,arquivo_json,indent=4)
