import imageio
import numpy as np

images = []

x = 0

# Forward loop 
for x in range(0,101):
    images.append(imageio.imread('/content/lshape_center/image'+str(x)+'.png'))
  
# Backward loop
for x in range(100,0,-1):
    images.append(imageio.imread('/content/lshape_center/image'+str(x)+'.png'))


imageio.mimsave('movie.gif', images, fps=30)
