import requests


def search_show(search_term):
    url = f"https://api.tvmaze.com/search/shows?q={search_term}"
    
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        print("Verkko-ongelma.")
        return

    if response.status_code != 200:
        print(f"Pyytö ei onnistunut, status: {response.status_code}")
        return
    
    response_body = response.json()

    if len(response_body) < 1:
        print("Ei tuloksia.")
        return

    print(f"Ohjelman nimi: {response_body[0]['show']['name']}")
    for item in response_body:
        print("---")
        print(item['show']['name'])
        print(f"Linkki: {item['show']['url']}")
        for genre in item['show']['genres']:
            print(genre)

search_show(input("Anna hakusana: "))