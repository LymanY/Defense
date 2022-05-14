classdef CKernel < handle
% CKernel - Class for handling kernels. It extends 'matrix' by adding
% functionalities which are proper of kernels.
%

%
%    ALFASVMLib: A Matlab library for
%         adversarial label flip attacks against SVMs
%    
% See also: CKernel.CKernel, CKernel.setKernel, CKernel.getKernel,
%           CKernel.clearKernelMatrix, CKernel.computeKernel
% --
    
    properties       
        kType;                      % Kernel type, default value is 'rbf'
        gamma;                      % Parameter for rbf
        coef;                       % Parameter for polynomial kernel: coef default 1
        degree;                     % Parameter for polynomial kernel: degree default 2
    end
    
    properties (Constant)
        SUPPORTED_KERNELS = {'linear','rbf','poly', 'precomputed'}; 
    end
    
    properties (SetAccess = private)
        matrix = [];                 % A cached matrix (precomputed or computed from data)
                                     % which will store euclidean distances
                                     % for the rbf kernel, and scalar
                                     % products for the linear and
                                     % polynomial kernels.
    end
    
    methods
        % Constructor
        function obj = CKernel(varargin)
            % CKernel object constructor
            % ---------
            % Usage:
            % k = CKernel():
            %   Construct a kernel object with default type RBF.
            % k = CKernel(kernel_str):
            %   Construct a kernel object with
            %   kernel string, kernel_str should be in {'linear','rbf','poly', 'precomputed'}
            %   Default kernel type is RBF kernel.
            %   E.g., K = Ckernel('linear');
            % k = CKernel(.., param, value):
            %   Construct a kernel object with optional param-value arguments
            %   Params:
            %       'gamma'   - parameter gamma for RBF kernel, numeric
            %                   default: 1
            %       'coef'    - parameter coef for polynomial kernel, numeric 
            %                   default: 0
            %       'degree'  - parameter degree for polynomial kernel, numeric 
            %                   default: 2
            %   E.g., K = CKenel('poly','coef',1,'d',3);
            %         K = CKenel('gamma',1.5);
            % Returns: CKernel object
            % See also: CKernel, CKernel.setKernel, CKernel.getKernel,
            %           CKernel.clearKernelMatrix, CKernel.computeKernel
            % ----------
            
            p = inputParser;
            p.KeepUnmatched = true;         % in case child class passed a unknown argument
            addOptional(p, 'kType', 'rbf', ...
                            @(x) assert(ismember(x, obj.SUPPORTED_KERNELS), ...
                                        'Supported kernels are: linear, rbf, poly, precomputed!')); 
            addParamValue(p, 'gamma', 1, @isnumeric);
            addParamValue(p, 'coef', 0, @isnumeric);
            addParamValue(p, 'degree', 2, @isnumeric);
            parse(p, varargin{:});
            obj.kType = p.Results.kType;
            obj.gamma = p.Results.gamma;
            obj.coef = p.Results.coef;
            obj.degree = p.Results.degree;
        end
        
        % setters
        function set.kType(obj, t)
            if ~ischar(t) || ~ismember(t, obj.SUPPORTED_KERNELS)
                error('Please input a valid kernel type (see CKernel.SUPPORTED_KERNELS)');
            end
            obj.kType = t;
            % reset the kernel type shall empty the kernel matrix as well
            obj.clearKernelMatrix();
        end        
        function set.gamma(obj, g)
            if ~isnumeric(g)
                error('gamma must be a numeric value!');
            end
            obj.gamma = g;
        end
        function set.coef(obj, c)
            if ~isnumeric(c)
                error('coef must be a numeric value!');
            end
            obj.coef = c;
        end
        function set.degree(obj, d)
            if ~isnumeric(d)
                error('degree must be a numeric value!');
            end
            obj.degree = d;
        end
        
        function setKernel(obj, x_tr, x_ts) 
            % CKernel.setKernel
            % Set up the kernel matrix within the CKernel object, it either supports a precomputed 
            % kernel matrix, or computing from two sets of data points.
            % --------
            % Usage:
            % setKernel(k):
            %   Set precomputed kernel matrix k
            % setKernel(u, v)
            %   Set kernel matrix of the data points u and v in the CKernel
            %   by using the kernel parameters set in the object.
            %       linear: K(u,v) = u*v';
            %       rbf:    K(u,v) = e^(-gamma*pdist2(u,v)^2); 
            %       poly:   K(u,v) = (gamma*u*v + coef)^degree
            % Returns: CKernel object
            % See also: CKernel.CKernel, CKernel, CKernel.getKernel,
            %           CKernel.clearKernelMatrix, CKernel.computeKernel
            % --------
            
            
            if nargin < 2 
                error('Please input data points!');
            end
            
            is_training_matrix = 0;
            if nargin < 3
                is_training_matrix=1;
            end
            
            switch obj.kType
                case 'linear' % K(x,y) = x*y';
                    if(is_training_matrix)
                        obj.matrix=x_tr*x_tr';
                    else
                        obj.matrix = x_tr*x_ts';
                    end
                    
                case 'rbf' % K(x,y) = e^(-gamma*pdist2(x,y)^2) 
                    % Store euclidean distances to avoid dependency on parameter
                    % changes (allow for fast updates)
                    if(is_training_matrix)
                        obj.matrix = pdist2(x_tr, x_tr);
                    else
                        obj.matrix = pdist2(x_tr, x_ts);
                    end
                    
                case 'poly' % K(x,y) = (gamma*x*y + coef)^degree
                    % Store linear kernel to avoid dependency on parameter
                    % changes (allow for fast updates)
                    if(is_training_matrix)
                        obj.matrix=x_tr*x_tr';
                    else
                        obj.matrix = x_tr*x_ts';
                    end
                    
                case 'precomputed' %in this case, tr is assumed to be the kernel matrix
                    obj.matrix = x_tr;
                    
                otherwise
                    % [ISSUE] !!condition never reached!!
                    error('Kernel type is not supported!'); 
            end
        end
               
        % Get cached kernel by type. 
        % RBF is calculated based on cached dist2
        function K = getKernel(obj)   
            % CKernel.getKernel
            % Get cached kernel by type from the CKernel object. 
            % Note: RBF is calculated based on cached dist2
            % --------
            % Usage:
            % E.g., kobj = CKernel('poly');
            %       K = kobj.getKernel();        
            % Returns: kernel matrix K
            % See also: CKernel.CKernel, CKernel.setKernel, CKernel,
            %           CKernel.clearKernelMatrix, CKernel.computeKernel
            % --------
            
            if ~isempty(obj.matrix)
                switch obj.kType
                    case 'linear'
                        K = obj.matrix;
                    case 'rbf'
                        K = exp(-obj.gamma*obj.matrix.^2);
                    case 'poly'
                        K = (obj.gamma.*obj.matrix + obj.coef).^obj.degree;
                    case 'precomputed'
                        K = obj.matrix;
                    otherwise
                        % [ISSUE] !!condition never reached!!
                        error('Kernel type is unknown!');
                end
            else
                K = [];
                warning('There is no cached kernel!'); 
            end
        end
        
        function clearKernelMatrix(obj)
            % CKernel.clearKernelMatrix
            % Clear the cached kernel matrix if neccessary
            % --------
            % Usage:
            % E.g., kobj = CKernel('poly');
            %       K = kobj.clearKernelMatrix();        
            % Returns: CKernel object with empty cached kernel matrix.
            % See also: CKernel.CKernel, CKernel.setKernel, CKernel.getKernel,
            %           CKernel, CKernel.computeKernel
            % --------
            if ~isempty(obj.matrix)
                display('The cached kernel matrix is cleared...');
                obj.matrix = [];
            end
        end
    end
    
    methods (Static)
        function K = computeKernel(u, varargin)
            % CKernel.computeKernel
            % Copmute the kernel matrix by two sets of data points.
            % --------
            % Usage:
            % CKernel.computeKernel(u):
            %   u - N*d matrix of data points
            %   Compute the kernel matrix K from u by default RBF kernel
            %   with gamma's default value 1
            % CKernel.computeKernel(u, v)
            %   u - N*d matrix of data points
            %   v - M*d matrix of data points 
            %   Compute the kernel matrix K from u and v by default RBF kernel
            %   with gamma's default value 1
            % CKernel.computeKernel(u, param, value)
            % CKernel.computeKernel(u, v, param, value)
            %   u - N*d matrix of data points
            %   v - [optional] M*d matrix of data points 
            %   Compute the kernel matrix K from u and v by given
            %   param-value pair arguments.
            %   Params:
            %       'type'    -  kernel type string: 'linear', 'rbf' or 'poly'  
            %       'gamma'   -  parameter for RBF kernel, default value 1
            %       'coef'    -  parameter for polynomial kernel, default value 0
            %       'degree'  -  parameter for polynomial kernel, default value 2
            %   Instructions: 
            %       linear: K(u,v) = u*v';
            %       rbf:    K(u,v) = e^(-gamma*pdist2(u,v)^2); 
            %       poly:   K(u,v) = (gamma*u*v + coef)^degree
            %
            % Returns: kernel matrix K
            % See also: CKernel.CKernel, CKernel.setKernel, CKernel.getKernel,
            %           CKernel.clearKernelMatrix, CKernel
            % --------
            
            
            SUPPORTED = {'linear','rbf','poly'};
            p = inputParser;
            addRequired(p, 'u', @isnumeric);
            addOptional(p, 'v', u, @isnumeric);
            addParamValue(p, 'type', 'rbf', ...
                            @(x) assert(ismember(x, SUPPORTED), ...
                               'To compute the kernel matrix, supported kernel type are: linear, rbf, poly!')); 
            addParamValue(p, 'gamma', 1, @isnumeric);
            addParamValue(p, 'coef', 0, @isnumeric);
            addParamValue(p, 'degree', 2, @isnumeric);
            parse(p, u, varargin{:});
            
            switch p.Results.type
                case 'linear'
                    K = u*p.Results.v' + p.Results.coef;
                case 'rbf'
                    K = exp(-p.Results.gamma * pdist2(u, p.Results.v).^2);
                case 'poly'
                    K = (p.Results.gamma*u*p.Results.v' + p.Results.coef)^p.Results.degree;
            end
        end
    end
end
