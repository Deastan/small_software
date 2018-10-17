import matplotlib.pyplot as plt
import numpy as np
import csv


# Initialize and Read data from CSV
base_link_x_odom_camera = []
base_link_y_odom_camera = []

def function(file_name_arg):
  #*******************************************************************************
  #           Parameters
  #*******************************************************************************

  file_name = file_name_arg
  #  Define waypoints
  Strecke_1 = [[1, -1.5],
               [3.7, -1.5],
               [3.7,-6],
               [1,-6]]
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
  for i in range(0, numberPoints, 1):#len(base_link_x_odom_camera), 1):
      # print(Strecke_1[i][0])
      x_err_1[i,] = np.subtract(data_soll[i][0], base_link_x_odom_camera)
      y_err_1[i,] = np.subtract(data_soll[i][1], base_link_y_odom_camera)
      err_abs_1[i,] = np.power(np.add(np.power(x_err_1[i,], 2), np.power(y_err_1[i,], 2)), 0.5)
      err_min_1[i] = min(err_abs_1[i,])
      n_1[i] = err_abs_1[i,].tolist().index(min(err_abs_1[i,]))
      # end of the loop

  return (err_min_1, err_min_1, n_1, Strecke_1)

if __name__== "__main__":

    plt.rcParams.update({'font.size': 30})

    file_name = 'squarewith_bad_end-GPS_Dragonfly.csv'
    err_min_1, err_min_1, n_1, Strecke_1 = function(file_name)
    # print(Strecke_1[int(1)][int(1)])
    f = plt.figure(1, figsize=(40, 32))
    ax = f.add_subplot(111)
    # for i in range(0, len(Strecke_1), 1):
        # plt.plot(Strecke_1[int(i)][int(0)], Strecke_1[int(i)][int(1)], 'o' ,color='red', markersize=20, label="Ground truth Point " +str(i+1) + ": "+str(Strecke_1[i]))
        # plt.plot(base_link_x_odom_camera[int(n_1[i])], base_link_y_odom_camera[int(n_1[i])], 'o' ,color='blue', markersize=20, label="Point " +str(i+1) + ": " + str(err_min_1[i]) + " m")
        # plt.annotate(
        #     str('( ' + str(Strecke_1[int(i)][int(0)]) +', ' + str(Strecke_1[int(i)][int(1)]) + ')'),
        #     xy=((Strecke_1[int(i)][int(0)]+0.0), (Strecke_1[int(i)][int(1)])+0.0), xytext=(-10, 10),
        #     textcoords='offset points', ha='right', va='bottom',
        #     bbox=dict(boxstyle='round,pad=0.5', fc='grey', alpha=0.5),
        #     arrowprops=dict(arrowstyle = '->', connectionstyle='arc3,rad=0'))
    plt.plot(base_link_x_odom_camera, base_link_y_odom_camera, label='Robot position in camera frame')
    # plt.plot(base_link_y_odom_camera_tf, base_link_x_odom_camera_tf, label='Camera position in Base link frame with tf')
    # plt.plot(base_camera_y_odom_camera, base_camera_x_odom_camera, label='Camera position in Base camera frame')
    # ax.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
    #         arrowprops=dict(facecolor='black', shrink=0.05),
    #         )


    plt.xlabel('x [m]')
    plt.ylabel('y [m]')
    # plt.title('Measurment of the odometry' + '\n' + file_name)
    # plt.legend()
    plt.legend(numpoints=1, bbox_to_anchor=(0., 1.02, 1., .102), loc=1,
               ncol=3, mode="expand", borderaxespad=0.)#bbox_to_anchor=(0., 1.02, 1., .102)
    # plt.legend(numpoints=1, bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    # plt.legend(numpoints=1, bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    # f.set_size_inches(20, 15)
    f.savefig(file_name+'.png')
    # plt.close(f)

    plt.show()
