import os, random
from io import BytesIO
from captcha.image import ImageCaptcha

# what fonts are we going to use?
# update this later to use all fonts in /fonts
image = ImageCaptcha(fonts=['fonts/OpenSans-Regular.ttf'])

#check if training/validation/test folders exist and make them if not
def make_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# the number of training, validation, and test examples; respectively
examples = {'training': 50000, 'validation': 10000, 'test': 10000}

for i, key in enumerate(examples):
    print(i, key)
    make_dir(key)
    
    for j in range(examples[key]):
        my_random = random.randrange(100000, 1000000)
        data = image.generate('{}'.format(my_random))
        assert isinstance(data, BytesIO)
        image.write('{}'.format(my_random), '{}/{}.png'.format(key, j+1))
