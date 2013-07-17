###Human Activity Recognition with Vowpal Wabbit


###Description
* Recognizing human activities from body and accelerometer data, using the Vowpal Wabbit machine learning system.
* This is a descriptive study, with code and some detail for data processing, model building, and performance evaluation.


###Data

The dataset consists of 165633 observations. Each observation contains one of 5 types of activities (sitting down, standing up, standing, walking, and sitting), performed by 4 human subjects. The features for each observation are information about the user and readings from 4 accelerometers.

A detailed description is available in links section.


###Approach

This study uses Vowpal Wabbit to learn and predict activities. Modules from the scikit-learn library are used to evaluate performance. 

The steps taken here are:
1. Look at the data. Check the types of values, and if there are any quality issues (using Excel, CLI, or any other tool).
2. Convert the original data file to vw format (`raw_to_format.py`) and randomly order observations.
3. Perform training and prediction with vw (`vw_main_train.py`).
4. Change algorithm, parameters, etc. based on performance.


###Data pre-processing

A timestamp was removed from row 122078.

For initial experiments, the data was converted to vw format using a different namespace for the body and accelerometer features. The 'user' feature was omitted. The original dataset has observations sorted by class, so the order in vw dataset was randomized (using `sort -R dataset.vw`).

```
#header and one observation in original format:
user;gender;age;how_tall_in_meters;weight;body_mass_index;x1;y1;z1;x2;y2;z2;x3;y3;z3;x4;y4;z4;class
debora;Woman;46;1.62;75;28.6;-3;92;-63;-23;18;-19;5;104;-92;-150;-103;-147;sitting

#same observation in vw format (with 'user' omitted):
1  |b1 Woman |b2 46 |b3 1.62 |b4 75 |b5 28.6 |a6 -3 |a7 92 |a8 -63 |a9 -23 |a10 18 |a11 -19 |a12 5 |a13 104 |a14 -92 |a15 -150 |a16 -103 |a17 -147
```

VW allows inclusion of quadratic and cubic feature interactions. For the namespace above, all quadratic interactions between accelerometer features could be specified with `-q aa`.


###Training and testing

Data is split into training and test sets, and the model is built using the training data. VW models are built using the multiclass option with a logistic loss function. Performance is evaluated using classification accuracy and confusion matrices. Using both training and test sets allows to get a sense of bias/variance and how well the algorithm generalizes.

- average loss plot
- accuracy vs training examples plot
- accuracy vs passes plot


###Findings

- It is possible to achieve a test accuracy of about 0.96 using the following specification: `vw -d <input> -f <output> -c --oaa 5 --bfgs --loss_function logistic --passes 30` 
- 'sitting down' and 'standing up' have the lowest scores and the smallest amount of observations. More data for these activities is likely to help.
- using vw's `--bfgs` increases accuracy by .03.
- random sort of observations increases accuracy by 0.001.


###Further improvement

- Use k-fold cross-validation to get a better sense of errors.
- Add importance weights to sittingdown and standingup to see how accuracy is affected.


###Usage and output example
```bash
#commands:
python raw_to_format.py ../data/input/dataset.csv ../data/working/dataset.vw vw #convert data to vw format
sort -R sort -R ../data/working/dataset.vw > ../data/working/dataset_rand.vw #randomize rows in dataset
python vw_main_train.py #split data into training and test set, build model, evaluate on test set

#output:
Executing: vw -d ../data/working/train.vw -f ../data/output/vw.model -c -k --oaa 5 --bfgs --loss_function logistic --passes 30 --quiet

Evaluate on training set:
accuracy:       0.97623
confusion matrix:
[[40457     3     0    16     2]
 [   42  8624   133   495   108]
 [    0    39 37296   106   292]
 [   40   474   389  8737   322]
 [    0   118   340   223 33917]]

Evaluate on test set:
accuracy:       0.96273
confusion matrix:
[[10119     7     1    21     5]
 [   27  2113    54   176    55]
 [    0    12  9473    47   105]
 [   25   189    95  1992   152]
 [    4    57   131    84  8516]]
```



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