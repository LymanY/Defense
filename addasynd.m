clc
clear
addpath('minmax\sever\svm')
addpath('libsvm');
addpath('libnear');
addpath('dbscan');
addpath('rhoagr');
addpath('attackfile');

%%
% attackn = 'mm';
% ri = 20;
% ind_pool = [25 35 45 55 65];
% ind_len = numel(ind_pool);
% svmn = 'rbf';
% eps = 2.65;
% minpts = 5;
% sh = 0.20;
% epsr = 2.65;
% minptsr = 5;
% shr = 0.2;
% rsh = 0.1;
% s = 3;
% delta = 0.0001;
% rate = 0.1;
% 
% 
% % attackn = 'mm';
% % ri = 20;
% % ind_pool = [25 35 45 55 65];
% % ind_len = numel(ind_pool);
% % svmn = 'linear';
% % eps = 2.65;
% % minpts = 5;
% % sh = 0.20;
% % epsr = 2.65;
% % minptsr = 5;
% % shr = 0.2;
% % rsh = 0.1;
% % s = 3;
% % delta = 0.0001;
% % rate = 0.1;
% 
% for ii = 1:ri
%     for i = 1:ind_len
%         dname = ['syn',num2str(ind_pool(i)),'ind',num2str(ii)];
%         addpath(['data\syni\']);
%         load([dname,'rx.mat']);
%         load([dname,'ry.mat']);
%         load([dname,'sx.mat']);
%         load([dname,'sy.mat']);
% 
%         %% poison attack
%         rate = 0.1;
%         load([attackn,svmn,dname,num2str(rate*100),'dirty_data.mat']);
%         load([attackn,svmn,dname,num2str(rate*100),'dirty_label.mat']);
% 
%         %% csvc on original data
%         model_org = lineartrain(org_label, org_data );
%         [~,acc1,~] = linearpredict(test_label, test_data, model_org );
% 
%         %% csvc on dirty data
%         model_noi = lineartrain(dirty_label, dirty_data );
%         [~,acc2,~] = linearpredict(test_label, test_data, model_noi );
% 
%         %% dbscan method on dirty data
%         indexl1 = find(dirty_label==1);
%         indexl2 = find(dirty_label~=1);
%         clean_in1 = dbscan(full(dirty_data(indexl1,:)),minpts,eps,sh);
%         clean_in2 = dbscan(full(dirty_data(indexl2,:)),minpts,eps,sh);
%         clean_index = [indexl1(clean_in1);indexl2(clean_in2)];
%         if numel(clean_index) ~= 0 
%             if strcmp(svmn,'linear')
%                 model_dbscan = lineartrain(dirty_label(clean_index,:), dirty_data(clean_index,:) );
%                 [~,acc4,~] = linearpredict(test_label, test_data, model_dbscan );
%             else
%                 model_dbscan = libsvmtrain(dirty_label(clean_index,:), dirty_data(clean_index,:) );
%                 [~,acc4,~] = libsvmpredict(test_label, test_data, model_dbscan );
%             end
%         else
%             disp('clean_index is empty, please adjust the parameter minpts!')
%             acc4 = zeros(1,1);
%         end
%         
%         %% dbscanr
%         indexl1 = find(dirty_label==1);
%         indexl2 = find(dirty_label~=1);
%         clean_in1 = dbscanr(full(dirty_data(indexl1,:)),minptsr,epsr,shr,rsh,s,delta,rate);
%         clean_in2 = dbscanr(full(dirty_data(indexl2,:)),minptsr,epsr,shr,rsh,s,delta,rate);
%         clean_index = [indexl1(clean_in1);indexl2(clean_in2)];
%         if numel(clean_index) ~= 0 
%             if strcmp(svmn,'linear')
%                 model_dbscanr = lineartrain(dirty_label(clean_index,:), dirty_data(clean_index,:) );
%                 [~,acc9,~] = linearpredict(test_label, test_data, model_dbscanr );
%             else
%                 model_dbscanr = libsvmtrain(dirty_label(clean_index,:), dirty_data(clean_index,:) );
%                 [~,acc9,~] = libsvmpredict(test_label, test_data, model_dbscanr );
%             end
%         else
%             disp('clean_index is empty, please adjust the parameter minpts!')
%             acc9 = zeros(1,1);
%             disp(acc9)
%         end
% 
%         acc_list1(ii,i) = acc1(1);
%         acc_list2(ii,i) = acc2(1);
%         acc_list4(ii,i) = acc4(1);
%         acc_list9(ii,i) = acc9(1);
%     end
% end
% 
% 
% meanth = mean(acc_list9,1);
% stdth = std(acc_list9,0,1);
% save(['results\syni\mean9',dname,svmn,attackn],'meanth');
% save(['results\syni\std9',dname,svmn,attackn],'stdth');




%% 
attackn = 'mm';
ri = 20;
ind_pool = [50 100 150 200];
eps_pool = [2.05 2.65 3.35 3.65];
ind_len = numel(ind_pool);
svmn = 'rbf';
% eps = 2.65;
minpts = 5;
sh = 0.25;
% epsr = 2.65;
minptsr = 5;
shr = 0.25;
rsh = 0.1;
s = 3;
delta = 0.0001;
rate = 0.1;


% attackn = 'mm';
% ri = 20;
% ind_pool = [50 100 150 200];
% eps_pool = [2.05 2.65 3.35 3.65];
% ind_len = numel(ind_pool);
% svmn = 'linear';
% % eps = 2.65;
% minpts = 5;
% sh = 0.25;
% % epsr = 2.65;
% minptsr = 5;
% shr = 0.25;
% rsh = 0.1;
% s = 3;
% delta = 0.0001;
% rate = 0.1;

for ii = 1:ri
    for i = 1:ind_len
        dname = ['syn',num2str(ind_pool(i)),'eud',num2str(ii)];
        addpath(['data\syne\']);
        load([dname,'rx.mat']);
        load([dname,'ry.mat']);
        load([dname,'sx.mat']);
        load([dname,'sy.mat']);

        %% poison attack
        rate = 0.1;
        load([attackn,svmn,dname,num2str(rate*100),'dirty_data.mat']);
        load([attackn,svmn,dname,num2str(rate*100),'dirty_label.mat']);

        %% csvc on original data
        model_org = lineartrain(org_label, org_data );
        [~,acc1,~] = linearpredict(test_label, test_data, model_org );

        %% csvc on dirty data
        model_noi = lineartrain(dirty_label, dirty_data );
        [~,acc2,~] = linearpredict(test_label, test_data, model_noi );

        %% dbscan method on dirty data
        indexl1 = find(dirty_label==1);
        indexl2 = find(dirty_label~=1);
        eps = eps_pool(i);
        clean_in1 = dbscan(full(dirty_data(indexl1,:)),minpts,eps,sh);
        clean_in2 = dbscan(full(dirty_data(indexl2,:)),minpts,eps,sh);
        clean_index = [indexl1(clean_in1);indexl2(clean_in2)];
        if numel(clean_index) ~= 0 
            if strcmp(svmn,'linear')
                model_dbscan = lineartrain(dirty_label(clean_index,:), dirty_data(clean_index,:) );
                [~,acc4,~] = linearpredict(test_label, test_data, model_dbscan );
            else
                model_dbscan = libsvmtrain(dirty_label(clean_index,:), dirty_data(clean_index,:) );
                [~,acc4,~] = libsvmpredict(test_label, test_data, model_dbscan );
            end
        else
            disp('clean_index is empty, please adjust the parameter minpts!')
            acc4 = zeros(1,1);
        end
        
        %% dbscanr
        indexl1 = find(dirty_label==1);
        indexl2 = find(dirty_label~=1);
        epsr = eps_pool(i);
        clean_in1 = dbscanr(full(dirty_data(indexl1,:)),minptsr,epsr,shr,rsh,s,delta,rate);
        clean_in2 = dbscanr(full(dirty_data(indexl2,:)),minptsr,epsr,shr,rsh,s,delta,rate);
        clean_index = [indexl1(clean_in1);indexl2(clean_in2)];
        if numel(clean_index) ~= 0 
            if strcmp(svmn,'linear')
                model_dbscanr = lineartrain(dirty_label(clean_index,:), dirty_data(clean_index,:) );
                [~,acc9,~] = linearpredict(test_label, test_data, model_dbscanr );
            else
                model_dbscanr = libsvmtrain(dirty_label(clean_index,:), dirty_data(clean_index,:) );
                [~,acc9,~] = libsvmpredict(test_label, test_data, model_dbscanr );
            end
        else
            disp('clean_index is empty, please adjust the parameter minpts!')
            acc9 = zeros(1,1);
            disp(acc9)
        end

        acc_list1(ii,i) = acc1(1);
        acc_list2(ii,i) = acc2(1);
        acc_list4(ii,i) = acc4(1);
        acc_list9(ii,i) = acc9(1);
    end
end


meanth = mean(acc_list9,1);
stdth = std(acc_list9,0,1);
save(['results\syne\mean9',dname,svmn,attackn],'meanth');
save(['results\syne\std9',dname,svmn,attackn],'stdth');