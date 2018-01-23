import requests

request = requests.get('www.google.com') # Dá pra colocar a opção allow=redirects=False

print(request.history) # pegando o redirecionamento