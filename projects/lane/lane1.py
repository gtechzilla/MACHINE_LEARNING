import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2
import math

# reading in an image

image = mpimg.imread('road3.jpeg')
print(image.shape)

def region_of_interest(img, vertices):
    # Define a blank matrix that matches the image height/width.
    mask = np.zeros_like(img)

    # Retrieve the number of color channels of the image.
    channel_count = img.shape[2]

    # Create a match color with the same color channel counts.
    match_mask_color = (255,) * channel_count
      
    # Fill inside the polygon
    cv2.fillPoly(mask, vertices, match_mask_color)
    
    # Returning the image only where mask pixels match
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image

height=image.shape[0]
width=image.shape[1]


region_of_interest_vertices = [
    (0, height),
    (width / 2, height / 2),
    (width, height),
]


cropped_image = region_of_interest(
    image,
    np.array([region_of_interest_vertices], np.int32),
)

plt.figure()
plt.imshow(cropped_image)


# Convert to grayscale here.
gray_image = cv2.cvtColor(cropped_image, cv2.COLOR_RGB2GRAY)

# Call Canny Edge Detection here.
cannyed_image = cv2.Canny(gray_image, 100, 200)

print(cannyed_image.shape)
'''# Moved the cropping operation to the end of the pipeline.
cropped_image = region_of_interest(
    cannyed_image,
    np.array([region_of_interest_vertices], np.int32)
)
'''
plt.figure()
plt.imshow(cropped_image)

plt.show()
