function [theta, J_history] = gradientDescentMulti(X, y, theta, alpha, num_iters)
%GRADIENTDESCENTMULTI Performs gradient descent to learn theta
%   theta = GRADIENTDESCENTMULTI(x, y, theta, alpha, num_iters) updates theta by
%   taking num_iters gradient steps with learning rate alpha

% Initialize some useful values
m = length(y); % number of training examples
n = length(theta); % number of features
J_history = zeros(num_iters, 1);
J = zeros(1,n); 

for iter = 1:num_iters    
    for j = 1:n
      J(j) = 0;  
      for i = 1:m
        h_x = 0;
        for k = 1:n
          h_x += theta(k) * X(i,k);
        end 
        J(j) += (h_x - y(i)) * X(i,j);
      end       
    end
    
    for j = 1:n
      theta(j) = theta(j) - (alpha/m) * J(j); 
    end
    
  
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
