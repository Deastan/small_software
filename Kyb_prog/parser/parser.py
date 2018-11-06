#!/usr/bin/env python
import ConfigParser
import numpy as np
import pandas as pd

# f = open ( 'environmentPSEs.cfg' , 'r')
# l = [[float(num) for num in line.split(' ')] for line in f ]
# print l

# import csv
# spamReader = csv.reader(open('environmentPSEs.cfg'))
# print spamReader[0][1]
# DELIMITER = ' '
# data = []
# with open('environmentPSEs.cfg') as fr:
#   fr = fr.iloc[4:]
#   for line in fr:
#     first_col = line.split('{}'.format(DELIMITER))[0]
#     data.append(first_col)
#     print data

# with open('/environmentPSEs.cfg') as f:
#     lines = f.read().splitlines()

# class FakeSecHead(object):
#     def __init__(self, fp):
#         self.fp = fp
#         self.sechead = '[drvN, devN, btype, stype, member, sNum, Atrib[0], Atrib[1], Atrib[2], Atrib[3], Atrib[4], Atrib[5], Atrib[6], Atrib[7]  , pos[0]  , pos[1]  , pos[2] , pUnc[0] , pUnc[1] , pUnc[2] , r[0][0] , r[0][1] , r[0][2] , r[1][0] , r[1][1] , r[1][2] , r[2][0] , r[2][1] , r[2][2] , rUnc[0] , rUnc[1] , rUnc[2] , kPar[0] , kPar[1] , kPar[2] , kPar[3] , kPar[4] , kPar[5] , kPar[6] , kPar[7] , kPar[8]]\n'
#
#     def readline(self):
#         if self.sechead:
#             try:
#                 return self.sechead
#             finally:
#                 self.sechead = None
#         else:
#             return self.fp.readline()
#
#
# config = ConfigParser.SafeConfigParser()
# config.readfp(FakeSecHead(open('environmentPSEs.cfg')))
# print config.items()
# print config.items('sNum')

# config = ConfigParser.RawConfigParser()
# config.read('environmentPSEs.cfg')

# import csv
#
# with open('environmentPSEs.cfg') as f:
#     data = [map(int, row) for row in csv.reader(f)]
# data[4]
# BEST ONE
# !/usr/local/bin/python
# print('start')
# n = 160
# m = 160
#
# a = 0
# file = open('environmentPSEs.cfg', "r")
# read = file.read()
# print 'reading ...'
# i = 0
# j = 0
# for line in read.splitlines()[3:]: #remove 3 first line
#     i += 1
#     # if(line != 0 or line != 1 or line != 2):
#     for num in line.split(' '):
#         # while (line.split(' ')):
#         # if(num == ' '):
#         #     a = 0
#         # else:
#             j += 1
#             print num
#             # v[i][j] = float(num)
#             #print(i, ' ', j) #num
#     j = 0
#
# # # print(v[:][3])
# print('end')

user1 = pd.read_csv('environmentPSEs.cfg', header=None, sep=' ', skipinitialspace=True, low_memory=False, skiprows=2)
# print user1
x_test = user1.values[:,:]
# x_test = np.delete(x_test, (0), axis=1)
# print(x_test[1][3])
print(x_test[2][1])
