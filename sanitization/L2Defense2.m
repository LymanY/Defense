function [clean_data, clean_label, clean_index]=L2Defense2(dirty_data,dirty_label,rate)

data1=dirty_data(dirty_label==1,:);
data2=dirty_data(dirty_label==-1,:);
centroid1=mean(data1);
centroid2=mean(data2);

[row,~]=size(dirty_data);
distance_all=zeros(row,1);
for r=1:row
    x=dirty_data(r,:);
    y=dirty_label(r,:);
    if y==1
        distance_all(r) = sum(abs(x-centroid1).^2,2);
    else
        distance_all(r) = sum(abs(x-centroid2).^2,2);
    end
    
end


k=round(rate*row);    %投毒的数量为k，
[~,maxIdx]=maxk(distance_all,k);
dirty_data(maxIdx,:)=[];   %%在data中删除k个最偏样本，data便是L2清洗后的数据
dirty_label(maxIdx,:)=[];
clean_data=dirty_data;
clean_label=dirty_label;

labelTag=ones(row,1);
labelTag(maxIdx)=0;
clean_index=labelTag;


end