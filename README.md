###Human Activity Recognition with Vowpal Wabbit


###Description
Recognizing human activities from body and accelerometer data, using the Vowpal Wabbit machine learning system.


###Data

The dataset consists of 165633 observations. Each observation contains one of 5 types of activities (sitting down, standing up, standing, walking, and sitting), performed by 4 human subjects. The features for each observation are information about the user and readings from 4 accelerometers.

A detailed description is available in links section.


###Approach

This study uses Vowpal Wabbit to learn and predict activities. Modules from the scikit-learn library are used to evaluate performance.



- describe data processing: removing bad line, vw namespaces
- describe evaluation strategy

###Training and testing

- average loss plot
- accuracy vs training examples plot
- accuracy vs passes plot



###Findings

###Usage and output example
```bash
#commands:
python raw_to_format.py ../data/input/dataset.csv ../data/working/dataset.vw vw #convert data to vw format
sort -R sort -R ../data/working/dataset.vw > ../data/working/dataset_rand.vw #randomize rows in dataset
python vw_main_train.py #split data into training and test set, build model, evaluate on test set

#output:
Executing: vw -d ../data/working/train.vw -f ../data/output/vw.model -c -k --oaa 5 --bfgs --loss_function logistic --passes 30 --quiet

Evaluate on training set:
accuracy:       0.97658
confusion matrix:
[[40280     3     0    23     0]
 [   31  8737   137   492    98]
 [    0    38 37334    98   267]
 [   38   485   378  8699   307]
 [    0   125   347   229 34027]]

Evaluate on test set:
accuracy:       0.96449
confusion matrix:
[[10301     9     1    10     4]
 [   21  2067    37   164    43]
 [    1    18  9487    31    96]
 [   19   203   104  2022   160]
 [    2    41   124   100  8395]]
```

####Findings
- 'sittingdown' and 'standingup' have the lowest F1 scores and the smallest amount of observations.
- adding importance weights to sittingdown and standingup classes decreases precision and recall for those classes
- using --bfgs increases accuracy by .03. Why?
- random sort of rows (with sort -R <filename>) increases accuracy by 0.001

####Links
- [Original data source and publication](http://groupware.les.inf.puc-rio.br/har)
- [Detailed data description](http://archive.ics.uci.edu/ml/datasets/Wearable+Computing%3A+Classification+of+Body+Postures+and+Movements+%28PUC-Rio%29)
- [Vowpal Wabbit](https://github.com/JohnLangford/vowpal_wabbit/wiki)
- [Scikit-learn](http://scikit-learn.org/stable/)
- [original soruce for split.py and raw_to_format.py](https://github.com/zygmuntz/phraug)



####Put the following in a separate file:

####Goals
- [ ] Do case study: machine learning classification task
- [ ] Follow patterns for machine learning points: http://arkitus.com/PRML/
- [ ] Eventually move project to Github 


####TODO
- [x] build classification report with scikits http://scikit-learn.org/dev/modules/generated/sklearn.metrics.classification_report.html#sklearn.metrics.classification_report
- [x] use importance weighting for highly misclassified samples
- [x] use cost for misclassified classes
- [x] vw - write python script to convert .csv to .vw format
- [ ] compare to benchmark in original study
- [ ] create plots of performance metrics, etc 
- [ ] look at data and create histogram of class distribution (use Excel)
- [ ] create hist/plots of data distribution (age, outliers, etc)
- [ ] skl - use feature scaling

####Technical findings
- vw csoaa: will output an additional line in the output prediction file. Ran prediction with labeled examples, and this line did not have an example label.
- vw csoaa: try removing class costs from testing file. Prediction is 100% accurate, not sure if this is because the test examples are labeled. If labels are removed, result is same as when running model with -t option. Seems that csoaa results in perfect prediction.
- vw csoaa: not using any costs with this option will result in 100% accuracy on test set. Is this because the --testonly option does not work if csoaa is specified in the model?


#####Five pound
####Four pound
###Three pound
##Two pound
#One pound