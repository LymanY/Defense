import scipy.io as scio
import numpy as np
# import rrsvm.robust_rescaled_svm.rsvm
from robust_rescaled_svm import rsvm
# import rrsvm.config.config
from config import config
# import rrsvm.robust_rescaled_svm
# import rrsvm.config

import os
import time


def rsvmf(rate, attackn, dname, svmn):

    pn = attackn + svmn + dname + str(int(rate*100))
    path1 = os.getcwd() + '\\..\\attackfile\\' + pn
    path2 = os.getcwd() + '\\..\\data\\' + dname + '\\' + dname

    p1 = path1 + 'dirty_data.mat'
    p2 = path1 + 'dirty_label.mat'
    p3 = path2 + 'sx.mat'
    p4 = path2 + 'sy.mat'

    dr_f = scio.loadmat(p1)
    dr_g = scio.loadmat(p2)
    ts_f = scio.loadmat(p3)
    ts_g = scio.loadmat(p4)
    dirty_fea = dr_f['dirty_data']
    dirty_g = dr_g['dirty_label']
    # dirty_gnd = dirty_g[0]
    dirty_gnd = dirty_g.reshape(-1)
    test_fea = ts_f['test_data']
    test_g = ts_g['test_label']
    # test_gnd = test_g[0]
    test_gnd = test_g.reshape(-1)

    traindsize1 = dirty_gnd.shape[0]

    # parameter settings
    config['kernel'] = svmn
    config['rsvm_v0'] = np.ones(shape=(traindsize1,))
    config['rsvm_eta'] = 1.0
    config['rsvm_iter_num'] = 10

    rsvm_obj1 = rsvm(config)
    rsvm_obj1.fit(dirty_fea, dirty_gnd)
    test_pred1 = rsvm_obj1.predict(test_fea, last_model_flag=False)

    test_accu_vec1 = np.zeros(shape=[config['rsvm_iter_num']])
    for i in range(config['rsvm_iter_num']):
        test_accu_vec1[i] = (test_pred1[:, i] == test_gnd).astype(np.float64).mean() * 100

    return test_accu_vec1[2], test_accu_vec1[9]



def rsvmfr(rate, attackn, pname, dname, svmn):

    pn = attackn + svmn + dname + str(int(rate*100))
    path1 = os.getcwd() + '\\..\\attackfile\\' + pn
    path2 = os.getcwd() + '\\..\\data\\' + pname + '\\' + dname

    p1 = path1 + 'dirty_data.mat'
    p2 = path1 + 'dirty_label.mat'
    p3 = path2 + 'sx.mat'
    p4 = path2 + 'sy.mat'

    dr_f = scio.loadmat(p1)
    dr_g = scio.loadmat(p2)
    ts_f = scio.loadmat(p3)
    ts_g = scio.loadmat(p4)
    dirty_fea = dr_f['dirty_data']
    dirty_g = dr_g['dirty_label']
    # dirty_gnd = dirty_g[0]
    dirty_gnd = dirty_g.reshape(-1)
    test_fea = ts_f['test_data']
    test_g = ts_g['test_label']
    # test_gnd = test_g[0]
    test_gnd = test_g.reshape(-1)

    traindsize1 = dirty_gnd.shape[0]

    # parameter settings
    config['kernel'] = svmn
    config['rsvm_v0'] = np.ones(shape=(traindsize1,))
    config['rsvm_eta'] = 1.0
    config['rsvm_iter_num'] = 10

    rsvm_obj1 = rsvm(config)
    rsvm_obj1.fit(dirty_fea, dirty_gnd)
    test_pred1 = rsvm_obj1.predict(test_fea, last_model_flag=False)

    test_accu_vec1 = np.zeros(shape=[config['rsvm_iter_num']])
    for i in range(config['rsvm_iter_num']):
        test_accu_vec1[i] = (test_pred1[:, i] == test_gnd).astype(np.float64).mean() * 100

    return test_accu_vec1[2], test_accu_vec1[9]



def rsvmfsyn(rate, attackn, pname, dname, svmn):

    pn = attackn + ' ' + dname + str(int(rate*100))
    path1 = os.getcwd() + '\\..\\attackfile\\' + pn
    path2 = os.getcwd() + '\\..\\data\\' + pname + '\\' + dname

    p1 = path1 + 'dirty_data.mat'
    p2 = path1 + 'dirty_label.mat'
    p3 = path2 + 'sx.mat'
    p4 = path2 + 'sy.mat'

    dr_f = scio.loadmat(p1)
    dr_g = scio.loadmat(p2)
    ts_f = scio.loadmat(p3)
    ts_g = scio.loadmat(p4)
    dirty_fea = dr_f['dirty_data']
    dirty_g = dr_g['dirty_label']
    # dirty_gnd = dirty_g[0]
    dirty_gnd = dirty_g.reshape(-1)
    test_fea = ts_f['test_data']
    test_g = ts_g['test_label']
    # test_gnd = test_g[0]
    test_gnd = test_g.reshape(-1)

    traindsize1 = dirty_gnd.shape[0]

    # parameter settings
    config['kernel'] = svmn
    config['rsvm_v0'] = np.ones(shape=(traindsize1,))
    config['rsvm_eta'] = 1.0
    config['rsvm_iter_num'] = 10

    rsvm_obj1 = rsvm(config)
    rsvm_obj1.fit(dirty_fea, dirty_gnd)
    test_pred1 = rsvm_obj1.predict(test_fea, last_model_flag=False)

    test_accu_vec1 = np.zeros(shape=[config['rsvm_iter_num']])
    for i in range(config['rsvm_iter_num']):
        test_accu_vec1[i] = (test_pred1[:, i] == test_gnd).astype(np.float64).mean() * 100

    return test_accu_vec1[2], test_accu_vec1[9]


def rsvmfreal(rate, attackn, pname, dname, svmn):

    pn = attackn + ' ' + dname + str(int(rate*100))
    path1 = os.getcwd() + '\\..\\attackfile\\' + pn
    path2 = os.getcwd() + '\\..\\data\\' + pname + '\\' + pname

    p1 = path1 + 'dirty_data.mat'
    p2 = path1 + 'dirty_label.mat'
    p3 = path2 + 'sx.mat'
    p4 = path2 + 'sy.mat'

    dr_f = scio.loadmat(p1)
    dr_g = scio.loadmat(p2)
    ts_f = scio.loadmat(p3)
    ts_g = scio.loadmat(p4)
    dirty_fea = dr_f['dirty_data']
    dirty_g = dr_g['dirty_label']
    # dirty_gnd = dirty_g[0]
    dirty_gnd = dirty_g.reshape(-1)
    test_fea = ts_f['test_data']
    test_g = ts_g['test_label']
    # test_gnd = test_g[0]
    test_gnd = test_g.reshape(-1)

    traindsize1 = dirty_gnd.shape[0]

    # parameter settings
    config['kernel'] = svmn
    config['rsvm_v0'] = np.ones(shape=(traindsize1,))
    config['rsvm_eta'] = 1.0
    config['rsvm_iter_num'] = 10

    rsvm_obj1 = rsvm(config)
    rsvm_obj1.fit(dirty_fea, dirty_gnd)
    test_pred1 = rsvm_obj1.predict(test_fea, last_model_flag=False)

    test_accu_vec1 = np.zeros(shape=[config['rsvm_iter_num']])
    for i in range(config['rsvm_iter_num']):
        test_accu_vec1[i] = (test_pred1[:, i] == test_gnd).astype(np.float64).mean() * 100

    return test_accu_vec1[2], test_accu_vec1[9]