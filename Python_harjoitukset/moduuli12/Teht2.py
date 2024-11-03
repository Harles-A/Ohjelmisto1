import requests

def hae_weather(name_input, api_key):
    pyynto = f"https://api.openweathermap.org/data/2.5/weather?q={name_input}&appid={api_key}&units=metric&lang=fi"
    vastaus = requests.get(pyynto).json()
    #print(vastaus)
    ilma = vastaus['weather'][0]['description']
    temp = vastaus['main']['temp']
    tuuli = vastaus['wind']['speed']
    return temp, ilma, tuuli

def main():
    name_input = input("Anna paikakunnan nimi: ")
    # Käytään API key input-ia koska tämä tehtävä on Githubissa public kansiossa.
    api_key = input("Anna API avain: ")
    temp, ilma, tuuli = hae_weather(name_input, api_key)
    print(f"\n - Sää {name_input} -")
    print(f"Lämpötila: {temp} °C")
    print(f"Sään kuvaus: {ilma.capitalize()}")
    print(f"Tuulen nopeus: {tuuli} m/s")

main()