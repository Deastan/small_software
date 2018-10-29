import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv
import tf
import tf.transformations
import sys, os

from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, balanced_accuracy_score

file_name = 'data.csv'

y_train = []
x_train = []


cur_dir = os.getcwd()
x_train_path = os.path.join(cur_dir,"x_train.csv")
y_train_path = os.path.join(cur_dir,"y_train.csv")

# Data  Train pandas
data_x_train = pd.read_csv(x_train_path, header=None, sep=',', low_memory=False, skiprows=1)
data_y_train = pd.read_csv(y_train_path, header=None, sep=',', low_memory=False, skiprows=1)

# Data x train to list
x_train = data_x_train.values[:,:]
x_train = np.delete(x_train, (0), axis=1) # Note usefule because it is done with panda
# Data y train
y_train = data_y_train.values[:,:]
y_train = np.delete(y_train, (0), axis=1)


scaler = StandardScaler().fit(x_train)
x_train = scaler.transform(x_train)


# #*******************************************************************************
# #          Ridge regression
# #*******************************************************************************
min_score = 0
# params = {0.001, 0.01, 0.1, 1, 10, 100, 1000, 10000, 100000}#, 250000000, 500000000, 750000000, 1000000000, 10000000000, 100000000000}
# for alph in params:
ridge = Ridge(fit_intercept=True, alpha=1)
ridge.fit(x_train, y_train)
# p = ridge.predict(x_train[test])
    # RMSE = mean_squared_error(y_train[test], p)**0.5
    # score = r2_score(y_train[test], p)
    # # BMAC = balanced_accuracy_score(y_train[test], p)
    # plt.plot(alph, score, 'o', markersize=10, label='%s data : ' %current_kf)
    # if(RMSE > min_score):
    #     min_score = score
    #     min_rmse = RMSE
    #     min_alpha = alph
        # plt.legend(['%s KFold' %i])
# print("Alpha minimum est : ", min_alpha, " sur le K_fold : ", min_kFold, ", with a score = ", min_score, ", RMSE = ", min_rmse, ", BMAC", BMAC)
print(get_params(ridge))
# To plot a pseudo graph of alpha in x-axis and score in y-axis
# plt.xscale('log')
# plt.xlabel('Alpha in ridge regression')
# plt.ylabel('Score')
# plt.legend()
# plt.title('Ridge regression' + '\n' +'Each row of a alpha-column is a k-Fold')
# plt.show()
#
# weight = np.polyfit(x_train, y_train, 3)
# print(weight)
