classdef (Abstract) CAttacker < handle 
% CAttacker - abstract attacker class attacking classifiers
%

%
%    ALFASVMLib: A Matlab library for
%         adversarial label flip attacks against SVMs
%   
% See also: CAttacker.plotFlippedLabels
% --
    

    properties 
        flip_rate;          % Fraction of label flips in the training set
        quiet;              % Mute while attacking
        flip_idx;           % Indices of flipped labels in the training set
        flipped_labels;     % Labels after flipping
    end
    
    methods (Abstract = true)
        flipLabels(obj, tr_labels, tr);         % Flip attack 
    end
    
    
    methods
        
        function obj = CAttacker()
            obj.flip_rate=0.1;
            obj.flip_idx=[];
            obj.flipped_labels=[];
            obj.quiet=true;         %use quiet for attacks, verbose for SVM
        end
        
        function set.flip_rate(obj, r)
            if r > 1 || r < 0
                error('Flip rate can only between 0 and 1!');
            else
                obj.flip_rate = r;
            end
        end
        
        function plotFlippedLabels(obj, tr)
        % CAttacker.plotFlippedLabels
        % Plot flipped labels in circle markers.
           plot(tr(obj.flip_idx,1), tr(obj.flip_idx,2),'go','MarkerSize',8);
        end
    end
        
end
