
function [clean_data, clean_label, clean_index]=SVDDefense2(dirty_data,dirty_label,rate)

        
        [row,~]=size(dirty_data);
        dirty_data=full(dirty_data);
        [U,S,V]= svd(dirty_data);
        sigularValues=diag(S);
        
        denominator = sum(sigularValues.^2);
        denominator = sqrt(denominator);
        sigularValues=sigularValues/denominator;%归一化
%        accumulatesigular=cumsum(sigularValues);
%         k=find(accumulatesigular>0.8);
%         k=k(1);
        r=size(sigularValues,1);
        
        
        FrobeniusError = 0;
        i=0;
        while FrobeniusError<0.05
            i=i+1;
            FrobeniusError = sqrt(sum(sigularValues(r-i:r).^2));
        end
        k = max(1,r-i);
        V=V(1:k,:);
        diagMat=eye(k);
        
        scoreMat=(diagMat-V*V');
        distScore=zeros(row,1);
        for j=1:row
            x=dirty_data(j,1:k);
            distScore(j)=norm(scoreMat*x',2);
            
        end
        
        
        
        attackNum=round(rate*row);     %投毒的数量为k，
        [maxDist,maxIdx]=maxk(distScore,attackNum);

        dirty_data(maxIdx,:)=[];
        dirty_label(maxIdx,:)=[];
        clean_data=dirty_data;
        clean_label=dirty_label;
        
        labelTag=ones(row,1);
        labelTag(maxIdx)=0;
        clean_index=labelTag;
        
end