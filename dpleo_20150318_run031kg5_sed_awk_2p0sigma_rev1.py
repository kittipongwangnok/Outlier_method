#PhD reseach 2020
#Kittipong Wangnok, D6010218
#School of Physics, Institute of Science, Suranaree University of Technology

#Import all module
import sys
import os
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
from statistics import stdev
from statistics import mean

#Latex font
import matplotlib as mpl
from matplotlib import rc
plt.rc('text', usetex=True)
plt.rc('font', family='serif',size=16)

'''
1. Input file: change 2 input files
'''

#Please change the input file
InputFile = open("dpleo_20150318_run031kg5_sed_awk.inp",'r').readlines()
N_InputFile = len(InputFile)

#Read data
BJD_time = []
BJD0 = []
P_orb1 = []
Cycle1 = []
Epoch1 = []
Phase1 = []
Relative_flux_12 = []
Relative_fluxe_12 = []
Relative_flux_32 = []
Relative_fluxe_32 = []
Relative_flux_42 = []
Relative_fluxe_42 = []
Relative_flux_52 = []
Relative_fluxe_52 = []
Relative_flux_34 = []
Relative_fluxe_34 = []
Relative_flux_53 = []
Relative_fluxe_53 = []
Relative_flux_54 = []
Relative_fluxe_54 = []
#Please change the input file
for line in open("dpleo_20150318_run031kg5_sed_awk.inp"):
    li=line.strip()
    if not li.startswith("#"):
        BJD_time.append(float(li.split(" ")[0]))
        BJD0.append(float(li.split(" ")[1]))
        P_orb1.append(float(li.split(" ")[2]))
        Cycle1.append(float(li.split(" ")[3]))
        Epoch1.append(float(li.split(" ")[4]))
        Phase1.append(float(li.split(" ")[5]))
        Relative_flux_12.append(float(li.split(" ")[6]))
        Relative_fluxe_12.append(float(li.split(" ")[7]))
        Relative_flux_32.append(float(li.split(" ")[8]))
        Relative_fluxe_32.append(float(li.split(" ")[9]))
        Relative_flux_42.append(float(li.split(" ")[10]))
        Relative_fluxe_42.append(float(li.split(" ")[11]))
        Relative_flux_52.append(float(li.split(" ")[12]))
        Relative_fluxe_52.append(float(li.split(" ")[13]))
        Relative_flux_34.append(float(li.split(" ")[14]))
        Relative_fluxe_34.append(float(li.split(" ")[15]))
        Relative_flux_53.append(float(li.split(" ")[16]))
        Relative_fluxe_53.append(float(li.split(" ")[17]))
        Relative_flux_54.append(float(li.split(" ")[18]))
        Relative_fluxe_54.append(float(li.split(" ")[19]))
########################################################
#Number of data point before reject
print ('Number of data point before data point rejection:', N_InputFile)
########################################################

'''
2. The calculation of average and standard deviation before data point rejection
2.1 Average relative flux of star3/star2
'''
#################################################################################
#Input data
x = Phase1
y_32 = Relative_flux_32
y_err_32 = Relative_fluxe_32

#Arrrays
x_a = [i for i in range(len(x))]
y_a_32 = [i for i in range(len(x))]
n_a_32 = [i for i in range(len(x))]
ne_a_32 = [i for i in range(len(x))]

#Set the range of phase to calculate flux average of ref2/ref3
ra_32 = Phase1[0]
rb_32 = Phase1[-1]

#Determine the phase maximum
for i in range(len(x)):
    print ('%0.0f\t%0.18f\t%0.18f\t%0.18f' %(i,x[i],y_32[i],y_err_32[i]))

#Input the initial and final numbers to calculate the flux average
max_inertial = int(input('Input the initial number to calculate the flux average: star3/star2 \t\t [Default: 0] \t:  ') or "0")
max_final = int(input('Input the final number to calculate the flux average: star3/star2 \t\t [Default: 1607] \t:  ') or "1607")

#Input for data average
a = max_inertial
b = max_final + 1

#The calculation of average and standard deviation before data point rejection
mean_32 = np.mean(y_32[a:b])
std_32 = np.std(y_32[a:b])

#################################################################################
'''
2.2 Average relative flux of star2/star4
'''
#################################################################################
#Input data
x = Phase1
y_42 = Relative_flux_42
y_err_42 = Relative_fluxe_42

#Arrrays
x_a = [i for i in range(len(x))]
y_a_42 = [i for i in range(len(x))]
n_a_42 = [i for i in range(len(x))]
ne_a_42 = [i for i in range(len(x))]

#Set the range of phase to calculate flux average of ref2/ref3
ra_42 = Phase1[0]
rb_42 = Phase1[-1]

