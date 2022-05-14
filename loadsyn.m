% addpath('dataGenerate');
% [data,label] = synth(5000,100,0.1,40);
% data = svmscale(data);
% [org_data,org_label,test_data,test_label] = divid(data,label); 
% 
% save('data\syn\synrx','org_data');
% save('data\syn\synry','org_label');
% save('data\syn\synsx','test_data');
% save('data\syn\synsy','test_label');


% for i = 25:10:65
%     addpath('dataGenerate');
%     [data,label] = synth(5000,100,0.1,i);
%     data = svmscale(data);
%     [org_data,org_label,test_data,test_label] = divid(data,label); 
%     dname = ['syn',num2str(i),'ind'];
% 
%     save(['data\',dname,'\',dname,'rx'],'org_data');
%     save(['data\',dname,'\',dname,'ry'],'org_label');
%     save(['data\',dname,'\',dname,'sx'],'test_data');
%     save(['data\',dname,'\',dname,'sy'],'test_label');
% end


% for i = 50:50:200
%     addpath('dataGenerate');
%     [data,label] = synthd(5000,i,40);
%     data = svmscale(data);
%     [org_data,org_label,test_data,test_label] = divid(data,label); 
%     dname = ['syn',num2str(i),'eud'];
% 
%     save(['data\',dname,'\',dname,'rx'],'org_data');
%     save(['data\',dname,'\',dname,'ry'],'org_label');
%     save(['data\',dname,'\',dname,'sx'],'test_data');
%     save(['data\',dname,'\',dname,'sy'],'test_label');
% end


% addpath('dataGenerate');
% [data,label] = synth(5000,100,0.5,40);
% data = svmscale(data);
% [org_data,org_label,test_data,test_label] = divid(data,label); 
% 
% save('data\syna\synarx','org_data');
% save('data\syna\synary','org_label');
% save('data\syna\synasx','test_data');
% save('data\syna\synasy','test_label');