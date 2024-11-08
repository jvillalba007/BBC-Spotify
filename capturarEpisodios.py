import requests
import sys
import os
from bs4 import BeautifulSoup

start = int(sys.argv[1]) if len(sys.argv) > 1 else 0
BBC = True

# URL del programa específico
program_url = "https://www.bbc.co.uk/sounds/brand/m000883z"

# Realizar la solicitud HTTP
response = requests.get(program_url)
soup = BeautifulSoup(response.content, 'html.parser')

# Encontrar la sección con id "container_list"
container = soup.find('section', id='container_list')

# Verificar si se encontró el contenedor y extraer la información de los episodios
if container:
    episodes = container.find_all('div', class_='sw-grow sw--ml-2 m:sw--ml-4 sw-relative')
    for episode in episodes[start:]:
        episode_url = episode.find('a')['href']
        episode_title = episode.find('a')['aria-label'].strip()
        full_url = f"https://www.bbc.co.uk{episode_url}"
        print(f"BBC URL: {full_url}")
        print(f"Episode: {episode_title}")
        if BBC == True:
        	print("Ejecuta Script") 
        	os.system(f'python3 BBC-Spotify.py {full_url}')
    else:
        print("No se encontraron episodios en el contenedor especificado.")
else:
    print("No se encontró la sección con id 'container_list'.")