#Determine the phase maximum
for i in range(len(x)):
    print ('%0.0f\t%0.18f\t%0.18f\t%0.18f' %(i,x[i],y_42[i], y_err_42[i]))

#Input the initial and final numbers to calculate the flux average
max_inertial = int(input('Input the initial number to calculate the flux average: star4/star2 \t\t [Default: 0] \t:  ') or "0")
max_final = int(input('Input the final number to calculate the flux average: star4/star2 \t\t [Default: 1607] \t:  ') or "1607")

#Input for data average
a = max_inertial
b = max_final + 1

#The calculation of average and standard deviation before data point rejection
mean_42 = np.mean(y_42[a:b])
std_42 = np.std(y_42[a:b])

#################################################################################
'''
2.3 Average relative flux of star5/star2
'''
#################################################################################
#Input data
x = Phase1
y_52 = Relative_flux_52
y_err_52 = Relative_fluxe_52

#Arrrays
x_a = [i for i in range(len(x))]
y_a_52 = [i for i in range(len(x))]
n_a_52 = [i for i in range(len(x))]
ne_a_52 = [i for i in range(len(x))]

#Set the range of phase to calculate flux average of ref2/ref3
ra_52 = Phase1[0]
rb_52 = Phase1[-1]

#Determine the phase maximum
for i in range(len(x)):
    print ('%0.0f\t%0.18f\t%0.18f\t%0.18f' %(i,x[i],y_52[i], y_err_52[i]))

#Input the initial and final numbers to calculate the flux average
max_inertial = int(input('Input the initial number to calculate the flux average: star5/star2 \t\t [Default: 0] \t:  ') or "0")
max_final = int(input('Input the final number to calculate the flux average: star5/star2 \t\t [Default: 1607] \t:  ') or "1607")

#Input for data average
a = max_inertial
b = max_final + 1

#The calculation of average and standard deviation before data point rejection
mean_52 = np.mean(y_52[a:b])
std_52 = np.std(y_52[a:b])

#################################################################################
'''
2.4 Average relative flux of star3/star4
'''
#################################################################################
#Input data
x = Phase1
y_34 = Relative_flux_34
y_err_34 = Relative_fluxe_34

#Arrrays
x_a = [i for i in range(len(x))]
y_a_34 = [i for i in range(len(x))]
n_a_34 = [i for i in range(len(x))]
ne_a_34 = [i for i in range(len(x))]

#Set the range of phase to calculate flux average of ref2/ref3
ra_34 = Phase1[0]
rb_34 = Phase1[-1]

#Determine the phase maximum
for i in range(len(x)):
    print ('%0.0f\t%0.18f\t%0.18f\t%0.18f' %(i,x[i],y_34[i], y_err_34[i]))

#Input the initial and final numbers to calculate the flux average
max_inertial = int(input('Input the initial number to calculate the flux average: star3/star4 \t\t [Default: 0] \t:  ') or "0")
max_final = int(input('Input the final number to calculate the flux average: star3/star4 \t\t [Default: 1607] \t:  ') or "1607")

#Input for data average
a = max_inertial
b = max_final + 1

#The calculation of average and standard deviation before data point rejection
mean_34 = np.mean(y_34[a:b])
std_34 = np.std(y_34[a:b])

#################################################################################
'''
2.5 Average relative flux of star5/star3
'''
#################################################################################
#Input data
x = Phase1
y_53 = Relative_flux_53
y_err_53 = Relative_fluxe_53

#Arrrays
x_a = [i for i in range(len(x))]
y_a_53 = [i for i in range(len(x))]
n_a_53 = [i for i in range(len(x))]
ne_a_53 = [i for i in range(len(x))]

#Set the range of phase to calculate flux average of ref2/ref3
ra_53 = Phase1[0]
rb_53 = Phase1[-1]

#Determine the phase maximum
for i in range(len(x)):
    print ('%0.0f\t%0.18f\t%0.18f\t%0.18f' %(i,x[i],y_53[i], y_err_53[i]))

#Input the initial and final numbers to calculate the flux average
max_inertial = int(input('Input the initial number to calculate the flux average: star5/star3 \t\t [Default: 0] \t:  ') or "0")
max_final = int(input('Input the final number to calculate the flux average: star5/star3 \t\t [Default: 1607] \t:  ') or "1607")

#Input for data average
a = max_inertial
b = max_final + 1

#The calculation of average and standard deviation before data point rejection
mean_53 = np.mean(y_53[a:b])
std_53 = np.std(y_53[a:b])

#################################################################################
'''
2.6 Average relative flux of star5/star4
'''
#################################################################################
#Input data
x = Phase1
y_54 = Relative_flux_54
y_err_54 = Relative_fluxe_54

