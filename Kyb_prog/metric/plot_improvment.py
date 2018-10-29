import matplotlib.pyplot as plt
import numpy as np
import csv
import tf
import tf.transformations

# Initialize and Read data from CSV
time = []
increment_time = 0.1
base_link_x_odom_camera = []
base_link_y_odom_camera = []


err_angle = []
err_dist = []
vect_yaw = []
velocity = []
predict_x = []
predict_y = []
err_predict = []

# cost_vector.append(alpha_1 * err_dist[i] + alpha_2 * err_predict[i] + alpha_3 * err_angle[i])
alpha_1 = 2#1
alpha_2 = 2#1
alpha_3 = 0.5
threshold = 1.0 #0.8
cost_vector = []

points = []
n_1 = []
def function(file_name_arg):
  #*******************************************************************************
  #           Parameters
  #*******************************************************************************

  file_name = file_name_arg


  #*******************************************************************************
  #           Get data from .csv
  #*******************************************************************************

  # del base_link_x_odom_camera[:]
  # del base_link_y_odom_camera[:]

  # with open(file_name,'r') as csvfile:
  #     next(csvfile)
  #     plots = csv.reader(csvfile, delimiter=',')
  #
  #     for row in plots:
  #         # don't forget the multiply by -1
  #         time.append(float(row[3]))
  #         base_link_x_odom_camera.append(np.multiply(1, float(row[6])))
  #         base_link_y_odom_camera.append(np.multiply(1, float(row[7])))
  #         (roll, pitch, yaw) = tf.transformations.euler_from_quaternion([0, 0, float(row[11]), float(row[12])])
  #         vect_yaw.append(yaw)
  #         velocity.append(float(row[14]))
  #
  # predict_x.append(float(0))
  # predict_y.append(float(0))
  # for i in range(1, base_link_x_odom_camera.size):
  #   # Close to covariance
  #   # Compare the error between the position actual position with the one before
  #   err_dist.append(np.power(np.power(base_link_x_odom_camera[i] - base_link_x_odom_camera[i-1], 2) + np.power(base_link_y_odom_camera[i] - base_link_y_odom_camera[i-1], 2)), 0.5)
  #   # Error btw where it should be and where it is
  #   predict_x.append(base_link_x_odom_camera[i-1] + increment_time * cos(vect_yaw[i-1]) * velocity[i-1])
  #   predict_y.append(base_link_y_odom_camera[i-1] + increment_time * sin(vect_yaw[i-1]) * velocity[i-1])
  #   err_predict.append(np.power(np.power(predict_x[i] - base_link_x_odom_camera[i], 2) + np.power(predict_y[i] - base_link_y_odom_camera[i], 2)), 0.5) # still positive
  #   # Error in direction compare to direction (normalized)
  #   err_angle.append((atan2(predict_y[i] - base_link_y_odom_camera[i-1], predict_x[i] - base_link_x_odom_camera[i-1]) - atan2(base_link_y_odom_camera[i] - base_link_y_odom_camera[i-1], base_link_x_odom_camera[i] - base_link_x_odom_camera[i-1]))/(2*3.1457))
  #   # Cost vector
  #   cost_vector.append(alpha_1 * err_dist + alpha_2 * err_predict + alpha_3 * err_angle)

  # x_err_1 = np.empty((numberPoints, len(base_link_x_odom_camera)))
  # y_err_1 = np.empty((numberPoints, len(base_link_x_odom_camera)))
  # err_abs_1 = np.empty((numberPoints, len(base_link_x_odom_camera)))
  # err_min_1 = np.empty((numberPoints, 1))
  # n_1 = np.empty((numberPoints, 1))

  #*******************************************************************************
  #           Min calulation
  #*******************************************************************************

  #  Assumptions : - The min point from odom are the closest to Strecke_1, if the
  #  robot drift, you could not have the real min which that mean it pass not in
  #  the right moment moment where you think.
  # for i in range(0, numberPoints, 1):#len(base_link_x_odom_camera), 1):
  #     # print(Strecke_1[i][0])
  #     x_err_1[i,] = np.subtract(data_soll[i][0], base_link_x_odom_camera)
  #     y_err_1[i,] = np.subtract(data_soll[i][1], base_link_y_odom_camera)
  #     err_abs_1[i,] = np.power(np.add(np.power(x_err_1[i,], 2), np.power(y_err_1[i,], 2)), 0.5)
  #     err_min_1[i] = min(err_abs_1[i,])
  #     n_1[i] = err_abs_1[i,].tolist().index(min(err_abs_1[i,]))
  #     # end of the loop

  return (err_min_1, err_min_1, n_1, Strecke_1)

