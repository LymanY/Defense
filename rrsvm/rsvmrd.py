import numpy as np
from rsvmfunc import rsvmfr
import scipy.io as scio


# attackn = 'mm'
# svmn = 'rbf'
# # svmn = 'linear'
#
# indpool = [25,35,45,55,65]
# ind_len = len(indpool)
# ri = 20
# acc_list10 = np.zeros((ri,ind_len))
# acc_list11 = np.zeros((ri,ind_len))
#
#
# for ii in range(ri):
#     for i in range(ind_len):
#         ind = indpool[i]
#         dname = 'syn'+str(ind)+'ind'+str(ii+1)
#         acc10, acc11 = rsvmfr(0.1, attackn, 'syni', dname, svmn)
#         acc_list10[ii,i] = acc10
#         acc_list11[ii,i] = acc11
#
#
# svname = dname + svmn + attackn
# # scio.savemat('..\\results\\syni\\acc_list10'+svname+'.mat', {'acc_list10': acc_list10})
# # scio.savemat('..\\results\\syni\\acc_list11'+svname+'.mat', {'acc_list11': acc_list11})
#
# ma = acc_list10
# meanth = ma.mean(axis=0)
# stdth = ma.std(axis=0)
# scio.savemat('..\\results\\syni\\mean10'+svname+'.mat', {'meanth': meanth})
# scio.savemat('..\\results\\syni\\std10'+svname+'.mat', {'stdth': stdth})
#
# ma = acc_list11
# meanth = ma.mean(axis=0)
# stdth = ma.std(axis=0)
# scio.savemat('..\\results\\syni\\mean11'+svname+'.mat', {'meanth': meanth})
# scio.savemat('..\\results\\syni\\std11'+svname+'.mat', {'stdth': stdth})




attackn = 'mm'
svmn = 'rbf'
# svmn = 'linear'

indpool = [50,100,150,200]
ind_len = len(indpool)
ri = 20
acc_list10 = np.zeros((ri,ind_len))
acc_list11 = np.zeros((ri,ind_len))


for ii in range(ri):
    for i in range(ind_len):
        ind = indpool[i]
        dname = 'syn'+str(ind)+'eud'+str(ii+1)
        acc10, acc11 = rsvmfr(0.1, attackn, 'syne', dname, svmn)
        acc_list10[ii,i] = acc10
        acc_list11[ii,i] = acc11


svname = dname + svmn + attackn
# scio.savemat('..\\results\\syne\\acc_list10'+svname+'.mat', {'acc_list10': acc_list10})
# scio.savemat('..\\results\\syne\\acc_list11'+svname+'.mat', {'acc_list11': acc_list11})

ma = acc_list10
meanth = ma.mean(axis=0)
stdth = ma.std(axis=0)
scio.savemat('..\\results\\syne\\mean10'+svname+'.mat', {'meanth': meanth})
scio.savemat('..\\results\\syne\\std10'+svname+'.mat', {'stdth': stdth})

ma = acc_list11
meanth = ma.mean(axis=0)
stdth = ma.std(axis=0)
scio.savemat('..\\results\\syne\\mean11'+svname+'.mat', {'meanth': meanth})
scio.savemat('..\\results\\syne\\std11'+svname+'.mat', {'stdth': stdth})



attackn = 'mm'
# svmn = 'rbf'
svmn = 'linear'

indpool = [25,35,45,55,65]
ind_len = len(indpool)
ri = 20
acc_list10 = np.zeros((ri,ind_len))
acc_list11 = np.zeros((ri,ind_len))


for ii in range(ri):
    for i in range(ind_len):
        ind = indpool[i]
        dname = 'syn'+str(ind)+'ind'+str(ii+1)
        acc10, acc11 = rsvmfr(0.1, attackn, 'syni', dname, svmn)
        acc_list10[ii,i] = acc10
        acc_list11[ii,i] = acc11


svname = dname + svmn + attackn
# scio.savemat('..\\results\\syni\\acc_list10'+svname+'.mat', {'acc_list10': acc_list10})
# scio.savemat('..\\results\\syni\\acc_list11'+svname+'.mat', {'acc_list11': acc_list11})

ma = acc_list10
meanth = ma.mean(axis=0)
stdth = ma.std(axis=0)
scio.savemat('..\\results\\syni\\mean10'+svname+'.mat', {'meanth': meanth})
scio.savemat('..\\results\\syni\\std10'+svname+'.mat', {'stdth': stdth})

ma = acc_list11
meanth = ma.mean(axis=0)
stdth = ma.std(axis=0)
scio.savemat('..\\results\\syni\\mean11'+svname+'.mat', {'meanth': meanth})
scio.savemat('..\\results\\syni\\std11'+svname+'.mat', {'stdth': stdth})




# attackn = 'mm'
# # svmn = 'rbf'
# svmn = 'linear'
#
# indpool = [50,100,150,200]
# ind_len = len(indpool)
# ri = 20
# acc_list10 = np.zeros((ri,ind_len))
# acc_list11 = np.zeros((ri,ind_len))
#
#
# for ii in range(ri):
#     for i in range(ind_len):
#         ind = indpool[i]
#         dname = 'syn'+str(ind)+'eud'+str(ii+1)
#         acc10, acc11 = rsvmfr(0.1, attackn, 'syne', dname, svmn)
#         acc_list10[ii,i] = acc10
#         acc_list11[ii,i] = acc11
#
#
# svname = dname + svmn + attackn
# # scio.savemat('..\\results\\syne\\acc_list10'+svname+'.mat', {'acc_list10': acc_list10})
# # scio.savemat('..\\results\\syne\\acc_list11'+svname+'.mat', {'acc_list11': acc_list11})
#
# ma = acc_list10
# meanth = ma.mean(axis=0)
# stdth = ma.std(axis=0)
# scio.savemat('..\\results\\syne\\mean10'+svname+'.mat', {'meanth': meanth})
# scio.savemat('..\\results\\syne\\std10'+svname+'.mat', {'stdth': stdth})
#
# ma = acc_list11
# meanth = ma.mean(axis=0)
# stdth = ma.std(axis=0)
# scio.savemat('..\\results\\syne\\mean11'+svname+'.mat', {'meanth': meanth})
# scio.savemat('..\\results\\syne\\std11'+svname+'.mat', {'stdth': stdth})