#Arrrays
x_a = [i for i in range(len(x))]
y_a_54 = [i for i in range(len(x))]
n_a_54 = [i for i in range(len(x))]
ne_a_54 = [i for i in range(len(x))]

#Set the range of phase to calculate flux average of ref2/ref3
ra_54 = Phase1[0]
rb_54 = Phase1[-1]

#Determine the phase maximum
for i in range(len(x)):
    print ('%0.0f\t%0.18f\t%0.18f\t%0.18f' %(i,x[i],y_54[i], y_err_54[i]))

#Input the initial and final numbers to calculate the flux average
max_inertial = int(input('Input the initial number to calculate the flux average: star5/star4 \t\t [Default: 0] \t:  ') or "0")
max_final = int(input('Input the final number to calculate the flux average: star5/star4 \t\t [Default: 1607] \t:  ') or "1607")

#Input for data average
a = max_inertial
b = max_final + 1

#The calculation of average and standard deviation before data point rejection
mean_54 = np.mean(y_54[a:b])
std_54 = np.std(y_54[a:b])


#################################################################################
#   The Flux and the standard deviation of flux before using the outlier method  #
#################################################################################
print ('#################################################################################')
print ('#   The Flux and the standard deviation of flux before using the outlier method  #')
print ('#################################################################################')
print ('The flux average of star3/star2 \t\t\t: %0.18f' %(mean_32))
print ('The standard deviation of flux average of star3/star2 \t: %0.18f' %(std_32))

print ('The flux average of star4/star2 \t\t\t: %0.18f' %(mean_42))
print ('The standard deviation of flux average of star4/star2 \t: %0.18f' %(std_42))

print ('The flux average of star5/star2 \t\t\t: %0.18f' %(mean_52))
print ('The standard deviation of flux average of star5/star2 \t: %0.18f' %(std_52))

print ('The flux average of star3/star4 \t\t\t: %0.18f' %(mean_34))
print ('The standard deviation of flux average of star3/star4 \t: %0.18f' %(std_34))

print ('The flux average of star5/star3 \t\t\t: %0.18f' %(mean_53))
print ('The standard deviation of flux average of star5/star3 \t: %0.18f' %(std_53))

print ('The flux average of star5/star4 \t\t\t: %0.18f' %(mean_54))
print ('The standard deviation of flux average of star5/star4 \t: %0.18f' %(std_54))
#################################################################################
'''
3. Data rejection using the outlier method
'''
#################################################################################
#                      Outlier calculation of star3/star2                       #
#################################################################################
N = [i for i in range(len(x))]
flux_32 = [i for i in range(len(x))]
flux_err_32 = [i for i in range(len(x))]
flux_average_32 = [i for i in range(len(x))]
flux_average_std_32 = [i for i in range(len(x))]

#Determine the upper and lower bounds: flag data
#print ('No.   Orbital phase          Flux            Flux_err')
upper_result = []
lower_result = []
mean_result = []
upper = mean_32 + 2*std_32
lower =  mean_32 - 2*std_32
#print ('The upper bound value:', upper)
#print ('The lower bound value:', lower)
for i in range(len(x)):
    if y_32[i] < lower:
        N[i] = x[i]
        flux_32[i] = y_32[i]
        flux_err_32[i] = y_err_32[i]
#        print ('%0.0f\t%0.15f\t%0.15f\t%0.15f' %(i, N[i], flux_32[i], flux_err_32[i]))
        upper_result.append('%0.15f\t%0.15f\t%0.15f' %(N[i], flux_32[i], flux_err_32[i]))
    elif y_32[i] > upper:
        N[i] = x[i]
        flux_32[i] = y_32[i]
        flux_err_32[i] = y_err_32[i]
#        print ('%0.0f\t%0.15f\t%0.15f\t%0.15f' %(i, N[i], flux_32[i], flux_err_32[i]))
        lower_result.append('%0.15f\t%0.15f\t%0.15f' %(N[i], flux_32[i], flux_err_32[i]))
    else:
        N[i] = x[i]
        flux_32[i] = y_32[i]
        flux_err_32[i] = y_err_32[i]
#        print ('%0.0f\t%0.15f\t%0.15f\t%0.15f' %(i, N[i], flux_32[i], flux_err_32[i]))
        mean_result.append('%0.15f\t%0.15f\t%0.15f' %(N[i], flux_32[i], flux_err_32[i]))
        
#lResults = upper_result
data_rej = lower_result + upper_result
f = open('rej_data_32_2p0sigma.txt', 'w')
#for upper_result in upper_result:
for i in range(len(data_rej)):
    f.write(str(data_rej[i])+ '\n')
#    f.write("%0.15f\t%0.15f\t%0.15f\n" % (N_a[i], plot_a_32[i], plot_a_32_err[i]))
f.close()

