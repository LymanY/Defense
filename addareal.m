clc
clear
addpath('minmax\sever\svm')
addpath('libsvm');
addpath('libnear');
addpath('rhoagr');
addpath('attackfile');

atsvmn = ' ';
ratepool = [0.04 0.06 0.08 0.1];
poi_len = numel(ratepool);
ri = 5;

svmn = 'linear'; % rbf or linear

dname = 'satimage';
attackn = 'alfa';
% parameter
eps = 2.5;
minpts = 3;
sh = 0.2;
epsr = 2.5;
minptsr = 3;
shr = 0.2;
rsh = 0.1;
s = 3;
delta = 0.0001;
rate = 0.1;

% dname = 'satimage';
% attackn = 'mm';
% % parameter
% eps = 1.5;
% minpts = 10;
% sh = 0.28;
% epsr = 2;
% minptsr = 5;
% shr = 0.28;
% rsh = -0.1;
% s = 3;
% delta = 0.0001;
% rate = 0.1;

% dname = 'mushroom';
% attackn = 'alfa';
% % parameter
% eps = 3.74;
% minpts = 5;
% sh = 0.2;
% epsr = 3.74;
% minptsr = 5;
% shr = 0.2;
% rsh = -0.5;
% s = 3;
% delta = 0.0001;
% rate = 0.1;

% dname = 'mushroom';
% attackn = 'mm';
% % parameter
% eps = 3.5;
% minpts = 5;
% sh = 0.2;
% epsr = 3.5;
% minptsr = 5;
% shr = 0.2;
% rsh = -0.5;
% s = 3;
% delta = 0.0001;
% rate = 0.1;

% dname = 'letter';
% attackn = 'alfa';
% % parameter
% eps = 0.9;
% minpts = 5;
% sh = 0.2;
% epsr = 0.9;
% minptsr = 5;
% shr = 0.2;
% rsh = -0.5;
% s = 3;
% delta = 0.0001;
% rate = 0.1;

% dname = 'letter';
% attackn = 'mm';
% % parameter
% eps = 0.9;
% minpts = 5;
% sh = 0.2;
% epsr = 0.9;
% minptsr = 5;
% shr = 0.2;
% rsh = -0.5;
% s = 3;
% delta = 0.0001;
% rate = 0.1;


for ii = 1:ri
    addpath(['data\',dname]);
    load([dname,'rx.mat']);
    load([dname,'ry.mat']);
    load([dname,'sx.mat']);
    load([dname,'sy.mat']);
    [m,~] = size(org_data);
    for i = 1:poi_len
        %% poison attack
        rate = ratepool(i);
        addpath('attackfile');
        load([attackn,atsvmn,dname,num2str(ii),num2str(rate*100),'dirty_label.mat']);
        load([attackn,atsvmn,dname,num2str(ii),num2str(rate*100),'dirty_data.mat']);
        
        if strcmp(svmn,'linear')
            %% csvc on original data
            model_org = lineartrain(org_label, org_data );
            [~,acc1,~] = linearpredict(test_label, test_data, model_org );
            %% csvc on dirty data
            model_noi = lineartrain(dirty_label, dirty_data );
            [~,acc2,~] = linearpredict(test_label, test_data, model_noi );
        else 
            %% csvc on original data
            model_org = libsvmtrain(org_label, org_data );
            [~,acc1,~] = libsvmpredict(test_label, test_data, model_org );
            %% csvc on dirty data
            model_noi = libsvmtrain(dirty_label, dirty_data );
            [~,acc2,~] = libsvmpredict(test_label, test_data, model_noi );
        end  
        %% dbscan method on dirty data

        indexl1 = find(dirty_label==1);
        indexl2 = find(dirty_label~=1);
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
        acc_list9(ii,i) = acc9(1);
    end
end

meanth = mean(acc_list9,1);
stdth = std(acc_list9,0,1);
disp(meanth)
disp(stdth)
save(['results\letter\mean9',dname,svmn,attackn],'meanth');
save(['results\letter\std9',dname,svmn,attackn],'stdth');