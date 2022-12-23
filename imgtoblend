import os
from PIL import Image
import numpy as np
import random

# Set the directory where the images are stored
image_dir = '/Users/ikarius/Desktop/Images'

# Collect all the image file paths in the directory
image_paths = []
for file in os.listdir(image_dir):
  if file.endswith('.png'):
    image_paths.append(os.path.join(image_dir, file))

# Print the number of images collected
print(f'Collected {len(image_paths)} images')

# Iterate over the image paths
for image_path in image_paths:
  image = Image.open(image_path)
  # Resize the image
  image = image.resize((128, 128))
  # Crop the image
  image = image.crop((0, 0, 64, 64))
  # Split the file name and extension from the file path
  file_name, file_ext = os.path.splitext(image_path)

  # Construct a new file path with a different extension
  modified_image_path = file_name + '.png'

  # Save the image with the modified file path
  image.save(modified_image_path)
# Convert the image to a numpy array
image_array = np.array(image)
# Normalize the array by dividing all the values by 255
image_array = image_array / 255.0
# Shuffle the images
random.shuffle(image_paths)
# Calculate the number of images for the training set
num_training_images = int(len(image_paths) * 0.8)
# Split the images into the training set and the test set
training_set = image_paths[:num_training_images]
test_set = image_paths[num_training_images:]
