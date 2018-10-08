import matplotlib.pyplot as plt
import numpy as np
import csv

t = []
x_odom = []
y_odom = []
x_odom_camera = []
y_odom_camera = []

with open('data4.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        t.append(float(row[0]))
        x_odom.append(float(row[1]))
        y_odom.append(float(row[2]))
        # don't forget the multiply by -1
        x_odom_camera.append(np.multiply(1, float(row[3])))
        y_odom_camera.append(np.multiply(1, float(row[4])))

# plt1.plot(t,x_odom, label='odom')
# plt1.plot(t,x_odom_camera, label='camera')
plt.plot(x_odom, y_odom, label='odom')
plt.plot(x_odom_camera, y_odom_camera, label='camera')

plt.xlabel('time')
plt.ylabel('x [m]')
plt.title('Difference btw 2 measurments from different sensors \n Movment in x direction')
plt.legend()
plt.show()
