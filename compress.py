import os,consts
from PIL import Image

for dir in os.listdir(os.path.join(consts.klasor,'deneme2')):
    file=os.path.join(consts.klasor,'deneme2',dir)
    image=Image.open(file)
    image.save(os.path.join(consts.klasor,'deneme',file.split('\\')[-1]),optimize=True,quality=60)
    image.close()