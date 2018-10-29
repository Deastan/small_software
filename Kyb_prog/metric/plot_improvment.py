import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv
import tf
import tf.transformations

# Initialize and Read data from CSV
time = []
increment_time = 0.1
pos_x = []
pos_y = []


err_angle = []
err_dist = []
vect_yaw = []
velocity = []
predict_x = []
predict_y = []
err_predict = []

# cost_vector = alpha_1 * err_dist[i] +
#               alpha_2 * err_predict[i] +
#               alpha_3 * err_angle[i]
alpha_1 = 1.5#1
alpha_2 = 1.5#1
alpha_3 = 0.5
threshold = 1.0 #0.8
cost_vector = []

points = []
n_1 = []

y = []

if __name__== "__main__":

    plt.rcParams.update({'font.size': 30})
    file_name = 'straight-base_link_odom_camera_is1500.csv'

    with open(file_name,'r') as csvfile:
      next(csvfile)
      plots = csv.reader(csvfile, delimiter=',')

      for row in plots:
          # don't forget the multiply by -1
          time.append(float(row[3]))
          pos_x.append(np.multiply(1, float(row[6])))
          pos_y.append(np.multiply(1, float(row[7])))
          (roll, pitch, yaw) = tf.transformations.euler_from_quaternion([0, 0,
            float(row[11]), float(row[12])])
          vect_yaw.append(yaw)
          velocity.append(float(row[14]))

    predict_x.append(float(0))
    predict_y.append(float(0))
    cost_vector.append(float(0))
    err_dist.append(float(0))
    err_predict.append(float(0))
    err_angle.append(float(0))
    y.append(0)
    for i in range(1,  len(pos_x)):
        # Close to covariance
        # Compare the error between the position actual position with the one before
        err_dist.append(np.power(np.power(pos_x[i] -
            pos_x[i-1], 2) +
            np.power(pos_y[i] -
            pos_y[i-1], 2), 0.5))
        # Error btw where it should be and where it is
        predict_x.append(pos_x[i-1] + increment_time * np.cos(vect_yaw[i-1])
            * velocity[i-1])
        predict_y.append(pos_y[i-1] + increment_time * np.sin(vect_yaw[i-1]) *
            velocity[i-1])
        err_predict.append(np.power(np.power(predict_x[i] - pos_x[i], 2) +
            np.power(predict_y[i] - pos_y[i], 2), 0.5)) # still positive
        # Error in direction compare to direction (normalized)
        err_angle.append(np.absolute((np.arctan2(predict_y[i] - pos_y[i-1],
            predict_x[i] - pos_x[i-1]) - np.arctan2(pos_y[i] - pos_y[i-1],
            pos_x[i] - pos_x[i-1]))/(2*3.1457)))
        # Cost vector
        cost_vector.append(alpha_1 * err_dist[i] + alpha_2 * err_predict[i] +
            alpha_3 * err_angle[i])
        if(cost_vector[i] > threshold):
            print('cost_vector: ', cost_vector[i], ', err_dist: ', err_dist[i],
                ', err_predict: ', err_predict[i],  ', err_angle: ',
                err_angle[i])
            points.append([pos_x[i], pos_y[i]])
            n_1.append(i)
            print(points)
            y.append(1)
        else:
            y.append(0)

    # f = plt.figure(1, figsize=(40, 32))
    # ax = f.add_subplot(111)
    for i in range(0, len(points), 1):
        plt.plot(pos_x[int(n_1[i])],
            pos_y[int(n_1[i])], 'o' ,color='red',
            markersize=20, label="Jump " + str(i+1) + ': Cost_vector: ' +
            str(cost_vector[int(n_1[i])]) + ', err_dist: ' +
            str(err_dist[int(n_1[i])]) + ', err_predict: ' +
            str(err_predict[int(n_1[i])]) +  ', err_angle: ' +
            str(err_angle[int(n_1[i])]))
    plt.plot(pos_x, pos_y, label='Robot position in camera frame')
    plt.xlabel('x [m]')
    plt.ylabel('y [m]')
    plt.xlim(0.0, 7.0)
    plt.ylim(0.0, -7.0)
    # plt.title('Measurment of the odometry' + '\n' + file_name)
    # plt.legend()
    plt.legend(numpoints=1, bbox_to_anchor=(0., 1.02, 1., .102), loc=1,
               ncol=1, mode="expand", borderaxespad=0.)
    # plt.legend(numpoints=1, bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    # plt.legend(numpoints=1, bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    # f.set_size_inches(20, 15)
    # f.savefig(file_name + '.png')
    # plt.close(f)

    plt.show()

    d = {'err_dist': err_dist, 'err_predict': err_predict, 'err_angle': err_angle, 'y': y}
    prediction_pd = pd.DataFrame(d)#, columns= ['err_dist', 'err_predict', 'err_angle'])
    prediction_pd.to_csv('y_' + file_name + '.csv', sep = ',')
