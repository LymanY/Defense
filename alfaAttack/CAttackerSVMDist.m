classdef CAttackerSVMDist < CAttackerSVM
% CAttackerSVMDist - Distance-based Label Flip Attack on SVM class main file
% CAttackerDist algorithm is a label flip strategy against binary
% SVM based on distances of data samples to hyperplane.
% Supported modes are 
%       1) far: flip the labels of furtherst points first;
%       2) near: flip the labels of nearest points first;
%       3) rand: randomly flip lables;
%

% --
%
% Superclass: CAttackerSVM, CAttacker
%   See also: CClassifierSVM, CAttackerSVMAlfa, CAttackerSVMAlfaCr,
%             CAttackerSVMCorrClusters

    properties
        mode;
    end
    
    methods
        % constructors
        function obj = CAttackerSVMDist(mode,varargin)
        % CAttackerSVMDist.CAttackerSVMDist
        % Constructor for CAttackerSVMDist class
        % ----------
        % Usage:
        % CAttackerSVMDist(mode):
        %    Construct a distance based adversarial label flip attacker
        %    in 'mode' {far, near, rand}
        % CAttackerSVMAlfa(mode, param, value)
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
        %   A CAttackerSVMDist object
        % See also:
        %   CAttackerSVM, CAttackerSVMDist.flipLabels
        % -------
            obj = obj@CAttackerSVM(varargin{:});
            p = inputParser;
            p.KeepUnmatched = true;     
            addRequired(p, 'mode', @(x) ...
                        assert(ismember(x, {'far','near','rand'}), ...
                               'The distance based attack shall be in (far, near, rand)'));
            parse(p, mode, varargin{:}); 
            obj.mode = p.Results.mode;
            obj.name = ['alfa-', obj.mode];
        end
        
        % setters
        function setMode(obj, m)
            if nargin < 1 || ~any(validatestring(m, {'far','near','rand'}))
                error('Supported distance-based attack modes only {''near'', ''far'', or ''rand''}!');
            else
                obj.mode = m;
                obj.name = ['Distance based ALFA: ', m];
            end
        end
        
        % attack
        function flipLabels(obj, tr_labels, tr)
            % CAttackerSVMDist.flipLabels
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
            
            num_flips = floor(length(tr_labels)*obj.flip_rate);

            % SVM properties shall be already set by previous training
            [~, dec_val] = obj.classify(tr);
            dist = abs(dec_val);
            switch obj.mode
                case 'far'
                    % far first
                    [~, idx] = sort(dist, 'descend');
                case 'near'
                    % near first
                    [~, idx] = sort(dist, 'ascend');
                case 'rand'
                    idx = randsample(length(tr_labels), length(tr_labels));
            end
            obj.flip_idx = idx(1:num_flips);
            obj.flipped_labels = tr_labels;
            obj.flipped_labels(obj.flip_idx) = -1*obj.flipped_labels(obj.flip_idx);
            
            % after label flip, we train on the contaminated training set
            % and update the SVM properties.
            obj.train(obj.flipped_labels, tr);
        end
    end
    
end
