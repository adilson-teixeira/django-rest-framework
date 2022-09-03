import requests

from decouple import config

Token = config('TOKEN')
headers = {'Authorization': Token}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes'

resultado = requests.delete(url=f'{url_base_cursos}21', headers=headers)

# Testando o código HTTP
assert resultado.status_code == 204

# Testando se o tamanho do conteúdo retornado é 0 ( método delete não retorna nada)
assert len(resultado.text) == 0