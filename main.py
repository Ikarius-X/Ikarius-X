import os
from PIL import Image
import numpy as np
import random

image_dir = '/Users/ikarius/Desktop/Images'

image_paths = []
for file in os.listdir(image_dir):
  if file.endswith('.png'):
    image_paths.append(os.path.join(image_dir, file))

print(f'Collected {len(image_paths)} images')

for image_path in image_paths:
  image = Image.open(image_path)
  image = image.resize((128, 128))
  image = image.crop((0, 0, 64, 64))
  file_name, file_ext = os.path.splitext(image_path)

  modified_image_path = file_name + '.png'

  image.save(modified_image_path)
image_array = np.array(image)
image_array = image_array / 255.0
random.shuffle(image_paths)
num_training_images = int(len(image_paths) * 0.8)
training_set = image_paths[:num_training_images]
test_set = image_paths[num_training_images:]
