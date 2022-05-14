import scipy.io as scio
import numpy as np 
from robust_rescaled_svm import rsvm 
from config import config
import time


####################################################################
# =============================================================================
# dr_f = scio.loadmat('gene1_dirty_fea.mat')
# dr_g = scio.loadmat('gene1_dirty_gnd.mat')
# cl_f = scio.loadmat('gene1_clean_fea.mat')
# cl_g = scio.loadmat('gene1_clean_gnd.mat')
# ts_f = scio.loadmat('gene1_test_fea.mat')
# ts_g = scio.loadmat('gene1_test_gnd.mat')
# =============================================================================
# =============================================================================
# dr_f = scio.loadmat('gene80_dirty_fea.mat')
# dr_g = scio.loadmat('gene80_dirty_gnd.mat')
# cl_f = scio.loadmat('gene80_clean_fea.mat')
# cl_g = scio.loadmat('gene80_clean_gnd.mat')
# ts_f = scio.loadmat('gene80_test_fea.mat')
# ts_g = scio.loadmat('gene80_test_gnd.mat')
# =============================================================================
# =============================================================================
# dr_f = scio.loadmat('gene60_dirty_fea.mat')
# dr_g = scio.loadmat('gene60_dirty_gnd.mat')
# cl_f = scio.loadmat('gene60_clean_fea.mat')
# cl_g = scio.loadmat('gene60_clean_gnd.mat')
# ts_f = scio.loadmat('gene60_test_fea.mat')
# ts_g = scio.loadmat('gene60_test_gnd.mat')
# =============================================================================
# =============================================================================
# dr_f = scio.loadmat('gene12_dirty_fea.mat')
# dr_g = scio.loadmat('gene12_dirty_gnd.mat')
# cl_f = scio.loadmat('gene12_clean_fea.mat')
# cl_g = scio.loadmat('gene12_clean_gnd.mat')
# ts_f = scio.loadmat('gene12_test_fea.mat')
# ts_g = scio.loadmat('gene12_test_gnd.mat')
# =============================================================================
# =============================================================================
# dr_f = scio.loadmat('g20d_dirty_fea.mat')
# dr_g = scio.loadmat('g20d_dirty_gnd.mat')
# cl_f = scio.loadmat('g20d_clean_fea.mat')
# cl_g = scio.loadmat('g20d_clean_gnd.mat')
# ts_f = scio.loadmat('g20d_test_fea.mat')
# ts_g = scio.loadmat('g20d_test_gnd.mat')
# =============================================================================
# =============================================================================
# dr_f = scio.loadmat('g15d_dirty_fea.mat')
# dr_g = scio.loadmat('g15d_dirty_gnd.mat')
# cl_f = scio.loadmat('g15d_clean_fea.mat')
# cl_g = scio.loadmat('g15d_clean_gnd.mat')
# ts_f = scio.loadmat('g15d_test_fea.mat')
# ts_g = scio.loadmat('g15d_test_gnd.mat')
# =============================================================================
# =============================================================================
# dr_f = scio.loadmat('g5d_dirty_fea.mat')
# dr_g = scio.loadmat('g5d_dirty_gnd.mat')
# cl_f = scio.loadmat('g5d_clean_fea.mat')
# cl_g = scio.loadmat('g5d_clean_gnd.mat')
# ts_f = scio.loadmat('g5d_test_fea.mat')
# ts_g = scio.loadmat('g5d_test_gnd.mat')
# =============================================================================
# =============================================================================
# dr_f = scio.loadmat('dna5_dirty_fea.mat')
# dr_g = scio.loadmat('dna5_dirty_gnd.mat')
# cl_f = scio.loadmat('dna5_clean_fea.mat')
# cl_g = scio.loadmat('dna5_clean_gnd.mat')
# ts_f = scio.loadmat('dna5_test_fea.mat')
# ts_g = scio.loadmat('dna5_test_gnd.mat')
# =============================================================================
# =============================================================================
# dr_f = scio.loadmat('dna20_dirty_fea.mat')
# dr_g = scio.loadmat('dna20_dirty_gnd.mat')
# cl_f = scio.loadmat('dna20_clean_fea.mat')
# cl_g = scio.loadmat('dna20_clean_gnd.mat')
# ts_f = scio.loadmat('dna20_test_fea.mat')
# ts_g = scio.loadmat('dna20_test_gnd.mat')
# =============================================================================
# =============================================================================
# dr_f = scio.loadmat('g8000_dirty_fea.mat')
# dr_g = scio.loadmat('g8000_dirty_gnd.mat')
# cl_f = scio.loadmat('g8000_clean_fea.mat')
# cl_g = scio.loadmat('g8000_clean_gnd.mat')
# ts_f = scio.loadmat('g8000_test_fea.mat')
# ts_g = scio.loadmat('g8000_test_gnd.mat')
# =============================================================================

