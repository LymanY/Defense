% clc
% clear
% 
% addpath('alfaAttack');
% addpath('minmax');
% addpath('dbscan');
% addpath('frtsvm');
% addpath('rrsvm');
% addpath('libsvm');
% addpath('libnear');
% addpath('sanitization');
% 
% % dname = 'letter';
% % dname = 'satimage';
% dname = 'mushroom';
% % dname = 'syn';
% 
% svmn = 'linear';
% % svmn = 'rbf';
% 
% % attackn = 'mm';
% attackn = 'alfa';
% 
% addpath(['data\',dname]);
% load([dname,'sx.mat']);
% load([dname,'sy.mat']);
% addpath('attackfile');
% 
% 
% ratepool = [0.04 0.06 0.08 0.1];
% poi_len = numel(ratepool);
% acc_list9 = zeros(1,poi_len);
% for i = 1:poi_len
%     %% SVD defense
%     rate = ratepool(i);
%     load([attackn,svmn,dname,num2str(rate*100),'dirty_data.mat']);
%     load([attackn,svmn,dname,num2str(rate*100),'dirty_label.mat']);
%     [clean_data,clean_label] = SVDDefense2(dirty_data,dirty_label,rate);
%     clean_data = sparse(clean_data);
%     if strcmp(svmn,'linear')
%         model_clean = lineartrain(clean_label,clean_data );
%         [~,acc9,~] = linearpredict(test_label, test_data, model_clean );
%     elseif strcmp(svmn,'rbf')
%         model_clean = libsvmtrain(clean_label,clean_data );
%         [~,acc9,~] = libsvmpredict(test_label, test_data, model_clean );
%     end
%     acc_list9(i) = acc9(1);
% end
% save(['results\acc_list9',dname,svmn,attackn],'acc_list9');


clc
clear

addpath('alfaAttack');
addpath('minmax');
addpath('dbscan');
addpath('frtsvm');
addpath('rrsvm');
addpath('libsvm');
addpath('libnear');
addpath('sanitization');

% dname = 'letter';
% dname = 'satimage';
% dname = 'mushroom';
% dname = 'syn';

% svmn = 'linear';
svmn = 'rbf';

attackn = 'mm';
% attackn = 'alfa';




indpool = [25 35 45 55 65];
ind_len = numel(indpool);
acc_list9 = zeros(1,ind_len);
for i = 1:ind_len
    %% SVD defense
    rate = 0.1;
    ind = indpool(i);
    dname = ['syn',num2str(ind),'ind'];
    addpath(['data\',dname]);
    load([dname,'sx.mat']);
    load([dname,'sy.mat']);
    addpath('attackfile');
    load([attackn,svmn,dname,num2str(rate*100),'dirty_data.mat']);
    load([attackn,svmn,dname,num2str(rate*100),'dirty_label.mat']);
%     [clean_data,clean_label] = SVDDefense2(dirty_data,dirty_label,rate);
%     clean_data = sparse(clean_data);
%     if strcmp(svmn,'linear')
%         model_clean = lineartrain(clean_label,clean_data );
%         [~,acc9,~] = linearpredict(test_label, test_data, model_clean );
%     elseif strcmp(svmn,'rbf')
%         model_clean = libsvmtrain(clean_label,clean_data );
%         [~,acc9,~] = libsvmpredict(test_label, test_data, model_clean );
%     end
%     acc_list9(i) = acc9(1);
    
    %% frtsvm on dirty data
    % parameter
    Parameter.ker=svmn;
    Parameter.CC=0.25;
    Parameter.CR=1;
    Parameter.p1=1;
    Parameter.v=10;
    Parameter.algorithm='cd';   
    Parameter.showplots= 0;
    frtsvm_struct = frtsvmtrain(dirty_data,dirty_label,Parameter);
    acc3= frtsvmclass(frtsvm_struct,test_data,test_label);
    acc_list3(i) = acc3;
end
save(['results\acc_list3','syn65ind',svmn,attackn],'acc_list3');