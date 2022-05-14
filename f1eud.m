clc
clear

addpath('libsvm');
addpath('sanitization');
addpath('dbscan');

ind_pool = [50 100 150 200];
svmn = 'rbf';
attackn = 'mm';
eps_pool = [2.05 2.75 3.40 3.95];

ri = 20;
ind_len = numel(ind_pool);
fscore = zeros(5,ind_len,ri);


for ii = 1:ri


    for i = 1:ind_len
        
        dname = ['syn',num2str(ind_pool(i)),'eud',num2str(ii)];
        addpath(['data\syne\']);
        load([dname,'rx.mat']);
        load([dname,'ry.mat']);
        load([dname,'sx.mat']);
        load([dname,'sy.mat']);
        [m,~] = size(org_data);
        
        
        %% poison attack
        rate = 0.1;

        addpath('attackfile');
        load([attackn,svmn,dname,num2str(10),'dirty_label.mat']);
        load([attackn,svmn,dname,num2str(10),'dirty_data.mat']);


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
        fscore(1,i,ii) = f1score(dirty_label,org_label,clean_index,attackn);


        %% L2 defense
        [~,~,clean_index] = L2Defense2(dirty_data,dirty_label,rate);
        clean_index = find(clean_index~=0);
        fscore(2,i,ii) = f1score(dirty_label,org_label,clean_index,attackn);

        %% Slab defense
        [~,~,clean_index] = SlabDefense2(dirty_data,dirty_label,rate);
        clean_index = find(clean_index~=0);
        fscore(3,i,ii) = f1score(dirty_label,org_label,clean_index,attackn);

        %% Loss defense
        [~,~,clean_index] = LossDefense2(dirty_data,dirty_label,rate);
        clean_index = find(clean_index~=0);
        fscore(4,i,ii) = f1score(dirty_label,org_label,clean_index,attackn);

        %% Knn defense
        [~,~,clean_index] = KnnDefense2(dirty_data,dirty_label,rate);
        clean_index = find(clean_index~=0);
        fscore(5,i,ii) = f1score(dirty_label,org_label,clean_index,attackn);

    end

end


fm = mean(fscore,3);
fs = std(fscore,0,3);
disp(fm);
disp(fs);