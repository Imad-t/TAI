from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_interactivity = "all"
import numpy as np
import math

def meth_newton(f, fprime, x0, epsilon, nmaxit):
    niter=0
    info_conv=0
    x=x0
    while abs(f(x))>=epsilon and niter < nmaxit:
        niter+=1
        x = x-f(x)/fprime(x)
        if abs(f(x))<epsilon:
            info_conv=1
            #print('conv')
            break
    return x, niter, info_conv
   
f= lambda x: math.exp(-x/4)*(2-x)-1
fprime= lambda x: math.exp(-x/4)*(-3/2+x/4)
meth_newton(f,fprime, 3, 1.e-6, 10)