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

dname = 'letter';
addpath(['data\',dname]);
load([dname,'rx.mat']);
load([dname,'ry.mat']);
load([dname,'sx.mat']);
load([dname,'sy.mat']);

for ii = 1:ri
    
%     dname = ['letter',num2str(ii)];

    for i = 1:4

        rate = rate_pool(i);
        [dirty_data,dirty_label] = minmax_at2(org_data,org_label,rate,dname,num2str(ii),svmn);
%         [dirty_label] = fliplabel(org_data,org_label,rate,svmn,[dname,num2str(ii)]);

    end  

end


%%
dname = 'mushroom';
addpath(['data\',dname]);
load([dname,'rx.mat']);
load([dname,'ry.mat']);
load([dname,'sx.mat']);
load([dname,'sy.mat']);

for ii = 1:ri
    
%     dname = ['mushroom',num2str(ii)];

    for i = 1:4

        rate = rate_pool(i);
        [dirty_data,dirty_label] = minmax_at2(org_data,org_label,rate,dname,num2str(ii),svmn);
%         [dirty_label] = fliplabel(org_data,org_label,rate,svmn,[dname,num2str(ii)]);

    end  

end


%%
dname = 'satimage';
addpath(['data\',dname]);
load([dname,'rx.mat']);
load([dname,'ry.mat']);
load([dname,'sx.mat']);
load([dname,'sy.mat']);

for ii = 1:ri
    
%     dname = ['satimage',num2str(ii)];

    for i = 1:4

        rate = rate_pool(i);
        [dirty_data,dirty_label] = minmax_at2(org_data,org_label,rate,dname,num2str(ii),svmn);
%         [dirty_label] = fliplabel(org_data,org_label,rate,svmn,[dname,num2str(ii)]);

    end  

end