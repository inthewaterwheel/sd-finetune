from bs4 import BeautifulSoup
import requests
import json

# fetch the following webpage:
url = "https://bulbapedia.bulbagarden.net/w/api.php?action=parse&format=json&page=List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number"

# get the webpage, with a user-agent header
# Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36

page = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"},
)

# from page as json, get page["parse"]["text"]["*"] and parse it with BeautifulSoup
soup = BeautifulSoup(page.json()["parse"]["text"]["*"], "html.parser")

# find all tables that have align="center"
tables = soup.find_all("table", {"align": "center"})

print("Found", len(tables), "tables")

# convert each row in each table into a json
# id: 2nd column as text
# name: 4th column as text
# types: array containing 5th column, as well as 6th column if it exists

pokemon = []
for table in tables:
    rows = table.find_all("tr")
    for row in rows:
        cols = row.find_all("td")
        print(cols)
        if len(cols) == 0:
            continue
        id = cols[1].text.strip()
        name = cols[2].text.strip()
        types = [cols[3].text.strip()]
        if len(cols) > 4 and cols[4].text != "":
            types.append(cols[4].text.strip())
        pokemon.append({"id": id, "name": name, "types": types})

# save the json
with open("data/pokemon.json", "w") as f:
    json.dump(pokemon, f)
