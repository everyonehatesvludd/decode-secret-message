import requests
from bs4 import BeautifulSoup

def decode(url):
    response = requests.get(url)
    parser = BeautifulSoup(response.text, 'html.parser')

    coords = []
    table = parser.find('table')
    rows = table.find_all('tr')[1:] 

    for row in rows:
        cols = row.find_all('td')
        x = int(cols[0].text.strip())
        char = cols[1].text.strip()
        y = int(cols[2].text.strip())
        coords.append((x, char, y))
    
    maxX = max(x for x, _, _ in coords) + 1
    maxY = max(y for _, _, y in coords) + 1
    
    grid = [[' ' for _ in range(maxX)] for _ in range(maxY)]
    for x, char, y in coords:
        grid[maxY - 1 - y][x] = char
    
    for row in grid:
        print(''.join(row))


decode("https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub")