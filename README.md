####Human Activity Recognition with Vowpal Wabbit

Project folder for human activity recognition project

Original data and publication: http://groupware.les.inf.puc-rio.br/har

####Description
Example of applying Vowpal Wabbit to accelerometer data

####Data Description

- include images



####Approach

- describe vw
- scikit-learn

- describe data processing: removing bad line, vw namespaces
- describe evaluation strategy

####Usage and output example
```bash
python raw_to_format.py ../data/input/dataset.csv ../data/working/dataset.vw vw #convert data to vw format
python vw_main_train.py #split data into training and test set, build model, evaluate on test set

Executing: vw -d ../data/working/train.vw -f ../data/output/vw.model -c -k --oaa 5 -l 0.05 --passes 40 --quiet

Model Evaluation:

accuracy:       0.95006
confusion matrix:
[[15055    17     0    29     3]
 [   29  2630    93   612   149]
 [    0     7 13861    97   417]
 [   35   148   117  2879   545]
 [    4    25    98    56 12769]]
             precision    recall  f1-score   support

    sitting       1.00      1.00      1.00     15104
sittingdown       0.93      0.75      0.83      3513
   standing       0.98      0.96      0.97     14382
 standingup       0.78      0.77      0.78      3724
    walking       0.92      0.99      0.95     12952

avg / total       0.95      0.95      0.95     49675

```

####Findings
sitting down and standing up have the lowest F1 scores and the smallest amount of observations

####Links
- [Original data source and publication](http://groupware.les.inf.puc-rio.br/har)
- [Vowpal Wabbit](https://github.com/JohnLangford/vowpal_wabbit/wiki)
- [Scikit-learn](http://scikit-learn.org/stable/)
- [split.py and raw_to_format.py source](https://github.com/zygmuntz/phraug)



####Put the following in a separate file:

####Goals
- [ ] Do case study: machine learning classification task
- [ ] Follow patterns for machine learning points: http://arkitus.com/PRML/
- [ ] Eventually move project to Github 


####TODO
- [ ] build classification report with scikits http://scikit-learn.org/dev/modules/generated/sklearn.metrics.classification_report.html#sklearn.metrics.classification_report
- [ ] use importance weighting for highly misclassified samples
- [ ] use perf for evaluation?
- [x] vw - write python script to convert .csv to .vw format
- [ ] compare to benchmark in original study
- [ ] create plots of performance metrics, etc 
- [ ] look at data and create histogram of class distribution (use Excel)
- [ ] create hist/plots of data distribution (age, outliers, etc)
- [ ] skl - use feature scaling