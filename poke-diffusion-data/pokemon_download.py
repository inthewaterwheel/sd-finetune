import json
import requests
import concurrent.futures

# read the pokemon.json file
with open("data/pokemon.json", "r") as f:
    pokemon = json.load(f)

# for each pokemon, construct the image url
# eg: https://bulbapedia.bulbagarden.net/w/index.php?title=Special:FilePath&file=001Bulbasaur.png

base_url = "https://bulbapedia.bulbagarden.net/w/index.php?title=Special:FilePath&file="
with concurrent.futures.ThreadPoolExecutor(16) as executor:
    for p in pokemon:
        im_name = ""
        if len(p["id"]) == 1:
            im_name = p["name"] + ".png"
        else:
            im_name = p["id"][1:] + p["name"] + ".png"

        # download the image
        url = base_url + im_name
        print("Downloading", url)
        r = executor.submit(requests.get, url, stream=True)
        with open("data/images/" + im_name, "wb") as f:
            for chunk in r.result().iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
