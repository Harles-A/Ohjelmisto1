import requests

def hae_weather(name_input, api_key):
    pyynto = f"https://api.openweathermap.org/data/2.5/weather?q={name_input}&appid={api_key}&units=metric&lang=fi"
    vastaus = requests.get(pyynto).json()
    #print(vastaus)
    ilma = vastaus['weather'][0]['description']
    temp = vastaus['main']['temp']
    return temp, ilma

def main():
    name_input = input("Anna paikakunnan nimi: ")
    # Käytään API key input-ia koska tämä tehtävä on Githubissa public paikassa.
    api_key = input("Anna API avain: ")
    print(f"Lämpotila paikassa {name_input} on {hae_weather(name_input, api_key)} astetta")

main()