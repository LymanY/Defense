import numpy as np
from rsvmfunc import rsvmfsyn
import scipy.io as scio

attackn = 'alfa'
# svmn = 'rbf'
svmn = 'linear'

indpool = [0.04,0.06,0.08,0.1]
ind_len = len(indpool)
ri = 5
acc_list10 = np.zeros((ri,ind_len))
acc_list11 = np.zeros((ri,ind_len))


for ii in range(ri):
    for i in range(ind_len):
        ind = indpool[i]
        dname = 'syna'+str(ii+1)
        acc10, acc11 = rsvmfsyn(indpool[i], attackn, 'syna', dname, svmn)
        acc_list10[ii,i] = acc10
        acc_list11[ii,i] = acc11


svname = dname + svmn + attackn
scio.savemat('..\\results\\syna\\acc_list10'+svname+'.mat', {'acc_list10': acc_list10})
scio.savemat('..\\results\\syna\\acc_list11'+svname+'.mat', {'acc_list11': acc_list11})

ma = acc_list10
meanth = ma.mean(axis=0)
stdth = ma.std(axis=0)
scio.savemat('..\\results\\syna\\mean10'+svname+'.mat', {'meanth': meanth})
scio.savemat('..\\results\\syna\\std10'+svname+'.mat', {'stdth': stdth})

ma = acc_list11
meanth = ma.mean(axis=0)
stdth = ma.std(axis=0)
scio.savemat('..\\results\\syna\\mean11'+svname+'.mat', {'meanth': meanth})
scio.savemat('..\\results\\syna\\std11'+svname+'.mat', {'stdth': stdth})