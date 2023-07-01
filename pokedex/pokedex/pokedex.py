import os
import requests
import json

def get_pokemon_data(pokemon_name):
    # Construir la URL para obtener los datos del Pokémon
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    
    # Realizar la solicitud GET a la API
    response = requests.get(url)
    
    # Verificar si el Pokémon existe o no
    if response.status_code == 404:
        raise ValueError("Este pokemon no existe JAJAJA.")
    
    # Obtener los datos del Pokémon en formato JSON
    pokemon_data = response.json()
    return pokemon_data

def save_pokemon_info(pokemon_name, pokemon_data):
    # Crear un directorio 'pokedex' si no existe
    pokedex_dir = "pokedex"
    if not os.path.exists(pokedex_dir):
        os.makedirs(pokedex_dir)

    # Construir la ruta del archivo .json para guardar los datos del Pokémon
    file_path = os.path.join(pokedex_dir, f"{pokemon_name.lower()}.json")
    
    # Guardar los datos del Pokémon en un archivo .json
    with open(file_path, "w") as file:
        json.dump(pokemon_data, file)

def download_pokemon_image(pokemon_name, sprite_url):
    # Crear un directorio 'pokedex' si no existe
    pokedex_dir = "pokedex"
    if not os.path.exists(pokedex_dir):
        os.makedirs(pokedex_dir)

    # Construir la ruta de la imagen del Pokémon
    image_path = os.path.join(pokedex_dir, f"{pokemon_name.lower()}.png")
    
    # Descargar la imagen frontal del Pokémon desde la URL proporcionada
    response = requests.get(sprite_url)
    with open(image_path, "wb") as image_file:
        image_file.write(response.content)

def display_pokemon_info(pokemon_data):
    # Mostrar la información del Pokémon
    print("Nombre del pokemon:", pokemon_data["name"].capitalize())
    print("Peso del pokemon:", pokemon_data["weight"])
    print("Altura del pokemon:", pokemon_data["height"])
    print("Movimientos del pokemon:")
    for move in pokemon_data["moves"]:
        print("-", move["move"]["name"].capitalize())
    print("Habilidades del pokemon:")
    for ability in pokemon_data["abilities"]:
        print("-", ability["ability"]["name"].capitalize())
    print("Tipo de pokemon:")
    for type_entry in pokemon_data["types"]:
        print("-", type_entry["type"]["name"].capitalize())

def search_pokemon(pokemon_name):
    try:
        # Obtener los datos del Pokémon
        pokemon_data = get_pokemon_data(pokemon_name)
        
        # Guardar los datos del Pokémon en un archivo .json
        save_pokemon_info(pokemon_name, pokemon_data)
        
        # Obtener la URL de la imagen frontal del Pokémon
        sprite_url = pokemon_data["sprites"]["front_default"]
        
        # Descargar la imagen frontal del Pokémon
        download_pokemon_image(pokemon_name, sprite_url)
        
        # Mostrar la información del Pokémon
        display_pokemon_info(pokemon_data)
    except ValueError as e:
        # Mostrar el mensaje de error si el Pokémon no fue encontrado
        print("Equivocado", str(e))

def main():
    # Solicitar al usuario el nombre de un Pokémon
    pokemon_name = input("Ingresa el nombre de algun pokemon: ")
    
    # Buscar y mostrar información del Pokémon
    search_pokemon(pokemon_name)

if __name__ == "__main__":
    # Ejecutar la función main si el archivo se ejecuta directamente
    main()