data_mean = mean_result
f = open('mean_data_32_2p0sigma.txt', 'w')
#for upper_result in upper_result:
for i in range(len(data_mean)):
    f.write(str(data_mean[i])+ '\n')
#    f.write("%0.15f\t%0.15f\t%0.15f\n" %(N_a[i], plot_a_32[i], plot_a_32_err[i]))
f.close()

#################################################################################
#                      Outlier calculation of star4/star2                       #
#################################################################################
N = [i for i in range(len(x))]
flux_42 = [i for i in range(len(x))]
flux_err_42 = [i for i in range(len(x))]
flux_average_42 = [i for i in range(len(x))]
flux_average_std_42 = [i for i in range(len(x))]

#Determine the upper and lower bounds: flag data
#print ('No.   Orbital phase          Flux            Flux_err')
upper_result = []
lower_result = []
mean_result = []
upper = mean_42 + 2*std_42
lower =  mean_42 - 2*std_42
#print ('The upper bound value:', upper)
#print ('The lower bound value:', lower)
for i in range(len(x)):
    if y_42[i] < lower:
        N[i] = x[i]
        flux_42[i] = y_42[i]
        flux_err_42[i] = y_err_42[i]
#        print ('%0.0f\t%0.15f\t%0.15f\t%0.15f' %(i, N[i], flux_42[i], flux_err_42[i]))
        upper_result.append('%0.15f\t%0.15f\t%0.15f' %(N[i], flux_42[i], flux_err_42[i]))
    elif y_42[i] > upper:
        N[i] = x[i]
        flux_42[i] = y_42[i]
        flux_err_42[i] = y_err_42[i]
#        print ('%0.0f\t%0.15f\t%0.15f\t%0.15f' %(i, N[i], flux_42[i], flux_err_42[i]))
        lower_result.append('%0.15f\t%0.15f\t%0.15f' %(N[i], flux_42[i], flux_err_42[i]))
    else:
        N[i] = x[i]
        flux_42[i] = y_42[i]
        flux_err_42[i] = y_err_42[i]
#        print ('%0.0f\t%0.15f\t%0.15f\t%0.15f' %(i, N[i], flux_42[i], flux_err_42[i]))
        mean_result.append('%0.15f\t%0.15f\t%0.15f' %(N[i], flux_42[i], flux_err_42[i]))
        
#lResults = upper_result
data_rej = lower_result + upper_result
f = open('rej_data_42_2p0sigma.txt', 'w')
#for upper_result in upper_result:
for i in range(len(data_rej)):
    f.write(str(data_rej[i])+ '\n')
f.close()

data_mean = mean_result
f = open('mean_data_42_2p0sigma.txt', 'w')
#for upper_result in upper_result:
for i in range(len(data_mean)):
    f.write(str(data_mean[i])+ '\n')
f.close()

#################################################################################
#                      Outlier calculation of star5/star2                       #
#################################################################################
N = [i for i in range(len(x))]
flux_52 = [i for i in range(len(x))]
flux_err_52 = [i for i in range(len(x))]
flux_average_52 = [i for i in range(len(x))]
flux_average_std_52 = [i for i in range(len(x))]

#Determine the upper and lower bounds: flag data
#print ('No.   Orbital phase          Flux            Flux_err')
upper_result = []
lower_result = []
mean_result = []
upper = mean_52 + 2*std_52
lower =  mean_52 - 2*std_52
#print ('The upper bound value:', upper)
#print ('The lower bound value:', lower)
for i in range(len(x)):
    if y_52[i] < lower:
        N[i] = x[i]
        flux_52[i] = y_52[i]
        flux_err_52[i] = y_err_52[i]
#        print ('%0.0f\t%0.15f\t%0.15f\t%0.15f' %(i, N[i], flux_52[i], flux_err_52[i]))
        upper_result.append('%0.15f\t%0.15f\t%0.15f' %(N[i], flux_52[i], flux_err_52[i]))
    elif y_52[i] > upper:
        N[i] = x[i]
        flux_52[i] = y_52[i]
        flux_err_52[i] = y_err_52[i]
#        print ('%0.0f\t%0.15f\t%0.15f\t%0.15f' %(i, N[i], flux_52[i], flux_err_52[i]))
        lower_result.append('%0.15f\t%0.15f\t%0.15f' %(N[i], flux_52[i], flux_err_52[i]))
    else:
        N[i] = x[i]
        flux_52[i] = y_52[i]
        flux_err_52[i] = y_err_52[i]
#        print ('%0.0f\t%0.15f\t%0.15f\t%0.15f' %(i, N[i], flux_52[i], flux_err_52[i]))
        mean_result.append('%0.15f\t%0.15f\t%0.15f' %(N[i], flux_52[i], flux_err_52[i]))
        
