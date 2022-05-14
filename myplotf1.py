import numpy as np
import matplotlib.pyplot as plt

x = np.array([4,6,8,10]);

y4 = [0.9,0.92,0.94,0.95];
y5 = [0.74,0.74,0.67,0.6];
y6 = [0.67,0.6,0.55,0.44];

sy4 = [0.01,0.01,0.01,0.01];
sy5 = [0.09,0.08,0.15,0.1];
sy6 = [0.4,0.33,0.31,0.21];

# y4 = [0.93,0.96,0.97,0.98];
# y5 = [0.95,0.94,0.93,0.92];
# y7 = [0.86,0.89,0.86,0.78];
#
# sy4 = [0.03,0.02,0.02,0.01];
# sy5 = [0.05,0.06,0.06,0.06];
# sy7 = [0.08,0.02,0.02,0.02];

bw = 0.3
plt.xlabel('Poisoned fraction (%)',fontsize=25)
plt.ylabel('F1 score',fontsize=25)
plt.xticks(x,fontsize=25)
plt.yticks(fontsize=25)

error_params1=dict(elinewidth=3,ecolor='g')#设置误差标记参数

ln4 = plt.bar(x,y4,width=bw ,yerr=sy4,color='k',label="DBSCAN",error_kw=error_params1, lw = bw )
ln5 = plt.bar(x+bw,y5,width=bw ,yerr=sy5,color='r',label="L2",error_kw=error_params1, lw = bw )
ln6 = plt.bar(x+2*bw,y6,width=bw ,yerr=sy6,color='c',label="Slab",error_kw=error_params1, lw = bw )
# ln7 = plt.bar(x+2*bw,y7,width=bw ,yerr=sy7,color='m',label="Loss",error_kw=error_params1, lw = bw )
# ln4 = plt.bar(x,y4,width=bw ,yerr=sy4,color='b',label="DBSCAN", lw = bw, hatch='/')
# ln5 = plt.bar(x+bw,y5,width=bw ,yerr=sy5,color='m',label="L2", lw = bw, hatch='-')
# ln6 = plt.bar(x+2*bw,y6,width=bw ,yerr=sy6,color='g',label="Slab", lw = bw, hatch='\\')

# plt.legend(loc="upper right",fontsize=25)
# plt.legend(bbox_to_anchor=(1.05, 0), loc=3, borderaxespad=0, fontsize=17)
plt.legend(bbox_to_anchor=(0., 1.05, 1., .102), loc=0, ncol=3, mode="expand", borderaxespad=0.,fontsize=18)
plt.tight_layout()
plt.show()

###################################################################################################################

x = np.array([25, 35, 45, 55, 65]);

y4 = [0.95,0.87,0.80,0.75,0.73];
y5 = [0.69,0.69,0.61,0.66,0.60];
y6 = [0.43,0.41,0.17,0.19,0.22];

sy4 = [0.01,0.02,0.03,0.03,0.04];
sy5 = [0.14,0.15,0.17,0.15,0.18];
sy6 = [0.29,0.24,0.20,0.14,0.23];

bw = 1.8
plt.xlabel('Degree',fontsize=25)
plt.ylabel('F1 score',fontsize=25)
plt.xticks(x,fontsize=25)
plt.yticks([0.0,0.2,0.4,0.6,0.8,1.0],fontsize=25)

error_params1=dict(elinewidth=3,ecolor='g')#设置误差标记参数

ln4 = plt.bar(x,y4,width=bw ,yerr=sy4,color='k',label="DBSCAN",error_kw=error_params1, lw = bw )
ln5 = plt.bar(x+bw,y5,width=bw ,yerr=sy5,color='r',label="L2",error_kw=error_params1, lw = bw )
ln6 = plt.bar(x+2*bw,y6,width=bw ,yerr=sy6,color='c',label="Slab",error_kw=error_params1, lw = bw )

plt.legend(bbox_to_anchor=(0., 1.05, 1., .102), loc=0, ncol=3, mode="expand", borderaxespad=0.,fontsize=18)
plt.tight_layout()
plt.show()

###################################################################################################################

x = np.array([50,100,150,200]);

y4 = [0.94,0.87,0.87,0.86];
y5 = [0.93,0.86,0.83,0.85];
y6 = [0.44,0.26,0.26,0.18];

sy4 = [0.18,0.02,0.03,0.02];
sy5 = [0.03,0.05,0.11,0.06];
sy6 = [0.2,0.16,0.20,0.20];

bw = 7
plt.xlabel('Euclidean dimension',fontsize=25)
plt.ylabel('F1 score',fontsize=25)
plt.xticks(x,fontsize=25)
plt.yticks(fontsize=25)

error_params1=dict(elinewidth=3,ecolor='g')#设置误差标记参数

ln4 = plt.bar(x,y4,width=bw ,yerr=sy4,color='k',label="DBSCAN",error_kw=error_params1, lw = bw )
ln5 = plt.bar(x+bw,y5,width=bw ,yerr=sy5,color='r',label="L2",error_kw=error_params1, lw = bw )
ln6 = plt.bar(x+2*bw,y6,width=bw ,yerr=sy6,color='c',label="Slab",error_kw=error_params1, lw = bw )

plt.legend(bbox_to_anchor=(0., 1.05, 1., .102), loc=0, ncol=3, mode="expand", borderaxespad=0.,fontsize=18)
plt.tight_layout()
plt.show()