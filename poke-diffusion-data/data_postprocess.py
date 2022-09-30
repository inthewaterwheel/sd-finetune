import json
import os
from PIL import Image

# read pokemon.json
# check if the pokemon exists in images
# read the image if so
# resize the image to 512x512
# save the image as "official_art_of_${pokemon},_${type1},_${type2}.png"

with open("data/pokemon.json", "r") as f:
    pokemon = json.load(f)

images = os.listdir("data/images")

errors_count = 0
ind = 0
for p in pokemon:
    im_name = ""
    if len(p["id"]) == 1:
        im_name = p["name"] + ".png"
    else:
        im_name = p["id"][1:] + p["name"] + ".png"

    if im_name in images:
        ind += 1
        name = f"image{ind:03d}"
        try:
            im = Image.open("data/images/" + im_name)
            im = im.resize((512, 512))
            im = im.convert("RGB")
            name_piece = (
                "official_art_of_pokemon_"
                + p["name"]
                + ",_"
                + p["types"][0]
                + (",_" + p["types"][1] if len(p["types"]) > 1 else "")
            )
            im.save("data/processed_images/img/" + name + ".jpg")
            with open("data/processed_images/txt/" + name + ".txt", "w") as f:
                f.write(name_piece.replace("_", " "))
        except:
            # the image file is broken
            print("Error with", im_name)
            errors_count += 1

print("Found", errors_count, "errors")
