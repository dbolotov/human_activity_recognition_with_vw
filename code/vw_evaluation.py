#!/usr/bin/python

'''
Evaluate result of vw model.

Load prediction output and true output
Use scikit-learn module for evaluation.
'''

import sys,csv
import numpy as np
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn import metrics

def main(y_pred_file,y_true_file):

    ## Create list for predicted class
    lines = [line.strip() for line in open(y_pred_file)]
    y_pred_raw = [float(item) for item in lines]
    y_pred = y_pred_raw
    # y_pred = [-1 if item<0.0 else 1 for item in y_pred_raw]

    # print y_pred_raw
    # print y_pred
    # sys.exit()
    
    
    ## Create list for true class
    lines = [line.strip() for line in open(y_true_file)]
    y_true = [float(item[0]) for item in lines]
    # y_true = [int(-1) if item[0]=='-' else int(1) for item in lines]
    
    ## Evaluation
    acc = accuracy_score(y_true, y_pred)
    # auc = auc_score(y_true, y_pred)

    cm = confusion_matrix(y_true,y_pred)
    print '\nModel Evaluation:\n'
    print '%-10s %12.5f' % ('accuracy:',acc)
    # print '%-10s %12.5f' % ('AUC:',auc)
    print 'confusion matrix:'
    print cm

if __name__=='__main__':
    sys.exit(main(sys.argv[1],sys.argv[2]))
