import numpy as np
import matplotlib.pyplot as plt
import scipy.io as scio
import os

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# attackn = 'mm'
# svmn = 'rbf'
# # svmn = 'linear'
#
# x = [50,100,150,200]
#
# datapath = os.getcwd() + '\\..\\results_\\syne\\mean'
# dname = 'syn200eud20'
# y2 = (scio.loadmat(datapath+'2'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y3 = (scio.loadmat(datapath+'3'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y4 = (scio.loadmat(datapath+'4'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y5 = (scio.loadmat(datapath+'5'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y6 = (scio.loadmat(datapath+'6'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y7 = (scio.loadmat(datapath+'7'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y8 = (scio.loadmat(datapath+'8'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y9 = (scio.loadmat(datapath+'9'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y10 = (scio.loadmat(datapath+'10'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y11 = (scio.loadmat(datapath+'11'+dname+svmn+attackn+'.mat'))['meanth'][0]
#
# datapath = os.getcwd() + '\\..\\results_\\syne\\std'
# dname = 'syn200eud20'
# sy2 = (scio.loadmat(datapath+'2'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy3 = (scio.loadmat(datapath+'3'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy4 = (scio.loadmat(datapath+'4'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy5 = (scio.loadmat(datapath+'5'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy6 = (scio.loadmat(datapath+'6'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy7 = (scio.loadmat(datapath+'7'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy8 = (scio.loadmat(datapath+'8'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy9 = (scio.loadmat(datapath+'9'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy10 = (scio.loadmat(datapath+'10'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy11 = (scio.loadmat(datapath+'11'+dname+svmn+attackn+'.mat'))['stdth'][0]
# plt.figure(figsize=(6.3, 5))
# plt.xlabel('空间维度',fontsize=25)
# plt.ylabel('准确率 (%)',fontsize=25)
#
# plt.xticks(x,fontsize=25)
# plt.yticks([60,70,80,90,100],fontsize=25)
# plt.ylim( 60, 105 )
#
# ln2 = plt.errorbar(x,y2,yerr=sy2,color='g',linewidth=3.0,linestyle='-',marker='+',label="Linear SVM")
# ln10 = plt.errorbar(x,y10,yerr=sy10,color='m',linewidth=3.0,linestyle='-',marker='^',label="RSVM-3")
# ln11 = plt.errorbar(x,y11,yerr=sy11,color='y',linewidth=3.0,linestyle='-',marker='d',label="RSVM-10")
# ln4 = plt.errorbar(x,y4,yerr=sy4,color='k',linewidth=3.0,linestyle='-',marker='o',label="DBSCAN("+r"$\rho_{Naive}$"+")\n+Linear SVM")
# ln9 = plt.errorbar(x,y9,yerr=sy9,color='orange',linewidth=3.0,linestyle='-',marker='o',label="DBSCAN("+r"$\rho_{Anchor}$"+")\n+Linear SVM")
# ln5 = plt.errorbar(x,y5,yerr=sy5,color='r',linewidth=3.0,linestyle='--',marker='s',label="L2+Linear SVM")
# ln6 = plt.errorbar(x,y6,yerr=sy6,color='c',linewidth=3.0,linestyle='--',marker='h',label="Slab+Linear SVM")
# ln7 = plt.errorbar(x,y7,yerr=sy7,color='m',linewidth=3.0,linestyle='--',marker='x',label="Loss+Linear SVM")
# ln8 = plt.errorbar(x,y8,yerr=sy8,color='b',linewidth=3.0,linestyle='--',marker='*',label="k-NN+Linear SVM")
# plt.title('投毒比例=6% 次数=40',fontsize=25)
#
# # plt.legend(bbox_to_anchor=(1.05, 0), loc=3, borderaxespad=0, fontsize=16)
#
# plt.tight_layout()
# # plt.show()
#
# plt.savefig('..\\figure_grad\\'+attackn+dname+svmn+'_x.pdf')
#
# plt.clf()
# plt.cla()
# plt.close()


####################################################################################################
attackn = 'mm'
svmn = 'rbf'
# svmn = 'linear'

x = [25,35,45,55,65]

datapath = os.getcwd() + '\\..\\results_\\syni\\mean'
dname = 'syn65ind20'
y2 = (scio.loadmat(datapath+'2'+dname+svmn+attackn+'.mat'))['meanth'][0]
y3 = (scio.loadmat(datapath+'3'+dname+svmn+attackn+'.mat'))['meanth'][0]
y4 = (scio.loadmat(datapath+'4'+dname+svmn+attackn+'.mat'))['meanth'][0]
y9 = (scio.loadmat(datapath+'9'+dname+svmn+attackn+'.mat'))['meanth'][0]
y5 = (scio.loadmat(datapath+'5'+dname+svmn+attackn+'.mat'))['meanth'][0]
y6 = (scio.loadmat(datapath+'6'+dname+svmn+attackn+'.mat'))['meanth'][0]
y7 = (scio.loadmat(datapath+'7'+dname+svmn+attackn+'.mat'))['meanth'][0]
y8 = (scio.loadmat(datapath+'8'+dname+svmn+attackn+'.mat'))['meanth'][0]
y10 = (scio.loadmat(datapath+'10'+dname+svmn+attackn+'.mat'))['meanth'][0]
y11 = (scio.loadmat(datapath+'11'+dname+svmn+attackn+'.mat'))['meanth'][0]

