import numpy
from scipy.optimize import minimize
from scipy.optimize import Bounds
from scipy.optimize import LinearConstraint
from scipy.optimize import NonlinearConstraint
from scipy.optimize import SR1

#the cost function
def fx(x):
    out = x[0]*7890 + x[1] * 2100 + x[2] * 65000 + x[3] * 78000 + x[4] * 3100
    return out

#bounds of variables : 0<x<1
bounds = Bounds(numpy.zeros(5), numpy.zeros(5)+numpy.inf)

#linear constraint = 22000 < x1 + x2 + x3 + x4 + x5 < 23000
linear_constraint = LinearConstraint ([1,1,1,1,1],22500,23000)

def cons_f(x):
    out =  [(5.7*x[0] + 16*x[1] + 22*x[2] + 30*x[3] + 37.9*x[4])/(sum(x)),
            (1.9*x[1] + 32*x[3] + 11*x[4])/(sum(x)),
            (.05*x[0] + .9*x[1] + 40 * x[2] + 21*x[3] + 4 * x[4])/(sum(x)),
            (51.83*x[0] + 43*x[1] + 2*x[3] + 20*x[4])/(sum(x))]
    return out

nonlinear_constraint = NonlinearConstraint (cons_f, [14,2.14,.82,41.01], [16,4.14,2.82,43.01])

x0 = numpy.random.rand(5)

res = minimize (fx, x0, method = 'trust-constr', jac = "2-point", hess = SR1 (),
               constraints =[linear_constraint,nonlinear_constraint],
               options = {'verbose': 1}, bounds = bounds)

print("the result is : ",res.x)
print("the final price is : ",fx(res.x)/sum(res.x))
print("sum of all : ",sum(res.x))
print("the last : ",cons_f(res.x))