if __name__== "__main__":

    plt.rcParams.update({'font.size': 30})
    file_name = 'straight-base_link_odom_camera_is1500.csv'

    with open(file_name,'r') as csvfile:
      next(csvfile)
      plots = csv.reader(csvfile, delimiter=',')

      for row in plots:
          # don't forget the multiply by -1
          time.append(float(row[3]))
          base_link_x_odom_camera.append(np.multiply(1, float(row[6])))
          base_link_y_odom_camera.append(np.multiply(1, float(row[7])))
          (roll, pitch, yaw) = tf.transformations.euler_from_quaternion([0, 0, float(row[11]), float(row[12])])
          vect_yaw.append(yaw)
          velocity.append(float(row[14]))

    predict_x.append(float(0))
    predict_y.append(float(0))
    cost_vector.append(float(0))
    err_dist.append(float(0))
    err_predict.append(float(0))
    err_angle.append(float(0))
    for i in range(1,  len(base_link_x_odom_camera)):
        # Close to covariance
        # Compare the error between the position actual position with the one before
        err_dist.append(np.power(np.power(base_link_x_odom_camera[i] - base_link_x_odom_camera[i-1], 2) + np.power(base_link_y_odom_camera[i] - base_link_y_odom_camera[i-1], 2), 0.5))
        # Error btw where it should be and where it is
        predict_x.append(base_link_x_odom_camera[i-1] + increment_time * np.cos(vect_yaw[i-1]) * velocity[i-1])
        predict_y.append(base_link_y_odom_camera[i-1] + increment_time * np.sin(vect_yaw[i-1]) * velocity[i-1])
        err_predict.append(np.power(np.power(predict_x[i] - base_link_x_odom_camera[i], 2) + np.power(predict_y[i] - base_link_y_odom_camera[i], 2), 0.5)) # still positive
        # Error in direction compare to direction (normalized)
        err_angle.append(np.absolute((np.arctan2(predict_y[i] - base_link_y_odom_camera[i-1], predict_x[i] - base_link_x_odom_camera[i-1]) - np.arctan2(base_link_y_odom_camera[i] - base_link_y_odom_camera[i-1], base_link_x_odom_camera[i] - base_link_x_odom_camera[i-1]))/(2*3.1457)))
        # Cost vector
        # print(alpha_1 * err_dist + alpha_2 * err_predict + alpha_3 * err_angle)
        cost_vector.append(alpha_1 * err_dist[i] + alpha_2 * err_predict[i] + alpha_3 * err_angle[i])
        if(cost_vector[i] > threshold):
            print('cost_vector: ', cost_vector[i], ', err_dist: ', err_dist[i], ', err_predict: ', err_predict[i],  ', err_angle: ', err_angle[i])
            points.append([base_link_x_odom_camera[i], base_link_y_odom_camera[i]])
            n_1.append(i)
            print(points)
    # print(cost_vector)

    f = plt.figure(1, figsize=(40, 32))
    ax = f.add_subplot(111)
    for i in range(0, len(points), 1):
    #     plt.plot(Strecke_1[int(i)][int(0)], Strecke_1[int(i)][int(1)], 'o' ,color='red', markersize=20, label="Ground truth Point " +str(i+1) + ": "+str(Strecke_1[i]))
        plt.plot(base_link_x_odom_camera[int(n_1[i])], base_link_y_odom_camera[int(n_1[i])], 'o' ,color='red', markersize=20, label="Jump " +str(i+1))
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
    plt.xlim(0.0, 7.0)
    plt.ylim(0.0, -7.0)
    # plt.title('Measurment of the odometry' + '\n' + file_name)
    # plt.legend()
    plt.legend(numpoints=1, bbox_to_anchor=(0., 1.02, 1., .102), loc=1,
               ncol=3, mode="expand", borderaxespad=0.) #bbox_to_anchor=(0., 1.02, 1., .102)
    # plt.legend(numpoints=1, bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    # plt.legend(numpoints=1, bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    # f.set_size_inches(20, 15)
    # f.savefig(file_name+'.png')
    # plt.close(f)

    plt.show()
