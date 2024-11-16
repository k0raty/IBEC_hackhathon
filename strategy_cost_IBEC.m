%%
clc
clear all
close all

%%

N=3; % number of strategy

%%% Construction of strategy_cost matrix
%%% First 2 value of 1st row for first strategy, other 2 value of 1st row for 2nd strategy and go on
%%% Values on 2nd row are cost values of upper strategies

%%% Basic strategy_cost construction
initial_value=2;
    for i=1:1:N*2
        strategy_cost(1,i)=initial_value;
        initial_value=initial_value+1;
    end

initial_value=-1;
   for i=1:1:N*2
        strategy_cost(2,i)=initial_value;
        initial_value=initial_value-1;
   end
strategy_cost
%%%

max_strategy=-inf; % initial value to find maximum strategy
min_cost=inf; %initial value to find minium cost


%%% Construct to find minimum cost for each strategy
i=1;
for j=1:2:2*N-1

    if strategy_cost(2,j+1) < strategy_cost(2,j)
       min_slug=strategy_cost(2,j+1);
    else
       min_slug=strategy_cost(2,j);

    end
    cost(i)=min_slug;
    i=i+1;
end
cost;
%%%


%%% Construct to find maximum strategy
j=1;
for i=1:2:N*2
  
    if strategy_cost(1,i+1) > strategy_cost(2,i)
       max_slug=strategy_cost(1,i+1);
    else
       max_slug=strategy_cost(1,j);

    end

   if max_slug >= max_strategy

       max_strategy=max_slug;
       index_of_max_strategy=j;

   end
   
   j=j+1;


end
max_strategy;
index_of_max_strategy;
%%%

%%% Optimum Solution
index_of_max_strategy
max_strategy
min_cost=cost(index_of_max_strategy)
payoff=max_strategy+cost(index_of_max_strategy)
