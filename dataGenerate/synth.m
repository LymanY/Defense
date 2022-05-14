function [data,label] = synth(nh,d,move,tarD)
    n1=nh;
    n2=nh;
    W=randn(d);
    A=zeros(d,n1);
    B=zeros(d,n2);
    pA=randn(tarD,n1);
    pB=randn(tarD,n2);
    sq1 = randperm(d);
    R1 = sq1(1:tarD);
    sq2 = randperm(d);
    R2 = sq2(1:tarD);
    A(R1,:)=pA;
    B(R2,:)=pB;
    
    A = A+move;
    B = B-move;
    
    A=W*A;
    B=W*B;
    data = [A';B'];
    data = sparse(data);
    label1 = ones(nh,1);
    label2 = zeros(nh,1);
    label = [label1;label2];

end

