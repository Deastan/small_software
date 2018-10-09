import matplotlib.pyplot as plt
import numpy as np
import csv


# Initialize and Read data from CSV
base_link_x_odom_camera = []
base_link_y_odom_camera = []


#*******************************************************************************
#           Parameters
#*******************************************************************************
file_name = 'drift-base_link_odom_camera_is1500.csv'

#  Define waypoints
Strecke_1 = [[2.080, -1.544]]
numberPoints = len(Strecke_1) # number points of Ground_Truth
data_soll = Strecke_1;


#*******************************************************************************
#           Get data from .csv
#*******************************************************************************

del base_link_x_odom_camera[:]
del base_link_y_odom_camera[:]
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
    # print(Strecke_1[i][0])
x_err_1 = np.subtract(data_soll[0][0], base_link_x_odom_camera)
y_err_1 = np.subtract(data_soll[0][1], base_link_y_odom_camera)
err_abs_1 = np.power(np.add(np.power(x_err_1, 2), np.power(y_err_1, 2)), 0.5)
err_min_1 = min(err_abs_1)
n_1 = err_abs_1.tolist().index(min(err_abs_1))
    # end of the loop

# print(np.var(base_link_x_odom_camera))
# print(np.var(base_link_y_odom_camera))

plt.rcParams.update({'font.size': 30})

# print(Strecke_1[int(1)][int(1)])
f = plt.figure(1, figsize=(30, 21))
plt.plot(0, 0, 'o' ,color='black', markersize=10, label="Origin, variance on x : " + str(np.var(base_link_x_odom_camera))+", variance on y : " + str(np.var(base_link_y_odom_camera)))
plt.plot(Strecke_1[int(0)][int(0)], Strecke_1[int(0)][int(1)], 'o' ,color='red', markersize=10, label="Ground truth Point, error = " + str(err_min_1))
plt.plot(base_link_x_odom_camera, base_link_y_odom_camera, label='Robot position in camera frame')
plt.plot(label='Variance on x : ' + str(np.var(base_link_x_odom_camera)))
plt.xlabel('x [m]')
plt.ylabel('y [m]')
plt.legend(numpoints=1, bbox_to_anchor=(0., 1.02, 1., .102), loc=1,
           ncol=1, mode="expand", borderaxespad=0.)#bbox_to_anchor=(0., 1.02, 1., .102)
f.savefig(file_name+'.png')
# plt.close(f)


plt.show()
