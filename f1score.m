function [fscore] = f1score(dirty_label,org_label,clean_index,attackn)

    if strcmp(attackn,'alfa')
        [m] = numel(org_label);
        po = dirty_label-org_label;
        sp = (po~=0);
        np = sum(sp);
        cn = ones(m,1);
        cn(clean_index) = 0;
        c = m - numel(clean_index);
        df = sp - cn;
        fp = sum(df == -1);
        fn = sum(df == 1);
        tp = c-fp;
        fscore = 2*tp/(2*tp+fp+fn);

    elseif strcmp(attackn,'mm')

        dlnum = numel(dirty_label);
        olnum = numel(org_label);
        atnum = dlnum - olnum;

        sp = [ones(atnum,1);zeros(olnum,1)];
        cn = ones(dlnum,1);
        cn(clean_index) = 0;
        df = sp - cn;

        fp = sum(df == -1);
        fn = sum(df == 1);
        c = dlnum - numel(clean_index);
        tp = c-fp;
        fscore = 2*tp/(2*tp+fp+fn);

    end

end



% function [fscore] = f1score(dirty_label,org_label,clean_index)
% 
% dlnum = numel(dirty_label);
% olnum = numel(org_label);
% atnum = dlnum - olnum;
% 
% % po = dirty_label-org_label;
% % sp = (po~=0);
% % np = sum(sp);
% % cn = ones(dlnum,1);
% % cn(clean_index) = 0;
% % c = dlnum - numel(clean_index);
% % df = sp - cn;
% 
% sp = [ones(atnum,1);zeros(olnum,1)];
% cn = ones(dlnum,1);
% cn(clean_index) = 0;
% df = sp - cn;
% 
% fp = sum(df == -1);
% fn = sum(df == 1);
% c = dlnum - numel(clean_index);
% tp = c-fp;
% fscore = 2*tp/(2*tp+fp+fn);
% 
% end
