import numpy
from scipy.optimize import minimize
from scipy.optimize import Bounds
from scipy.optimize import LinearConstraint
from scipy.optimize import NonlinearConstraint
from scipy.optimize import SR1

stop = "y"
while stop == "y":

    answer = input("Do you want to use default variables ? (y/n): ")

    if answer == 'n':
        # the cost function
        num = int(input("enter the number of variables : "))
        print(f"you have {num} Variables")

        prices = []
        for i in range(num):
            prices.append(int(input(f"enter the price of {i+1}th Variables : ")))
        print(f"your prices are : {prices}")


        def fx(x):
            out = 0
            for i,price in enumerate(prices):
                out += x[i] * price
            return out

        # bounds of variables : 0<x<1
        bounds = Bounds(numpy.zeros(num), numpy.zeros(num) + numpy.inf)

        # linear constraint = 22000 < x1 + x2 + x3 + x4 + x5 < 23000
        min_of_capicity = int(input("Enter the minimum of product : "))
        max_of_capicity = int(input("Enter the maximum of product : "))
        print(f"the total product has : ({min_of_capicity} < x < {max_of_capicity})")
        linear_constraint = LinearConstraint(numpy.ones(num), min_of_capicity, max_of_capicity)

        Sio2 = []
        for i in range(num):
            Sio2.append(float(input(f"Enter the {i+1}th coefficient of Sio2 : ")))
        print(f"your Sio2 coefficients are : {Sio2}")

        Al2O3 = []
        for i in range(num):
            Al2O3.append(float(input(f"Enter the {i+1}th coefficient of Al2O3 : ")))
        print(f"your Al2O3 coefficients are : {Al2O3}")

        Fe2O3 = []
        for i in range(num):
            Fe2O3.append(float(input(f"Enter the {i+1}th coefficient of Fe2O3 : ")))
        print(f"your Fe2O3 coefficients are : {Fe2O3}")

        CaO = []
        for i in range(num):
            CaO.append(float(input(f"Enter the {i+1}th coefficient of CaO : ")))
        print(f"your CaO coefficients are : {CaO}")

        def cons_f(x):
            out = []
            temp = 0
            for j in range(num):
                temp += Sio2[j] * x[j]
            out.append(temp/sum(x))

            temp = 0
            for j in range(num):
                temp += Al2O3[j] * x[j]
            out.append(temp / sum(x))

            temp = 0
            for j in range(num):
                temp += Fe2O3[j] * x[j]
            out.append(temp / sum(x))

            temp = 0
            for j in range(num):
                temp += CaO[j] * x[j]
            out.append(temp / sum(x))

            return out

        lbound = []
        ubound = []
        for i in range(4):
            lbound.append(float(input(f"enter the lower bound for {i + 1}th constraint : ")))
            ubound.append(float(input(f"enter the upper bound for {i + 1}th constraint : ")))
        print(f"your lower bounds are : {lbound}\n yout upper bounds are : {ubound}")


        nonlinear_constraint = NonlinearConstraint(cons_f, lbound, ubound)

        x0 = numpy.random.rand(num)

        res = minimize(fx, x0, method='trust-constr', jac="2-point", hess=SR1(),
                       constraints=[linear_constraint, nonlinear_constraint],
                       options={'verbose': 1}, bounds=bounds)

        print("the result is : ", res.x)
        print("the final price is : ", fx(res.x) / sum(res.x))
        print("sum of all : ", sum(res.x))
        print("the last : ", cons_f(res.x))

    elif answer == "y":
        # the cost function
        def fx(x):
            out = x[0] * 7890 + x[1] * 2100 + x[2] * 65000 + x[3] * 78000 + x[4] * 3100
            return out


        # bounds of variables : 0<x<1
        bounds = Bounds(numpy.zeros(5), numpy.zeros(5) + numpy.inf)

        # linear constraint = 22000 < x1 + x2 + x3 + x4 + x5 < 23000
        linear_constraint = LinearConstraint([1, 1, 1, 1, 1], 22500, 23000)


        def cons_f(x):
            out = [(5.7 * x[0] + 16 * x[1] + 22 * x[2] + 30 * x[3] + 37.9 * x[4]) / (sum(x)),
                   (1.9 * x[1] + 32 * x[3] + 11 * x[4]) / (sum(x)),
                   (.05 * x[0] + .9 * x[1] + 40 * x[2] + 21 * x[3] + 4 * x[4]) / (sum(x)),
                   (51.83 * x[0] + 43 * x[1] + 2 * x[3] + 20 * x[4]) / (sum(x))]
            return out


        nonlinear_constraint = NonlinearConstraint(cons_f, [14, 2.14, .82, 41.01], [16, 4.14, 2.82, 43.01])

        x0 = numpy.random.rand(5)

        res = minimize(fx, x0, method='trust-constr', jac="2-point", hess=SR1(),
                       constraints=[linear_constraint, nonlinear_constraint],
                       options={'verbose': 1}, bounds=bounds)

        print("the result is : ", res.x)
        print("the final price is : ", fx(res.x) / sum(res.x),"per ton")
        print("sum of all : ", sum(res.x))
        print("the analysers : ", cons_f(res.x))

    else:
        print("wrong answer\nnow start over")

    stop = input("Do you want to start over ? (y/n): ")



