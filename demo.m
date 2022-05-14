clc
clear
addpath('minmax');
addpath('dbscan');
addpath('rrsvm');
addpath('libsvm');
addpath('libnear');
addpath('sanitization');

ratepool = [0.04 0.06 0.08 0.1];
dname = 'satimage';
atsvmn = ' ';
attackn = 'mm';
svmn = 'linear';

ri = 1;
poi_len = numel(ratepool);

addpath(['data\',dname]);
load([dname,'rx.mat']);
load([dname,'ry.mat']);
load([dname,'sx.mat']);
load([dname,'sy.mat']);
[m,~] = size(org_data);

acc_list1 = zeros(ri,poi_len);
acc_list2 = zeros(ri,poi_len);
% acc_list3 = zeros(ri,poi_len);
acc_list4 = zeros(ri,poi_len);
acc_list5 = zeros(ri,poi_len);
acc_list6 = zeros(ri,poi_len);
acc_list7 = zeros(ri,poi_len);
acc_list8 = zeros(ri,poi_len);

for ii = 1:ri
    for i = 1:poi_len
        %% poison attack
        rate = ratepool(i);
        addpath('attackfile');
        load([attackn,atsvmn,dname,num2str(ii),num2str(rate*100),'dirty_label.mat']);
        load([attackn,atsvmn,dname,num2str(ii),num2str(rate*100),'dirty_data.mat']);

        %% csvc on original data
        model_org = lineartrain(org_label, org_data );
        [~,acc1,~] = linearpredict(test_label, test_data, model_org );

        %% csvc on dirty data
        model_noi = lineartrain(dirty_label, dirty_data );
        [~,acc2,~] = linearpredict(test_label, test_data, model_noi );

        %% dbscan method on dirty data
        % parameter
        eps = 1.5;
        minpts = 10;
        sh = 0.28;

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
        [clean_data,clean_label,~] = L2Defense2(dirty_data,dirty_label,rate);
        clean_data = sparse(clean_data);
        model_clean = lineartrain(clean_label,clean_data );
        [~,acc5,~] = linearpredict(test_label, test_data, model_clean );

        %% Slab defense
        [clean_data,clean_label,~] = SlabDefense2(dirty_data,dirty_label,rate);
        clean_data = sparse(clean_data);
        model_clean = lineartrain(clean_label,clean_data );
        [~,acc6,~] = linearpredict(test_label, test_data, model_clean );

        %% Loss defense
        [clean_data,clean_label,~] = LossDefense2(dirty_data,dirty_label,rate);
        clean_data = sparse(clean_data);
        model_clean = lineartrain(clean_label,clean_data );
        [~,acc7,~] = linearpredict(test_label, test_data, model_clean );

        %% Knn defense
        [clean_data,clean_label,~] = KnnDefense2(dirty_data,dirty_label,rate);
        clean_data = sparse(clean_data);
        model_clean = lineartrain(clean_label,clean_data );
        [~,acc8,~] = linearpredict(test_label, test_data, model_clean );
        
        acc_list1(ii,i) = acc1(1);
        acc_list2(ii,i) = acc2(1);
        acc_list4(ii,i) = acc4(1);
        acc_list5(ii,i) = acc5(1);
        acc_list6(ii,i) = acc6(1);
        acc_list7(ii,i) = acc7(1);
        acc_list8(ii,i) = acc8(1);
        
    end
end

clear acc1 acc2 acc4 acc5 acc6 acc7 acc8
% save(['results\satimage\acc_list1',dname,svmn,attackn],'acc_list1');
% save(['results\satimage\acc_list2',dname,svmn,attackn],'acc_list2');
% save(['results\satimage\acc_list4',dname,svmn,attackn],'acc_list4');
% save(['results\satimage\acc_list5',dname,svmn,attackn],'acc_list5');
% save(['results\satimage\acc_list6',dname,svmn,attackn],'acc_list6');
% save(['results\satimage\acc_list7',dname,svmn,attackn],'acc_list7');
% save(['results\satimage\acc_list8',dname,svmn,attackn],'acc_list8');
% 
% for j = 1:8
%     if j==3
%         continue;
%     end
%     ma = eval(['acc_list',num2str(j)]);
%     meanth = mean(ma,1);
%     stdth = std(ma,0,1);
%     save(['results\satimage\mean',num2str(j),dname,svmn,attackn],'meanth');
%     save(['results\satimage\std',num2str(j),dname,svmn,attackn],'stdth');
% end
