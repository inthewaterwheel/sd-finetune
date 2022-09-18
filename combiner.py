dir = "results/pokemon/poke_diffusion_v0"

import os
from PIL import Image

# combine 4 images in the directory into one

files = [x for x in os.listdir(dir) if (x.endswith(".png") or x.endswith(".webp"))]
files.sort()

images = [Image.open(dir + "/" + f) for f in files]

width, height = images[0].size

result = Image.new("RGB", (width * 2, height * 2))

result.paste(im=images[0], box=(0, 0))
result.paste(im=images[1], box=(width, 0))
result.paste(im=images[2], box=(0, height))
result.paste(im=images[3], box=(width, height))

# split filename at last _ and add _combined
filename = files[0].rsplit("_", 1)[0] + "_combined.png"

result.save(dir + "/" + filename)
