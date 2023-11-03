import cv2
import numpy as np

image = cv2.imread('fig2.png', cv2.IMREAD_GRAYSCALE)

# create a mask to store regions
mask = np.zeros_like(image, dtype=np.uint8)

def region_growing(image, mask, seed, region_num):
    height, width = image.shape[:2]
    queue = [seed]
    while queue:
        x, y = queue.pop()
        if mask[x, y] == 0 and (image[x, y] == image[seed]): 
            mask[x, y] = region_num  # assign a unique number to each shape
            neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1),(x-1,y-1),(x-1,y+1),(x+1,y-1),(x+1,y+1)]  
            for nx, ny in neighbors:
                if 0 <= nx < height and 0 <= ny < width:
                    queue.append((nx, ny))

colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  # blue, green, red

region_num = 1
for x in range(image.shape[0]):
    for y in range(image.shape[1]):
        if image[x, y] == 0 and mask[x, y] == 0:  # check if the pixel is black and not touched
            region_growing(image, mask, (x, y), region_num)  
            region_num += 1

# create a color image
color_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

# assign colors to rwegions
for i in range(1, region_num):
    region_mask = (mask == i)
    #print(color_image[region_mask])

    #color_image[x][y] = colors[ 1 % 3] = colors[1]= (0, 255, 0)
    color_image[region_mask] = colors[i % len(colors)]

cv2.imshow('Segmented Image', color_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
