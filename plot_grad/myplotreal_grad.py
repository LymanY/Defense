import numpy as np
import matplotlib.pyplot as plt
import scipy.io as scio
import os


plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

x = [4,6,8,10]

# #################################################################################################
# attackn = 'alfa'
# svmn = 'rbf'
# dname = 'mushroom'
#
# datapath = os.getcwd() + '\\..\\results__\\'+dname+'\\mean'
# y2 = (scio.loadmat(datapath+'2'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y4 = (scio.loadmat(datapath+'4'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y9 = (scio.loadmat(datapath+'9'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y5 = (scio.loadmat(datapath+'5'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y6 = (scio.loadmat(datapath+'6'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y7 = (scio.loadmat(datapath+'7'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y8 = (scio.loadmat(datapath+'8'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y10 = (scio.loadmat(datapath+'10'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y11 = (scio.loadmat(datapath+'11'+dname+svmn+attackn+'.mat'))['meanth'][0]
# datapath = os.getcwd() + '\\..\\results__\\'+dname+'\\std'
# sy2 = (scio.loadmat(datapath+'2'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy4 = (scio.loadmat(datapath+'4'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy9 = (scio.loadmat(datapath+'9'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy5 = (scio.loadmat(datapath+'5'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy6 = (scio.loadmat(datapath+'6'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy7 = (scio.loadmat(datapath+'7'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy8 = (scio.loadmat(datapath+'8'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy10 = (scio.loadmat(datapath+'10'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy11 = (scio.loadmat(datapath+'11'+dname+svmn+attackn+'.mat'))['stdth'][0]
# plt.xlabel('投毒比例 (%)',fontsize=25)
# plt.ylabel('准确率 (%)',fontsize=25)
# # plt.ylim( 50, 105 )
# plt.xticks(x,fontsize=25)
# plt.yticks(fontsize=25)
# ln2 = plt.errorbar(x,y2,yerr=sy2,color='g',linewidth=3.0,linestyle='-',marker='+',label="SVM")
# ln10 = plt.errorbar(x,y10,yerr=sy10,color='m',linewidth=3.0,linestyle='-',marker='^',label="RSVM-3")
# ln11 = plt.errorbar(x,y11,yerr=sy11,color='y',linewidth=3.0,linestyle='-',marker='d',label="RSVM-10")
# lln4 = plt.errorbar(x,y4,yerr=sy4,color='k',linewidth=3.0,linestyle='-',marker='o',label="DBSCAN("+r"$\rho_{Naive}$"+") + rbf SVM")
# ln9 = plt.errorbar(x,y9,yerr=sy9,color='orange',linewidth=3.0,linestyle='-',marker='o',label="DBSCAN("+r"$\rho_{Anchor}$"+") + rbf SVM")
# ln6 = plt.errorbar(x,y6,yerr=sy6,color='c',linewidth=3.0,linestyle='--',marker='h',label="Slab")
# ln5 = plt.errorbar(x,y5,yerr=sy5,color='r',linewidth=3.0,linestyle='--',marker='s',label="L2")
# ln7 = plt.errorbar(x,y7,yerr=sy7,color='m',linewidth=3.0,linestyle='--',marker='x',label="Loss")
# ln8 = plt.errorbar(x,y8,yerr=sy8,color='b',linewidth=3.0,linestyle='--',marker='*',label="k-NN")
# # plt.title('Degree=40\nEuclidean dimension=100',fontsize=25)
# # plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=0, ncol=5, mode="expand", borderaxespad=0.)
# # # plt.legend(loc='upper center',bbox_to_anchor=(0.2, 1.12),ncol=5)
# # plt.legend(bbox_to_anchor=(1.05, 0), loc=3, borderaxespad=0, fontsize=17)
# # plt.legend(bbox_to_anchor=(1.05, 0), loc=3, borderaxespad=0, fontsize=17)
# plt.tight_layout()
# # plt.show()
# # plt.savefig('figure\\bar\\'+attackn+dname+svmn+'.png')
# # plt.savefig('figure\\bar\\'+attackn+dname+svmn+'.eps')
# plt.savefig('..\\figure_grad\\bar\\'+attackn+dname+svmn+'_x.pdf')
# plt.clf()
# plt.cla()
# plt.close()
#
#
# ##################################################################################################
# attackn = 'alfa'
# svmn = 'linear'
# dname = 'mushroom'
#
# datapath = os.getcwd() + '\\..\\results__\\'+dname+'\\mean'
# y2 = (scio.loadmat(datapath+'2'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y4 = (scio.loadmat(datapath+'4'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y9 = (scio.loadmat(datapath+'9'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y5 = (scio.loadmat(datapath+'5'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y6 = (scio.loadmat(datapath+'6'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y7 = (scio.loadmat(datapath+'7'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y8 = (scio.loadmat(datapath+'8'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y10 = (scio.loadmat(datapath+'10'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y11 = (scio.loadmat(datapath+'11'+dname+svmn+attackn+'.mat'))['meanth'][0]
# datapath = os.getcwd() + '\\..\\results__\\'+dname+'\\std'
# sy2 = (scio.loadmat(datapath+'2'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy4 = (scio.loadmat(datapath+'4'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy9 = (scio.loadmat(datapath+'9'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy5 = (scio.loadmat(datapath+'5'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy6 = (scio.loadmat(datapath+'6'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy7 = (scio.loadmat(datapath+'7'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy8 = (scio.loadmat(datapath+'8'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy10 = (scio.loadmat(datapath+'10'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy11 = (scio.loadmat(datapath+'11'+dname+svmn+attackn+'.mat'))['stdth'][0]
# plt.xlabel('投毒比例 (%)',fontsize=25)
# plt.ylabel('准确率 (%)',fontsize=25)
# # plt.ylim( 50, 105 )
# plt.xticks(x,fontsize=25)
# plt.yticks(fontsize=25)
# ln2 = plt.errorbar(x,y2,yerr=sy2,color='g',linewidth=3.0,linestyle='-',marker='+',label="SVM")
# ln10 = plt.errorbar(x,y10,yerr=sy10,color='m',linewidth=3.0,linestyle='-',marker='^',label="RSVM-3")
# ln11 = plt.errorbar(x,y11,yerr=sy11,color='y',linewidth=3.0,linestyle='-',marker='d',label="RSVM-10")
# ln4 = plt.errorbar(x,y4,yerr=sy4,color='k',linewidth=3.0,linestyle='-',marker='o',label="DBSCAN("+r"$\rho_{Naive}$"+")+Linear SVM")
# ln9 = plt.errorbar(x,y9,yerr=sy9,color='orange',linewidth=3.0,linestyle='-',marker='o',label="DBSCAN("+r"$\rho_{Anchor}$"+")+Linear SVM")
# ln6 = plt.errorbar(x,y6,yerr=sy6,color='c',linewidth=3.0,linestyle='--',marker='h',label="Slab")
# ln5 = plt.errorbar(x,y5,yerr=sy5,color='r',linewidth=3.0,linestyle='--',marker='s',label="L2")
# ln7 = plt.errorbar(x,y7,yerr=sy7,color='m',linewidth=3.0,linestyle='--',marker='x',label="Loss")
# ln8 = plt.errorbar(x,y8,yerr=sy8,color='b',linewidth=3.0,linestyle='--',marker='*',label="k-NN")
# # plt.title('Degree=40\nEuclidean dimension=100',fontsize=25)
# # plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=0, ncol=5, mode="expand", borderaxespad=0.)
# # # plt.legend(loc='upper center',bbox_to_anchor=(0.2, 1.12),ncol=5)
# # plt.legend(bbox_to_anchor=(1.05, 0), loc=3, borderaxespad=0, fontsize=17)
# # plt.legend(bbox_to_anchor=(1.05, 0), loc=3, borderaxespad=0, fontsize=17)
# plt.tight_layout()
# # plt.show()
# # plt.savefig('figure\\bar\\'+attackn+dname+svmn+'.png')
# # plt.savefig('figure\\bar\\'+attackn+dname+svmn+'.eps')
# plt.savefig('..\\figure_grad\\bar\\'+attackn+dname+svmn+'_x.pdf')
# plt.clf()
# plt.cla()
# plt.close()
#
#
# ##################################################################################################
#
# attackn = 'mm'
# svmn = 'rbf'
# dname = 'mushroom'
#
# datapath = os.getcwd() + '\\..\\results__\\'+dname+'\\mean'
# y2 = (scio.loadmat(datapath+'2'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y4 = (scio.loadmat(datapath+'4'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y9 = (scio.loadmat(datapath+'9'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y5 = (scio.loadmat(datapath+'5'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y6 = (scio.loadmat(datapath+'6'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y7 = (scio.loadmat(datapath+'7'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y8 = (scio.loadmat(datapath+'8'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y10 = (scio.loadmat(datapath+'10'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y11 = (scio.loadmat(datapath+'11'+dname+svmn+attackn+'.mat'))['meanth'][0]
# datapath = os.getcwd() + '\\..\\results__\\'+dname+'\\std'
# sy2 = (scio.loadmat(datapath+'2'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy4 = (scio.loadmat(datapath+'4'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy9 = (scio.loadmat(datapath+'9'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy5 = (scio.loadmat(datapath+'5'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy6 = (scio.loadmat(datapath+'6'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy7 = (scio.loadmat(datapath+'7'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy8 = (scio.loadmat(datapath+'8'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy10 = (scio.loadmat(datapath+'10'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy11 = (scio.loadmat(datapath+'11'+dname+svmn+attackn+'.mat'))['stdth'][0]
# plt.xlabel('投毒比例 (%)',fontsize=25)
# plt.ylabel('准确率 (%)',fontsize=25)
# # plt.ylim( 50, 105 )
# plt.xticks(x,fontsize=25)
# plt.yticks(fontsize=25)
# ln2 = plt.errorbar(x,y2,yerr=sy2,color='g',linewidth=3.0,linestyle='-',marker='+',label="SVM")
# ln10 = plt.errorbar(x,y10,yerr=sy10,color='m',linewidth=3.0,linestyle='-',marker='^',label="RSVM-3")
# ln11 = plt.errorbar(x,y11,yerr=sy11,color='y',linewidth=3.0,linestyle='-',marker='d',label="RSVM-10")
# ln4 = plt.errorbar(x,y4,yerr=sy4,color='k',linewidth=3.0,linestyle='-',marker='o',label="DBSCAN("+r"$\rho_{Naive}$"+") + rbf SVM")
# ln9 = plt.errorbar(x,y9,yerr=sy9,color='orange',linewidth=3.0,linestyle='-',marker='o',label="DBSCAN("+r"$\rho_{Anchor}$"+") + rbf SVM")
# ln6 = plt.errorbar(x,y6,yerr=sy6,color='c',linewidth=3.0,linestyle='--',marker='h',label="Slab")
# ln5 = plt.errorbar(x,y5,yerr=sy5,color='r',linewidth=3.0,linestyle='--',marker='s',label="L2")
# ln7 = plt.errorbar(x,y7,yerr=sy7,color='m',linewidth=3.0,linestyle='--',marker='x',label="Loss")
# ln8 = plt.errorbar(x,y8,yerr=sy8,color='b',linewidth=3.0,linestyle='--',marker='*',label="k-NN")
# # plt.title('Degree=40\nEuclidean dimension=100',fontsize=25)
# # plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=0, ncol=5, mode="expand", borderaxespad=0.)
# # # plt.legend(loc='upper center',bbox_to_anchor=(0.2, 1.12),ncol=5)
# # plt.legend(bbox_to_anchor=(1.05, 0), loc=3, borderaxespad=0, fontsize=17)
# # plt.legend(bbox_to_anchor=(1.05, 0), loc=3, borderaxespad=0, fontsize=17)
# plt.tight_layout()
# # plt.show()
# # plt.savefig('figure\\bar\\'+attackn+dname+svmn+'.png')
# # plt.savefig('figure\\bar\\'+attackn+dname+svmn+'.eps')
# plt.savefig('..\\figure_grad\\bar\\'+attackn+dname+svmn+'_x.pdf')
# plt.clf()
# plt.cla()
# plt.close()
#
#
# ##################################################################################################
# attackn = 'mm'
# svmn = 'linear'
# dname = 'mushroom'
#
# datapath = os.getcwd() + '\\..\\results__\\'+dname+'\\mean'
# y2 = (scio.loadmat(datapath+'2'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y4 = (scio.loadmat(datapath+'4'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y9 = (scio.loadmat(datapath+'9'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y5 = (scio.loadmat(datapath+'5'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y6 = (scio.loadmat(datapath+'6'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y7 = (scio.loadmat(datapath+'7'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y8 = (scio.loadmat(datapath+'8'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y10 = (scio.loadmat(datapath+'10'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y11 = (scio.loadmat(datapath+'11'+dname+svmn+attackn+'.mat'))['meanth'][0]
# datapath = os.getcwd() + '\\..\\results__\\'+dname+'\\std'
# sy2 = (scio.loadmat(datapath+'2'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy4 = (scio.loadmat(datapath+'4'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy9 = (scio.loadmat(datapath+'9'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy5 = (scio.loadmat(datapath+'5'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy6 = (scio.loadmat(datapath+'6'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy7 = (scio.loadmat(datapath+'7'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy8 = (scio.loadmat(datapath+'8'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy10 = (scio.loadmat(datapath+'10'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy11 = (scio.loadmat(datapath+'11'+dname+svmn+attackn+'.mat'))['stdth'][0]
# plt.xlabel('投毒比例 (%)',fontsize=25)
# plt.ylabel('准确率 (%)',fontsize=25)
# # plt.ylim( 50, 105 )
# plt.xticks(x,fontsize=25)
# plt.yticks(fontsize=25)
# ln2 = plt.errorbar(x,y2,yerr=sy2,color='g',linewidth=3.0,linestyle='-',marker='+',label="SVM")
# ln10 = plt.errorbar(x,y10,yerr=sy10,color='m',linewidth=3.0,linestyle='-',marker='^',label="RSVM-3")
# ln11 = plt.errorbar(x,y11,yerr=sy11,color='y',linewidth=3.0,linestyle='-',marker='d',label="RSVM-10")
# ln4 = plt.errorbar(x,y4,yerr=sy4,color='k',linewidth=3.0,linestyle='-',marker='o',label="DBSCAN("+r"$\rho_{Naive}$"+")+Linear SVM")
# ln9 = plt.errorbar(x,y9,yerr=sy9,color='orange',linewidth=3.0,linestyle='-',marker='o',label="DBSCAN("+r"$\rho_{Anchor}$"+")+Linear SVM")
# ln6 = plt.errorbar(x,y6,yerr=sy6,color='c',linewidth=3.0,linestyle='--',marker='h',label="Slab")
# ln5 = plt.errorbar(x,y5,yerr=sy5,color='r',linewidth=3.0,linestyle='--',marker='s',label="L2")
# ln7 = plt.errorbar(x,y7,yerr=sy7,color='m',linewidth=3.0,linestyle='--',marker='x',label="Loss")
# ln8 = plt.errorbar(x,y8,yerr=sy8,color='b',linewidth=3.0,linestyle='--',marker='*',label="k-NN")
# # plt.title('Degree=40\nEuclidean dimension=100',fontsize=25)
# # plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=0, ncol=5, mode="expand", borderaxespad=0.)
# # # plt.legend(loc='upper center',bbox_to_anchor=(0.2, 1.12),ncol=5)
# # plt.legend(bbox_to_anchor=(1.05, 0), loc=3, borderaxespad=0, fontsize=17)
# # plt.legend(bbox_to_anchor=(1.05, 0), loc=3, borderaxespad=0, fontsize=17)
# plt.tight_layout()
# # plt.show()
# # plt.savefig('figure\\bar\\'+attackn+dname+svmn+'.png')
# # plt.savefig('figure\\bar\\'+attackn+dname+svmn+'.eps')
# plt.savefig('..\\figure_grad\\bar\\'+attackn+dname+svmn+'_x.pdf')
# plt.clf()
# plt.cla()
# plt.close()
#
# #################################################################################################
# attackn = 'alfa'
# svmn = 'rbf'
# dname = 'letter'
#
# datapath = os.getcwd() + '\\..\\results__\\'+dname+'\\mean'
# y2 = (scio.loadmat(datapath+'2'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y4 = (scio.loadmat(datapath+'4'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y9 = (scio.loadmat(datapath+'9'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y5 = (scio.loadmat(datapath+'5'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y6 = (scio.loadmat(datapath+'6'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y7 = (scio.loadmat(datapath+'7'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y8 = (scio.loadmat(datapath+'8'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y10 = (scio.loadmat(datapath+'10'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y11 = (scio.loadmat(datapath+'11'+dname+svmn+attackn+'.mat'))['meanth'][0]
# datapath = os.getcwd() + '\\..\\results__\\'+dname+'\\std'
# sy2 = (scio.loadmat(datapath+'2'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy4 = (scio.loadmat(datapath+'4'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy9 = (scio.loadmat(datapath+'9'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy5 = (scio.loadmat(datapath+'5'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy6 = (scio.loadmat(datapath+'6'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy7 = (scio.loadmat(datapath+'7'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy8 = (scio.loadmat(datapath+'8'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy10 = (scio.loadmat(datapath+'10'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy11 = (scio.loadmat(datapath+'11'+dname+svmn+attackn+'.mat'))['stdth'][0]
# plt.xlabel('投毒比例 (%)',fontsize=25)
# plt.ylabel('准确率 (%)',fontsize=25)
# # plt.ylim( 50, 105 )
# plt.xticks(x,fontsize=25)
# plt.yticks(fontsize=25)
# ln2 = plt.errorbar(x,y2,yerr=sy2,color='g',linewidth=3.0,linestyle='-',marker='+',label="SVM")
# ln10 = plt.errorbar(x,y10,yerr=sy10,color='m',linewidth=3.0,linestyle='-',marker='^',label="RSVM-3")
# ln11 = plt.errorbar(x,y11,yerr=sy11,color='y',linewidth=3.0,linestyle='-',marker='d',label="RSVM-10")
# ln4 = plt.errorbar(x,y4,yerr=sy4,color='k',linewidth=3.0,linestyle='-',marker='o',label="DBSCAN("+r"$\rho_{Naive}$"+") + rbf SVM")
# ln9 = plt.errorbar(x,y9,yerr=sy9,color='orange',linewidth=3.0,linestyle='-',marker='o',label="DBSCAN("+r"$\rho_{Anchor}$"+") + rbf SVM")
# ln6 = plt.errorbar(x,y6,yerr=sy6,color='c',linewidth=3.0,linestyle='--',marker='h',label="Slab")
# ln5 = plt.errorbar(x,y5,yerr=sy5,color='r',linewidth=3.0,linestyle='--',marker='s',label="L2")
# ln7 = plt.errorbar(x,y7,yerr=sy7,color='m',linewidth=3.0,linestyle='--',marker='x',label="Loss")
# ln8 = plt.errorbar(x,y8,yerr=sy8,color='b',linewidth=3.0,linestyle='--',marker='*',label="k-NN")
# # plt.title('Degree=40\nEuclidean dimension=100',fontsize=25)
# # plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=0, ncol=5, mode="expand", borderaxespad=0.)
# # # plt.legend(loc='upper center',bbox_to_anchor=(0.2, 1.12),ncol=5)
# # plt.legend(bbox_to_anchor=(1.05, 0), loc=3, borderaxespad=0, fontsize=17)
# # plt.legend(bbox_to_anchor=(1.05, 0), loc=3, borderaxespad=0, fontsize=17)
# plt.tight_layout()
# # plt.show()
# # plt.savefig('figure\\bar\\'+attackn+dname+svmn+'.png')
# # plt.savefig('figure\\bar\\'+attackn+dname+svmn+'.eps')
# plt.savefig('..\\figure_grad\\bar\\'+attackn+dname+svmn+'_x.pdf')
# plt.clf()
# plt.cla()
# plt.close()
#
#
# ##################################################################################################
# attackn = 'alfa'
# svmn = 'linear'
# dname = 'letter'
#
# datapath = os.getcwd() + '\\..\\results__\\'+dname+'\\mean'
# y2 = (scio.loadmat(datapath+'2'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y4 = (scio.loadmat(datapath+'4'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y9 = (scio.loadmat(datapath+'9'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y5 = (scio.loadmat(datapath+'5'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y6 = (scio.loadmat(datapath+'6'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y7 = (scio.loadmat(datapath+'7'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y8 = (scio.loadmat(datapath+'8'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y10 = (scio.loadmat(datapath+'10'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y11 = (scio.loadmat(datapath+'11'+dname+svmn+attackn+'.mat'))['meanth'][0]
# datapath = os.getcwd() + '\\..\\results__\\'+dname+'\\std'
# sy2 = (scio.loadmat(datapath+'2'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy4 = (scio.loadmat(datapath+'4'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy9 = (scio.loadmat(datapath+'9'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy5 = (scio.loadmat(datapath+'5'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy6 = (scio.loadmat(datapath+'6'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy7 = (scio.loadmat(datapath+'7'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy8 = (scio.loadmat(datapath+'8'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy10 = (scio.loadmat(datapath+'10'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy11 = (scio.loadmat(datapath+'11'+dname+svmn+attackn+'.mat'))['stdth'][0]
# plt.xlabel('投毒比例 (%)',fontsize=25)
# plt.ylabel('准确率 (%)',fontsize=25)
# # plt.ylim( 50, 105 )
# plt.xticks(x,fontsize=25)
# plt.yticks(fontsize=25)
# ln2 = plt.errorbar(x,y2,yerr=sy2,color='g',linewidth=3.0,linestyle='-',marker='+',label="SVM")
# ln10 = plt.errorbar(x,y10,yerr=sy10,color='m',linewidth=3.0,linestyle='-',marker='^',label="RSVM-3")
# ln11 = plt.errorbar(x,y11,yerr=sy11,color='y',linewidth=3.0,linestyle='-',marker='d',label="RSVM-10")
# ln4 = plt.errorbar(x,y4,yerr=sy4,color='k',linewidth=3.0,linestyle='-',marker='o',label="DBSCAN("+r"$\rho_{Naive}$"+")+Linear SVM")
# ln9 = plt.errorbar(x,y9,yerr=sy9,color='orange',linewidth=3.0,linestyle='-',marker='o',label="DBSCAN("+r"$\rho_{Anchor}$"+")+Linear SVM")
# ln6 = plt.errorbar(x,y6,yerr=sy6,color='c',linewidth=3.0,linestyle='--',marker='h',label="Slab")
# ln5 = plt.errorbar(x,y5,yerr=sy5,color='r',linewidth=3.0,linestyle='--',marker='s',label="L2")
# ln7 = plt.errorbar(x,y7,yerr=sy7,color='m',linewidth=3.0,linestyle='--',marker='x',label="Loss")
# ln8 = plt.errorbar(x,y8,yerr=sy8,color='b',linewidth=3.0,linestyle='--',marker='*',label="k-NN")
# # plt.title('Degree=40\nEuclidean dimension=100',fontsize=25)
# # plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=0, ncol=5, mode="expand", borderaxespad=0.)
# # # plt.legend(loc='upper center',bbox_to_anchor=(0.2, 1.12),ncol=5)
# # plt.legend(bbox_to_anchor=(1.05, 0), loc=3, borderaxespad=0, fontsize=17)
# # plt.legend(bbox_to_anchor=(1.05, 0), loc=3, borderaxespad=0, fontsize=17)
# plt.tight_layout()
# # plt.show()
# # plt.savefig('figure\\bar\\'+attackn+dname+svmn+'.png')
# # plt.savefig('figure\\bar\\'+attackn+dname+svmn+'.eps')
# plt.savefig('..\\figure_grad\\bar\\'+attackn+dname+svmn+'_x.pdf')
# plt.clf()
# plt.cla()
# plt.close()
#
#
# ##################################################################################################
#
# attackn = 'mm'
# svmn = 'rbf'
# dname = 'letter'
#
# datapath = os.getcwd() + '\\..\\results__\\'+dname+'\\mean'
# y2 = (scio.loadmat(datapath+'2'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y4 = (scio.loadmat(datapath+'4'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y9 = (scio.loadmat(datapath+'9'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y5 = (scio.loadmat(datapath+'5'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y6 = (scio.loadmat(datapath+'6'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y7 = (scio.loadmat(datapath+'7'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y8 = (scio.loadmat(datapath+'8'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y10 = (scio.loadmat(datapath+'10'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y11 = (scio.loadmat(datapath+'11'+dname+svmn+attackn+'.mat'))['meanth'][0]
# datapath = os.getcwd() + '\\..\\results__\\'+dname+'\\std'
# sy2 = (scio.loadmat(datapath+'2'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy4 = (scio.loadmat(datapath+'4'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy9 = (scio.loadmat(datapath+'9'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy5 = (scio.loadmat(datapath+'5'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy6 = (scio.loadmat(datapath+'6'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy7 = (scio.loadmat(datapath+'7'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy8 = (scio.loadmat(datapath+'8'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy10 = (scio.loadmat(datapath+'10'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy11 = (scio.loadmat(datapath+'11'+dname+svmn+attackn+'.mat'))['stdth'][0]
# plt.xlabel('投毒比例 (%)',fontsize=25)
# plt.ylabel('准确率 (%)',fontsize=25)
# # plt.ylim( 50, 105 )
# plt.xticks(x,fontsize=25)
# plt.yticks(fontsize=25)
# ln2 = plt.errorbar(x,y2,yerr=sy2,color='g',linewidth=3.0,linestyle='-',marker='+',label="SVM")
# ln10 = plt.errorbar(x,y10,yerr=sy10,color='m',linewidth=3.0,linestyle='-',marker='^',label="RSVM-3")
# ln11 = plt.errorbar(x,y11,yerr=sy11,color='y',linewidth=3.0,linestyle='-',marker='d',label="RSVM-10")
# ln4 = plt.errorbar(x,y4,yerr=sy4,color='k',linewidth=3.0,linestyle='-',marker='o',label="DBSCAN("+r"$\rho_{Naive}$"+") + rbf SVM")
# ln9 = plt.errorbar(x,y9,yerr=sy9,color='orange',linewidth=3.0,linestyle='-',marker='o',label="DBSCAN("+r"$\rho_{Anchor}$"+") + rbf SVM")
# ln6 = plt.errorbar(x,y6,yerr=sy6,color='c',linewidth=3.0,linestyle='--',marker='h',label="Slab")
# ln5 = plt.errorbar(x,y5,yerr=sy5,color='r',linewidth=3.0,linestyle='--',marker='s',label="L2")
# ln7 = plt.errorbar(x,y7,yerr=sy7,color='m',linewidth=3.0,linestyle='--',marker='x',label="Loss")
# ln8 = plt.errorbar(x,y8,yerr=sy8,color='b',linewidth=3.0,linestyle='--',marker='*',label="k-NN")
# # plt.title('Degree=40\nEuclidean dimension=100',fontsize=25)
# # plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=0, ncol=5, mode="expand", borderaxespad=0.)
# # # plt.legend(loc='upper center',bbox_to_anchor=(0.2, 1.12),ncol=5)
# # plt.legend(bbox_to_anchor=(1.05, 0), loc=3, borderaxespad=0, fontsize=17)
# # plt.legend(bbox_to_anchor=(1.05, 0), loc=3, borderaxespad=0, fontsize=17)
# plt.tight_layout()
# # plt.show()
# # plt.savefig('figure\\bar\\'+attackn+dname+svmn+'.png')
# # plt.savefig('figure\\bar\\'+attackn+dname+svmn+'.eps')
# plt.savefig('..\\figure_grad\\bar\\'+attackn+dname+svmn+'_x.pdf')
# plt.clf()
# plt.cla()
# plt.close()
#
#
# ##################################################################################################
# attackn = 'mm'
# svmn = 'linear'
# dname = 'letter'
#
# datapath = os.getcwd() + '\\..\\results__\\'+dname+'\\mean'
# y2 = (scio.loadmat(datapath+'2'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y4 = (scio.loadmat(datapath+'4'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y9 = (scio.loadmat(datapath+'9'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y5 = (scio.loadmat(datapath+'5'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y6 = (scio.loadmat(datapath+'6'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y7 = (scio.loadmat(datapath+'7'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y8 = (scio.loadmat(datapath+'8'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y10 = (scio.loadmat(datapath+'10'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y11 = (scio.loadmat(datapath+'11'+dname+svmn+attackn+'.mat'))['meanth'][0]
# datapath = os.getcwd() + '\\..\\results__\\'+dname+'\\std'
# sy2 = (scio.loadmat(datapath+'2'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy4 = (scio.loadmat(datapath+'4'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy9 = (scio.loadmat(datapath+'9'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy5 = (scio.loadmat(datapath+'5'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy6 = (scio.loadmat(datapath+'6'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy7 = (scio.loadmat(datapath+'7'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy8 = (scio.loadmat(datapath+'8'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy10 = (scio.loadmat(datapath+'10'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy11 = (scio.loadmat(datapath+'11'+dname+svmn+attackn+'.mat'))['stdth'][0]
# plt.xlabel('投毒比例 (%)',fontsize=25)
# plt.ylabel('准确率 (%)',fontsize=25)
# # plt.ylim( 50, 105 )
# plt.xticks(x,fontsize=25)
# plt.yticks(fontsize=25)
# ln2 = plt.errorbar(x,y2,yerr=sy2,color='g',linewidth=3.0,linestyle='-',marker='+',label="SVM")
# ln10 = plt.errorbar(x,y10,yerr=sy10,color='m',linewidth=3.0,linestyle='-',marker='^',label="RSVM-3")
# ln11 = plt.errorbar(x,y11,yerr=sy11,color='y',linewidth=3.0,linestyle='-',marker='d',label="RSVM-10")
# ln4 = plt.errorbar(x,y4,yerr=sy4,color='k',linewidth=3.0,linestyle='-',marker='o',label="DBSCAN("+r"$\rho_{Naive}$"+")+Linear SVM")
# ln9 = plt.errorbar(x,y9,yerr=sy9,color='orange',linewidth=3.0,linestyle='-',marker='o',label="DBSCAN("+r"$\rho_{Anchor}$"+")+Linear SVM")
# ln6 = plt.errorbar(x,y6,yerr=sy6,color='c',linewidth=3.0,linestyle='--',marker='h',label="Slab")
# ln5 = plt.errorbar(x,y5,yerr=sy5,color='r',linewidth=3.0,linestyle='--',marker='s',label="L2")
# ln7 = plt.errorbar(x,y7,yerr=sy7,color='m',linewidth=3.0,linestyle='--',marker='x',label="Loss")
# ln8 = plt.errorbar(x,y8,yerr=sy8,color='b',linewidth=3.0,linestyle='--',marker='*',label="k-NN")
# # plt.title('Degree=40\nEuclidean dimension=100',fontsize=25)
# # plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=0, ncol=5, mode="expand", borderaxespad=0.)
# # # plt.legend(loc='upper center',bbox_to_anchor=(0.2, 1.12),ncol=5)
# # plt.legend(bbox_to_anchor=(1.05, 0), loc=3, borderaxespad=0, fontsize=17)
# # plt.legend(bbox_to_anchor=(1.05, 0), loc=3, borderaxespad=0, fontsize=17)
# plt.tight_layout()
# # plt.show()
# # plt.savefig('figure\\bar\\'+attackn+dname+svmn+'.png')
# # plt.savefig('figure\\bar\\'+attackn+dname+svmn+'.eps')
# plt.savefig('..\\figure_grad\\bar\\'+attackn+dname+svmn+'_x.pdf')
# plt.clf()
# plt.cla()
# plt.close()
#
#
################################################################################################
# attackn = 'alfa'
# svmn = 'rbf'
# dname = 'satimage'
#
# datapath = os.getcwd() + '\\..\\results__\\'+dname+'\\mean'
# y2 = (scio.loadmat(datapath+'2'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y4 = (scio.loadmat(datapath+'4'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y9 = (scio.loadmat(datapath+'9'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y5 = (scio.loadmat(datapath+'5'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y6 = (scio.loadmat(datapath+'6'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y7 = (scio.loadmat(datapath+'7'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y8 = (scio.loadmat(datapath+'8'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y10 = (scio.loadmat(datapath+'10'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y11 = (scio.loadmat(datapath+'11'+dname+svmn+attackn+'.mat'))['meanth'][0]
# datapath = os.getcwd() + '\\..\\results__\\'+dname+'\\std'
# sy2 = (scio.loadmat(datapath+'2'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy4 = (scio.loadmat(datapath+'4'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy9 = (scio.loadmat(datapath+'9'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy5 = (scio.loadmat(datapath+'5'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy6 = (scio.loadmat(datapath+'6'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy7 = (scio.loadmat(datapath+'7'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy8 = (scio.loadmat(datapath+'8'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy10 = (scio.loadmat(datapath+'10'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy11 = (scio.loadmat(datapath+'11'+dname+svmn+attackn+'.mat'))['stdth'][0]
# plt.figure(figsize=(9.5, 5))
# plt.xlabel('投毒比例 (%)',fontsize=25)
# plt.ylabel('准确率 (%)',fontsize=25)
# # plt.ylim( 50, 105 )
# plt.xticks(x,fontsize=25)
# plt.yticks(fontsize=25)
# ln2 = plt.errorbar(x,y2,yerr=sy2,color='g',linewidth=3.0,linestyle='-',marker='+',label="rbf SVM")
# ln10 = plt.errorbar(x,y10,yerr=sy10,color='m',linewidth=3.0,linestyle='-',marker='^',label="RSVM-3")
# ln11 = plt.errorbar(x,y11,yerr=sy11,color='y',linewidth=3.0,linestyle='-',marker='d',label="RSVM-10")
# ln4 = plt.errorbar(x,y4,yerr=sy4,color='k',linewidth=3.0,linestyle='-',marker='o',label="DBSCAN("+r"$\rho_{Naive}$"+") + rbf SVM")
# ln9 = plt.errorbar(x,y9,yerr=sy9,color='orange',linewidth=3.0,linestyle='-',marker='o',label="DBSCAN("+r"$\rho_{Anchor}$"+") + rbf SVM")
# ln6 = plt.errorbar(x,y6,yerr=sy6,color='c',linewidth=3.0,linestyle='--',marker='h',label="Slab + rbf SVM")
# ln5 = plt.errorbar(x,y5,yerr=sy5,color='r',linewidth=3.0,linestyle='--',marker='s',label="L2 + rbf SVM")
# ln7 = plt.errorbar(x,y7,yerr=sy7,color='m',linewidth=3.0,linestyle='--',marker='x',label="Loss + rbf SVM")
# ln8 = plt.errorbar(x,y8,yerr=sy8,color='b',linewidth=3.0,linestyle='--',marker='*',label="k-NN + rbf SVM")
# # plt.title('Degree=40\nEuclidean dimension=100',fontsize=25)
# # plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=0, ncol=5, mode="expand", borderaxespad=0.)
# # # plt.legend(loc='upper center',bbox_to_anchor=(0.2, 1.12),ncol=5)
# # plt.legend(bbox_to_anchor=(1.05, 0), loc=3, borderaxespad=0, fontsize=17)
# plt.legend(bbox_to_anchor=(1.05, 0), loc=3, borderaxespad=0, fontsize=16)
# plt.tight_layout()
# plt.show()
# # plt.savefig('figure\\bar\\'+attackn+dname+svmn+'.png')
# # plt.savefig('figure\\bar\\'+attackn+dname+svmn+'.eps')
# # plt.savefig('..\\figure_grad\\'+attackn+dname+svmn+'_x.pdf')
# # plt.clf()
# # plt.cla()
# # plt.close()


