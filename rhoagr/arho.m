function rho = arho(data,s,delta,rate)
    [n, d] = size(data);
    m = floor(rate*n);

    tic
    [~,anchor] = kmeans(data, m);
    Z = AnchorGraph(data', anchor', s, 0, 0); 
    w = full(Z * Z');
    w(logical(eye(size(w))))=0;
    w = w + delta;
    w = w./sum(w,2);
    rho = sum(w, 1);
    toc
end