#lResults = upper_result
data_rej = lower_result + upper_result
f = open('rej_data_52_2p0sigma.txt', 'w')
#for upper_result in upper_result:
for i in range(len(data_rej)):
    f.write(str(data_rej[i])+ '\n')
f.close()

data_mean = mean_result
f = open('mean_data_52_2p0sigma.txt', 'w')
#for upper_result in upper_result:
for i in range(len(data_mean)):
    f.write(str(data_mean[i])+ '\n')
f.close()

#################################################################################
#                      Outlier calculation of star3/star4                       #
#################################################################################
N = [i for i in range(len(x))]
flux_34 = [i for i in range(len(x))]
flux_err_34 = [i for i in range(len(x))]
flux_average_34 = [i for i in range(len(x))]
flux_average_std_34 = [i for i in range(len(x))]

#Determine the upper and lower bounds: flag data
#print ('No.   Orbital phase          Flux            Flux_err')
upper_result = []
lower_result = []
mean_result = []
upper = mean_34 + 2*std_34
lower =  mean_34 - 2*std_34
#print ('The upper bound value:', upper)
#print ('The lower bound value:', lower)
for i in range(len(x)):
    if y_34[i] < lower:
        N[i] = x[i]
        flux_34[i] = y_34[i]
        flux_err_34[i] = y_err_34[i]
#        print ('%0.0f\t%0.15f\t%0.15f\t%0.15f' %(i, N[i], flux_34[i], flux_err_34[i]))
        upper_result.append('%0.15f\t%0.15f\t%0.15f' %(N[i], flux_34[i], flux_err_34[i]))
    elif y_34[i] > upper:
        N[i] = x[i]
        flux_34[i] = y_34[i]
        flux_err_34[i] = y_err_34[i]
#        print ('%0.0f\t%0.15f\t%0.15f\t%0.15f' %(i, N[i], flux_34[i], flux_err_34[i]))
        lower_result.append('%0.15f\t%0.15f\t%0.15f' %(N[i], flux_34[i], flux_err_34[i]))
    else:
        N[i] = x[i]
        flux_34[i] = y_34[i]
        flux_err_34[i] = y_err_34[i]
#        print ('%0.0f\t%0.15f\t%0.15f\t%0.15f' %(i, N[i], flux_34[i], flux_err_34[i]))
        mean_result.append('%0.15f\t%0.15f\t%0.15f' %(N[i], flux_34[i], flux_err_34[i]))
        
#lResults = upper_result
data_rej = lower_result + upper_result
f = open('rej_data_34_2p0sigma.txt', 'w')
#for upper_result in upper_result:
for i in range(len(data_rej)):
    f.write(str(data_rej[i])+ '\n')
f.close()

data_mean = mean_result
f = open('mean_data_34_2p0sigma.txt', 'w')
#for upper_result in upper_result:
for i in range(len(data_mean)):
    f.write(str(data_mean[i])+ '\n')
f.close()

#################################################################################
#                      Outlier calculation of star5/star3                       #
#################################################################################
N = [i for i in range(len(x))]
flux_53 = [i for i in range(len(x))]
flux_err_53 = [i for i in range(len(x))]
flux_average_53 = [i for i in range(len(x))]
flux_average_std_53 = [i for i in range(len(x))]

#Determine the upper and lower bounds: flag data
#print ('No.   Orbital phase          Flux            Flux_err')
upper_result = []
lower_result = []
mean_result = []
upper = mean_53 + 2*std_53
lower =  mean_53 - 2*std_53
#print ('The upper bound value:', upper)
#print ('The lower bound value:', lower)
for i in range(len(x)):
    if y_53[i] < lower:
        N[i] = x[i]
        flux_53[i] = y_53[i]
        flux_err_53[i] = y_err_53[i]
#        print ('%0.0f\t%0.15f\t%0.15f\t%0.15f' %(i, N[i], flux_53[i], flux_err_53[i]))
        upper_result.append('%0.15f\t%0.15f\t%0.15f' %(N[i], flux_53[i], flux_err_53[i]))
    elif y_53[i] > upper:
        N[i] = x[i]
        flux_53[i] = y_53[i]
        flux_err_53[i] = y_err_53[i]
#        print ('%0.0f\t%0.15f\t%0.15f\t%0.15f' %(i, N[i], flux_53[i], flux_err_53[i]))
        lower_result.append('%0.15f\t%0.15f\t%0.15f' %(N[i], flux_53[i], flux_err_53[i]))
    else:
        N[i] = x[i]
        flux_53[i] = y_53[i]
        flux_err_53[i] = y_err_53[i]
