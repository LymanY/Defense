classdef CClassifierSVM < CClassifier & CKernel 
% SVM class wrapping for libsvm ver >= 3.17 (required)
%

%    ALFASVMLib: A Matlab library for
%         adversarial label flip attacks against SVMs
%    
% See also: CClassifier, CClassifierSVM.CClassifierSVM, CKernel,
% CClassifierSVM.train, CClassifierSVM.classify,
% CClassifierSVM.classifyPrecomputed, CClassifierSVM.plot
% --
    
    properties
        name = 'SVM';
        verbose = false;    % Default set verbose off while learning;
        C = 1;              % Default cost coefficient is 1;
        sv;                 % Support vectors
        sv_idx;             % Indices of support vectors 
        alpha;              % Learned SVM alphas
        b;                  % Bias term
        y;                  % Labels of SVs
        cmd;                % libsvm options string
        n;                  % number of training samples
        one_class;          % indicate wether it is 1-class or 2-class SVM classification
        nu;                 %it sets an upper bound on the fraction of outliers (training examples regarded out-of-class) and,
                            %it is a lower bound on the number of training examples used as Support Vector.
    end
    
    methods
        % constructor
        function obj = CClassifierSVM(varargin)
        % CClassifierSVM.CClassifierSVM
        % Constructor for CClassifierSVM class
        % ----------
        % Usage:
        % CClassifierSVM():
        %    Constructor without argument will create a default SVM object
        %    with RBF kernel setting C=1, gamma=1, see also parent class CKernel.
        % CClassifierSVM(kernel_str):
        %    Constructor with a input kernel string will create a SVM
        %    object with given kernel type in {'linear','rbf','poly','precomputed'}
        %    using default C=1, and default kernel parameters. 
        %    e.g., CClassifierSVM('poly')
        % CClassifierSVM(param, value)
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
        %       'one_class' - indication wether this is one-class
        %                     classification, true or false
        %                     default: false
        %       'nu'        - it sets an upper bound on the fraction of outliers (training examples regarded out-of-class) and,
        %                     it is a lower bound on the number of training examples used as Support Vector.
        % Returns:
        %   A CClassifierSVM object
        % See also:
        %   CClassifier, CClassifierSVM, CKernel.CKernel
        % -------
            
            obj = obj@CKernel();             % Default kernel for SVM 
            p = inputParser;
            p.KeepUnmatched = true;                     % in case child class passed a unknown argument
            addOptional(p, 'ker', 'rbf', @(x) any(validatestring(x,obj.SUPPORTED_KERNELS)));
            addParamValue(p, 'C', 1, @(x) x>0);    
            addParamValue(p, 'verbose', false);
            addParamValue(p, 'gamma', 1, @isnumeric);
            addParamValue(p, 'coef', 0, @isnumeric);
            addParamValue(p, 'degree', 2, @isnumeric);
            addParamValue(p, 'one_class', false);
            addParamValue(p, 'nu', 0.5);
            parse(p, varargin{:}); 
            obj.kType = p.Results.ker;
            obj.C = p.Results.C;                        % Default cost coef is 1  
            obj.gamma = p.Results.gamma;                % Default gamma is 1 
            obj.coef = p.Results.coef;                  % Default coef is 0
            obj.degree = p.Results.degree;              % Default degree is 2
            obj.verbose = p.Results.verbose;            % Default true: set mute while learning
            obj.one_class = p.Results.one_class;        % Defalut one_class is false
            obj.nu = p.Results.nu;                      % Defalut nu is 0.5
        end
        
        % setters
        function set.C(obj, c)
            if ~isnumeric(c)
                error('You should input a numeric value for C!');
            end
            obj.C = c;
        end
        function set.nu(obj, nu)
            obj.nu = nu;
        end
        function set.verbose(obj, v)
            obj.verbose = v;
        end

        % SVM training (should return the training kernel matrix)
        function train(obj, tr_labels, tr)
            % CClassifierSVM.train
            % SVM training from training data and labels
            % It will set all the SVM model properties in the object after
            % training, which can be used for classification.
            % ----------
            % Usage:
            % train(tr_labels):
            %    SVM train using only the precomputed kernel inside the SVM
            %    object. Only training labels are needed.
            %    Inputs:
            %       tr_labels: N*1 vectors containing classes
            %                  e.g., binary classification, [-1,+1]
            % train(tr_labels, tr):
            %    SVM train from N*1 training labels and N*d training data
            %    Inputs:
            %       tr_labels: N*1 vectors containing classes
            %       tr:        N*d matrix containing training samples
            % See also: CClassifierSVM.CClassifierSVM,
            %   CClassifierSVM.classify, CClassifierSVM.plot
            % -------
            
            % TODO: support more SVM type, incl. multi-class, nu-SVM,
            %      one-class, SVR and so on.
            if obj.one_class
                obj.cmd = [  '-s 2', ... %this is for one-class in libsvm
                        ' -t 4', ... %kernel precomputed (always as such in this wrapper)
                        ' -c ', num2str(obj.C),...
                        ' -n ', num2str(obj.nu)];
            else
                obj.cmd = [  '-s 0', ... %this is for SVC in libsvm
                        ' -t 4', ... %kernel precomputed (always as such in this wrapper)
                        ' -c ', num2str(obj.C)];
            end
            if obj.verbose==0
                obj.cmd = [obj.cmd, ' -q'];
            end
            
            obj.n=size(tr_labels,1);    %number of samples
            
            if nargin > 2  
                if strcmp(obj.kType, 'precomputed')
                    error('You need to set a precomputed kernel matrix first, and call train(tr_labels)!');
                end
                %this stores/computes the training kernel matrix inside the SVM
                obj.setKernel(tr); 
                K = obj.getKernel();
                
                % SVM training with precomputed kernel
                model = libsvmtrain(tr_labels, [(1:size(K,1))', K], obj.cmd); 
                
                % Set the SVM model properties after training 
                % [ISSUE] model.SVs in precomputed mode only contain sv_indices
                [obj.sv_idx, idx]= sort(full(model.SVs));
                obj.alpha = abs(model.sv_coef);
                obj.alpha = obj.alpha(idx);     %sort alpha's according to sv_idx
                obj.b = -model.rho;
                obj.y = tr_labels(obj.sv_idx);
                obj.sv = tr(obj.sv_idx, :);
            else  
                % If there is no input training set
                % Only training labels are given, we assume a precomputed K
                % is set already in the SVM object.
                
                if strcmp(obj.kType, 'precomputed') && ~isempty(obj.matrix)
                    K = obj.getKernel();
                    model = libsvmtrain(tr_labels, [(1:size(K,1))', K], obj.cmd);
                    [obj.sv_idx, idx]= sort(full(model.SVs));
                    obj.alpha = abs(model.sv_coef);
                    obj.alpha = obj.alpha(idx);     % Sort alpha's according to sv_idx
                    obj.b = -model.rho;
                    obj.y = tr_labels(obj.sv_idx);
                    obj.sv = [];                    % No training set is given, so SVs are empty
                else
                    error('You need either a precomputed kernel matrix or a training set!');
                end
            end                
        end
               
        %Classification
        function [yc, score] = classify(obj, ts)
            % CClassifierSVM.classify
            % Classify test set by the SVM object after training
            % The SVM model is already stored inside the object.
            % ----------
            % Usage:
            % [yc, score] = classify(ts)
            %    Classify test set either by input a test sample set or a
            %    precomputed kernel.
            %    Inputs:
            %       ts: M*d vectors of testing data set 
            %           or M*N matrix of kernel matrix 
            % Returns:
            %    yc:    predicted class labels
            %    score: decision values 
            % See also: CClassifierSVM.CClassifierSVM,
            %   CClassifierSVM.train, CClassifierSVM.plot,
            %   CClassifierSVM.classifyPrecomputed
            % -------
            
            if nargin < 2 
                error('No samples to be classified!');
            end
            if strcmp(obj.kType, 'precomputed')
                warning('The passed argument should be a precomputed kernel matrix!'); 
                [yc, score] = obj.classifyPrecomputed(ts); 
                return; 
            else
                % classify test data using SVs.
                % compute TS x SVs kernel matrix
                K_ts=CKernel(obj.kType, ...
                                'g', obj.gamma, ...
                                'coef', obj.coef, ...
                                'd', obj.degree);
                K_ts.setKernel(ts, obj.sv);

                [yc, score] = obj.classifyPrecomputed(K_ts.getKernel());        
            end
        end
        
        % SVM classification using precomputed (test) kernel
        % TODO: I think K should not be a 'generic matrix', but an instance
        % of CKernel instead!
        function  [yc, score] = classifyPrecomputed(obj, K)  
            % CClassifierSVM.classifyPrecomputed
            % Classify test set by the SVM object using a precomputed
            % kernel.
            % ----------
            % Usage:
            % [yc, score] = classify(K)
            %    Inputs:
            %       K: M*s matrix of kernel matrix, s is number of SVs
            % Returns:
            %    yc:    predicted class labels
            %    score: decision values 
            % See also: CClassifierSVM.CClassifierSVM,
            %   CClassifierSVM.train, CClassifierSVM.plot,
            %   CClassifierSVM.classify
            % -------
            score = K*(obj.y.*obj.alpha)+obj.b;
            yc = 2*(score >= 0)-1;
        end
        
        %Get SVM dual solution 
        function [alpha b] = getDualCoeff(obj)
            % CClassifierSVM.getDualCoeff
            % Returns SVM dual solution alpha and b
            
            alpha=zeros(obj.n,1);
            alpha(obj.sv_idx)=obj.alpha;
            b=obj.b;
        end
        
        function margin_SV_idx = getMarginSVs(obj)
            % CClassifierSVM.getDualCoeff
            % Returns SVM margin SVs's indices
            
            alpha_n = obj.getDualCoeff();
            margin_SV_idx = find(alpha_n > 1E-6 & alpha_n < obj.C-1E-6);
        end
        
        function [bigX, bigY, bigZ]=plot(obj, tr_labels, tr, varargin)
            % CClassifierSVM.plot
            % Plots the decision boundary of SVM classifier
            % on two-dimensional data, and highlights -1 and +1 margins
            % as well as the support vectors.
            % ------
            % Usage:
            % [bigX, bigY, bigZ]=plot(tr_labels, tr)
            % [bigX, bigY, bigZ]=plot(tr_labels, tr, param, value)
            % Inputs:  
            %   tr_labels: N*1 training labels, in {-1,+1} (can be easily extended to
            %                    the multi-class case, see code)
            %   tr:        N*d training samples
            %   params:
            %       background:     - Whether show shading background,
            %                         default:false
            %       pointSize:      - size of sample point
            %       svSize:         - size of SVs
            %       grids:          - 1x4 vector for the range of plotting
            %                         grid, default value is determined from tr.
            %       title:          - Title text string
            %       xLabel:         - Label string for x-axis
            %       yLabel:         - Label string for y-axis
            % Returns:
            %   bigX: X coordinates of the plotting grids
            %   bigY: Y coordinates of the plotting grids
            %   bigZ: Decision values of the plotting grids
            % -------
            
            
            % [BUG FIX]: plot for precomputed kernel type is not working
            
            [bigX, bigY, bigZ]=plot@CClassifier(obj, tr_labels, tr, varargin{:});
            p = inputParser;
            p.KeepUnmatched = true;
            addParamValue(p, 'svSize', 12, @(x) isnumeric(x) && x>=0);
            parse(p, varargin{:});
            hold on;
            
            % add -1/+1 margins
            contour(bigX, bigY, bigZ, [-1 0 1], '--k'); %clabel(C,h);
            
            % highlight SVs
            if p.Results.svSize
                plot(tr(obj.sv_idx,1),tr(obj.sv_idx,2),'ko','MarkerSize',p.Results.svSize);
            end
        end 
    end
    
end
