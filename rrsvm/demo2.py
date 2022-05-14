import scipy.io as scio
import numpy as np 
from robust_rescaled_svm import rsvm 
from config import config
import time


#str = '200s80d-1'

amean3 = np.zeros(5)
astd3 = np.zeros(5)
amean6 = np.zeros(5)
astd6 = np.zeros(5)
amean10 = np.zeros(5)
astd10 = np.zeros(5)

for outi in [25,35,45,55,65]:
    
    sc1 = 'ind'+str(outi) 
    
    atemp3 = np.zeros(5)
    atemp6 = np.zeros(5)
    atemp10 = np.zeros(5)
    
    for inni in [1,2,3,4,5]:
        
        sc2 = 'i'+str(inni)
        strs = sc1+sc2;
        

        p1 = strs+'_dirty_fea.mat'
        p2 = strs+'_dirty_gnd.mat'
        p3 = strs+'_test_fea.mat'
        p4 = strs+'_test_gnd.mat'
        
        
        dr_f = scio.loadmat(p1)
        dr_g = scio.loadmat(p2)
        ts_f = scio.loadmat(p3)
        ts_g = scio.loadmat(p4)
        
        
        ####################################################################
        dirty_fea = dr_f['dirty_data']
        dirty_g = dr_g['dirty_label']
        dirty_gnd = dirty_g[0]
        
        
        test_fea = ts_f['test_data']
        test_g = ts_g['test_label']
        test_gnd = test_g[0]
        
        
        traindsize1 = dirty_gnd.shape[0]
        
        
        
        # parameter settings
        config['kernel'] = 'rbf'
        config['rsvm_v0'] = np.ones(shape = (traindsize1,))
        config['rsvm_eta'] = 1.0
        config['rsvm_iter_num'] = 10
        
        # without outliers
        
        time_start = time.time()
        
        rsvm_obj1 = rsvm(config)
        rsvm_obj1.fit(dirty_fea, dirty_gnd)
        test_pred1 = rsvm_obj1.predict(test_fea, last_model_flag = False)
        
        # =============================================================================
        # time_end = time.time()
        # print('Time cost = %fs' % (time_end - time_start))
        # =============================================================================
        
        test_accu_vec1 = np.zeros(shape = [config['rsvm_iter_num']])
        for i in range(config['rsvm_iter_num']):
        	test_accu_vec1[i] = (test_pred1[:, i] == test_gnd).astype(np.float64).mean() * 100
        # =============================================================================
        # print ('dirty :')    
        # print ('# testing accuracy (predict): {}'.format(test_accu_vec1))
        # =============================================================================
# =============================================================================
#         print( test_accu_vec1[2] )
#         print( test_accu_vec1[5] )
#         print( test_accu_vec1[9] )
# =============================================================================
        
        atemp3[inni-1] = test_accu_vec1[2]
        atemp6[inni-1] = test_accu_vec1[5]
        atemp10[inni-1] = test_accu_vec1[9]
        
    ind = int((outi-25)/10)
    amean3[ind] = np.mean(atemp3)
    astd3[ind] = np.std(atemp3)
    amean6[ind] = np.mean(atemp6)
    astd6[ind] = np.std(atemp6)
    amean10[ind] = np.mean(atemp10)
    astd10[ind] = np.std(atemp10)


scio.savemat('D:\\WorkSpace\\svm\\robust_rescaled_svm-master\\racc3.mat',{'acc3':amean3})
scio.savemat('D:\\WorkSpace\\svm\\robust_rescaled_svm-master\\ratd3.mat',{'atd3':astd3})
scio.savemat('D:\\WorkSpace\\svm\\robust_rescaled_svm-master\\raac6.mat',{'acc6':amean6})
scio.savemat('D:\\WorkSpace\\svm\\robust_rescaled_svm-master\\ratd6.mat',{'atd6':astd6})
scio.savemat('D:\\WorkSpace\\svm\\robust_rescaled_svm-master\\racc10.mat',{'acc10':amean10})
scio.savemat('D:\\WorkSpace\\svm\\robust_rescaled_svm-master\\ratd10.mat',{'atd10':astd10})