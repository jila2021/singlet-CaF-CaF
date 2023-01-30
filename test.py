#this code is used to check the accuracy of the GP interpolation
#on test data set interm of root mean squre error
# Edited by Dibyendu Sardar 
import numpy as np
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, DotProduct, Matern, WhiteKernel, ConstantKernel as C
from symfuncs import *
from sklearn.model_selection import train_test_split
from numpy import asarray
from numpy import savetxt
import pickle

easymp=-273.09286 #MRCI+Q asymptote in Hartree

cm1=1.0/2.19474631e5 #unit

GP=pickle.load(open('gpr.pkl','rb'))#load GP 

#load test data points
test_array=np.loadtxt('test_data.txt')
Emrciqt = test_array[:,6]
eVmt=Emrciqt-easymp
ind=np.where(eVmt>0.00455)[0]
# remove test data points with energies 0.00455 Hartree = 1000 cm^-1 above with respect to CaF-CaF threshold
test_array=np.delete(test_array,ind,axis=0)

#Emrciqt = test_array[:,6]-easymp
#indd=np.where(Emrciqt>np.amin(Emrciqt)+0.2)[0]
#gpsym=symGP(GP)

r12t = test_array[:,0]  
r13t = test_array[:,1]
r23t = test_array[:,2]
r14t = test_array[:,3]
r24t = test_array[:,4]
r34t = test_array[:,5]
Vt = test_array[:,6]
Vt = Vt-easymp
print(Vt.shape)
x_test_sp = np.asarray([r12t,r13t,r23t,r14t,r24t,r34t]).T  
y_test = Vt

x_test=1/x_test_sp 
Ntest=len(y_test)

gpsym=symGP(GP)
y_pred = gpsym(1/x_test_sp)
y_diff = y_test-y_pred
rms = np.sqrt(sum(y_diff*y_diff)/Ntest)/cm1
print('RMS test error', rms)
