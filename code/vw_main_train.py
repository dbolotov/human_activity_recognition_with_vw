#!/usr/bin/python

'''
Driver script for building and evaluating vw models

'''
import os,sys
import split,vw_evaluation

#vectors with training examples and numbers of passes, can be used with a for-loop to compute training and test errors for plots
# obs = [1000, 5000,10000,20000,30000,40000,50000,60000,70000,80000,90000,100000,110000,120000,132173]
# passes = [10,20,30,40,50,60,70,80,90,100]


## Split into training and test sets
split.main('../data/working/dataset_rand.vw','../data/working/train.vw','../data/working/test.vw', 0.7, 'randy')

## Train vw model using train set (run as system cmd from python), save into file
model_cmd = "vw -d ../data/working/train.vw -f ../data/output/vw.model -c -k --oaa 5 --bfgs --loss_function logistic --passes 30"
# model_cmd = "vw -d ../data/working/train.vw -f ../data/output/vw.model -c -k --oaa 5 --bfgs --loss_function logistic --passes "+str(num)+" --quiet"

print 'Executing:', model_cmd
os.system(model_cmd) 


## Predict using vw model and train and test sets, save into file
os.system("vw -i ../data/output/vw.model --testonly -d ../data/working/train.vw -p ../data/working/train_pred.txt --quiet")
os.system("vw -i ../data/output/vw.model --testonly -d ../data/working/test.vw -p ../data/working/test_pred.txt --quiet")


## Evaluate results
print '\nEvaluate on training set:'
vw_evaluation.main('../data/working/train_pred.txt','../data/working/train.vw')
print '\nEvaluate on test set:'
vw_evaluation.main('../data/working/test_pred.txt','../data/working/test.vw')