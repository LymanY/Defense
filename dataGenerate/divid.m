function [org_data,org_label,test_data,test_label] = divid (data,label)
    [m n] = size(data);
    sh = randperm(m);
    ra = 0.3*m;
    q = sh(1:ra);
    r = sh(ra+1:m);
    org_data = data(q,:);
    test_data = data(r,:);
    org_label = label(q);
    test_label = label(r);

    org_label = org_label*2-1;
    test_label = test_label*2-1;
end

