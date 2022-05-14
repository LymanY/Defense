import numpy as np
from rsvmfunc import rsvmf
import scipy.io as scio


attackn = 'mm'
# attackn = 'alfa'

svmn = 'rbf'
# svmn = 'linear'

# dname = 'letter'
# dname = 'mushroom'
# dname = 'satimage'
# dname = 'syn65'

# ratepool1 = [0.06,0.07,0.08,0.09,0.1]
# ratepool2 = [0.08,0.09,0.1,0.11,0.12]
# ratepool3 = [0.06,0.08,0.1,0.12]
# if attackn is 'alfa':
#     ratepool = ratepool1
# if attackn is 'mm':
#     ratepool = ratepool1
# if dname is 'syn':
#     ratepool = ratepool3
indpool = [25,35,45,55,65]
ind_len = len(indpool)


acc_list10 = np.zeros(ind_len)
acc_list11 = np.zeros(ind_len)

for i in range(ind_len):
    ind = indpool[i]
    dname = 'syn'+str(ind)+'ind'
    acc10, acc11 = rsvmf(0.1, attackn, dname, svmn)
    acc_list10[i] = acc10
    acc_list11[i] = acc11


svname = dname + svmn + attackn
scio.savemat('..\\results\\acc_list10'+svname+'.mat', {'acc_list10': acc_list10})
scio.savemat('..\\results\\acc_list11'+svname+'.mat', {'acc_list11': acc_list11})
