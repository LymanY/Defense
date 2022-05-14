import numpy as np
from rsvmfunc import rsvmfreal
import scipy.io as scio



indpool = [0.04,0.06,0.08,0.1]
ind_len = len(indpool)
ri = 5
acc_list10 = np.zeros((ri,ind_len))
acc_list11 = np.zeros((ri,ind_len))



#########################################################################################
attackn = 'mm'
svmn = 'rbf'
dname = 'letter'

for ii in range(ri):
    for i in range(ind_len):
        ind = indpool[i]
        rdname = dname+str(ii+1)
        acc10, acc11 = rsvmfreal(indpool[i], attackn, dname, rdname, svmn)
        acc_list10[ii,i] = acc10
        acc_list11[ii,i] = acc11


svname = dname + svmn + attackn
scio.savemat('..\\results\\'+dname+'\\acc_list10'+svname+'.mat', {'acc_list10': acc_list10})
scio.savemat('..\\results\\'+dname+'\\acc_list11'+svname+'.mat', {'acc_list11': acc_list11})

ma = acc_list10
meanth = ma.mean(axis=0)
stdth = ma.std(axis=0)
scio.savemat('..\\results\\'+dname+'\\mean10'+svname+'.mat', {'meanth': meanth})
scio.savemat('..\\results\\'+dname+'\\std10'+svname+'.mat', {'stdth': stdth})

ma = acc_list11
meanth = ma.mean(axis=0)
stdth = ma.std(axis=0)
scio.savemat('..\\results\\'+dname+'\\mean11'+svname+'.mat', {'meanth': meanth})
scio.savemat('..\\results\\'+dname+'\\std11'+svname+'.mat', {'stdth': stdth})




#########################################################################################
attackn = 'mm'
svmn = 'linear'
dname = 'letter'

for ii in range(ri):
    for i in range(ind_len):
        ind = indpool[i]
        rdname = dname+str(ii+1)
        acc10, acc11 = rsvmfreal(indpool[i], attackn, dname, rdname, svmn)
        acc_list10[ii,i] = acc10
        acc_list11[ii,i] = acc11


svname = dname + svmn + attackn
scio.savemat('..\\results\\'+dname+'\\acc_list10'+svname+'.mat', {'acc_list10': acc_list10})
scio.savemat('..\\results\\'+dname+'\\acc_list11'+svname+'.mat', {'acc_list11': acc_list11})

ma = acc_list10
meanth = ma.mean(axis=0)
stdth = ma.std(axis=0)
scio.savemat('..\\results\\'+dname+'\\mean10'+svname+'.mat', {'meanth': meanth})
scio.savemat('..\\results\\'+dname+'\\std10'+svname+'.mat', {'stdth': stdth})

ma = acc_list11
meanth = ma.mean(axis=0)
stdth = ma.std(axis=0)
scio.savemat('..\\results\\'+dname+'\\mean11'+svname+'.mat', {'meanth': meanth})
scio.savemat('..\\results\\'+dname+'\\std11'+svname+'.mat', {'stdth': stdth})


#########################################################################################
# attackn = 'alfa'
# svmn = 'rbf'
# dname = 'letter'
#
# for ii in range(ri):
#     for i in range(ind_len):
#         ind = indpool[i]
#         rdname = dname+str(ii+1)
#         acc10, acc11 = rsvmfreal(indpool[i], attackn, dname, rdname, svmn)
#         acc_list10[ii,i] = acc10
#         acc_list11[ii,i] = acc11
#
#
# svname = dname + svmn + attackn
# scio.savemat('..\\results\\'+dname+'\\acc_list10'+svname+'.mat', {'acc_list10': acc_list10})
# scio.savemat('..\\results\\'+dname+'\\acc_list11'+svname+'.mat', {'acc_list11': acc_list11})
#
# ma = acc_list10
# meanth = ma.mean(axis=0)
# stdth = ma.std(axis=0)
# scio.savemat('..\\results\\'+dname+'\\mean10'+svname+'.mat', {'meanth': meanth})
# scio.savemat('..\\results\\'+dname+'\\std10'+svname+'.mat', {'stdth': stdth})
#
# ma = acc_list11
# meanth = ma.mean(axis=0)
# stdth = ma.std(axis=0)
# scio.savemat('..\\results\\'+dname+'\\mean11'+svname+'.mat', {'meanth': meanth})
# scio.savemat('..\\results\\'+dname+'\\std11'+svname+'.mat', {'stdth': stdth})



#########################################################################################
# attackn = 'alfa'
# svmn = 'linear'
# dname = 'letter'
#
# for ii in range(ri):
#     for i in range(ind_len):
#         ind = indpool[i]
#         rdname = dname+str(ii+1)
#         acc10, acc11 = rsvmfreal(indpool[i], attackn, dname, rdname, svmn)
#         acc_list10[ii,i] = acc10
#         acc_list11[ii,i] = acc11
#
#
# svname = dname + svmn + attackn
# scio.savemat('..\\results\\'+dname+'\\acc_list10'+svname+'.mat', {'acc_list10': acc_list10})
# scio.savemat('..\\results\\'+dname+'\\acc_list11'+svname+'.mat', {'acc_list11': acc_list11})
#
# ma = acc_list10
# meanth = ma.mean(axis=0)
# stdth = ma.std(axis=0)
# scio.savemat('..\\results\\'+dname+'\\mean10'+svname+'.mat', {'meanth': meanth})
# scio.savemat('..\\results\\'+dname+'\\std10'+svname+'.mat', {'stdth': stdth})
#
# ma = acc_list11
# meanth = ma.mean(axis=0)
# stdth = ma.std(axis=0)
# scio.savemat('..\\results\\'+dname+'\\mean11'+svname+'.mat', {'meanth': meanth})
# scio.savemat('..\\results\\'+dname+'\\std11'+svname+'.mat', {'stdth': stdth})


#########################################################################################
attackn = 'mm'
svmn = 'rbf'
dname = 'mushroom'

for ii in range(ri):
    for i in range(ind_len):
        ind = indpool[i]
        rdname = dname+str(ii+1)
        acc10, acc11 = rsvmfreal(indpool[i], attackn, dname, rdname, svmn)
        acc_list10[ii,i] = acc10
        acc_list11[ii,i] = acc11


svname = dname + svmn + attackn
scio.savemat('..\\results\\'+dname+'\\acc_list10'+svname+'.mat', {'acc_list10': acc_list10})
scio.savemat('..\\results\\'+dname+'\\acc_list11'+svname+'.mat', {'acc_list11': acc_list11})

ma = acc_list10
meanth = ma.mean(axis=0)
stdth = ma.std(axis=0)
scio.savemat('..\\results\\'+dname+'\\mean10'+svname+'.mat', {'meanth': meanth})
scio.savemat('..\\results\\'+dname+'\\std10'+svname+'.mat', {'stdth': stdth})

ma = acc_list11
meanth = ma.mean(axis=0)
stdth = ma.std(axis=0)
scio.savemat('..\\results\\'+dname+'\\mean11'+svname+'.mat', {'meanth': meanth})
scio.savemat('..\\results\\'+dname+'\\std11'+svname+'.mat', {'stdth': stdth})




#########################################################################################
attackn = 'mm'
svmn = 'linear'
dname = 'mushroom'

for ii in range(ri):
    for i in range(ind_len):
        ind = indpool[i]
        rdname = dname+str(ii+1)
        acc10, acc11 = rsvmfreal(indpool[i], attackn, dname, rdname, svmn)
        acc_list10[ii,i] = acc10
        acc_list11[ii,i] = acc11


svname = dname + svmn + attackn
scio.savemat('..\\results\\'+dname+'\\acc_list10'+svname+'.mat', {'acc_list10': acc_list10})
scio.savemat('..\\results\\'+dname+'\\acc_list11'+svname+'.mat', {'acc_list11': acc_list11})

ma = acc_list10
meanth = ma.mean(axis=0)
stdth = ma.std(axis=0)
scio.savemat('..\\results\\'+dname+'\\mean10'+svname+'.mat', {'meanth': meanth})
scio.savemat('..\\results\\'+dname+'\\std10'+svname+'.mat', {'stdth': stdth})

ma = acc_list11
meanth = ma.mean(axis=0)
stdth = ma.std(axis=0)
scio.savemat('..\\results\\'+dname+'\\mean11'+svname+'.mat', {'meanth': meanth})
scio.savemat('..\\results\\'+dname+'\\std11'+svname+'.mat', {'stdth': stdth})


