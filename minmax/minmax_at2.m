function [dirty_data,dirty_label] = minmax_at(org_data,org_label,epsilon,dname,stringi,svmn)
   %% options
    options = struct();
    options.quantile_tape = [0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55];% [0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35];
    options.rep_tape = [1, 2, 3, 5, 8, 12, 18, 25, 33];% [1, 2, 3, 5, 8, 12, 18, 25];
    options.prune = 1;
    options.method = 'adagrad';
%     options.method = 'sgd';
%     options.method = 'exact';
    n = numel(org_label);
    options.batch_size = min(100, ceil(0.005 * n));
    options.decay = 0.001;
    options.guarder = @(t){0*t};
    options.use_train = 1;
    options.loss = 'hinge';
    options.LP = 1;
    options.eta_mm = 0.06;
    options.eta = 0.04;
    options.p = 0.3 ;% 0.010;
    options.burn_frac = 1.0;
    options.rho_max = 0.25;
    options.att_rep = 2;
    options.evaluation_trials = 1;
    options.slab = 0;
    
    options.method = 'adagrad';
    options.decay = 0.003;
    options.p = 0.002;
    options.eta_mm = 0.06;
    options.eta = 0.04;
    
    if strcmp(dname,'letter')
        options.method = 'exact';
        options.decay = 0.0008;
        options.p = 0.1;  
        options.eta_mm = 0.06;
        options.eta = 0.04;
    end
    
    if strcmp(dname,'mushroom')
        options.method = 'sgd';
        options.decay = 0.003;
        options.p = 0.002;
        options.eta_mm = 0.15;
        options.eta = 0.1;
        if strcmp(svmn,'linear')
            options.eta_mm = 0.6;
            options.eta = 0.4;
        else
            options.eta_mm = 0.06;
            options.eta = 0.04;
        end        
    end
    
    if strcmp(dname,'satimage')
        options.method = 'adagrad';
        options.decoy = 0.03;
        options.p = 0.01;   
        options.eta_mm = 0.15;
        options.eta = 0.1;
    end
    
%     if strcmp(dname,'syn')
%         options.method = 'adagrad';
%         options.decay = 0.003;
%         options.p = 0.002;
%         options.eta_mm = 0.06;
%         options.eta = 0.04;   
%     end
%     
%     if strcmp(dname,'syn50eud')||strcmp(dname,'syn100eud')||strcmp(dname,'syn150eud')||strcmp(dname,'syn200eud')
%         options.method = 'adagrad';
%         options.decay = 0.003;
%         options.p = 0.002;
%         options.eta_mm = 0.06;
%         options.eta = 0.04;   
%     end
%     
%     if strcmp(dname,'syn25ind')||strcmp(dname,'syn35ind')||strcmp(dname,'syn45ind')||strcmp(dname,'syn55ind')||strcmp(dname,'syn65ind')
%         options.method = 'adagrad';
%         options.decay = 0.003;
%         options.p = 0.002;
%         options.eta_mm = 0.06;
%         options.eta = 0.04;   
%     end
    
   %% decoy parameter
    [thetas, biases, train_losses, test_errors, quantiles, reps, options] = generateTheta(org_data, org_label, org_data, org_label, org_data, org_label, options);

   %% pre
    i_s = 1;
    theta_tar = thetas{i_s};
    bias_tar = biases{i_s};
    pn = round(epsilon * size(org_data,1));
    
   %% attack
    [X_attack, y_attack, ~, ~, base_err] = generateAttackTar(org_data, org_label, org_data, org_label, org_data, org_label, theta_tar, bias_tar, epsilon, options, pn);
    
   %% 
    dirty_data = sparse([full(X_attack);full(org_data)]);
    dirty_label = [y_attack;org_label];
    save(['attackfile\','mm',svmn,dname,stringi,num2str(epsilon*100),'dirty_data.mat'],'dirty_data');
    save(['attackfile\','mm',svmn,dname,stringi,num2str(epsilon*100),'dirty_label.mat'],'dirty_label');
end

