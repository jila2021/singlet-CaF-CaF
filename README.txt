*The code (total-gp.py) is written in python having version 3.6. 

*The training and test data sets both are in inverse atomic coordinates that
we mentioned in our manuscript. The energy is expressed in atomic unit. 
 
*Here we consider two sets of training data named as train_set1.txt and train_set2.txt, respectively.
We exclude the data points which are above: 0.00455 Hartree = 1000 cm^-1 with respect to CaF-CaF threshold.

*To check the accuracy of the GP, we use a test data set named as
 test_data.txt

*The subroutine symfuncs.py is used for the symmetrization.

*The code total-gp.py is used for making the fit of the surface using the training data set
 & it is run by the command: 
 python total-gp.py

*Finally to check the accuracy of the fit, one need to run the code test.py on some test data points 
 and it is run by the command
 python test.py
 