
function [clean_data, clean_label, clean_index]=LossDefense2(dirty_data,dirty_label,rate)


        [row,~]=size(dirty_data);
        dirty_model = libsvmtrain(dirty_label, dirty_data);
        %timer(2)=toc(tmark1);
        [predict_label, accuracy, dec_values] = libsvmpredict(dirty_label, dirty_data, dirty_model);
        
        %index1=org_label==1;index2=org_label==-1;
        
        dec_values_abs=abs(dec_values);
        
        k=round(rate*row);    
        [minDist,minIdx]=mink(dec_values_abs,k);
        dirty_data(minIdx,:)=[];
        dirty_label(minIdx,:)=[];
        clean_data=dirty_data;
        clean_label=dirty_label;
        
        labelTag=ones(row,1);
        labelTag(minIdx)=0;
        clean_index=labelTag;
        
end