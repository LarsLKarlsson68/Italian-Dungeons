import numpy
import pylab

import math
import random


import scipy.optimize

# Exponential function (similar to CO2 curve)
def f1(x):
    return 4.7*(1.02**x-1)

# Integration
def integrate(data):
    integral = data[:1]
    for i in range(1,len(data)):
        integral.append(integral[-1]+data[i])
    return integral


# Computation of R2 between a list of obs data, and a list of predicted data.
def calc_r2(obs, pred):
    obsmean = sum(obs)/len(obs)
    ss_tot = sum([ (obs[i]-obsmean)**2 for i in range(len(obs)) ])
    ss_res = sum([ (obs[i]-pred[i])**2 for i in range(len(obs)) ])
    return 1-ss_res/ss_tot

# Add AR(3) noise to list of data    
def add_noise(data,var):
    noise = [ random.random()*2*var-var for i in range(3) ]
    for i in range(len(data)):
        noise.append((0.1*noise[-3]+0.2*noise[-2]+0.3*noise[-1]+0.4*(random.random()*2*var-var)))
    return [ data[i]+noise[i+3] for i in range(len(data)) ]


# Numerically fit data2 to data1, return fitten version of data 2
def curve_fit(data1, data2):
    xdata = numpy.array(range(len(data1)))
    ydata = numpy.array(data1)
    zdata = numpy.array(data2)

    f = (lambda x, a, b: zdata*a+b )
    x0 = numpy.array([0.0, 0.0])
    sigma = numpy.array([1.0 for i in range(len(data1))])

    (a,b),covar = scipy.optimize.curve_fit(f,xdata,ydata,x0,sigma)

    data2_fitted = [ data2[i]*a + b  for i in range(len(data2)) ]

    return data2_fitted, calc_r2(data1, data2_fitted)
  

# Numerically fit data2 (which has been integrated) to data1, return fitted version of integrated data2
# Important: offset is handled differently. Instead of a constant it becomes a linear function
def curve_fit_int(data1, data2):
    xdata = numpy.array(range(len(data1)))
    ydata = numpy.array(data1)
    zdata = numpy.array(data2)

    f = (lambda x, a, b: zdata*a+b*x )
    x0 = numpy.array([0.0, 0.0])
    sigma = numpy.array([1.0 for i in range(len(data1))])

    (a,b),covar = scipy.optimize.curve_fit(f,xdata,ydata,x0,sigma)

    data2_fitted = [ data2[i]*a + b*i  for i in range(len(data2)) ]

    return data2_fitted, calc_r2(data1, data2_fitted)
             



# Experiment!

# Repeat 10 times
for var in range(10):
    # Generate syntethic CO2 data as exponential function plus small noise
    co2 = add_noise([ f1(i) for i in range(150) ],5)
    # Generate syntethic temp data as CO2 plus large noise (we can imagine unit is 100th of degree C).
    temp = add_noise(co2,40)
    # Fit temp to CO2, and compute R2
    temp_fit, r2_orig = curve_fit(co2,temp)
    # Integrate temp
    temp_int = integrate(temp)
    # Fit integrated temp to CO2, and compute R2
    temp_int_fit, r2_int = curve_fit_int(co2,temp_int)
    # Print comparison
    print("Iteration:", var, "R2 for unintegrated temp =", r2_orig, calc_r2(co2,temp), "R2 for integrated temp =", r2_int)
    pylab.plot(numpy.array(range(150)),numpy.array(co2)) 
#for i in range(150):
#	print("{}\t{}\t{}\t{}".format(i,co2[i],temp_fit[i],temp_int_fit[i]))       
