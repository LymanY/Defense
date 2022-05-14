clc
clear

addpath('minmax\sever\svm')
addpath('alfaAttack');
addpath('minmax');
addpath('dbscan');
addpath('frtsvm');
addpath('rrsvm');
addpath('libsvm');
addpath('libnear');
addpath('sanitization');
addpath('dataGenerate');


%% parameters
% eps: \epsilon for DBSCAN
% sh: If a cluster has less than sh*n points, we assume that it is a small
%     cluster, and we remove the points in this cluster.

%% input
% ratepool = [0.06 0.08 0.1 0.12];
ratepool = [0.04 0.06 0.08 0.1];
dname = 'syna';
svmn = 'linear';
attackn = 'alfa';

%%
poi_len = numel(ratepool);

addpath(['data\',dname]);
load([dname,'rx.mat']);
load([dname,'ry.mat']);
load([dname,'sx.mat']);
load([dname,'sy.mat']);

acc_list1 = zeros(1,poi_len);
acc_list2 = zeros(1,poi_len);
acc_list3 = zeros(1,poi_len);
acc_list4 = zeros(1,poi_len);
acc_list5 = zeros(1,poi_len);
acc_list6 = zeros(1,poi_len);
acc_list7 = zeros(1,poi_len);
acc_list8 = zeros(1,poi_len);
acc_list9 = zeros(1,poi_len);
% acc_list10 = zeros(1,poi_len);
% acc_list11 = zeros(1,poi_len);

%%
for i = 1:poi_len
    %% poison attack
    rate = ratepool(i);
    dirty_label = fliplabel(org_data,org_label,rate,svmn,dname);
    dirty_data = org_data;
    
    %% csvc on original data
    model_org = lineartrain(org_label, org_data );
    [~,acc1,~] = linearpredict(test_label, test_data, model_org );

    %% csvc on dirty data
    model_noi = lineartrain(dirty_label, dirty_data );
    [~,acc2,~] = linearpredict(test_label, test_data, model_noi );

    %% frtsvm on dirty data
    % parameter
    Parameter.ker=svmn;
    Parameter.CC=0.005;
    Parameter.CR=1;
    Parameter.p1=1;
    Parameter.v=10;
    Parameter.algorithm='cd';   
    Parameter.showplots= 0;
    frtsvm_struct = frtsvmtrain(dirty_data,dirty_label,Parameter);
    acc3= frtsvmclass(frtsvm_struct,test_data,test_label);

    %% dbscan method on dirty data
    % parameter
    eps = 2.65;
    minpts = 5;
    sh = 0.20;

    indexl1 = find(dirty_label==1);
    indexl2 = find(dirty_label~=1);
    clean_in1 = dbscan(full(dirty_data(indexl1,:)),minpts,eps,sh);
    clean_in2 = dbscan(full(dirty_data(indexl2,:)),minpts,eps,sh);
    clean_index = [indexl1(clean_in1);indexl2(clean_in2)];
    if numel(clean_index) ~= 0 
        model_dbscan = lineartrain(dirty_label(clean_index,:), dirty_data(clean_index,:) );
        [~,acc4,~] = linearpredict(test_label, test_data, model_dbscan );
    else
        disp('clean_index is empty, please adjust the parameter minpts!')
        acc4 = zeros(1,1);
    end
    
    %% L2 defense
    [clean_data,clean_label] = L2Defense(dirty_data,dirty_label,rate);
    clean_data = sparse(clean_data);
    model_clean = lineartrain(clean_label,clean_data );
    [~,acc5,~] = linearpredict(test_label, test_data, model_clean );

    %% Slab defense
    [clean_data,clean_label] = SlabDefense2(dirty_data,dirty_label,rate);
    clean_data = sparse(clean_data);
    model_clean = lineartrain(clean_label,clean_data );
    [~,acc6,~] = linearpredict(test_label, test_data, model_clean );

    %% Loss defense
    [clean_data,clean_label] = LossDefense2(dirty_data,dirty_label,rate);
    clean_data = sparse(clean_data);
    model_clean = lineartrain(clean_label,clean_data );
    [~,acc7,~] = linearpredict(test_label, test_data, model_clean );

    %% Knn defense
    [clean_data,clean_label] = KnnDefense2(dirty_data,dirty_label,rate);
    clean_data = sparse(clean_data);
    model_clean = lineartrain(clean_label,clean_data );
    [~,acc8,~] = linearpredict(test_label, test_data, model_clean );

    %% SVD defense
    [clean_data,clean_label] = SVDDefense2(dirty_data,dirty_label,rate);
    clean_data = sparse(clean_data);
    model_clean = lineartrain(clean_label,clean_data );
    [~,acc9,~] = linearpredict(test_label, test_data, model_clean );

    %% RSVM
%     currPath = fileparts(mfilename('fullpath'));
%     comd = strcat('python',32,currPath,'\rrsvm\rsvm_fun.py',32,num2str(0.1),32, 'mm',32, 'letter',32, 'rbf');
%     [acc10s,ac11s] = system(comd);
%     % [acc10s,ac11s] = system(strcat('python',32,currPath,'\rsvm_fun.py',num2str(rate), attackn, dname, svmn));
    
    %%
    acc_list1(i) = acc1(1);
    acc_list2(i) = acc2(1);
    acc_list3(i) = acc3;
    acc_list4(i) = acc4(1);
    acc_list5(i) = acc5(1);
    acc_list6(i) = acc6(1);
    acc_list7(i) = acc7(1);
    acc_list8(i) = acc8(1);
    acc_list9(i) = acc9(1);
%     acc_list10(i) = acc10;
%     acc_list11(i) = acc11;
end

save(['results\acc_list1',dname,svmn,attackn],'acc_list1');
save(['results\acc_list2',dname,svmn,attackn],'acc_list2');
save(['results\acc_list3',dname,svmn,attackn],'acc_list3');
save(['results\acc_list4',dname,svmn,attackn],'acc_list4');
save(['results\acc_list5',dname,svmn,attackn],'acc_list5');
save(['results\acc_list6',dname,svmn,attackn],'acc_list6');
save(['results\acc_list7',dname,svmn,attackn],'acc_list7');
save(['results\acc_list8',dname,svmn,attackn],'acc_list8');
save(['results\acc_list9',dname,svmn,attackn],'acc_list9');