#        print ('%0.0f\t%0.15f\t%0.15f\t%0.15f' %(i, N[i], flux_53[i], flux_err_53[i]))
        mean_result.append('%0.15f\t%0.15f\t%0.15f' %(N[i], flux_53[i], flux_err_53[i]))
        
#lResults = upper_result
data_rej = lower_result + upper_result
f = open('rej_data_53_2p0sigma.txt', 'w')
#for upper_result in upper_result:
for i in range(len(data_rej)):
    f.write(str(data_rej[i])+ '\n')
f.close()

data_mean = mean_result
f = open('mean_data_53_2p0sigma.txt', 'w')
#for upper_result in upper_result:
for i in range(len(data_mean)):
    f.write(str(data_mean[i])+ '\n')
f.close()

#################################################################################
#                      Outlier calculation of star5/star4                       #
#################################################################################
N = [i for i in range(len(x))]
flux_54 = [i for i in range(len(x))]
flux_err_54 = [i for i in range(len(x))]
flux_average_54 = [i for i in range(len(x))]
flux_average_std_54 = [i for i in range(len(x))]

#Determine the upper and lower bounds: flag data
#print ('No.   Orbital phase          Flux            Flux_err')
upper_result = []
lower_result = []
mean_result = []
upper = mean_54 + 2*std_54
lower =  mean_54 - 2*std_54
#print ('The upper bound value:', upper)
#print ('The lower bound value:', lower)
for i in range(len(x)):
    if y_54[i] < lower:
        N[i] = x[i]
        flux_54[i] = y_54[i]
        flux_err_54[i] = y_err_54[i]
#        print ('%0.0f\t%0.15f\t%0.15f\t%0.15f' %(i, N[i], flux_54[i], flux_err_54[i]))
        upper_result.append('%0.15f\t%0.15f\t%0.15f' %(N[i], flux_54[i], flux_err_54[i]))
    elif y_54[i] > upper:
        N[i] = x[i]
        flux_54[i] = y_54[i]
        flux_err_54[i] = y_err_54[i]
#        print ('%0.0f\t%0.15f\t%0.15f\t%0.15f' %(i, N[i], flux_54[i], flux_err_54[i]))
        lower_result.append('%0.15f\t%0.15f\t%0.15f' %(N[i], flux_54[i], flux_err_54[i]))
    else:
        N[i] = x[i]
        flux_54[i] = y_54[i]
        flux_err_54[i] = y_err_54[i]
#        print ('%0.0f\t%0.15f\t%0.15f\t%0.15f' %(i, N[i], flux_54[i], flux_err_54[i]))
        mean_result.append('%0.15f\t%0.15f\t%0.15f' %(N[i], flux_54[i], flux_err_54[i]))
        
#lResults = upper_result
data_rej = lower_result + upper_result
f = open('rej_data_54_2p0sigma.txt', 'w')
#for upper_result in upper_result:
for i in range(len(data_rej)):
    f.write(str(data_rej[i])+ '\n')
f.close()

data_mean = mean_result
f = open('mean_data_54_2p0sigma.txt', 'w')
#for upper_result in upper_result:
for i in range(len(data_mean)):
    f.write(str(data_mean[i])+ '\n')
f.close()

#save file
#np.savetxt('data_mean_45_2p0sigma_demo.txt', np.array([mean_result]).T, fmt="%.10f")

'''
4. Plot graph to obtain the result
'''
########################################################
InputFile_1 = "mean_data_32_2p0sigma.txt"
Data_1   = np.genfromtxt(InputFile_1)

InputFile_2 = "rej_data_32_2p0sigma.txt"
Data_2   = np.genfromtxt(InputFile_2)

InputFile_3 = "mean_data_42_2p0sigma.txt"
Data_3   = np.genfromtxt(InputFile_3)

InputFile_4 = "rej_data_42_2p0sigma.txt"
Data_4   = np.genfromtxt(InputFile_4)

InputFile_5 = "mean_data_52_2p0sigma.txt"
Data_5   = np.genfromtxt(InputFile_5)

InputFile_6 = "rej_data_52_2p0sigma.txt"
Data_6   = np.genfromtxt(InputFile_6)

InputFile_7 = "mean_data_34_2p0sigma.txt"
Data_7   = np.genfromtxt(InputFile_7)

InputFile_8 = "rej_data_34_2p0sigma.txt"
Data_8   = np.genfromtxt(InputFile_8)

InputFile_9 = "mean_data_53_2p0sigma.txt"
Data_9   = np.genfromtxt(InputFile_9)

InputFile_10 = "rej_data_53_2p0sigma.txt"
Data_10   = np.genfromtxt(InputFile_10)

InputFile_11 = "mean_data_54_2p0sigma.txt"
Data_11   = np.genfromtxt(InputFile_11)

