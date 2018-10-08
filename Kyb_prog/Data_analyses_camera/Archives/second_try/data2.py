import matplotlib.pyplot as plt
import csv

t = []
x_odom = []
x_odom_camera = []

with open('data2.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        t.append(float(row[0]))
        x_odom.append(float(row[1]))
        x_odom_camera.append(float(row[2]))

plt.plot(t,x_odom, label='odom')
plt.plot(t,x_odom_camera, label='camera')
plt.xlabel('time')
plt.ylabel('x [m]')
plt.title('Difference btw 2 measurments from different sensors \n Movment in x direction')
plt.legend()
plt.show()
