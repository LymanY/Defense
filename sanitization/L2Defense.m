function [clean_data, clean_label]=L2Defense(dirty_data,dirty_label,rate)

        data1=dirty_data(dirty_label==1,:);
        data2=dirty_data(dirty_label==-1,:);
        centroid1=mean(data1);
        centroid2=mean(data2);
        distance1=sum(abs(data1-centroid1).^2,2);
        distance2=sum(abs(data2-centroid2).^2,2);
        distance_all=[distance1; distance2];
        [row,~]=size(distance_all);

        k=round(rate*row);    
        [~,maxIdx]=maxk(distance_all,k);
        data=[data1;data2];
        label=[ones(size(data1,1),1);-ones(size(data2,1),1)];
        data(maxIdx,:)=[];   
        label(maxIdx,:)=[];
        randIndex = randperm(size(data,1));
        clean_data=data(randIndex,:);  
        clean_label=label(randIndex,:);  

end