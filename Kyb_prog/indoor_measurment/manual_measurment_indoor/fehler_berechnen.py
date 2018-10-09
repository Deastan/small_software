import matplotlib.pyplot as plt
import numpy as np
import csv

#*******************************************************************************
#           Parameters
#*******************************************************************************

file_name = 'measure_1-base_link_odom_camera_is1500.csv'
#  Define waypoints
Strecke_1 = [[1, 1.5],
             [3.7, -1.5],
             [3.7,-6],
             [1,-6]]
numberPoints = len(Strecke_1) # number points of Ground_Truth
data_soll = Strecke_1;

# Initialize and Read data from CSV
base_link_x_odom_camera = []
base_link_y_odom_camera = []

#*******************************************************************************
#           Get data from .csv
#*******************************************************************************

with open(file_name,'r') as csvfile:
    next(csvfile)
    plots = csv.reader(csvfile, delimiter=',')

    for row in plots:
        # don't forget the multiply by -1

        base_link_x_odom_camera.append(np.multiply(1, float(row[6])))
        base_link_y_odom_camera.append(np.multiply(1, float(row[7])))


x_err_1 = np.empty((numberPoints, len(base_link_x_odom_camera)))
y_err_1 = np.empty((numberPoints, len(base_link_x_odom_camera)))
err_abs_1 = np.empty((numberPoints, len(base_link_x_odom_camera)))
err_min_1 = np.empty((numberPoints, 1))
n_1 = np.empty((numberPoints, 1))

#*******************************************************************************
#           Min calulation
#*******************************************************************************

#  Assumptions : - The min point from odom are the closest to Strecke_1, if the
#  robot drift, you could not have the real min which that mean it pass not in
#  the right moment moment where you think.
for i in range(0, numberPoints, 1):#len(base_link_x_odom_camera), 1):
    # print(Strecke_1[i][0])
    x_err_1[i,] = np.subtract(data_soll[i][0], base_link_x_odom_camera)
    y_err_1[i,] = np.subtract(data_soll[i][1], base_link_y_odom_camera)
    err_abs_1[i,] = np.power(np.add(np.power(x_err_1[i,], 2), np.power(y_err_1[i,], 2)), 0.5)
    err_min_1[i] = min(err_abs_1[i,])
    n_1[i] = err_abs_1[i,].tolist().index(min(err_abs_1[i,]))
    # end of the loop

#*******************************************************************************
#           Plot data
#*******************************************************************************
f = plt.figure(1)
for i in range(0, numberPoints, 1):
    # plt.plot(Strecke_1[int(i),int(1)], Strecke_1[int(i),int(0)], 'o' ,color='blue', markersize=20, label="Origin")
    plt.plot(base_link_x_odom_camera[int(n_1[i])], base_link_y_odom_camera[int(n_1[i])], 'o' ,color='blue', markersize=20, label="Point " +str(i+1) + ": " + str(err_min_1[i]) + " m")
plt.plot(base_link_x_odom_camera, base_link_y_odom_camera, label='Camera position in Base link frame')
# plt.plot(base_link_y_odom_camera_tf, base_link_x_odom_camera_tf, label='Camera position in Base link frame with tf')
# plt.plot(base_camera_y_odom_camera, base_camera_x_odom_camera, label='Camera position in Base camera frame')

plt.xlabel('y [m]')
plt.ylabel('x [m]')
plt.title('Measurment of the odometry')
# plt.legend()
plt.legend(numpoints=1, bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=2, mode="expand", borderaxespad=0.)
# f.show()

g = plt.figure(2)
for i in range(0, numberPoints, 1):
    # plt.plot(Strecke_1[int(i),int(1)], Strecke_1[int(i),int(0)], 'o' ,color='blue', markersize=20, label="Origin")
    plt.plot(base_link_x_odom_camera[int(n_1[i])], base_link_y_odom_camera[int(n_1[i])], 'o' ,color='blue', markersize=20, label="Point " +str(i+1) + ": " + str(err_min_1[i]) + " m")
plt.plot(base_link_x_odom_camera, base_link_y_odom_camera, label='Camera position in Base link frame')
# plt.plot(base_link_y_odom_camera_tf, base_link_x_odom_camera_tf, label='Camera position in Base link frame with tf')
# plt.plot(base_camera_y_odom_camera, base_camera_x_odom_camera, label='Camera position in Base camera frame')

plt.xlabel('y [m]')
plt.ylabel('x [m]')
plt.title('Measurment of the odometry')
# plt.legend()
plt.legend(numpoints=1, bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=2, mode="expand", borderaxespad=0.)
plt.show()
# raw_input()
