%%
clc
clear all
close all
% complexity_selection

first_file_path='strategy_cost_IBEC.m';
second_file_path='calculateCyclomaticComplexityWithNesting_IBEC.m';
file_path{1}=first_file_path;
file_path{2}=second_file_path;

N=2; % number of file

for i=1:1:N

    [complexity,number_of_line]=calculateCyclomaticComplexityWithNesting(file_path{i});
    complexity_matrix(1:2,i)=[complexity;number_of_line];


end

complexity_matrix;

complexity_time_weight=10;
complexity_line_weight=1;

complexity_matrix(1,1:end)=complexity_matrix(1,1:end)*complexity_time_weight;
complexity_matrix(2,1:end)=complexity_matrix(2,1:end)*complexity_line_weight;

complexity_matrix

[number_of_row,number_of_column]=size(complexity_matrix);

for i=1:1:number_of_column

    sum_matrix(i)=complexity_matrix(1,i)+complexity_matrix(2,i);

end

min=inf;
code_index=-1;

for i=1:1:number_of_column

    if sum_matrix(i) < min
        min=sum_matrix(i);
        code_index=i;
    end


end


complexity_matrix
sum_matrix
code_index










function [output,total_line]=calculateCyclomaticComplexityWithNesting(filePath)
    % List of decision keywords to search for
    keywords = {'if', 'else if', 'for', 'while', 'switch', 'case', 'try', 'catch'};
    endKeyword = 'end'; % To track nesting depth
    
    % Initialize complexity counters
    complexityCount = 0;
    nestingDepth = 0;
    total_line = 0;
    decisionCounts = containers.Map('KeyType', 'char', 'ValueType', 'double');
    
    % Initialize counters for each keyword
    for i = 1:length(keywords)
        decisionCounts(keywords{i}) = 0;
    end
    
    % Read the file content
    try
        fileID = fopen(filePath, 'r');
        if fileID == -1
            error('File could not be opened.');
        end
        
        % Read file line by line
        while ~feof(fileID)
            line = strtrim(fgetl(fileID)); % Trim whitespace
            total_line = total_line + 1;
            % Ignore comments and blank lines
            if isempty(line) || startsWith(line, '%')
                continue;
            end
            
            % Check for nesting keywords
            for k = 1:length(keywords)
                keyword = keywords{k};
                if contains(line, keyword)
                    nestingDepth = nestingDepth + 1; % Enter new block
                    decisionCounts(keyword) = decisionCounts(keyword) + 1;
                end
            end
            
            % Check for block exits
            if contains(line, endKeyword)
                nestingDepth = max(0, nestingDepth - 1); % Exit block safely
            end
        end
        fclose(fileID);
        
        % Calculate total decision points
        complexityCount = sum(cell2mat(values(decisionCounts)));
        
        % Cyclomatic complexity formula
        cyclomaticComplexity = complexityCount + 1;
        
        % Display detailed results
        fprintf('Cyclomatic Complexity of %s: %d\n', filePath, cyclomaticComplexity);
        fprintf('Nesting Depth Detected: %d\n', nestingDepth);
        fprintf('Detailed Contributions:\n');
        for k = 1:length(keywords)
            keyword = keywords{k};
            fprintf('  %s: %d\n', keyword, decisionCounts(keyword));
        end
        
    catch ME
        fprintf('Error: %s\n', ME.message);
    end
    output=cyclomaticComplexity;
    total_line=total_line;
end