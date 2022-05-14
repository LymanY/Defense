clear

addpath('sever\svm');
% load('mushroomrx.mat');
% load('mushroomry.mat');
% load('mushroomsx.mat');
% load('mushroomsy.mat');
load('letterrx.mat');
load('letterry.mat');
load('lettersx.mat');
load('lettersy.mat');
% [data,label] = synth(5000,100,0.1,40);
% data = svmscale(data);
% % label = label*2-1;
% [org_data,org_label,test_data,test_label] = divid(data,label,0.4); 
% loadmnist;
% loadenron;
% loadijcnn;
% loaddna;
% loadsatimage;
% loaddata;


X_train = org_data;
y_train = org_label;
% clear org_data;
% clear org_label;
n = size(X_train,1);


% tidx = randperm(n);
% idx1 = tidx(1:ceil(0.7*n));
% idx2 = tidx(ceil(0.7*n)+1:n);
% X_test = X_train(idx2,:);
% y_test = y_train(idx2);
% X_train = X_train(idx1,:);
% y_train = y_train(idx1);


%%
% options.timeit = 0;
options = struct();

options.quantile_tape = [0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55];% [0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35];
options.rep_tape = [1, 2, 3, 5, 8, 12, 18, 25, 33];% [1, 2, 3, 5, 8, 12, 18, 25];
options.prune = 1;
% options.method = 'adagrad';
% options.method = 'sgd';
options.method = 'exact';
options.batch_size = min(100, ceil(0.005 * n));
options.decay = 0.001;
% options.guarder = @(t){0*t,t};
options.guarder = @(t){0*t};
options.use_train = 1;
options.loss = 'hinge';

%%
options.LP = 1;
options.eta_mm = 0.06;
options.eta = 0.04;
options.p = 0.3 ;% 0.30;
options.burn_frac = 1.0;
options.rho_max = 0.25;
options.att_rep = 2;
options.evaluation_trials = 1;
options.slab = 0;

% options.decay = 0.01;
% options.burn_frac = 0.33;
% options.prune = 0;
% options.batch_size = 66;
% options.p = 0.3;


%%
% [thetas, biases, train_losses, test_errors, quantiles, reps, options] = generateTheta(X_train, y_train, X_train, y_train, X_test, y_test, options);
[thetas, biases, train_losses, test_errors, quantiles, reps, options] = generateTheta(X_train, y_train, X_train, y_train, X_train, y_train, options);

%%

% i_s = size(thetas);
i_s = 1;
theta_tar = thetas{i_s};
bias_tar = biases{i_s};
epsilon = 0.1;
pn = round(epsilon * size(org_data,1));

%%
% [X_attack, y_attack, ~, ~, base_err] = generateAttackTar(X_train, y_train, X_train, y_train, X_test, y_test, theta_tar, bias_tar, epsilon, options, pn);
[X_attack, y_attack, ~, ~, base_err] = generateAttackTar(X_train, y_train, X_train, y_train, X_train, y_train, theta_tar, bias_tar, epsilon, options, pn);


%%

dirty_data = sparse([full(X_attack);full(org_data)]);
dirty_label = [y_attack;org_label];
save('dirty_data.mat','dirty_data');
save('dirty_label.mat','dirty_label');

%%

% org_data = full(org_data);
model_org = libsvmtrain(org_label, org_data );
% model_org = libsvmtrain(org_label, org_data ,'-c 8 -g 0.005');
[~,acc1,~] = svmpredict(test_label, test_data, model_org );

model_noi = libsvmtrain(dirty_label, dirty_data );
% model_noi = libsvmtrain(dirty_label, dirty_data ,'-c 8 -g 0.005');
[~,acc2,~] = svmpredict(test_label, test_data, model_noi );


%%

org_data = sparse(org_data);
model_org = lineartrain(org_label, org_data );
[~,acc1,~] = linearpredict(test_label, test_data, model_org );

test_data = sparse(test_data);
model_noi = lineartrain(dirty_label, dirty_data );
[~,acc2,~] = linearpredict(test_label, test_data, model_noi );
    