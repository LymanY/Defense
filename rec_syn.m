% clc
% clear
% 
% for ii = 1:20
% 
%     for i = 25:10:65
%         addpath('dataGenerate');
%         [data,label] = synth(5000,100,0.1,i);
%         data = svmscale(data);
%         [org_data,org_label,test_data,test_label] = divid(data,label); 
%         dname = ['syn',num2str(i),'ind',num2str(ii)];
% 
%         save(['data\syni\',dname,'rx'],'org_data');
%         save(['data\syni\',dname,'ry'],'org_label');
%         save(['data\syni\',dname,'sx'],'test_data');
%         save(['data\syni\',dname,'sy'],'test_label');
%     end
% 
% 
%     for i = 50:50:200
%         addpath('dataGenerate');
%         [data,label] = synthd(5000,i,40);
%         data = svmscale(data);
%         [org_data,org_label,test_data,test_label] = divid(data,label); 
%         dname = ['syn',num2str(i),'eud',num2str(ii)];
% 
%         save(['data\syne\',dname,'rx'],'org_data');
%         save(['data\syne\',dname,'ry'],'org_label');
%         save(['data\syne\',dname,'sx'],'test_data');
%         save(['data\syne\',dname,'sy'],'test_label');
%     end
%     
% end


% run_syneud_linear_mm;
% run_syneud_rbf_mm;
% run_synind_linear_mm;
% run_synind_rbf_mm;