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


ri = 5;
rate_pool = [0.04 0.06 0.08 0.1];
svmn = ' ';

for ii = 1:ri

    addpath('dataGenerate');
    [data,label] = synth(5000,100,0.5,40);
    data = svmscale(data);
    [org_data,org_label,test_data,test_label] = divid(data,label); 
    save(['data\syna\syna',num2str(ii),'rx'],'org_data');
    save(['data\syna\syna',num2str(ii),'ry'],'org_label');
    save(['data\syna\syna',num2str(ii),'sx'],'test_data');
    save(['data\syna\syna',num2str(ii),'sy'],'test_label');
    dname = ['syna',num2str(ii)];

    for i = 1:4

        rate = rate_pool(i);
        dirty_data = org_data;
        [dirty_label] = fliplabel(org_data,org_label,rate,svmn,dname);

    end  

end

%%

clc
clear


addpath('minmax');
addpath('dbscan');
addpath('frtsvm');
addpath('rrsvm');
addpath('libsvm');
addpath('libnear');
addpath('sanitization');

ratepool = [0.04 0.06 0.08 0.1];
dname = 'syna';
atsvmn = ' ';
attackn = 'alfa';
svmn = 'linear';

ri = 5;
poi_len = numel(ratepool);
% fscore = zeros(5,poi_len,ri);
addpath('data\syna');

acc_list1 = zeros(ri,poi_len);
acc_list2 = zeros(ri,poi_len);
acc_list3 = zeros(ri,poi_len);
acc_list4 = zeros(ri,poi_len);
acc_list5 = zeros(ri,poi_len);
acc_list6 = zeros(ri,poi_len);
acc_list7 = zeros(ri,poi_len);
acc_list8 = zeros(ri,poi_len);
acc_list9 = zeros(ri,poi_len);

for ii = 1:ri

    dname = ['syna',num2str(ii)];
    load([dname,'rx.mat']);
    load([dname,'ry.mat']);
    load([dname,'sx.mat']);
    load([dname,'sy.mat']);

    [m,~] = size(org_data);


    for i = 1:poi_len
        %% poison attack
        rate = ratepool(i);

        addpath('attackfile');
        load([attackn,atsvmn,dname,num2str(rate*100),'dirty_label.mat']);
        load([attackn,atsvmn,dname,num2str(rate*100),'dirty_data.mat']);


        %% csvc on original data
        model_org = lineartrain(org_label, org_data );
        [~,acc1,~] = linearpredict(test_label, test_data, model_org );

        %% csvc on dirty data
        model_noi = lineartrain(dirty_label, dirty_data );
        [~,acc2,~] = linearpredict(test_label, test_data, model_noi );

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


save(['results\syna\acc_list1',dname,svmn,attackn],'acc_list1');
save(['results\syna\acc_list2',dname,svmn,attackn],'acc_list2');
save(['results\syna\acc_list4',dname,svmn,attackn],'acc_list4');
save(['results\syna\acc_list5',dname,svmn,attackn],'acc_list5');
save(['results\syna\acc_list6',dname,svmn,attackn],'acc_list6');
save(['results\syna\acc_list7',dname,svmn,attackn],'acc_list7');
save(['results\syna\acc_list8',dname,svmn,attackn],'acc_list8');



for j = 1:9
    
    ma = eval(['acc_list',num2str(j)]);
    meanth = mean(ma,1);
    stdth = std(ma,0,1);
    save(['results\syna\mean',num2str(j),dname,svmn,attackn],'meanth');
    save(['results\syna\std',num2str(j),dname,svmn,attackn],'stdth');

end


%%

clc
clear


addpath('minmax');
addpath('dbscan');
addpath('frtsvm');
addpath('rrsvm');
addpath('libsvm');
addpath('libnear');
addpath('sanitization');

ratepool = [0.04 0.06 0.08 0.1];
dname = 'syna';
atsvmn = ' ';
attackn = 'alfa';
svmn = 'rbf';

ri = 5;
poi_len = numel(ratepool);
% fscore = zeros(5,poi_len,ri);
addpath('data\syna');

acc_list1 = zeros(ri,poi_len);
acc_list2 = zeros(ri,poi_len);
acc_list3 = zeros(ri,poi_len);
acc_list4 = zeros(ri,poi_len);
acc_list5 = zeros(ri,poi_len);
acc_list6 = zeros(ri,poi_len);
acc_list7 = zeros(ri,poi_len);
acc_list8 = zeros(ri,poi_len);
acc_list9 = zeros(ri,poi_len);

for ii = 1:ri

    dname = ['syna',num2str(ii)];
    load([dname,'rx.mat']);
    load([dname,'ry.mat']);
    load([dname,'sx.mat']);
    load([dname,'sy.mat']);

    [m,~] = size(org_data);


    for i = 1:poi_len
        %% poison attack
        rate = ratepool(i);

        addpath('attackfile');
        load([attackn,atsvmn,dname,num2str(rate*100),'dirty_label.mat']);
        load([attackn,atsvmn,dname,num2str(rate*100),'dirty_data.mat']);


        %% csvc on original data
        model_org = libsvmtrain(org_label, org_data );
        [~,acc1,~] = libsvmpredict(test_label, test_data, model_org );

        %% csvc on dirty data
        model_noi = libsvmtrain(dirty_label, dirty_data );
        [~,acc2,~] = libsvmpredict(test_label, test_data, model_noi );

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
        
        acc_list1(ii,i) = acc1(1);
        acc_list2(ii,i) = acc2(1);
        acc_list4(ii,i) = acc4(1);
        acc_list5(ii,i) = acc5(1);
        acc_list6(ii,i) = acc6(1);
        acc_list7(ii,i) = acc7(1);
        acc_list8(ii,i) = acc8(1);
        
    end

end


save(['results\syna\acc_list1',dname,svmn,attackn],'acc_list1');
save(['results\syna\acc_list2',dname,svmn,attackn],'acc_list2');
save(['results\syna\acc_list4',dname,svmn,attackn],'acc_list4');
save(['results\syna\acc_list5',dname,svmn,attackn],'acc_list5');
save(['results\syna\acc_list6',dname,svmn,attackn],'acc_list6');
save(['results\syna\acc_list7',dname,svmn,attackn],'acc_list7');
save(['results\syna\acc_list8',dname,svmn,attackn],'acc_list8');



for j = 1:9
    
    ma = eval(['acc_list',num2str(j)]);
    meanth = mean(ma,1);
    stdth = std(ma,0,1);
    save(['results\syna\mean',num2str(j),dname,svmn,attackn],'meanth');
    save(['results\syna\std',num2str(j),dname,svmn,attackn],'stdth');

end