import requests
import jsonpath


avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')

# resultados = jsonpath.jsonpath(avaliacoes.json(), 'results')

# print(resultados)


# primeira = jsonpath.jsonpath(avaliacoes.json(), 'results[0]')
# print(primeira)

#nome = jsonpath.jsonpath(avaliacoes.json(), 'results[0].nome') # navegando nos resultados
#print(nome)

#nota = jsonpath.jsonpath(avaliacoes.json(), 'results[0].avaliacao') # navegando nos resultados
#print(nota)

# Todos os nomes das pessoas que avaliaram o curso
#nomes = jsonpath.jsonpath(avaliacoes.json(), 'results[*].nome')
#print(nomes)

# Todos as notas das pessoas que avaliaram o curso
notas = jsonpath.jsonpath(avaliacoes.json(), 'results[*].avaliacao')
print(notas)
