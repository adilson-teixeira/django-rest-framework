from email import header
from tokenize import Token
import requests
from decouple import config


# GET Avaliações

#avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')

# Acessando o código de status HTTP
#print(avaliacoes.status_code)

# Acessando os dados da resposta
#print(avaliacoes.json()) # apesar do nome json a resposta é um  dicionário python

# Acessando a quantidade de registros
#print(avaliacoes.json()['count'])

# Acessando a próxima página dos resultados
#print(avaliacoes.json()['next'])

# Acessando os resultados desta página
#print(avaliacoes.json()['results']) # Retorna uma lista de resultados [{ }, { }]

# Acessando o primeiro elemento da lista de resultados
#print(avaliacoes.json()['results'][0])

# Acessando o último elemento da lista de resultados
#print(avaliacoes.json()['results'][-1])

# Acessando apenas o nome da pessoa que fez a última avaliação
#print(avaliacoes.json()['results'][-1]['nome'])


# GET Avaliação

avaliacao = requests.get('http://localhost:8000/api/v2/avaliacoes/3/')

# print(avaliacao.json())

# GET Cursos

Token = config('TOKEN')
headers = {'Authorization': Token}
# os dados de autorização são passados na variável headers
cursos =  requests.get('http://localhost:8000/api/v2/cursos/', headers=headers)
print(cursos.status_code)
print(cursos.json())
