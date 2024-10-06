import requests

# Function to fetch planet data from the Solar System API
def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['bodies']
    else:
        print("Error fetching planet data")
        return []

# Function to find the heaviest planet
def find_heaviest_planet(planets):
    heaviest = max(planets, key=lambda planet: planet['mass']['massValue'] if 'mass' in planet and planet['mass'] else 0)
    return heaviest['englishName'], heaviest['mass']['massValue']

# Main execution code
planets = fetch_planet_data()

# Filter out non-planet bodies
planets = [planet for planet in planets if planet['isPlanet']]

# Display each planet's details
for planet in planets:
    name = planet['englishName']
    mass = planet.get('mass', {}).get('massValue', 'Unknown')
    orbit_period = planet.get('sideralOrbit', 'Unknown')
    print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")

# Find and display the heaviest planet
heaviest_name, heaviest_mass = find_heaviest_planet(planets)
print(f"\nThe heaviest planet is {heaviest_name} with a mass of {heaviest_mass} kg.")
