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
Strecke_1 = [[2.124, -1.558]]
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


plt.rcParams.update({'font.size': 30})

# print(Strecke_1[int(1)][int(1)])
f = plt.figure(1, figsize=(30, 21))
plt.plot(Strecke_1[int(0)][int(0)], Strecke_1[int(0)][int(1)], 'o' ,color='red', markersize=20, label="Ground truth Point ")
plt.plot(base_link_x_odom_camera, base_link_y_odom_camera, label='Camera position in Base link frame')
plt.xlabel('x [m]')
plt.ylabel('y [m]')
plt.legend(numpoints=1, bbox_to_anchor=(0., 1.02, 1., .102), loc=1,
           ncol=3, mode="expand", borderaxespad=0.)#bbox_to_anchor=(0., 1.02, 1., .102)
f.savefig(file_name+'.png')
# plt.close(f)


plt.show()
