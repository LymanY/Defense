function [c] = svmscale(c)
    [m,n]=size(c);                  %%��ȡ����m �� ����  n
    lower=-1;
    upper=1;                       %%���ù�һ����Χ [lower ,upper]
    Cmax=zeros(1,n);                     
    Cmin=zeros(1,n);                     
    for i=1:n
        Cmax(1,i)=max(c(:,i));              %%Cmax��������ÿһ���е����ֵ
    end
    for i=1:n
        Cmin(1,i)=min(c(:,i));               %%Cmin��������ÿһ���е���Сֵ
    end
    for i=1:m
        for j=1:n
            if Cmax(1,j)~=Cmin(1,j)
                c(i,j)=lower+(upper-lower)*(  c(i,j)-Cmin(1,j)   )/(Cmax(1,j)-Cmin(1,j));  %%ִ��ǰ���Ĺ�ʽ���й�һ��
            else
                c(i,j)=0;
            end
        end
    end
end

