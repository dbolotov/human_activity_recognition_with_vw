#!/usr/bin/python

'''
Driver script for building and evaluating vw models

'''
import os,sys
import split
import vw_evaluation

## Split into training and test sets
split.main('../data/working/dataset_no_body_data.vw','train.vw','test.vw', 0.8, 'randy')

## Train vw model, save into file
# cmd = "vw -d train_train.vw -f vw.model -c -k --loss_function logistic --passes 20 -q ee -b 27"

cmd = "vw -d ../data/working/dataset.vw -f vw.model -c -k --oaa 5 -l 0.05 -q ff --passes 20"


# cmd = "vw-varinfo -c -k --passes 10 --l1 0.0000001 train_train.vw > varinfo.txt"

os.system(cmd) 

# sys.exit() 
## Predict using vw model and test set, save into file
cmd = "vw -i vw.model -t test.vw -p vw_training_set_result.txt --quiet"
os.system(cmd)

## Evaluate model results
vw_evaluation.main('vw_training_set_result.txt','test.vw')


