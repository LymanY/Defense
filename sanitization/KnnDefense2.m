
function [clean_data, clean_label, clean_index]=KnnDefense2(dirty_data,dirty_label,rate)
Kneighbor=5;
distMat=pdist2(dirty_data,dirty_data);
[row,~]=size(dirty_data);
KneighborDist=ones(row,1);
for r=1:row
    [~,KDist]=maxk(distMat(r,:),Kneighbor);
    KneighborDist(r)=KDist(Kneighbor);
end


k=round(rate*row);    
[maxDist,maxIdx]=maxk(KneighborDist,k);
dirty_data(maxIdx,:)=[];
dirty_label(maxIdx,:)=[];
clean_data=dirty_data;
clean_label=dirty_label;

labelTag=ones(row,1);
labelTag(maxIdx)=0;
clean_index=labelTag;

end

