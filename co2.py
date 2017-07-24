import math
import random

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
    sqrt2 = math.sqrt(2)
    delta_scale = data1[-1]/data2[-1]
    delta_scale1 = max([ abs(data1[i]/data2[i]) for i in range(100,len(data1))])
    delta_scale2 = min([ abs(data1[i]/data2[i]) for i in range(100,len(data1))])
    if 1/delta_scale2 > delta_scale1:
        delta_scale = delta_scale2
    else:
        delta_scale = delta_scale1
    delta_offset = max([abs(data1[i]-data2[i]) for i in range(len(data1))])
    scale = delta_scale
    offset = delta_offset
    best_r2 = -99999
    for i in range(200):
        if i == -1:
            print(i, "R2", best_r2, "s", scale, "ds", delta_scale, "o", offset, "do", delta_offset)
        best_ds = 0
        best_do = 0
        for ds in [-delta_scale,0,delta_scale]:
            for do in [-delta_offset,0,delta_offset]:
                data2_fitted = [ data2[i]*(scale+ds) + (offset+do)  for i in range(len(data2)) ]
                this_r2 = calc_r2(data1, data2_fitted)
                if this_r2 > best_r2:
                    best_ds = ds
                    best_do = do
        scale += best_ds
        offset += best_do
        if best_ds == 0 and best_do == 0 and i > 0:
            delta_scale = delta_scale/sqrt2
            delta_offset = delta_offset/sqrt2
        data2_fitted = [ data2[i]*scale + offset  for i in range(len(data2)) ]
        best_r2 = calc_r2(data1, data2_fitted)
    return data2_fitted, best_r2

# Numerically fit data2 (which has been integrated) to data1, return fitted version of integrated data2
# Important: offset is handled differently. Instead of a constant it becomes a linear function
def curve_fit_int(data1, data2):
    sqrt2 = math.sqrt(2)
    delta_scale = max([abs(data1[i]/data2[i]) for i in range(len(data1))])
    delta_offset = max([abs(data1[i]-data2[i])/(i+1) for i in range(len(data1))])
    scale = delta_scale
    offset = delta_offset
    best_r2 = -99999
    for i in range(100):
        if i == -1:
            print(i, "R2", best_r2, "s", scale, "ds", delta_scale, "o", offset, "do", delta_offset)
        best_ds = 0
        best_do = 0
        for ds in [-delta_scale,0,delta_scale]:
            for do in [-delta_offset,0,delta_offset]:
                data2_fitted = [ data2[i]*(scale+ds) + i*(offset+do)  for i in range(len(data2)) ]
                this_r2 = calc_r2(data1, data2_fitted)
                if this_r2 > best_r2:
                    best_ds = ds
                    best_do = do
        scale += best_ds
        offset += best_do
        if best_ds == 0 and best_do == 0 and i > 0:
            delta_scale = delta_scale/sqrt2
            delta_offset = delta_offset/sqrt2
        data2_fitted = [ data2[i]*scale + i*offset  for i in range(len(data2)) ]
        best_r2 = calc_r2(data1, data2_fitted)
    return data2_fitted, best_r2
            



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

for i in range(150):
	print("{}\t{}\t{}\t{}".format(i,co2[i],temp_fit[i],temp_int_fit[i]))       
