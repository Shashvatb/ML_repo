"""
Linear Regression is a regression method to estimate unknown parameters

The equation is given by: y = Xw + b;
where X are the input features, w are the weights to be learned and b is the bias term

Assumptions:
1. Weak exogeneity: The values of X are fixed variables rather than random variables
2. Linearity: This means that "y" is a linear combination of its "x" values

It fits the parameters by minimizing the least square error
error = sum((yi - wixi)^2)

"""