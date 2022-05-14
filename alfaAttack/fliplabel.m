function [dirty_label] = fliplabel(org_data,org_label,rate,svmn,dname)

test_data = org_data;
test_label = org_label;

% rate = 0.1;
%%
x_tr = org_data;
y_tr = org_label;
x_ts = test_data;
y_ts = test_label;
perf = CPerfEval();
perf.setCriterion('accuracy');
mySVM = CClassifierSVM('rbf');
mySVM.verbose = 1;
params = {'C', 'gamma'};
values = {2.^[-5,3], 2.^[-5,3]};
best = mySVM.crossval(y_tr, x_tr, ...
                      params, values, 'cperf', 'accuracy', 'kfold', 5);
best_c = best{1};       % best C for SVM
best_g = best{2};       % best gamma for SVM
fprintf('Cross validation for SVM: best_C=%f, best_gamma=%f\n', mySVM.C, mySVM.gamma);
mySVM.verbose = 0;

mySVM.train(y_tr, x_tr);
fprintf('SVM trained on %d training samples.\n', length(y_tr));
y_tt = mySVM.classify(x_ts);
acc = perf.performance(y_ts, y_tt);
err = 100*(1-acc);
fprintf('SVM Accuracy on predicting %d test samples is %f.\n', length(y_ts), acc);

flip_rate = rate;            % Default flip rate, you can change it by explicitly set it.
atk_alfa = CAttackerSVMAlfa(mySVM.kType, 'C', best_c, 'gamma', best_g);
atk_alfa.flip_rate = flip_rate;



atk_alfa.train(y_tr, x_tr); 
atk_alfa.flipLabels(y_tr, x_tr);
atk_alfa_yt = atk_alfa.classify(x_ts);
atk_alfa_yt_err = 100*(1-perf.performance(y_ts, atk_alfa_yt));

%%
dirty_label = atk_alfa.flipped_labels;

%% save

dirty_data = org_data;
save(['attackfile\','alfa',svmn,dname,num2str(rate*100),'dirty_data.mat'],'dirty_data');
save(['attackfile\','alfa',svmn,dname,num2str(rate*100),'dirty_label.mat'],'dirty_label');


end

