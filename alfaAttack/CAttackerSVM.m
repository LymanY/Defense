classdef (Abstract) CAttackerSVM < CAttacker & CClassifierSVM
    % CAttackerSVM - abstract attacker class attacking SVM-based classifiers
    %
    % Superclass: CAttacker and CClassifierSVM
    %   See also: CClassifierSVM

    %
    %    ALFASVMLib: A Matlab library for
    %         adversarial label flip attacks against SVMs
    %
    % Super classes: CAttacker, CClassifierSVM
    % See also: CAttacker, CClassifierSVM, CAttackerSVM.plot
    % --
    
    
    methods
        function obj = CAttackerSVM(varargin)
            obj = obj@CAttacker();
            obj = obj@CClassifierSVM(varargin{:});
        end
        
        function [bigX, bigY, bigZ]=plot(obj, tr, varargin)
            % CAttackerSVM.plot
            % Plots the decision boundary of SVM classifier after attack
            % on two-dimensional data, and highlight the flipped labels in
            % circles. 
            % ------
            % Usage:
            % [bigX, bigY, bigZ]=plot(tr)
            % [bigX, bigY, bigZ]=plot(tr, param, value)
            % Inputs:  
            %   tr:         N*d training samples
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
            % See also: CClassifierSVM.plot, CAttacker.plotFlippedLabels
            % -------
            
            [bigX, bigY, bigZ]=plot@CClassifierSVM(obj, obj.flipped_labels, tr, varargin{:});
            hold on;
            obj.plotFlippedLabels(tr);
        end
    end
    
end
