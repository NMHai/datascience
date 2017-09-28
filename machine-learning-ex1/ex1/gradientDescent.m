function [theta, J_history] = gradientDescent(X, y, theta, alpha, num_iters)
%GRADIENTDESCENT Performs gradient descent to learn theta
%   theta = GRADIENTDESCENT(X, y, theta, alpha, num_iters) updates theta by 
%   taking num_iters gradient steps with learning rate alpha

% Initialize some useful values
m = length(y); % number of training examples
n = length(theta); % number of features
J_history = zeros(num_iters, 1);

for iter = 1:num_iters    
    %for j = 1:n
     % J = 0;  
     % for i = 1:m
     %   h_x = 0;
     %   for k = 1:n
      %    h_x += theta(k) * X(i,k);
      %  end 
      %  J += (h_x - y(i)) * X(i,j);
      %end 
      
      %theta(j) = theta(j) - (alpha/m) * J;       
    %end
    J_1 = 0;
    for i = 1:m
      J_1 += (theta(1) + theta(2)*X(i,2) - y(i));      
    end

    J_2 = 0;
    for i = 1:m
      J_2 += (theta(1) + theta(2)*X(i,2) - y(i)) * X(i,2);      
    end    
    theta(1) = theta(1) - (alpha/m) * J_1; 
    theta(2) = theta(2) - (alpha/m) * J_2; 
    
  
    % ====================== YOUR CODE HERE ======================
    % Instructions: Perform a single gradient step on the parameter vector
    %               theta. 
    %
    % Hint: While debugging, it can be useful to print out the values
    %       of the cost function (computeCost) and gradient here.
    %







    % ============================================================

    % Save the cost J in every iteration    
    J_history(iter) = computeCost(X, y, theta);
end

end
