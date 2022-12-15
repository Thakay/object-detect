import cv2 
   
# path 
path = r'./zidane.jpg'
   
# Reading an image in default mode
image = cv2.imread(path)
   
# Window name in which image is displayed
window_name = 'Image'
  
# Start coordinate, here (5, 5)
# represents the top left corner of rectangle
start_point = (123, 193)
  
# Ending coordinate, here (220, 220)
# represents the bottom right corner of rectangle
end_point = (600 ,720)
  
# Blue color in BGR
color = (0, 0, 255)
  
# Line thickness of 2 px
thickness = 2
  
# Using cv2.rectangle() method
# Draw a rectangle with blue line borders of thickness of 2 px
image = cv2.rectangle(image, start_point, end_point, color, thickness)
  
# Displaying the image 
cv2.imwrite("./draw.jpg", image)