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


%% parameters
% eps: \epsilon for DBSCAN
% sh: If a cluster has less than sh*n points, we assume that it is a small
%     cluster, and we remove the points in this cluster.

%% input
ind_pool = [50 100 150 200];
% dname = 'syn';
svmn = 'rbf';
attackn = 'mm';
eps_pool = [2.05 2.65 3.35 3.65];

%%
ind_len = numel(ind_pool);


ri = 20;



acc_list1 = zeros(ri,ind_len);
acc_list2 = zeros(ri,ind_len);
acc_list3 = zeros(ri,ind_len);
acc_list4 = zeros(ri,ind_len);
acc_list5 = zeros(ri,ind_len);
acc_list6 = zeros(ri,ind_len);
acc_list7 = zeros(ri,ind_len);
acc_list8 = zeros(ri,ind_len);
acc_list9 = zeros(ri,ind_len);
% acc_list10 = zeros(1,ind_len);
% acc_list11 = zeros(1,ind_len);
    

for ii = 1:ri
    

%%
    for i = 1:ind_len

        dname = ['syn',num2str(ind_pool(i)),'eud',num2str(ii)];
        addpath(['data\syne\']);
        load([dname,'rx.mat']);
        load([dname,'ry.mat']);
        load([dname,'sx.mat']);
        load([dname,'sy.mat']);

        %% poison attack
        rate = 0.1;
%         [dirty_data,dirty_label] = minmax_at(org_data,org_label,rate,dname,svmn);
        addpath('attackfile');
        load([attackn,svmn,dname,num2str(rate*100),'dirty_data.mat']);
        load([attackn,svmn,dname,num2str(rate*100),'dirty_label.mat']);

        %% csvc on original data
        model_org = libsvmtrain(org_label, org_data );
        [~,acc1,~] = libsvmpredict(test_label, test_data, model_org );

        %% csvc on dirty data
        model_noi = libsvmtrain(dirty_label, dirty_data );
        [~,acc2,~] = libsvmpredict(test_label, test_data, model_noi );

%         %% frtsvm on dirty data
%         % parameter
%         Parameter.ker=svmn;
%         Parameter.CC=0.005;
%         Parameter.CR=1;
%         Parameter.p1=1;
%         Parameter.v=10;
%         Parameter.algorithm='cd';   
%         Parameter.showplots= 0;
%         frtsvm_struct = frtsvmtrain(dirty_data,dirty_label,Parameter);
%         acc3= frtsvmclass(frtsvm_struct,test_data,test_label);

        %% dbscan method on dirty data
        % parameter
        eps = eps_pool(i);
        minpts = 5;
        sh = 0.25;

        indexl1 = find(dirty_label==1);
        indexl2 = find(dirty_label~=1);
        clean_in1 = dbscan(full(dirty_data(indexl1,:)),minpts,eps,sh);
        clean_in2 = dbscan(full(dirty_data(indexl2,:)),minpts,eps,sh);
        clean_index = [indexl1(clean_in1);indexl2(clean_in2)];
        if numel(clean_index) ~= 0 
            model_dbscan = libsvmtrain(dirty_label(clean_index,:), dirty_data(clean_index,:) );
            [~,acc4,~] = libsvmpredict(test_label, test_data, model_dbscan );
        else
            disp('clean_index is empty, please adjust the parameter minpts!')
            acc4 = zeros(1,1);
        end

        %% L2 defense
        [clean_data,clean_label,~] = L2Defense2(dirty_data,dirty_label,rate);
        clean_data = sparse(clean_data);
        model_clean = libsvmtrain(clean_label,clean_data );
        [~,acc5,~] = libsvmpredict(test_label, test_data, model_clean );

        %% Slab defense
        [clean_data,clean_label,~] = SlabDefense2(dirty_data,dirty_label,rate);
        clean_data = sparse(clean_data);
        model_clean = libsvmtrain(clean_label,clean_data );
        [~,acc6,~] = libsvmpredict(test_label, test_data, model_clean );

        %% Loss defense
        [clean_data,clean_label,~] = LossDefense2(dirty_data,dirty_label,rate);
        clean_data = sparse(clean_data);
        model_clean = libsvmtrain(clean_label,clean_data );
        [~,acc7,~] = libsvmpredict(test_label, test_data, model_clean );

        %% Knn defense
        [clean_data,clean_label,~] = KnnDefense2(dirty_data,dirty_label,rate);
        clean_data = sparse(clean_data);
        model_clean = libsvmtrain(clean_label,clean_data );
        [~,acc8,~] = libsvmpredict(test_label, test_data, model_clean );

%         %% SVD defense
%         [clean_data,clean_label,~] = SVDDefense2(dirty_data,dirty_label,rate);
%         clean_data = sparse(clean_data);
%         model_clean = libsvmtrain(clean_label,clean_data );
%         [~,acc9,~] = libsvmpredict(test_label, test_data, model_clean );

        %% RSVM
    %     currPath = fileparts(mfilename('fullpath'));
    %     comd = strcat('python',32,currPath,'\rrsvm\rsvm_fun.py',32,num2str(0.1),32, 'mm',32, 'letter',32, 'rbf');
    %     [acc10s,ac11s] = system(comd);
    %     % [acc10s,ac11s] = system(strcat('python',32,currPath,'\rsvm_fun.py',num2str(rate), attackn, dname, svmn));

        %%
        acc_list1(ii,i) = acc1(1);
        acc_list2(ii,i) = acc2(1);
%         acc_list3(ii,i) = acc3;
        acc_list4(ii,i) = acc4(1);
        acc_list5(ii,i) = acc5(1);
        acc_list6(ii,i) = acc6(1);
        acc_list7(ii,i) = acc7(1);
        acc_list8(ii,i) = acc8(1);
%         acc_list9(ii,i) = acc9(1);
    %     acc_list10(i) = acc10;
    %     acc_list11(i) = acc11;
    end




end


save(['results\syne\acc_list1',dname,svmn,attackn],'acc_list1');
save(['results\syne\acc_list2',dname,svmn,attackn],'acc_list2');
% save(['results\syne\acc_list3',dname,svmn,attackn],'acc_list3');
save(['results\syne\acc_list4',dname,svmn,attackn],'acc_list4');
save(['results\syne\acc_list5',dname,svmn,attackn],'acc_list5');
save(['results\syne\acc_list6',dname,svmn,attackn],'acc_list6');
save(['results\syne\acc_list7',dname,svmn,attackn],'acc_list7');
save(['results\syne\acc_list8',dname,svmn,attackn],'acc_list8');
% save(['results\syne\acc_list9',dname,svmn,attackn],'acc_list9');



for j = 1:9
    
    ma = eval(['acc_list',num2str(j)]);
    meanth = mean(ma,1);
    stdth = std(ma,0,1);
    save(['results\syne\mean',num2str(j),dname,svmn,attackn],'meanth');
    save(['results\syne\std',num2str(j),dname,svmn,attackn],'stdth');

end


