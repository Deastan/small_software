import matplotlib.pyplot as plt
import numpy as np
import csv

base_link_x_odom_camera = []
base_link_y_odom_camera = []
# base_link_theta_odom_camera = []
base_camera_x_odom_camera = []
base_camera_y_odom_camera = []
l = 0.835

with open('data_simple.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        # t.append(float(row[0]))
        # x_odom.append(np.multiply(-1, float(row[8])))
        # y_odom.append(np.multiply(-1, float(row[9])))
        # theta_odom.append(float(row[3]))
        # don't forget the multiply by -1
        base_camera_x_odom_camera.append(np.multiply(1, float(row[0])))
        base_camera_y_odom_camera.append(np.multiply(1, float(row[1])))

        base_link_x_odom_camera.append(np.multiply(1, float(row[2])))
        base_link_y_odom_camera.append(np.multiply(1, float(row[3])))


    # Plot For Ground_Truth
    plt.plot(0,0 , 'ro', markersize=20, label="Origin")

plt.plot(base_link_y_odom_camera, base_link_x_odom_camera, label='Camera position in Base link frame')
plt.plot(base_camera_y_odom_camera, base_camera_x_odom_camera, label='Camera position in Base camera frame')

plt.xlabel('y [m]')
plt.ylabel('x [m]')
plt.title('Measurment of the odometry')
plt.legend()
plt.show()
