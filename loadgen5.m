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
svmn = ' '

for ii = 1:ri

    addpath('dataGenerate');
    [data,label] = synth(5000,100,0.1,40);
    data = svmscale(data);
    [org_data,org_label,test_data,test_label] = divid(data,label); 
    save(['data\syn\syn',num2str(ii),'rx'],'org_data');
    save(['data\syn\syn',num2str(ii),'ry'],'org_label');
    save(['data\syn\syn',num2str(ii),'sx'],'test_data');
    save(['data\syn\syn',num2str(ii),'sy'],'test_label');
    dname = ['syn',num2str(ii)]

    for i = 1:4

        rate = rate_pool(i);
        [dirty_data,dirty_label] = minmax_at(org_data,org_label,rate,dname,svmn);

    end  

end