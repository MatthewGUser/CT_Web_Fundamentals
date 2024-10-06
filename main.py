from pokemon_api import fetch_pokemon_data, calculate_average_weight
from space_api import fetch_planet_data, find_heaviest_planet

def main():
    # Pokémon API Data Fetching
    pokemon_names = ["pikachu", "bulbasaur", "charmander"]
    print("Fetching Pokémon data...\n")
    fetch_pokemon_data(pokemon_names)
    
    average_weight = calculate_average_weight(pokemon_names)
    print(f"Average Weight of selected Pokémon: {average_weight}")

    # Space API Data Fetching
    print("\nFetching Space API data...\n")
    planets = fetch_planet_data()
    
    # Finding and displaying the heaviest planet
    name, mass = find_heaviest_planet(planets)
    print(f"The heaviest planet is {name} with a mass of {mass} kg.")

if __name__ == "__main__":
    main()
