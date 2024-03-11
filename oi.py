import requests
from bs4 import BeautifulSoup

# Fazendo a solicitação HTTP para obter o conteúdo da página
response = requests.get('https://www.gov.br/pt-br')

# Verificando se a solicitação foi bem-sucedida
if response.status_code == 200:
    # Passando o conteúdo HTML da página para o BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Imprimindo o conteúdo formatado
    print(soup.find_all('a'))
else:
    print('Erro ao carregar a página:', response.status_code)