# =============================================================================
# dr_f = scio.loadmat('g10000_dirty_fea.mat')
# dr_g = scio.loadmat('g10000_dirty_gnd.mat')
# cl_f = scio.loadmat('g10000_clean_fea.mat')
# cl_g = scio.loadmat('g10000_clean_gnd.mat')
# ts_f = scio.loadmat('g10000_test_fea.mat')
# ts_g = scio.loadmat('g10000_test_gnd.mat')
# =============================================================================

# =============================================================================
# dr_f = scio.loadmat('g12000_dirty_fea.mat')
# dr_g = scio.loadmat('g12000_dirty_gnd.mat')
# cl_f = scio.loadmat('g12000_clean_fea.mat')
# cl_g = scio.loadmat('g12000_clean_gnd.mat')
# ts_f = scio.loadmat('g12000_test_fea.mat')
# ts_g = scio.loadmat('g12000_test_gnd.mat')
# =============================================================================

# =============================================================================
# dr_f = scio.loadmat('g14000_dirty_fea.mat')
# dr_g = scio.loadmat('g14000_dirty_gnd.mat')
# cl_f = scio.loadmat('g14000_clean_fea.mat')
# cl_g = scio.loadmat('g14000_clean_gnd.mat')
# ts_f = scio.loadmat('g14000_test_fea.mat')
# ts_g = scio.loadmat('g14000_test_gnd.mat')
# =============================================================================




# =============================================================================
# dr_f = scio.loadmat('ss1-5d_dirty_fea.mat')
# dr_g = scio.loadmat('ss1-5d_dirty_gnd.mat')
# ts_f = scio.loadmat('ss1-5d_test_fea.mat')
# ts_g = scio.loadmat('ss1-5d_test_gnd.mat')
# =============================================================================

# =============================================================================
# dr_f = scio.loadmat('ss1-10d_dirty_fea.mat')
# dr_g = scio.loadmat('ss1-10d_dirty_gnd.mat')
# ts_f = scio.loadmat('ss1-10d_test_fea.mat')
# ts_g = scio.loadmat('ss1-10d_test_gnd.mat')
# =============================================================================

# =============================================================================
# dr_f = scio.loadmat('ss1-15d_dirty_fea.mat')
# dr_g = scio.loadmat('ss1-15d_dirty_gnd.mat')
# ts_f = scio.loadmat('ss1-15d_test_fea.mat')
# ts_g = scio.loadmat('ss1-15d_test_gnd.mat')
# =============================================================================

# =============================================================================
# dr_f = scio.loadmat('ss1-20d_dirty_fea.mat')
# dr_g = scio.loadmat('ss1-20d_dirty_gnd.mat')
# ts_f = scio.loadmat('ss1-20d_test_fea.mat')
# ts_g = scio.loadmat('ss1-20d_test_gnd.mat')
# =============================================================================

# =============================================================================
# dr_f = scio.loadmat('ss1-25d_dirty_fea.mat')
# dr_g = scio.loadmat('ss1-25d_dirty_gnd.mat')
# ts_f = scio.loadmat('ss1-25d_test_fea.mat')
# ts_g = scio.loadmat('ss1-25d_test_gnd.mat')
# 
# =============================================================================

# =============================================================================
# dr_f = scio.loadmat('ss1-n35d_dirty_fea.mat')
# dr_g = scio.loadmat('ss1-n35d_dirty_gnd.mat')
# ts_f = scio.loadmat('ss1-n35d_test_fea.mat')
# ts_g = scio.loadmat('ss1-n35d_test_gnd.mat')
# =============================================================================

# =============================================================================
# dr_f = scio.loadmat('ss1-n15d_dirty_fea.mat')
# dr_g = scio.loadmat('ss1-n15d_dirty_gnd.mat')
# ts_f = scio.loadmat('ss1-n15d_test_fea.mat')
# ts_g = scio.loadmat('ss1-n15d_test_gnd.mat')
# =============================================================================