#########################################################################################
# attackn = 'alfa'
# svmn = 'rbf'
# dname = 'mushroom'
#
# for ii in range(ri):
#     for i in range(ind_len):
#         ind = indpool[i]
#         rdname = dname+str(ii+1)
#         acc10, acc11 = rsvmfreal(indpool[i], attackn, dname, rdname, svmn)
#         acc_list10[ii,i] = acc10
#         acc_list11[ii,i] = acc11
#
#
# svname = dname + svmn + attackn
# scio.savemat('..\\results\\'+dname+'\\acc_list10'+svname+'.mat', {'acc_list10': acc_list10})
# scio.savemat('..\\results\\'+dname+'\\acc_list11'+svname+'.mat', {'acc_list11': acc_list11})
#
# ma = acc_list10
# meanth = ma.mean(axis=0)
# stdth = ma.std(axis=0)
# scio.savemat('..\\results\\'+dname+'\\mean10'+svname+'.mat', {'meanth': meanth})
# scio.savemat('..\\results\\'+dname+'\\std10'+svname+'.mat', {'stdth': stdth})
#
# ma = acc_list11
# meanth = ma.mean(axis=0)
# stdth = ma.std(axis=0)
# scio.savemat('..\\results\\'+dname+'\\mean11'+svname+'.mat', {'meanth': meanth})
# scio.savemat('..\\results\\'+dname+'\\std11'+svname+'.mat', {'stdth': stdth})



#########################################################################################
# attackn = 'alfa'
# svmn = 'linear'
# dname = 'mushroom'
#
# for ii in range(ri):
#     for i in range(ind_len):
#         ind = indpool[i]
#         rdname = dname+str(ii+1)
#         acc10, acc11 = rsvmfreal(indpool[i], attackn, dname, rdname, svmn)
#         acc_list10[ii,i] = acc10
#         acc_list11[ii,i] = acc11
#
#
# svname = dname + svmn + attackn
# scio.savemat('..\\results\\'+dname+'\\acc_list10'+svname+'.mat', {'acc_list10': acc_list10})
# scio.savemat('..\\results\\'+dname+'\\acc_list11'+svname+'.mat', {'acc_list11': acc_list11})
#
# ma = acc_list10
# meanth = ma.mean(axis=0)
# stdth = ma.std(axis=0)
# scio.savemat('..\\results\\'+dname+'\\mean10'+svname+'.mat', {'meanth': meanth})
# scio.savemat('..\\results\\'+dname+'\\std10'+svname+'.mat', {'stdth': stdth})
#
# ma = acc_list11
# meanth = ma.mean(axis=0)
# stdth = ma.std(axis=0)
# scio.savemat('..\\results\\'+dname+'\\mean11'+svname+'.mat', {'meanth': meanth})
# scio.savemat('..\\results\\'+dname+'\\std11'+svname+'.mat', {'stdth': stdth})




#########################################################################################
attackn = 'mm'
svmn = 'rbf'
dname = 'satimage'

for ii in range(ri):
    for i in range(ind_len):
        ind = indpool[i]
        rdname = dname+str(ii+1)
        acc10, acc11 = rsvmfreal(indpool[i], attackn, dname, rdname, svmn)
        acc_list10[ii,i] = acc10
        acc_list11[ii,i] = acc11


svname = dname + svmn + attackn
scio.savemat('..\\results\\'+dname+'\\acc_list10'+svname+'.mat', {'acc_list10': acc_list10})
scio.savemat('..\\results\\'+dname+'\\acc_list11'+svname+'.mat', {'acc_list11': acc_list11})

ma = acc_list10
meanth = ma.mean(axis=0)
stdth = ma.std(axis=0)
scio.savemat('..\\results\\'+dname+'\\mean10'+svname+'.mat', {'meanth': meanth})
scio.savemat('..\\results\\'+dname+'\\std10'+svname+'.mat', {'stdth': stdth})

ma = acc_list11
meanth = ma.mean(axis=0)
stdth = ma.std(axis=0)
scio.savemat('..\\results\\'+dname+'\\mean11'+svname+'.mat', {'meanth': meanth})
scio.savemat('..\\results\\'+dname+'\\std11'+svname+'.mat', {'stdth': stdth})




