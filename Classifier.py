import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = tensorflow.keras.models.load_model('./Trained-Model/keras_model.h5')
# print(model)
# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1.
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# Replace this with the path to your image
# Image path from the drag and drop code.
image = Image.open('')

#resize the image to a 224x224 with the same strategy as in TM2:
#resizing the image to be at least 224x224 and then cropping from the center
size = (224, 224)
image = ImageOps.fit(image, size, Image.ANTIALIAS)

#turn the image into a numpy array
image_array = np.asarray(image)

# display the resized image
# image.show()

# Normalize the image
normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

# Load the image into the array
data[0] = normalized_image_array

# run the inference
prediction = model.predict(data)
# print(prediction)

new = str(prediction)
# print(new)
new = new.replace('[','')
new = new.replace(']','')
length = len(new)
# print(length)
new1 = new
elliptical_galaxy = ""
irregular_galaxy = ""
spiral_galaxy = ""
for i in range(0,length):
  if new[i]==" ":
    j=i
    new = new[j:length]
    new = new.strip()
    break
  else:
    elliptical_galaxy = elliptical_galaxy + new[i]
# print(elliptical_galaxy)
# print(new)
length = len(new)
for i in range(0,length):  
  if new[i]==" ":
    j=i
    new = new[j:length]
    new = new.strip()
    break
  else:
    irregular_galaxy = irregular_galaxy + new[i]
# print(irregular_galaxy)
length = len(new)
for i in range(0,length):
  if new[i]==" ":
    j=i
    new = new[j:length]
    new = new.strip()
    break
  else:
    spiral_galaxy = spiral_galaxy + new[i]
print("Elliptical Galaxy: ",float(elliptical_galaxy)*100,"%")
print("Irregular Galaxy: ",float(irregular_galaxy)*100,"%")
print("Spiral Galaxy: ",float(spiral_galaxy)*100,"%")