InputFile_12 = "rej_data_54_2p0sigma.txt"
Data_12   = np.genfromtxt(InputFile_12)
########################################################
#Read data
Phase_1 = Data_1[:,0]
Flux_1 = Data_1[:,1]
Flux_err_1 = Data_1[:,2]

Phase_2 = Data_2[:,0]
Flux_2 = Data_2[:,1]
Flux_err_2 = Data_2[:,2]

Phase_3 = Data_3[:,0]
Flux_3 = Data_3[:,1]
Flux_err_3 = Data_3[:,2]

Phase_4 = Data_4[:,0]
Flux_4 = Data_4[:,1]
Flux_err_4 = Data_4[:,2]

Phase_5 = Data_5[:,0]
Flux_5 = Data_5[:,1]
Flux_err_5 = Data_5[:,2]

Phase_6 = Data_6[:,0]
Flux_6 = Data_6[:,1]
Flux_err_6 = Data_6[:,2]

Phase_7 = Data_7[:,0]
Flux_7 = Data_7[:,1]
Flux_err_7 = Data_7[:,2]

Phase_8 = Data_8[:,0]
Flux_8 = Data_8[:,1]
Flux_err_8 = Data_8[:,2]

Phase_9 = Data_9[:,0]
Flux_9 = Data_9[:,1]
Flux_err_9 = Data_9[:,2]

Phase_10 = Data_10[:,0]
Flux_10 = Data_10[:,1]
Flux_err_10 = Data_10[:,2]

Phase_11 = Data_11[:,0]
Flux_11 = Data_11[:,1]
Flux_err_11 = Data_11[:,2]

Phase_12 = Data_12[:,0]
Flux_12 = Data_12[:,1]
Flux_err_12 = Data_12[:,2]

#The calculation of average and standard deviation after using the outlier method
flux_average_32 = np.mean(Flux_1)
flux_average_std_32 = stdev(Flux_1)

flux_average_42 = np.mean(Flux_3)
flux_average_std_42 = stdev(Flux_3)

flux_average_52 = np.mean(Flux_5)
flux_average_std_52 = stdev(Flux_5)

flux_average_34 = np.mean(Flux_7)
flux_average_std_34 = stdev(Flux_7)

flux_average_53 = np.mean(Flux_9)
flux_average_std_53 = stdev(Flux_9)

flux_average_54 = np.mean(Flux_11)
flux_average_std_54 = stdev(Flux_11)

#################################################################################
#   The Flux and the standard deviation of flux after using the outlier method  #
#################################################################################
print ('#################################################################################')
print ('#   The Flux and the standard deviation of flux after using the outlier method  #')
print ('#################################################################################')
print ('The flux average of star3/star2 \t\t\t: %0.18f' %(flux_average_32))
print ('The standard deviation of flux average of star3/star2 \t: %0.18f' %(flux_average_std_32))

print ('The flux average of star4/star2 \t\t\t: %0.18f' %(flux_average_42))
print ('The standard deviation of flux average of star4/star2 \t: %0.18f' %(flux_average_std_42))

print ('The flux average of star5/star2 \t\t\t: %0.18f' %(flux_average_52))
print ('The standard deviation of flux average of star5/star2 \t: %0.18f' %(flux_average_std_52))

print ('The flux average of star3/star4 \t\t\t: %0.18f' %(flux_average_34))
print ('The standard deviation of flux average of star3/star4 \t: %0.18f' %(flux_average_std_34))

print ('The flux average of star5/star3 \t\t\t: %0.18f' %(flux_average_53))
print ('The standard deviation of flux average of star5/star3 \t: %0.18f' %(flux_average_std_53))

print ('The flux average of star5/star4 \t\t\t: %0.18f' %(flux_average_54))
print ('The standard deviation of flux average of star5/star4 \t: %0.18f' %(flux_average_std_54))

'''
Save the sumary of the relative flux
5.1 The relative flux calcuation before we do the data point rejection.
'''
############################################################
np.savetxt("dpleo_20150318_run031kg5_sed_awk_2p0sigma.pre",
np.c_[mean_32, std_32,
    mean_42, std_42,
    mean_52, std_52,
    mean_34, std_34,
    mean_53, std_53,
    mean_54, std_54])
############################################################

'''
Save the sumary of the relative flux
5.2 The relative flux calcuation before we do the data point rejection.
'''
############################################################
np.savetxt("dpleo_20150318_run031kg5_sed_awk_2p0sigma.pos",
np.c_[flux_average_32, flux_average_std_32,
    flux_average_42, flux_average_std_42,
    flux_average_52, flux_average_std_52,
    flux_average_34, flux_average_std_34,
    flux_average_53, flux_average_std_53,
    flux_average_54, flux_average_std_54])
