currentDepth = 1; % get the supper path of the current path
currPath = fileparts(mfilename('fullpath'));% get current path
fsep = filesep;
pos_v = strfind(currPath,fsep);
p = currPath(1:pos_v(length(pos_v)-currentDepth+1)-1);