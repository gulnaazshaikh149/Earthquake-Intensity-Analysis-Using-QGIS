import cv2
import glob
 
img_array = []
for filename in sorted(glob.glob('pics/*.png')):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)

# this will generate a video called pirates.avi that runs at 5 frames per second
out = cv2.VideoWriter('pirates.avi',cv2.VideoWriter_fourcc(*'DIVX'), 5, size)

for i in range(len(img_array)):
    out.write(img_array[i])
out.release()