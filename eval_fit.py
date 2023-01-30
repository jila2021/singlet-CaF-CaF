import numpy as np
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, DotProduct, Matern, WhiteKernel, ConstantKernel as C
from symfuncs import *
from sklearn.model_selection import train_test_split
from numpy import asarray
from numpy import savetxt
import pickle

cm1=1.0/2.19474631e5 #unit

GP=pickle.load(open('gpr.pkl','rb'))#load GP object

#load coordinates
test_array=np.loadtxt('example_input.txt')
r12t = test_array[:,0]  
r13t = test_array[:,1]
r23t = test_array[:,2]
r14t = test_array[:,3]
r24t = test_array[:,4]
r34t = test_array[:,5]

x_test_sp = np.asarray([r12t,r13t,r23t,r14t,r24t,r34t]).T  
x_test=1/x_test_sp 

gpsym=symGP(GP)
y_pred = gpsym(1/x_test_sp)
#Save energies to file in cm^-1
np.savetxt('example_output.txt',y_pred/cm1)
