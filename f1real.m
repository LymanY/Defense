clc
clear

addpath('libsvm');
addpath('sanitization');
addpath('dbscan');

ratepool = [0.04 0.06 0.08 0.1];
dname = 'satimage';
svmn = ' ';
attackn = 'alfa';

ri = 5;
poi_len = numel(ratepool);
fscore = zeros(5,poi_len,ri);
addpath(['data\',dname]);

for ii = 1:ri

    load([dname,'rx.mat']);
    load([dname,'ry.mat']);
    load([dname,'sx.mat']);
    load([dname,'sy.mat']);

    [m,~] = size(org_data);


    for i = 1:poi_len
        %% poison attack
        rate = ratepool(i);

        addpath('attackfile');
        load([attackn,svmn,dname,num2str(ii),num2str(rate*100),'dirty_label.mat']);
        load([attackn,svmn,dname,num2str(ii),num2str(rate*100),'dirty_data.mat']);


        %% dbscan method on dirty data
        % parameter
        eps = 2.5;
        minpts = 3;
        sh = 0.2;

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