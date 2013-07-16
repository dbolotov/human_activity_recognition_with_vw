#!/usr/bin/python

'''
Driver script for building and evaluating vw models

'''
import os,sys
import split,vw_evaluation

## Split into training and test sets
split.main('../data/working/dataset.vw','../data/working/train.vw','../data/working/test.vw', 0.7, 'rand')

## Train vw model using train set (run as system cmd from python), save into file
os.system("vw -d ../data/working/train.vw -f ../data/output/vw.model -c -k --oaa 5 -l 0.05 --passes 40") 

## Predict using vw model and test set, save into file
os.system("vw -i ../data/output/vw.model -t ../data/working/test.vw -p ../data/working/test_pred.txt --quiet")

## Evaluate results of test set prediction
vw_evaluation.main('../data/working/test_pred.txt','../data/working/test.vw')