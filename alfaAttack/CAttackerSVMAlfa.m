classdef CAttackerSVMAlfa < CAttackerSVM
% CAttackerSVMAlfa - Adv. Label Flip Attack class main file
% ALFA algorithm is an adversarial label flip strategy against binary
% SVM, details please refer to Han Xiao & Huang Xiao's paper (Adversarial 
% Label Flips Attack on Support Vector Machines, ECAI'12)
%

%
% Superclass: CAttackerSVM
%   See also: CAttackerSVM,CAttackerSVMAlfa.flipLabels
% --
    
    properties
        maxIter = 50;       % Maximal number of iterations
    end
    
    methods
        % constructors
        function obj = CAttackerSVMAlfa(varargin)
        % CAttackerSVMAlfa.CAttackerSVMAlfa
        % Constructor for CAttackerSVMAlfa class
        % ----------
        % Usage:
        % CAttackerSVMAlfa():
        %    Constructor without argument will create a default CAttackerSVMAlfa object
        %    with RBF kernel setting C=1, gamma=1, see also class CClassifierSVM.
        % CAttackerSVMAlfa(kernel_str):
        %    Constructor with a input kernel string will create a CAttackerSVMAlfa
        %    object with given kernel type in {'linear','rbf','poly','precomputed'}
        %    using default C=1, and default kernel parameters. 
        %    e.g., CAttackerSVMAlfa('poly')
        % CAttackerSVMAlfa(param, value)
        %    Construtor with optional param-value pair arguments.
        %    Params:
        %       'ker':    - kernel string in {'linear','rbf','poly','precomputed'}
        %       'C':      - regularization coefficient, default as 1,
        %                   numeric, positive
        %       'gamma'   - parameter gamma for RBF kernel, numeric
        %                   default: 1
        %       'coef'    - parameter coef for polynomial kernel, numeric 
        %                   default: 0
        %       'degree'  - parameter degree for polynomial kernel, numeric 
        %                   default: 2
        %       'verbose' - set verbose while learning, true or false
        % Returns:
        %   A CAttackerSVMAlfa object
        % See also:
        %   CAttackerSVM, CAttackerSVMAlfa.flipLabels
        % -------
            obj = obj@CAttackerSVM(varargin{:});
            obj.maxIter = 50;
            obj.name = 'alfa';
        end
% <REMOVEME>    
%         % setTargetClassifier: SVM
%         function obj = setTargetClassifier(obj, svm)
%             if ~isa(svm, 'CClassifierSVM')
%                 error('You can not set a target other than SVM!');
%             end
%             % Set corresponding SVM properties from svm to the current ALFA
%             if isempty(svm.sv)
%                 warning('Target SVM model is not valid, maybe using a precomputed kernel?');
%                 return;
%             else
%                 obj.type = svm.type;
%                 obj.C = svm.C;
%                 obj.gamma = svm.gamma;
%                 obj.degree = svm.degree;
%                 obj.coef = svm.coef;
%                 obj.sv = svm.sv;                    % Support vectors
%                 obj.sv_idx = svm.sv_idx;            % Indices of support vectors 
%                 obj.alpha = svm.alpha;              % Learned SVM alphas
%                 obj.b = svm.b;                      % Bias term
%                 obj.y = svm.y;                      % Labels of SVs
%                 obj.isTargetReady = true;
%             end
%         end
%</REMOVEME>    
        % setters
        function set.maxIter(obj, max_iter)
            if max_iter <= 0
                error('Maximum iteration must be a positive number!');
            else
                obj.maxIter=max_iter;
            end
        end
        
        % attack
        function flipLabels(obj, tr_labels, tr)
            % CAttackerSVMAlfa.flipLabels
            % Adversarial label attack flip will flip a certain amount of
            % labels in training set, the SVM is retrained on the
            % contaminated data set to incur a degration of final SVM
            % classification performance. 
            % ----------
            % Usage:
            % flipLabels(tr_labels, tr):
            %    Inputs:
            %       tr_labels: N*1 vectors containing classes
            %                  e.g., binary classification, [-1,+1]
            %       tr:        N*d training data set
            % Returns:
            %   Properties:
            %       obj.flipped_labels
            %       obj.flip_idx 
            %   are both set in the object.
            % See also: CClassifierSVM.CClassifierSVM, CAttacker,
            %           CAttackerSVM.
            % -------
            
            if nargin < 3
                error('Not enough inputs, please input training labels and training set.');
            end
               
            % No flip at all
            if obj.flip_rate == 0 
                warning('Nothing happend, no label is flipped!');
                obj.flipped_labels = tr_labels;
                return;
            end
            
            % shuffle the data
            obj.flipped_labels = tr_labels;
            rand_idx = randsample(length(tr_labels),length(tr_labels));
            tr_labels = tr_labels(rand_idx,:);
            tr = tr(rand_idx, :);
            
            % duplicate data
            dbl_labels = [tr_labels; -tr_labels];
            dbl_tr = [tr; tr];    
            n1 = length(tr_labels);
            num_flips = floor(obj.flip_rate * n1);
            
            A = zeros(2*n1, 2*n1);
            B = [ones(n1,1); zeros(n1,1)];
            
            % ensure flip
            for j = 1:n1
                A(j, j) = 1;
                A(j, n1+j) = 1;
            end
            A(n1+1, (n1+1):end) = 1;
            B = [ones(n1,1); zeros(n1,1)];
            B(n1+1) = num_flips;                % Ensure flip m at most
            
            % dec_value using target's SVM model on duplicate data set
            [~, dec_val] = obj.classify(dbl_tr);
            old_e = max(0, 1 - dbl_labels .* dec_val);
            
            % start cvx optimization process ...
            cvx_clear;
            cvx_quiet(1);
                        
            % Reset variables
            old_q = [ones(n1,1); zeros(n1,1)];
            % A heustics to avoid stucking in initial local optimal
            cur_e = rand(2*n1,1);
            
            C=1;
            clear q
            
            % start iteration
            for k = 1:obj.maxIter
                if obj.quiet
                    fprintf('.');
                end
                cvx_begin %solve linear program
                    variables q(2*n1)
                    minimize(C*(sum(q.*(cur_e-old_e))))
                    subject to
                        0 <= q <= 1;
                        A*q == B;
                cvx_end
                
                [~, allIdx] = sort(q, 'descend');
                selected_labels = dbl_labels(allIdx(1:n1));
                selected_data = dbl_tr(allIdx(1:n1), :);
                
                % update the model using selected samples
                obj.train(selected_labels, selected_data);
                
                % dec_value on new model
                [~, dec_val] = obj.classify(dbl_tr);
                cur_e = max(0,1-dbl_labels .* dec_val);
                
                diff_q = find(abs((old_q - q)) > 1e-3);
                
                if any(diff_q)
                    if ~obj.quiet
                        fprintf('[%d] %d instances flipped.\n', k, length(diff_q)/2);
                    end
                    old_q = q;
                else
                    fprintf('\n\t ALFA terminated at %d iteration.\n', k);
                    break;
                end
            end
            allIdx=allIdx(allIdx > n1);
            obj.flip_idx = rand_idx(allIdx(1:min(num_flips, numel(allIdx)))-n1);
            obj.flipped_labels(obj.flip_idx) = -obj.flipped_labels(obj.flip_idx);
        end
        
    end
    
end
