import matplotlib.pyplot as plt
import numpy as np
import csv

# t = []
# x_odom = []
# y_odom = []
# theta_odom = []
base_link_x_odom_camera = []
base_link_y_odom_camera = []
# base_link_theta_odom_camera = []
base_camera_x_odom_camera = []
base_camera_y_odom_camera = []
# base_camera_theta_odom_camera = []

with open('data_simple.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        # t.append(float(row[0]))
        # x_odom.append(float(row[1]))
        # y_odom.append(float(row[2]))
        # theta_odom.append(float(row[3]))
        # don't forget the multiply by -1
        base_link_x_odom_camera.append(np.multiply(1, float(row[2])))
        base_link_y_odom_camera.append(np.multiply(1, float(row[3])))
        # base_link_theta_odom_camera.append(np.multiply(1, float(row[6])))
        base_camera_x_odom_camera.append(np.multiply(1, float(row[0])))
        base_camera_y_odom_camera.append(np.multiply(1, float(row[1])))
        # base_camera_theta_odom_camera.append(np.multiply(1, float(row[9])))

# plt1.plot(t,x_odom, label='odom')
# plt1.plot(t,x_odom_camera, label='camera')
# plt.plot(x_odom, y_odom, label='odom')
# plt.plot(base_link_y_odom_camera, base_link_x_odom_camera, label='Camera position in Base link frame')
plt.plot(base_camera_y_odom_camera, base_camera_x_odom_camera, label='Camera position in Base camera frame')

plt.xlabel('y [m]')
plt.ylabel('x [m]')
plt.title('Measurment of the odometry')
plt.legend()
plt.show()