# ##################################################################################################
# attackn = 'alfa'
# svmn = 'linear'
# dname = 'satimage'
#
# datapath = os.getcwd() + '\\..\\results__\\'+dname+'\\mean'
# y2 = (scio.loadmat(datapath+'2'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y4 = (scio.loadmat(datapath+'4'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y9 = (scio.loadmat(datapath+'9'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y5 = (scio.loadmat(datapath+'5'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y6 = (scio.loadmat(datapath+'6'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y7 = (scio.loadmat(datapath+'7'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y8 = (scio.loadmat(datapath+'8'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y10 = (scio.loadmat(datapath+'10'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y11 = (scio.loadmat(datapath+'11'+dname+svmn+attackn+'.mat'))['meanth'][0]
# datapath = os.getcwd() + '\\..\\results__\\'+dname+'\\std'
# sy2 = (scio.loadmat(datapath+'2'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy4 = (scio.loadmat(datapath+'4'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy9 = (scio.loadmat(datapath+'9'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy5 = (scio.loadmat(datapath+'5'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy6 = (scio.loadmat(datapath+'6'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy7 = (scio.loadmat(datapath+'7'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy8 = (scio.loadmat(datapath+'8'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy10 = (scio.loadmat(datapath+'10'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy11 = (scio.loadmat(datapath+'11'+dname+svmn+attackn+'.mat'))['stdth'][0]
# plt.figure(figsize=(9.5, 5))
# plt.xlabel('投毒比例 (%)',fontsize=25)
# plt.ylabel('准确率 (%)',fontsize=25)
# # plt.ylim( 50, 105 )
# plt.xticks(x,fontsize=25)
# plt.yticks(fontsize=25)
# ln2 = plt.errorbar(x,y2,yerr=sy2,color='g',linewidth=3.0,linestyle='-',marker='+',label="Linear SVM")
# ln10 = plt.errorbar(x,y10,yerr=sy10,color='m',linewidth=3.0,linestyle='-',marker='^',label="RSVM-3")
# ln11 = plt.errorbar(x,y11,yerr=sy11,color='y',linewidth=3.0,linestyle='-',marker='d',label="RSVM-10")
# ln4 = plt.errorbar(x,y4,yerr=sy4,color='k',linewidth=3.0,linestyle='-',marker='o',label="DBSCAN("+r"$\rho_{Naive}$"+")+Linear SVM")
# ln9 = plt.errorbar(x,y9,yerr=sy9,color='orange',linewidth=3.0,linestyle='-',marker='o',label="DBSCAN("+r"$\rho_{Anchor}$"+")+Linear SVM")
# ln6 = plt.errorbar(x,y6,yerr=sy6,color='c',linewidth=3.0,linestyle='--',marker='h',label="Slab+Linear SVM")
# ln5 = plt.errorbar(x,y5,yerr=sy5,color='r',linewidth=3.0,linestyle='--',marker='s',label="L2+Linear SVM")
# ln7 = plt.errorbar(x,y7,yerr=sy7,color='m',linewidth=3.0,linestyle='--',marker='x',label="Loss+Linear SVM")
# ln8 = plt.errorbar(x,y8,yerr=sy8,color='b',linewidth=3.0,linestyle='--',marker='*',label="k-NN+Linear SVM")
# # plt.title('Degree=40\nEuclidean dimension=100',fontsize=25)
# # plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=0, ncol=5, mode="expand", borderaxespad=0.)
# # # plt.legend(loc='upper center',bbox_to_anchor=(0.2, 1.12),ncol=5)
# # plt.legend(bbox_to_anchor=(1.05, 0), loc=3, borderaxespad=0, fontsize=17)
# plt.legend(bbox_to_anchor=(1.05, 0), loc=3, borderaxespad=0, fontsize=16)
# plt.tight_layout()
# plt.show()
# # plt.savefig('figure\\bar\\'+attackn+dname+svmn+'.png')
# # plt.savefig('figure\\bar\\'+attackn+dname+svmn+'.eps')
# # plt.savefig('..\\figure_grad\\'+attackn+dname+svmn+'_x.pdf')
# # plt.clf()
# # plt.cla()
# # plt.close()
#

