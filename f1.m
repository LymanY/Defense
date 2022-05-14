clc
clear

addpath('libsvm');
addpath('libnear');
addpath('sanitization');
addpath('dbscan');

ratepool = [0.04 0.06 0.08 0.1];
dname = 'syn';
svmn = ' ';
attackn = 'mm';

ri = 5;
poi_len = numel(ratepool);
fscore = zeros(5,poi_len,ri);
addpath('data\syn');

for ii = 1:ri

    dname = ['syn',num2str(ii)];
    load([dname,'rx.mat']);
    load([dname,'ry.mat']);
    load([dname,'sx.mat']);
    load([dname,'sy.mat']);

    [m,~] = size(org_data);


    for i = 1:poi_len
        %% poison attack
        rate = ratepool(i);

        addpath('attackfile');
        load([attackn,svmn,dname,num2str(rate*100),'dirty_label.mat']);
        load([attackn,svmn,dname,num2str(rate*100),'dirty_data.mat']);


        %% dbscan method on dirty data
        % parameter
        eps = 2.85;
        minpts = 5;
        sh = 0.20;

        indexl1 = find(dirty_label==1);
        indexl2 = find(dirty_label~=1);
        clean_in1 = dbscan(full(dirty_data(indexl1,:)),minpts,eps,sh);
        clean_in2 = dbscan(full(dirty_data(indexl2,:)),minpts,eps,sh);
        clean_index = [indexl1(clean_in1);indexl2(clean_in2)];
        fscore(1,i,ii) = f1score(dirty_label,org_label,clean_index);


        %% L2 defense
        [~,~,clean_index] = L2Defense2(dirty_data,dirty_label,rate);
        clean_index = find(clean_index~=0);
        fscore(2,i,ii) = f1score(dirty_label,org_label,clean_index);

        %% Slab defense
        [~,~,clean_index] = SlabDefense2(dirty_data,dirty_label,rate);
        clean_index = find(clean_index~=0);
        fscore(3,i,ii) = f1score(dirty_label,org_label,clean_index);

        %% Loss defense
        [~,~,clean_index] = LossDefense2(dirty_data,dirty_label,rate);
        clean_index = find(clean_index~=0);
        fscore(4,i,ii) = f1score(dirty_label,org_label,clean_index);

        %% Knn defense
        [~,~,clean_index] = KnnDefense2(dirty_data,dirty_label,rate);
        clean_index = find(clean_index~=0);
        fscore(5,i,ii) = f1score(dirty_label,org_label,clean_index);

    end

end