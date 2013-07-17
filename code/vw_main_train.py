#!/usr/bin/python

'''
Driver script for building and evaluating vw models

'''
import os,sys
import split,vw_evaluation

## Split into training and test sets
# split.main('../data/working/dataset_rand.vw','../data/working/train.vw','../data/working/test.vw', 0.8, 'randy')


## Train vw model using train set (run as system cmd from python), save into file
# model_cmd = "vw -d ../data/working/train.vw -f ../data/output/vw.model -c -k --oaa 5 --loss_function logistic -l 0.05 --passes 40"
# model_cmd = "vw -d ../data/working/train.vw -f ../data/output/vw.model -c --oaa 5 --bfgs --loss_function logistic --passes 40"
# model_cmd = "vw -d ../data/working/train.vw -f ../data/output/vw.model -c --oaa 5 --bfgs --loss_function logistic --passes 40"

os.system("head -1000 ../data/working/train.vw > ../data/working/train_tmp.vw")



model_cmd = "vw -d ../data/working/train_tmp.vw -f ../data/output/vw.model -c -k --oaa 5 --bfgs --loss_function logistic --passes 30"



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