datapath = os.getcwd() + '\\..\\results_\\syni\\std'
dname = 'syn65ind20'
sy2 = (scio.loadmat(datapath+'2'+dname+svmn+attackn+'.mat'))['stdth'][0]
sy3 = (scio.loadmat(datapath+'3'+dname+svmn+attackn+'.mat'))['stdth'][0]
sy4 = (scio.loadmat(datapath+'4'+dname+svmn+attackn+'.mat'))['stdth'][0]
sy9 = (scio.loadmat(datapath+'9'+dname+svmn+attackn+'.mat'))['stdth'][0]
sy5 = (scio.loadmat(datapath+'5'+dname+svmn+attackn+'.mat'))['stdth'][0]
sy6 = (scio.loadmat(datapath+'6'+dname+svmn+attackn+'.mat'))['stdth'][0]
sy7 = (scio.loadmat(datapath+'7'+dname+svmn+attackn+'.mat'))['stdth'][0]
sy8 = (scio.loadmat(datapath+'8'+dname+svmn+attackn+'.mat'))['stdth'][0]
sy10 = (scio.loadmat(datapath+'10'+dname+svmn+attackn+'.mat'))['stdth'][0]
sy11 = (scio.loadmat(datapath+'11'+dname+svmn+attackn+'.mat'))['stdth'][0]
plt.figure(figsize=(8.8, 5))
plt.xlabel('次数',fontsize=25)
plt.ylabel('准确率 (%)',fontsize=25)
plt.ylim( 60, 105 )
plt.xticks(x,fontsize=25)
plt.yticks([60,70,80,90,100],fontsize=25)

ln2 = plt.errorbar(x,y2,yerr=sy2,color='g',linewidth=3.0,linestyle='-',marker='+',label="rbf SVM")
ln10 = plt.errorbar(x,y10,yerr=sy10,color='m',linewidth=3.0,linestyle='-',marker='^',label="RSVM-3")
ln11 = plt.errorbar(x,y11,yerr=sy11,color='y',linewidth=3.0,linestyle='-',marker='d',label="RSVM-10")
ln4 = plt.errorbar(x,y4,yerr=sy4,color='k',linewidth=3.0,linestyle='-',marker='o',label="DBSCAN("+r"$\rho_{Naive}$"+")\n + rbf SVM")
ln9 = plt.errorbar(x,y9,yerr=sy9,color='orange',linewidth=3.0,linestyle='-',marker='o',label="DBSCAN("+r"$\rho_{Anchor}$"+")\n + rbf SVM")
ln6 = plt.errorbar(x,y6,yerr=sy6,color='c',linewidth=3.0,linestyle='--',marker='h',label="Slab + rbf SVM")
ln5 = plt.errorbar(x,y5,yerr=sy5,color='r',linewidth=3.0,linestyle='--',marker='s',label="L2 + rbf SVM")
ln7 = plt.errorbar(x,y7,yerr=sy7,color='m',linewidth=3.0,linestyle='--',marker='x',label="Loss + rbf SVM")
ln8 = plt.errorbar(x,y8,yerr=sy8,color='b',linewidth=3.0,linestyle='--',marker='*',label="k-NN + rbf SVM")
# ln2 = plt.errorbar(x,y2,yerr=sy2,color='g',linewidth=3.0,linestyle='-',marker='+',label="Linear SVM")
# ln10 = plt.errorbar(x,y10,yerr=sy10,color='m',linewidth=3.0,linestyle='-',marker='^',label="RSVM-3")
# ln11 = plt.errorbar(x,y11,yerr=sy11,color='y',linewidth=3.0,linestyle='-',marker='d',label="RSVM-10")
# ln4 = plt.errorbar(x,y4,yerr=sy4,color='k',linewidth=3.0,linestyle='-',marker='o',label="DBSCAN("+r"$\rho_{Naive}$"+")\n+Linear SVM")
# ln9 = plt.errorbar(x,y9,yerr=sy9,color='orange',linewidth=3.0,linestyle='-',marker='o',label="DBSCAN("+r"$\rho_{Anchor}$"+")\n+Linear SVM")
# ln5 = plt.errorbar(x,y5,yerr=sy5,color='r',linewidth=3.0,linestyle='--',marker='s',label="L2+Linear SVM")
# ln6 = plt.errorbar(x,y6,yerr=sy6,color='c',linewidth=3.0,linestyle='--',marker='h',label="Slab+Linear SVM")
# ln7 = plt.errorbar(x,y7,yerr=sy7,color='m',linewidth=3.0,linestyle='--',marker='x',label="Loss+Linear SVM")
# ln8 = plt.errorbar(x,y8,yerr=sy8,color='b',linewidth=3.0,linestyle='--',marker='*',label="k-NN+Linear SVM")
plt.title('投毒比例=6% 空间维度=100',fontsize=25)

plt.legend(bbox_to_anchor=(1.05, 0), loc=3, borderaxespad=0, fontsize=16)

plt.tight_layout()
# plt.show()

plt.savefig('..\\figure_grad\\'+attackn+dname+svmn+'_x.pdf')

# plt.clf()
# plt.cla()
# plt.close()

