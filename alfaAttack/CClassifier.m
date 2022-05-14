classdef (Abstract) CClassifier < handle
    % CClassifier - abstract class defining common
    %               classifier members and methods.
    %

    %
    %    ALFASVMLib: A Matlab library for
    %         adversarial label flip attacks against SVMs
    %
    % See also: CClassifier.crossval, CClassifier.plot
    % --
    
    properties (Abstract)
        name;       % classifier name / id
        verbose;    % verbose mode
    end
    
    
    methods (Abstract)
        train(obj, tr_labels, tr);
        classify(obj, tt_labels, tt);
    end
    
    
    methods
        
        function set(obj, param, value)
            % CClassifier.set
            % A wrapping function to set parameters of classifier
            % -------
            % Usage:
            % E.g., svm.set('C',0.1)
            % -------
            
            eval(['obj.' param '=' num2str(value) ';' ]);
        end
        
        % <REMOVEME>
        %         function [cv_partition best_values cv_perf_mean cv_perf_std]= ...
        %                 crossval(obj, tr_labels, tr, peval, params, values, num_folds, cv_partition)
        % --- Huang: I think num_folds and cv_partition is kinda of
        % duplicated. I recommend to avoid passing customized
        % cv_partition obj. A traditional CV process by k-folds shall be
        % enough for users.
        % Another thing is that peval obj can be optional by setting a
        % default performance standard of accuracy, it is more
        % practical for users I think.
        % </REMOVEME>
        
        function [best means stds cvp]= ...
                crossval(obj, tr_labels, tr, params, values, varargin)
            % CClassifier.crossval
            % Cross-validation procedure for model selection of the
            % classifier. After the best parameters are found, classifier is trained over
            % all training data using the best parameters.
            % ---------
            % Usage:
            % [best means stds cvp] = crossval(tr_labels, tr, params, values)
            % Inputs: tr_labels: N*1 labels of training data
            %         tr:        N*d training samples
            %         params:    Cell array of strings containing evaluated
            %                    parameters' name, e.g. {'C','gamma'}
            %         values:    Cell array of vectors containing evaluated
            %                    value sets, e.g. {10.^[-3:3],10.^[-3:3]}
            % [best means stds cvp] = crossval(tr_labels, tr, params, values, cperf)    
            % Inputs: peval: istance of CPerEval class (to set the performance metric)
            %         cperf (Optional):   
            %               A string for classifier performace measurement, 
            %               which must be in {'accuracy', 'auc', 'pauc', 'tp_at_fp', 'eer'}
            %
            % [best means stds cvp] = crossval(tr_labels, tr, params, values, cperf, param, value) 
            %         Param:  'kfold':   the number of folds (default: 5)
            %
            % Returns:
            % best:   The best selected value for each parameter in params
            %
            % means:  The vector of CV means of evaluated performances of
            %         classifier on given paramters
            % stds:   The vector of CV standard deviations of evaluated performances of
            %         classifier on given paramters
            % cvp:    The indexes of each fold (as a 'cvpartition' object).
            %               In case one wants to repeat xval on the same folds, this
            %               parameter can be passed as input
            % 
            % See also: CClassifier
            % ---------
            
            %  Parsing the input arguments
            p = inputParser;
            addRequired(p, 'tr_labels');
            addRequired(p, 'tr');
            addRequired(p, 'params', @iscellstr);
            addRequired(p, 'values', @(x) ...
                        assert(all(cellfun(@isnumeric, x)),...
                        'You can only pass numeric values to the parameters!'));
            addOptional(p, 'cperf', 'accuracy', @(x) ...
                        assert(any(ismember(x, {'accuracy', 'auc', 'pauc', 'tp_at_fp', 'eer'})), ...
                                    'Evaluation criteria must be in [accuracy, auc, pauc, tp_at_fp, eer]'));
            addParamValue(p, 'kfold', 5, @(x) ...
                        assert(x>0, 'Number of folds must be a positive integer!'));
            parse(p, tr_labels, tr, params, values, varargin{:});
            
            %  Setting up the parameters
            num_folds = p.Results.kfold;
            peval = CPerfEval();
            peval.setCriterion(p.Results.cperf);
            cvp = cvpartition(numel(tr_labels),'kfold',num_folds);
            
            %             if(nargin < 7)
            %                 num_folds=5;
            %             end
            %
            %             if(nargin < 8)
            %                cv_partition = cvpartition(numel(tr_labels),'kfold',num_folds);
            %             end
            
            %set num_folds consistently with cv_partition, if this parameter is passed.
            %             num_folds=cv_partition.NumTestSets;
            
            %now, let's analyze params and values
            num_params = numel(params);
            
            % [ISSUE]Huang: I'm not sure if we should give user this option to
            % pass a single grid matrix
            grids=values{1}; %if values has a single vector inside, it is assumed to be in the right 'grid' format
            %otherwise, we generate the grid
            if(num_params==numel(values)) %values is of type {10.^[-3:3],10.^[-3:3]}
                %then we have to create a unique grid
                grids = combvec(values{:})';
            else
                error('Number of value sets must equal the number of parameters to be evaluated!');
            end
            
            %this is the cross-validation
            cv_perf_mean = zeros(size(grids,1),1);
            cv_perf_std = zeros(size(grids,1),1);
            parfor i=1:size(grids,1)
                disp_str=[];
                for p=1:num_params
                    obj.set(params{p},grids(i,p)); %set all parameter values
                    disp_str= [disp_str params{p} ': ' num2str(grids(i,p)) ', '];
                end
                
                perf=zeros(num_folds,1);
                for k=1:num_folds
                    tr_idx = cvp.training(k);
                    ts_idx = cvp.test(k);
                    
                    %train
                    obj.train(tr_labels(tr_idx), tr(tr_idx,:));
                    
                    %test
                    [~,score]=obj.classify(tr(ts_idx,:));
                    perf(k)=peval.performance(tr_labels(ts_idx),score);
                end
                %average performance
                cv_perf_mean(i)=mean(perf);
                cv_perf_std(i)=std(perf);
                disp_str=['crossval: ' disp_str 'perf. (mean): ' num2str(cv_perf_mean(i)) ' (std: ' num2str(cv_perf_std(i)) ')\n'];
                
                if(obj.verbose)
                    fprintf(disp_str);
                end
            end
            
            %now pick the best parameters
            [~, idx]=max(cv_perf_mean);
            best=cell(1,num_params);
            for p=1:num_params
                best{p}=grids(idx,p);
                obj.set(params{p},best{p}); %set best parameter values
            end
            
            
            means = cv_perf_mean(idx);
            stds = cv_perf_std(idx);
            obj.train(tr_labels,tr); %train over all data
            display('====== Cross validation finished! =======');
        end
        
        function [bigX, bigY, bigZ]=plot(obj, tr_labels, tr, varargin)
            % CClassifier.plot
            % Plots the decision function of a two-class classifier
            % on two-dimensional data
            % ------
            % Usage:
            % [bigX, bigY, bigZ]=plot(tr_labels, tr)
            % [bigX, bigY, bigZ]=plot(tr_labels, tr, param, value)
            % Inputs:  
            %   tr_labels: N*1 training labels, in {-1,+1} (can be easily extended to
            %                    the multi-class case, see code)
            %   tr:        N*d training samples
            %
            %   params:
            %       background:     - Whether show shading background,
            %                         default:false
            %       pointSize:      - size of sample point
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
            
            if(size(tr,2)>2)
                error('You can only draw 2-D classifier boundary!');
            end
            
            grid_coords=[min(tr(:,1)), max(tr(:,1)), min(tr(:,2)), max(tr(:,2))];
            p = inputParser;
            p.KeepUnmatched = true;
            addParamValue(p, 'background', false);
            addParamValue(p, 'pointSize', 18, @(x) isnumeric(x) && x>=0);
            addParamValue(p, 'grids', grid_coords, @(x) length(x(:))==4 && isnumeric(x));
            addParamValue(p, 'title', 'Classifier Boundary', @(x) ischar(x));
            addParamValue(p, 'xLabel', '', @(x) ischar(x));
            addParamValue(p, 'yLabel', '', @(x) ischar(x));
            parse(p, varargin{:});
            minX=p.Results.grids(1);
            maxX=p.Results.grids(2);
            minY=p.Results.grids(3);
            maxY=p.Results.grids(4);
            
            % Create an n x n grid of points
            n=40; [bigX, bigY] = meshgrid(minX:(maxX-minX)/(n-1):maxX, ...
                minY:(maxY-minY)/(n-1):maxY);
            
            ntest=size(bigX, 1) * size(bigX, 2);
            instance_test=[reshape(bigX, ntest, 1), ...
                reshape(bigY, ntest, 1)];
            
            % Classify points in the grid
            [~, Z] = obj.classify(instance_test);
            bigZ = reshape(Z, size(bigX, 1), size(bigX, 2));
            
            % Drawing background, and decision boundary
            if(p.Results.background)
                contourf(bigX, bigY, bigZ, 50); %colorbar;
%               colormap('cool'); 
                shading flat
            end
            hold on
            box on
            axis square
            contour(bigX, bigY, bigZ, [0 0], 'k');
            
            % Printing data points in red or blue according to y
            if p.Results.pointSize
                plot(tr(tr_labels==1,1),tr(tr_labels==1,2),'r.','MarkerSize',p.Results.pointSize);
                plot(tr(tr_labels==-1,1),tr(tr_labels==-1,2),'b.','MarkerSize',p.Results.pointSize);
            
                % Making points' border more prominent
                plot(tr(:,1),tr(:,2),'ko','MarkerSize',p.Results.pointSize/3);
            end
            grid on
            set(gca,'layer','top');
            axis(p.Results.grids);
            title(p.Results.title);
            xlabel(p.Results.xLabel);
            ylabel(p.Results.yLabel);
        end
    end
end
