dirty_data = sparse([full(X_attack);full(X_train)]);
dirty_label = [y_attack;y_train];
save('dirty_data.mat','dirty_data');
save('dirty_label.mat','dirty_label');