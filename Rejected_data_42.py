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
1. Input file
'''
#################################################################################
#Read data
mean_data_42_1p0sigma = open("mean_data_42_1p0sigma.txt",'r').readlines()
N_mean_data_42_1p0sigma = len(mean_data_42_1p0sigma)
rej_data_42_1p0sigma = open("rej_data_42_1p0sigma.txt",'r').readlines()
N_rej_data_42_1p0sigma = len(rej_data_42_1p0sigma)

mean_data_42_1p5sigma = open("mean_data_42_1p5sigma.txt",'r').readlines()
N_mean_data_42_1p5sigma = len(mean_data_42_1p5sigma)
rej_data_42_1p5sigma = open("rej_data_42_1p5sigma.txt",'r').readlines()
N_rej_data_42_1p5sigma = len(rej_data_42_1p5sigma)

mean_data_42_2p0sigma = open("mean_data_42_2p0sigma.txt",'r').readlines()
N_mean_data_42_2p0sigma = len(mean_data_42_2p0sigma)
rej_data_42_2p0sigma = open("rej_data_42_2p0sigma.txt",'r').readlines()
N_rej_data_42_2p0sigma = len(rej_data_42_2p0sigma)

mean_data_42_2p5sigma = open("mean_data_42_2p5sigma.txt",'r').readlines()
N_mean_data_42_2p5sigma = len(mean_data_42_2p5sigma)
rej_data_42_2p5sigma = open("rej_data_42_2p5sigma.txt",'r').readlines()
N_rej_data_42_2p5sigma = len(rej_data_42_2p5sigma)


'''
2. save file
'''
#################################################################################
np.savetxt("Rejected_data_42.out",
np.array([N_mean_data_42_1p0sigma, N_rej_data_42_1p0sigma,
          N_mean_data_42_1p5sigma, N_rej_data_42_1p5sigma,
          N_mean_data_42_2p0sigma, N_rej_data_42_2p0sigma,
          N_mean_data_42_2p5sigma, N_rej_data_42_2p5sigma]).T, fmt="%0.0f")

print ('---------------------------------------------------------------------------')
print ('The 1\u03C3 data rejection')
print ('---------------------------------------------------------------------------')
print ('The number of data point for calculating:', N_mean_data_42_1p0sigma)
print ('The number of data point for rejecting:', N_rej_data_42_1p0sigma)
print ('---------------------------------------------------------------------------')
print ('The 1.5\u03C3 data rejection')
print ('---------------------------------------------------------------------------')
print ('The number of data point for calculating:', N_mean_data_42_1p5sigma)
print ('The number of data point for rejecting:', N_rej_data_42_1p5sigma)
print ('---------------------------------------------------------------------------')
print ('The 2.0\u03C3 data rejection')
print ('---------------------------------------------------------------------------')
print ('The number of data point for calculating:', N_mean_data_42_2p0sigma)
print ('The number of data point for rejecting:', N_rej_data_42_2p0sigma)
print ('---------------------------------------------------------------------------')
print ('The 2.5\u03C3 data rejection')
print ('---------------------------------------------------------------------------')
print ('The number of data point for calculating:', N_mean_data_42_2p5sigma)
print ('The number of data point for rejecting:', N_rej_data_42_2p5sigma)
print ('---------------------------------------------------------------------------')


#Number of sigma: x-axis
sigma_I = 1.0
sigma_II = 1.5
sigma_IV = 2.0
sigma_VI = 2.5

#Set of sata: y-axis
y_mean_1p0sigma = N_mean_data_42_1p0sigma
y_rej_1p0sigma = N_rej_data_42_1p0sigma

y_mean_1p5sigma = N_mean_data_42_1p5sigma
y_rej_1p5sigma = N_rej_data_42_1p5sigma

y_mean_2p0sigma = N_mean_data_42_2p0sigma
y_rej_2p0sigma = N_rej_data_42_2p0sigma

y_mean_2p5sigma = N_mean_data_42_2p5sigma
y_rej_2p5sigma = N_rej_data_42_2p5sigma


#plot data
fig = plt.figure(figsize=(8, 5))
plt.scatter(sigma_I, y_mean_1p0sigma, color='red', alpha=1.0, label = 'Calculated data')
plt.scatter(sigma_I, y_rej_1p0sigma, color='blue', alpha=1.0, label = 'Rejected data')

plt.scatter(sigma_II, y_mean_1p5sigma, color='red', alpha=1.0)
plt.scatter(sigma_II, y_rej_1p5sigma, color='blue', alpha=1.0)

plt.scatter(sigma_IV, y_mean_2p0sigma, color='red', alpha=1.0)
plt.scatter(sigma_IV, y_rej_2p0sigma, color='blue', alpha=1.0)

plt.scatter(sigma_VI, y_mean_2p5sigma, color='red', alpha=1.0)
plt.scatter(sigma_VI, y_rej_2p5sigma, color='blue', alpha=1.0)

plt.xlabel('$\sigma$')
plt.ylabel('Number of data')
plt.legend(loc='best')
plt.title( 'Number of data rejection for star4/2')
plt.grid(linestyle='dotted')
fig.align_ylabels()
output_filename = os.path.splitext(__file__)[0] + '.png'
plt.savefig(output_filename, dpi=1000)
plt.show()

sys.exit

print ('---------------------------------------------------------------------------')
print ('-                         Mission completed                               -')
print ('---------------------------------------------------------------------------')
print ('---------------------------------------------------------------------------')
