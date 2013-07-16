#!/usr/bin/python

'''
Evaluate result of vw model using scikit-learn library.

Usage: vw_evaluation.py <predicted_classes> <true_classes>
'''

import sys,csv
import numpy as np
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

def main(y_pred_file,y_true_file):

    ## Create list for predicted class
    lines = [line.strip() for line in open(y_pred_file)]
    y_pred = [float(item) for item in lines]
    y_pred = y_pred[:-1] #remove last line if using csoaa

    ## Create list for true class
    lines = [line.strip() for line in open(y_true_file)]
    y_true = [float(item[0]) for item in lines]
    
    print len(y_true)
    print len(y_pred)
    print set(y_pred)
    # sys.exit()
    ## Define labels for classes
    target_names = ['sitting', 'sittingdown', 'standing', 'standingup', 'walking']
    ## Evaluation
    acc = accuracy_score(y_true, y_pred)
    cm = confusion_matrix(y_true,y_pred)
    cr = classification_report(y_true,y_pred,target_names=target_names)

    ## Print results
    print '\nModel Evaluation:\n'
    print '%-10s %12.5f' % ('accuracy:',acc)
    print 'confusion matrix:'
    print cm
    print cr

if __name__=='__main__':
    sys.exit(main(sys.argv[1],sys.argv[2]))