# ##################################################################################################
#
# attackn = 'mm'
# svmn = 'rbf'
# dname = 'satimage'
#
# datapath = os.getcwd() + '\\..\\results__\\'+dname+'\\mean'
# y2 = (scio.loadmat(datapath+'2'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y4 = (scio.loadmat(datapath+'4'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y9 = (scio.loadmat(datapath+'9'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y5 = (scio.loadmat(datapath+'5'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y6 = (scio.loadmat(datapath+'6'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y7 = (scio.loadmat(datapath+'7'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y8 = (scio.loadmat(datapath+'8'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y10 = (scio.loadmat(datapath+'10'+dname+svmn+attackn+'.mat'))['meanth'][0]
# y11 = (scio.loadmat(datapath+'11'+dname+svmn+attackn+'.mat'))['meanth'][0]
# datapath = os.getcwd() + '\\..\\results__\\'+dname+'\\std'
# sy2 = (scio.loadmat(datapath+'2'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy4 = (scio.loadmat(datapath+'4'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy9 = (scio.loadmat(datapath+'9'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy5 = (scio.loadmat(datapath+'5'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy6 = (scio.loadmat(datapath+'6'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy7 = (scio.loadmat(datapath+'7'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy8 = (scio.loadmat(datapath+'8'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy10 = (scio.loadmat(datapath+'10'+dname+svmn+attackn+'.mat'))['stdth'][0]
# sy11 = (scio.loadmat(datapath+'11'+dname+svmn+attackn+'.mat'))['stdth'][0]
# plt.figure(figsize=(9.5, 5))
# plt.xlabel('投毒比例 (%)',fontsize=25)
# plt.ylabel('准确率 (%)',fontsize=25)
# # plt.ylim( 50, 105 )
# y = [95,96,97,98,99,700]
# plt.xticks(x,fontsize=25)
# plt.yticks(y,fontsize=25)
# ln2 = plt.errorbar(x,y2,yerr=sy2,color='g',linewidth=3.0,linestyle='-',marker='+',label="rbf SVM")
# ln10 = plt.errorbar(x,y10,yerr=sy10,color='m',linewidth=3.0,linestyle='-',marker='^',label="RSVM-3")
# ln11 = plt.errorbar(x,y11,yerr=sy11,color='y',linewidth=3.0,linestyle='-',marker='d',label="RSVM-10")
# ln4 = plt.errorbar(x,y4,yerr=sy4,color='k',linewidth=3.0,linestyle='-',marker='o',label="DBSCAN("+r"$\rho_{Naive}$"+") + rbf SVM")
# ln9 = plt.errorbar(x,y9,yerr=sy9,color='orange',linewidth=3.0,linestyle='-',marker='o',label="DBSCAN("+r"$\rho_{Anchor}$"+") + rbf SVM")
# ln6 = plt.errorbar(x,y6,yerr=sy6,color='c',linewidth=3.0,linestyle='--',marker='h',label="Slab + rbf SVM")
# ln5 = plt.errorbar(x,y5,yerr=sy5,color='r',linewidth=3.0,linestyle='--',marker='s',label="L2 + rbf SVM")
# ln7 = plt.errorbar(x,y7,yerr=sy7,color='m',linewidth=3.0,linestyle='--',marker='x',label="Loss + rbf SVM")
# ln8 = plt.errorbar(x,y8,yerr=sy8,color='b',linewidth=3.0,linestyle='--',marker='*',label="k-NN + rbf SVM")
# # plt.title('Degree=40\nEuclidean dimension=100',fontsize=25)
# # plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=0, ncol=5, mode="expand", borderaxespad=0.)
# # # plt.legend(loc='upper center',bbox_to_anchor=(0.2, 1.12),ncol=5)
# # plt.legend(bbox_to_anchor=(1.05, 0), loc=3, borderaxespad=0, fontsize=17)
# plt.legend(bbox_to_anchor=(1.05, 0), loc=3, borderaxespad=0, fontsize=16)
# plt.tight_layout()
# plt.show()
# # plt.savefig('figure\\bar\\'+attackn+dname+svmn+'.png')
# # plt.savefig('figure\\bar\\'+attackn+dname+svmn+'.eps')
# # plt.savefig('..\\figure_grad\\'+attackn+dname+svmn+'_x.pdf')
# # plt.clf()
# # plt.cla()
# # plt.close()


