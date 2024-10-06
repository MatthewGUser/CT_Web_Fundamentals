import requests

def fetch_pokemon_data(pokemon_names):
    for name in pokemon_names:
        url = f"https://pokeapi.co/api/v2/pokemon/{name}"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            abilities = ', '.join([ability['ability']['name'] for ability in data['abilities']])
            weight = data['weight']
            print(f"Name: {data['name']}\nAbilities: {abilities}\nWeight: {weight}")
        else:
            print(f"Error fetching data for {name}")

def calculate_average_weight(pokemon_names):
    total_weight = 0
    for name in pokemon_names:
        url = f"https://pokeapi.co/api/v2/pokemon/{name}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            total_weight += data['weight']
        else:
            print(f"Error fetching data for {name}")
    
    return total_weight / len(pokemon_names) if pokemon_names else 0