############################################################

##Plotgraph: Relative flux of Star1/Star2
fig, (ax0, ax1, ax2, ax3, ax4, ax5) = plt.subplots(nrows=6, sharex=True, sharey=False, figsize=(10, 12), tight_layout=True)
plt.xlim(Phase1[a], Phase1[b-1])
plt.xlabel('Orbital phase')

ax0.tick_params(direction='in', which='both', bottom='on',top='on', right = 'on')
ax1.tick_params(direction='in', which='both', bottom='on',top='on', right = 'on')
ax2.tick_params(direction='in', which='both', bottom='on',top='on', right = 'on')
ax3.tick_params(direction='in', which='both', bottom='on',top='on', right = 'on')
ax4.tick_params(direction='in', which='both', bottom='on',top='on', right = 'on')
ax5.tick_params(direction='in', which='both', bottom='on',top='on', right = 'on')

ax0.errorbar(Phase_1, Flux_1, yerr=Flux_err_1, fmt='o', color='red', alpha = 0.5, markersize='3.00', label = 'data\_star32')
ax0.errorbar(Phase_2, Flux_2, yerr=Flux_err_2, fmt='o', color='blue', alpha = 0.5, markersize='3.00', label = 'data\_rej\_star32')
ax0.hlines(y=mean_32, xmin=x[0], xmax=x[-1], colors='black', linestyles='--', lw=1)
ax0.legend(loc="upper right")
ax0.set_ylabel('Relative flux')
#ax0.set_ylim(0.32, 0.38)

ax1.errorbar(Phase_3, Flux_3, yerr=Flux_err_3, fmt='o', color='red', alpha = 0.5, markersize='3.00', label = 'data\_star42')
ax1.errorbar(Phase_4, Flux_4, yerr=Flux_err_4, fmt='o', color='blue', alpha = 0.5, markersize='3.00', label = 'data\_rej\_star42')
ax1.hlines(y=mean_42, xmin=x[0], xmax=x[-1], colors='black', linestyles='--', lw=1)
ax1.legend(loc="upper right")
ax1.set_ylabel('Relative flux')

ax2.errorbar(Phase_5, Flux_5, yerr=Flux_err_5, fmt='o', color='red', alpha = 0.5, markersize='3.00', label = 'data\_star52')
ax2.errorbar(Phase_6, Flux_6, yerr=Flux_err_6, fmt='o', color='blue', alpha = 0.5, markersize='3.00', label = 'data\_rej\_star52')
ax2.hlines(y=mean_52, xmin=x[0], xmax=x[-1], colors='black', linestyles='--', lw=1)
ax2.legend(loc="upper right")
ax2.set_ylabel('Relative flux')

ax3.errorbar(Phase_7, Flux_7, yerr=Flux_err_7, fmt='o', color='red', alpha = 0.5, markersize='3.00', label = 'data\_star34')
ax3.errorbar(Phase_8, Flux_8, yerr=Flux_err_8, fmt='o', color='blue', alpha = 0.5, markersize='3.00', label = 'data\_rej\_star34')
ax3.hlines(y=mean_34, xmin=x[0], xmax=x[-1], colors='black', linestyles='--', lw=1)
ax3.legend(loc="upper right")
ax3.set_ylabel('Relative flux')

ax4.errorbar(Phase_9, Flux_9, yerr=Flux_err_9, fmt='o', color='red', alpha = 0.5, markersize='3.00', label = 'data\_star53')
ax4.errorbar(Phase_10, Flux_10, yerr=Flux_err_10, fmt='o', color='blue', alpha = 0.5, markersize='3.00', label = 'data\_rej\_star53')
ax4.hlines(y=mean_53, xmin=x[0], xmax=x[-1], colors='black', linestyles='--', lw=1)
ax4.legend(loc="upper right")
ax4.set_ylabel('Relative flux')

ax5.errorbar(Phase_11, Flux_11, yerr=Flux_err_11, fmt='o', color='red', alpha = 0.5, markersize='3.00', label = 'data\_star54')
ax5.errorbar(Phase_12, Flux_12, yerr=Flux_err_12, fmt='o', color='blue', alpha = 0.5, markersize='3.00', label = 'data\_rej\_star54')
ax5.hlines(y=mean_54, xmin=x[0], xmax=x[-1], colors='black', linestyles='--', lw=1)
ax5.legend(loc="upper right")
ax5.set_ylabel('Relative flux')


fig.align_ylabels()
output_filename = os.path.splitext(__file__)[0] + '.png'
plt.savefig(output_filename, dpi=500)
plt.show()

sys.exit

print ('#################################################################################')
print ('#                               Mission completed                               #')
print ('#################################################################################')
