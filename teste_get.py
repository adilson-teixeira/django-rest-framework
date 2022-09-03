import requests

from decouple import config

Token = config('TOKEN')
headers = {'Authorization': Token}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes'


resultado =  requests.get(url_base_cursos, headers=headers)

print(resultado.json())

"""EXEMPLOS DE TESTES"""

# Testando se o endpoint está correto
assert resultado.status_code == 200

# Testando a quantidade de registros
assert resultado.json()['count'] == 10

# Testando se o título do primeiro curso está correto

assert resultado.json()['results'][0]['titulo'] == 'Criação de  APIs REST Com Python E Django REST Framework: Essencial'