# =============================================================================
# dr_f = scio.loadmat('ss1-20d6_dirty_fea.mat')
# dr_g = scio.loadmat('ss1-20d6_dirty_gnd.mat')
# ts_f = scio.loadmat('ss1-20d6_test_fea.mat')
# ts_g = scio.loadmat('ss1-20d6_test_gnd.mat')
# =============================================================================

# =============================================================================
# dr_f = scio.loadmat('ss1-20d8_dirty_fea.mat')
# dr_g = scio.loadmat('ss1-20d8_dirty_gnd.mat')
# ts_f = scio.loadmat('ss1-20d8_test_fea.mat')
# ts_g = scio.loadmat('ss1-20d8_test_gnd.mat')
# =============================================================================

# =============================================================================
# dr_f = scio.loadmat('ss1-20d12_dirty_fea.mat')
# dr_g = scio.loadmat('ss1-20d12_dirty_gnd.mat')
# ts_f = scio.loadmat('ss1-20d12_test_fea.mat')
# ts_g = scio.loadmat('ss1-20d12_test_gnd.mat')
# 
# =============================================================================
# =============================================================================
# dr_f = scio.loadmat('letter6_dirty_fea.mat')
# dr_g = scio.loadmat('letter6_dirty_gnd.mat')
# ts_f = scio.loadmat('letter6_test_fea.mat')
# ts_g = scio.loadmat('letter6_test_gnd.mat')
# =============================================================================

# =============================================================================
# dr_f = scio.loadmat('letter7_dirty_fea.mat')
# dr_g = scio.loadmat('letter7_dirty_gnd.mat')
# ts_f = scio.loadmat('letter7_test_fea.mat')
# ts_g = scio.loadmat('letter7_test_gnd.mat')
# =============================================================================

# =============================================================================
# dr_f = scio.loadmat('letter8_dirty_fea.mat')
# dr_g = scio.loadmat('letter8_dirty_gnd.mat')
# ts_f = scio.loadmat('letter8_test_fea.mat')
# ts_g = scio.loadmat('letter8_test_gnd.mat')
# =============================================================================

# =============================================================================
# dr_f = scio.loadmat('letter9_dirty_fea.mat')
# dr_g = scio.loadmat('letter9_dirty_gnd.mat')
# ts_f = scio.loadmat('letter9_test_fea.mat')
# ts_g = scio.loadmat('letter9_test_gnd.mat')
# =============================================================================

# =============================================================================
# dr_f = scio.loadmat('letter10_dirty_fea.mat')
# dr_g = scio.loadmat('letter10_dirty_gnd.mat')
# ts_f = scio.loadmat('letter10_test_fea.mat')
# ts_g = scio.loadmat('letter10_test_gnd.mat')
# =============================================================================

# =============================================================================
# dr_f = scio.loadmat('mushrooms6_dirty_fea.mat')
# dr_g = scio.loadmat('mushrooms6_dirty_gnd.mat')
# ts_f = scio.loadmat('mushrooms6_test_fea.mat')
# ts_g = scio.loadmat('mushrooms6_test_gnd.mat')
# =============================================================================

# =============================================================================
# dr_f = scio.loadmat('mushrooms7_dirty_fea.mat')
# dr_g = scio.loadmat('mushrooms7_dirty_gnd.mat')
# ts_f = scio.loadmat('mushrooms7_test_fea.mat')
# ts_g = scio.loadmat('mushrooms7_test_gnd.mat')
# =============================================================================

# =============================================================================
# dr_f = scio.loadmat('mushrooms8_dirty_fea.mat')
# dr_g = scio.loadmat('mushrooms8_dirty_gnd.mat')
# ts_f = scio.loadmat('mushrooms8_test_fea.mat')
# ts_g = scio.loadmat('mushrooms8_test_gnd.mat')
# =============================================================================

# =============================================================================
# dr_f = scio.loadmat('mushrooms9_dirty_fea.mat')
# dr_g = scio.loadmat('mushrooms9_dirty_gnd.mat')
# ts_f = scio.loadmat('mushrooms9_test_fea.mat')
# ts_g = scio.loadmat('mushrooms9_test_gnd.mat')
# =============================================================================

