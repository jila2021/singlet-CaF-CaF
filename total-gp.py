import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, DotProduct, Matern, WhiteKernel, ConstantKernel as C
from symfuncs import *
#from coordtransform import *
from sklearn.model_selection import train_test_split
from numpy import asarray
from numpy import savetxt
import pandas as pd
import csv
import pickle

cm1=1.0/2.19474631e5 #unit
# read dataset
data_array=np.loadtxt('train_set1.txt')
#MRCI+Q asymptote in Hartree
easymp=-273.09286

Emrciq = data_array[:,6]
eVm=Emrciq-easymp
inddel=np.where(eVm>0.00455)[0]

#inddel=np.where(Emrciq>np.amin(Emrciq)+0.2)[0]
# remove high energy data points with respect to CaF-CaF threshold

# remove data points with energies 1000 cm^-1 above of CaF-CaF threshold
data_array=np.delete(data_array,inddel,axis=0)

#If true then extra symmetric equivalent training points are added to the training set
add_sympoints=True
#If true, the fit is symmetrized when evaluating
symmetrize=True

#For R<Rsym, symmetrically equivalent points are added to the training set
Rsym=8

R = 1/data_array[:,0]  #  used in symmetrization
r13 = data_array[:,1]
r23 = data_array[:,2]
r14 = data_array[:,3]
r24 = data_array[:,4]
r34 = data_array[:,5]
V = data_array[:,6]
V = V-easymp


x_data=data_array[:,:6]#1/(x_data_n)
y_data = V

if add_sympoints==True:
    print('Number of points before adding extra symmetric points:', len(y_data))
    extrapoints=np.where(R<Rsym)[0]
    extrax=perm3(x_data[extrapoints,:])
    extray=y_data[extrapoints]
    x_data=np.concatenate([x_data,extrax])
    y_data=np.concatenate([y_data,extray])
    print('Number of points after adding extra symmetric points:',len(y_data))


#Define kernel
kernel =C(1.0, (1e-5, 1e5))* Matern(length_scale=[1.0,1.0,1.0,1.0,1.0,1.0], length_scale_bounds=(1e-5, 1e5), nu=2.5) + WhiteKernel(noise_level=0.1)
 
#Construct GP fit
gp = GaussianProcessRegressor(kernel=kernel)
model = gp.fit(x_data, y_data)
#Display trained kernel and marginal Log-likelihood
print("\nLearned kernel: %s" % gp.kernel_)
print("Log-marginal-likelihood: %.3f", gp.log_marginal_likelihood(gp.kernel_.theta))

with open('gpr.pkl','wb') as gprpickle:
          pickle.dump(gp,gprpickle)