#########################################################################################
attackn = 'mm'
svmn = 'linear'
dname = 'satimage'

for ii in range(ri):
    for i in range(ind_len):
        ind = indpool[i]
        rdname = dname+str(ii+1)
        acc10, acc11 = rsvmfreal(indpool[i], attackn, dname, rdname, svmn)
        acc_list10[ii,i] = acc10
        acc_list11[ii,i] = acc11


svname = dname + svmn + attackn
scio.savemat('..\\results\\'+dname+'\\acc_list10'+svname+'.mat', {'acc_list10': acc_list10})
scio.savemat('..\\results\\'+dname+'\\acc_list11'+svname+'.mat', {'acc_list11': acc_list11})

ma = acc_list10
meanth = ma.mean(axis=0)
stdth = ma.std(axis=0)
scio.savemat('..\\results\\'+dname+'\\mean10'+svname+'.mat', {'meanth': meanth})
scio.savemat('..\\results\\'+dname+'\\std10'+svname+'.mat', {'stdth': stdth})

ma = acc_list11
meanth = ma.mean(axis=0)
stdth = ma.std(axis=0)
scio.savemat('..\\results\\'+dname+'\\mean11'+svname+'.mat', {'meanth': meanth})
scio.savemat('..\\results\\'+dname+'\\std11'+svname+'.mat', {'stdth': stdth})


#########################################################################################
# attackn = 'alfa'
# svmn = 'rbf'
# dname = 'satimage'
#
# for ii in range(ri):
#     for i in range(ind_len):
#         ind = indpool[i]
#         rdname = dname+str(ii+1)
#         acc10, acc11 = rsvmfreal(indpool[i], attackn, dname, rdname, svmn)
#         acc_list10[ii,i] = acc10
#         acc_list11[ii,i] = acc11
#
#
# svname = dname + svmn + attackn
# scio.savemat('..\\results\\'+dname+'\\acc_list10'+svname+'.mat', {'acc_list10': acc_list10})
# scio.savemat('..\\results\\'+dname+'\\acc_list11'+svname+'.mat', {'acc_list11': acc_list11})
#
# ma = acc_list10
# meanth = ma.mean(axis=0)
# stdth = ma.std(axis=0)
# scio.savemat('..\\results\\'+dname+'\\mean10'+svname+'.mat', {'meanth': meanth})
# scio.savemat('..\\results\\'+dname+'\\std10'+svname+'.mat', {'stdth': stdth})
#
# ma = acc_list11
# meanth = ma.mean(axis=0)
# stdth = ma.std(axis=0)
# scio.savemat('..\\results\\'+dname+'\\mean11'+svname+'.mat', {'meanth': meanth})
# scio.savemat('..\\results\\'+dname+'\\std11'+svname+'.mat', {'stdth': stdth})



#########################################################################################
# attackn = 'alfa'
# svmn = 'linear'
# dname = 'satimage'
#
# for ii in range(ri):
#     for i in range(ind_len):
#         ind = indpool[i]
#         rdname = dname+str(ii+1)
#         acc10, acc11 = rsvmfreal(indpool[i], attackn, dname, rdname, svmn)
#         acc_list10[ii,i] = acc10
#         acc_list11[ii,i] = acc11
#
#
# svname = dname + svmn + attackn
# scio.savemat('..\\results\\'+dname+'\\acc_list10'+svname+'.mat', {'acc_list10': acc_list10})
# scio.savemat('..\\results\\'+dname+'\\acc_list11'+svname+'.mat', {'acc_list11': acc_list11})
#
# ma = acc_list10
# meanth = ma.mean(axis=0)
# stdth = ma.std(axis=0)
# scio.savemat('..\\results\\'+dname+'\\mean10'+svname+'.mat', {'meanth': meanth})
# scio.savemat('..\\results\\'+dname+'\\std10'+svname+'.mat', {'stdth': stdth})
#
# ma = acc_list11
# meanth = ma.mean(axis=0)
# stdth = ma.std(axis=0)
# scio.savemat('..\\results\\'+dname+'\\mean11'+svname+'.mat', {'meanth': meanth})
# scio.savemat('..\\results\\'+dname+'\\std11'+svname+'.mat', {'stdth': stdth})