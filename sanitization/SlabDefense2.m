function [clean_data, clean_label, clean_index]=SlabDefense2(dirty_data,dirty_label,rate)

        data1=dirty_data(dirty_label==1,:);
        data2=dirty_data(dirty_label==-1,:);
        centroid1=mean(data1);
        centroid2=mean(data2);
        centroidDiff=centroid1-centroid2;
        
        [row,~]=size(dirty_data);
        distScore=zeros(row,1);
        for r=1:row
            x=dirty_data(r,:);
            distScore(r)=dot(centroidDiff,x);
          
        end
        
        k=round(rate*row);     
        [maxDist,maxIdx]=maxk(distScore,k);

        dirty_data(maxIdx,:)=[];
        dirty_label(maxIdx,:)=[];
        clean_data=dirty_data;
        clean_label=dirty_label;
        
        labelTag=ones(row,1);
        labelTag(maxIdx)=0;
        clean_index=labelTag;
end