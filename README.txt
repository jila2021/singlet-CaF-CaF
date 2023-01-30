This folder contains the necessary files to calculate the potential energy surface of the singlet 
CaF-CaF based on the manuscript
D. Sardar, A. Christianen, H. Li and J. L. Bohn; "Four-body singlet potential energy surface for 
reactions of calcium monofluoride"; arXiv:2211.05909 (2022). 

*The codes are written in python having version 3.6. 

*The training and test data sets are in inverse atomic coordinates that
we mentioned in our manuscript. The energy is expressed in atomic unit. 
 
*Here we consider two sets of training data named as train_set1.txt and train_set2.txt, respectively. We set zero
of the energy at CaF-CaF threshold. Inside the code, we put a condition to exclude the high energy data points with respect 
to the CaF-CaF threshold. For our purpose we ran the code for training data which are 
below: 0.00455 Hartree = 1000 cm^-1 to CaF-CaF threshold. But, one can set the repuslive barrier of the potential by 
changing this number and run the code. 

*The auxiliary python function symfuncs.py is used for the symmetrization.

*The code singlet_Ca2F2.py is used for making the fit of the surface using the training data set
& it is run by the command: 
python total-gp.py

*After fitting, the GP object is stored in gp.pkl. Therefore, the fit only needs to be done once,
then the result is available for whatever use a user wants to put it to.


*After the GP object has been made, the fit can be evaluated by the code eval_fit.py. This script demonstrate
an example on how to do this. It loads coordinates (inverse interatomic distances) from the example_input.txt
and writes the energies in the file example_output.txt after evaluating the PES. The script runs by command
python eval_fit.py 

*To check the accuracy of the GP fit, the user needs to run the script test.py on a test data set named as test_data.txt.
 