# =============================================================================
# dr_f = scio.loadmat('mushrooms10_dirty_fea.mat')
# dr_g = scio.loadmat('mushrooms10_dirty_gnd.mat')
# ts_f = scio.loadmat('mushrooms10_test_fea.mat')
# ts_g = scio.loadmat('mushrooms10_test_gnd.mat')
# =============================================================================

# =============================================================================
# dr_f = scio.loadmat('ss1-3k_dirty_fea.mat')
# dr_g = scio.loadmat('ss1-3k_dirty_gnd.mat')
# ts_f = scio.loadmat('ss1-3k_test_fea.mat')
# ts_g = scio.loadmat('ss1-3k_test_gnd.mat')
# =============================================================================

# =============================================================================
# dr_f = scio.loadmat('ss1-7k_dirty_fea.mat')
# dr_g = scio.loadmat('ss1-7k_dirty_gnd.mat')
# ts_f = scio.loadmat('ss1-7k_test_fea.mat')
# ts_g = scio.loadmat('ss1-7k_test_gnd.mat')
# 
# =============================================================================
str = 'ind25i1'
#str = '200s80d-1'

p1 = str+'_dirty_fea.mat'
p2 = str+'_dirty_gnd.mat'
p3 = str+'_test_fea.mat'
p4 = str+'_test_gnd.mat'


dr_f = scio.loadmat(p1)
dr_g = scio.loadmat(p2)
ts_f = scio.loadmat(p3)
ts_g = scio.loadmat(p4)


####################################################################
dirty_fea = dr_f['dirty_data']
dirty_g = dr_g['dirty_label']
dirty_gnd = dirty_g[0]

# =============================================================================
# clean_fea = cl_f['clean_data']
# clean_g = cl_g['clean_label']
# clean_gnd = clean_g[0]
# =============================================================================

test_fea = ts_f['test_data']
test_g = ts_g['test_label']
test_gnd = test_g[0]


traindsize1 = dirty_gnd.shape[0]
# =============================================================================
# traindsize2 = clean_gnd.shape[0]
# =============================================================================
# =============================================================================
# print(train_fea)
# print(train_gnd)
# b = np.array(train_fea)
# print(b.shape)
# =============================================================================



# parameter settings
config['kernel'] = 'rbf'
config['rsvm_v0'] = np.ones(shape = (traindsize1,))
#config['rsvm_eta'] = 1.0
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

# =============================================================================
# test_accu = (test_pred == test_gnd).astype(np.float64).mean() * 100
# print( test_accu )
# =============================================================================
test_accu_vec1 = np.zeros(shape = [config['rsvm_iter_num']])
for i in range(config['rsvm_iter_num']):
	test_accu_vec1[i] = (test_pred1[:, i] == test_gnd).astype(np.float64).mean() * 100
print ('dirty :')    
print ('# testing accuracy (predict): {}'.format(test_accu_vec1))
print( test_accu_vec1[2] )
print( test_accu_vec1[5] )
print( test_accu_vec1[9] )

# =============================================================================
# # parameter settings
# config['kernel'] = 'rbf'
# config['rsvm_v0'] = np.ones(shape = (traindsize2,))
# config['rsvm_eta'] = 1.0
# config['rsvm_iter_num'] = 3
# 
# # without outliers
# rsvm_obj2 = rsvm(config)
# rsvm_obj2.fit(clean_fea, clean_gnd)
# test_pred2 = rsvm_obj2.predict(test_fea, last_model_flag = False)
# # =============================================================================
# # test_accu = (test_pred == test_gnd).astype(np.float64).mean() * 100
# # print( test_accu )
# # =============================================================================
# test_accu_vec2 = np.zeros(shape = [config['rsvm_iter_num']])
# for i in range(config['rsvm_iter_num']):
# 	test_accu_vec2[i] = (test_pred2[:, i] == test_gnd).astype(np.float64).mean() * 100
# 
# print ('clean :')       
# print ('# testing accuracy (predict): {}'.format(test_accu_vec2))
# =============================================================================


# =============================================================================
# p1 = 'letterrx.mat'
# p2 = 'letterry.mat'
# 
# import scipy.sparse as sp
# dr_f = scio.loadmat(p1)
# dr_g = scio.loadmat(p2)
# 
# 
# ####################################################################
# dirty_fea = dr_f['org_data'].todense()
# dirty_g = dr_g['org_label']
# dirty_gnd = dirty_g[0]
# =============================================================================