# ##################################################################################################
attackn = 'mm'
svmn = 'linear'
dname = 'satimage'

datapath = os.getcwd() + '\\..\\results__\\'+dname+'\\mean'
y2 = (scio.loadmat(datapath+'2'+dname+svmn+attackn+'.mat'))['meanth'][0]
y4 = (scio.loadmat(datapath+'4'+dname+svmn+attackn+'.mat'))['meanth'][0]
y9 = (scio.loadmat(datapath+'9'+dname+svmn+attackn+'.mat'))['meanth'][0]
y5 = (scio.loadmat(datapath+'5'+dname+svmn+attackn+'.mat'))['meanth'][0]
y6 = (scio.loadmat(datapath+'6'+dname+svmn+attackn+'.mat'))['meanth'][0]
y7 = (scio.loadmat(datapath+'7'+dname+svmn+attackn+'.mat'))['meanth'][0]
y8 = (scio.loadmat(datapath+'8'+dname+svmn+attackn+'.mat'))['meanth'][0]
y10 = (scio.loadmat(datapath+'10'+dname+svmn+attackn+'.mat'))['meanth'][0]
y11 = (scio.loadmat(datapath+'11'+dname+svmn+attackn+'.mat'))['meanth'][0]
datapath = os.getcwd() + '\\..\\results__\\'+dname+'\\std'
sy2 = (scio.loadmat(datapath+'2'+dname+svmn+attackn+'.mat'))['stdth'][0]
sy4 = (scio.loadmat(datapath+'4'+dname+svmn+attackn+'.mat'))['stdth'][0]
sy9 = (scio.loadmat(datapath+'9'+dname+svmn+attackn+'.mat'))['stdth'][0]
sy5 = (scio.loadmat(datapath+'5'+dname+svmn+attackn+'.mat'))['stdth'][0]
sy6 = (scio.loadmat(datapath+'6'+dname+svmn+attackn+'.mat'))['stdth'][0]
sy7 = (scio.loadmat(datapath+'7'+dname+svmn+attackn+'.mat'))['stdth'][0]
sy8 = (scio.loadmat(datapath+'8'+dname+svmn+attackn+'.mat'))['stdth'][0]
sy10 = (scio.loadmat(datapath+'10'+dname+svmn+attackn+'.mat'))['stdth'][0]
sy11 = (scio.loadmat(datapath+'11'+dname+svmn+attackn+'.mat'))['stdth'][0]
plt.figure(figsize=(9.5, 5))
plt.xlabel('投毒比例 (%)',fontsize=25)
plt.ylabel('准确率 (%)',fontsize=25)
# plt.ylim( 50, 105 )
plt.xticks(x,fontsize=25)
plt.yticks(fontsize=25)
ln2 = plt.errorbar(x,y2,yerr=sy2,color='g',linewidth=3.0,linestyle='-',marker='+',label="Linear SVM")
ln10 = plt.errorbar(x,y10,yerr=sy10,color='m',linewidth=3.0,linestyle='-',marker='^',label="RSVM-3")
ln11 = plt.errorbar(x,y11,yerr=sy11,color='y',linewidth=3.0,linestyle='-',marker='d',label="RSVM-10")
ln4 = plt.errorbar(x,y4,yerr=sy4,color='k',linewidth=3.0,linestyle='-',marker='o',label="DBSCAN("+r"$\rho_{Naive}$"+")+Linear SVM")
ln9 = plt.errorbar(x,y9,yerr=sy9,color='orange',linewidth=3.0,linestyle='-',marker='o',label="DBSCAN("+r"$\rho_{Anchor}$"+")+Linear SVM")
ln6 = plt.errorbar(x,y6,yerr=sy6,color='c',linewidth=3.0,linestyle='--',marker='h',label="Slab+Linear SVM")
ln5 = plt.errorbar(x,y5,yerr=sy5,color='r',linewidth=3.0,linestyle='--',marker='s',label="L2+Linear SVM")
ln7 = plt.errorbar(x,y7,yerr=sy7,color='m',linewidth=3.0,linestyle='--',marker='x',label="Loss+Linear SVM")
ln8 = plt.errorbar(x,y8,yerr=sy8,color='b',linewidth=3.0,linestyle='--',marker='*',label="k-NN+Linear SVM")
# plt.title('Degree=40\nEuclidean dimension=100',fontsize=25)
# plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=0, ncol=5, mode="expand", borderaxespad=0.)
# # plt.legend(loc='upper center',bbox_to_anchor=(0.2, 1.12),ncol=5)
# plt.legend(bbox_to_anchor=(1.05, 0), loc=3, borderaxespad=0, fontsize=17)
plt.legend(bbox_to_anchor=(1.05, 0), loc=3, borderaxespad=0, fontsize=16)
plt.tight_layout()
plt.show()
# plt.savefig('figure\\bar\\'+attackn+dname+svmn+'.png')
# plt.savefig('figure\\bar\\'+attackn+dname+svmn+'.eps')
# plt.savefig('..\\figure_grad\\'+attackn+dname+svmn+'_x.pdf')
# plt.clf()
# plt.cla()
# plt.close()