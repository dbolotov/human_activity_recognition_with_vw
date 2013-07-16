#!/usr/bin/python

'''
Driver script for building and evaluating vw models

'''
import os,sys
import split
import vw_evaluation

## Split into training and test sets
split.main('../data/working/dataset.vw','../data/working/train.vw','../data/working/test.vw', 0.8, 'randy')

## Train vw model, save into file
cmd = "vw -d ../data/working/dataset.vw -f ../data/output/vw.model -c -k --oaa 5 -l 0.05 --passes 5"
os.system(cmd) 

## Predict using vw model and test set, save into file
os.system("vw -i ../data/output/vw.model -t ../data/working/test.vw -p ../data/working/test_pred.txt --quiet")

## Evaluate model results
vw_evaluation.main('../data/working/test_pred.txt','../data/working/test.vw')


