import requests

def hae_vitsi():
    pyynto = "https://api.chucknorris.io/jokes/random"
    vastaus = requests.get(pyynto).json()
    return vastaus["value"]

print(hae_vitsi())
