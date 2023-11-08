import matplotlib.pyplot as plt
import numpy as np
import csv

tumble_val = 0.2 #edit this for other files

frame = []
orientation = []

with open("t_{}.txt".format(tumble_val),'r') as file:
    reader = csv.reader(file,delimiter=' ')
    for row in reader:
        frame.append(int(row[0]))
        orientation.append(float(row[1]))

print(frame)

print (orientation)

fig,ax=plt.subplots(1,1,figsize=(4,4))

ax.plot(frame,orientation,color='red')
ax.scatter(frame,orientation,c='purple')
ax.set_xlabel("Frame Number")
ax.set_ylabel("Total Orientation")

plt.show()