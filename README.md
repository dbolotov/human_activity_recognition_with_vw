###Human Activity Recognition with Vowpal Wabbit


###Description

* This is a descriptive study on classifying human activities using body and accelerometer data.
* The project uses Vowpal Wabbit, python, and some linux command line utilities.
* Code and some detail for data processing, learning, and performance evaluation is included.


###Data

The benchmark dataset is taken from [Wearable Computing: Accelerometers' Data Classification of Body Postures and Movements](http://archive.ics.uci.edu/ml/datasets/Wearable+Computing%3A+Classification+of+Body+Postures+and+Movements+%28PUC-Rio%29). Each of the 165633 observation contains one of 5 types of activities, performed by human subjects: sitting down, standing up, standing, walking, and sitting. Information about the user and readings from 4 accelerometers are used as features in the learning algorithm.

See links for detailed description.

###Approach

This is a multi-class classification problem with categorical and continuous features. The approach consists of the following steps:

1. 'Look' at the data. Check the types of values, ranges, etc., and if there are any quality issues.

2. Preprocess the data into appropriate format and condition.

3. Perform training and testing.

4. Change algorithm, parameters, etc. based on performance.


This study uses Vowpal Wabbit to build the prediction model. Vowpal Wabbit is fast, simple to set up and use, and makes you chuckle when its name is said out loud.   

Modules from the scikit-learn python library are used to evaluate performance. The training, testing and evaluation steps are performed via a python script. All code is run on linux. 



###Data pre-processing

A timestamp was removed from row 122078 in the original .csv file.

Data was converted to vw format using a different namespace for the body and accelerometer features. The 'user' feature was omitted. The original dataset has observations sorted by class; the vw-formatted dataset was randomized.

The original and vw formats for one observation are shown below:
```
#header and one observation in original format:
user;gender;age;how_tall_in_meters;weight;body_mass_index;x1;y1;z1;x2;y2;z2;x3;y3;z3;x4;y4;z4;class
debora;Woman;46;1.62;75;28.6;-3;92;-63;-23;18;-19;5;104;-92;-150;-103;-147;sitting

#same observation in vw format (with 'user' omitted):
1  |b1 Woman |b2 46 |b3 1.62 |b4 75 |b5 28.6 |a6 -3 |a7 92 |a8 -63 |a9 -23 |a10 18 |a11 -19 |a12 5 |a13 104 |a14 -92 |a15 -150 |a16 -103 |a17 -147
```

VW allows inclusion of quadratic and cubic feature interactions. For the namespace above, quadratic interactions between all accelerometer features could be specified with `-q aa`.


###Training and testing

Data was split into training and test sets, and the model was built using the training data. Performance was evaluated using classification accuracy and confusion matrices. Using both training and test sets allows to get a sense of bias/variance and how well the algorithm generalizes.

The following plots were made using an 80/20 training/test split, using all but 'user' and 'gender' features, with the following vw command pattern: `vw -d <input> -f <output> -c --oaa 5 --bfgs --loss_function logistic --passes <n>`.
The learning curves (accuracy vs num examples plot) were made by training on an increasing number of observations and computing test error on the same held out test set.

- average loss plot
- accuracy vs training examples plot
- accuracy vs passes plot


###Usage and output example
```bash
## commands:

#convert data to vw format
python raw_to_format.py ../data/input/dataset.csv ../data/working/dataset.vw vw 
#randomize rows in dataset
sort -R sort -R ../data/working/dataset.vw > ../data/working/dataset_rand.vw 
#split data into training and test set, build model, evaluate on test set
python vw_main_train.py 

## output:
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



###Findings

- It is possible to achieve a test accuracy of about 0.96 using the following specification: `vw -d <input> -f <output> -c --oaa 5 --bfgs --loss_function logistic --passes 30` 
- 'sitting down' and 'standing up' have the lowest F1 scores and the smallest amount of observations. More data for these activities is likely to help.
- using vw's `--bfgs` increases accuracy by .03.
- random sorting of observations increases accuracy by 0.001.


###Further tasks

- Use k-fold cross-validation to get a better sense of errors.
- Add importance weights to sittingdown and standingup to see how accuracy is affected. Can be done with something like `sed -e 's/<class1> /<class1> <weight1>  /g' -e 's/<class2>  /<class2> <weight2>  /g' <inputfile> > <outputfile>`
- Try nonlinear options in vw
- Try adjusting rank of inverse hessian approximation for bfgs option in vw
- Omit all body-related features from the dataset (gender, age, height, weight, BMI)




###Links
- [Original data source and publication](http://groupware.les.inf.puc-rio.br/har)
- [Detailed data description at UC Irvine database](http://archive.ics.uci.edu/ml/datasets/Wearable+Computing%3A+Classification+of+Body+Postures+and+Movements+%28PUC-Rio%29)
- [Vowpal Wabbit](https://github.com/JohnLangford/vowpal_wabbit/wiki)
- [Scikit-learn](http://scikit-learn.org/stable/)
- [Original source for split.py and raw_to_format.py](https://github.com/zygmuntz/phraug)
- [Machine learning experiment organization](http://arkitus.com/PRML/)




####TODO
- [x] build classification report with scikits http://scikit-learn.org/dev/modules/generated/sklearn.metrics.classification_report.html#sklearn.metrics.classification_report
- [x] use importance weighting for highly misclassified samples
- [x] use cost for misclassified classes - this did not work, probably implemented wrong
- [x] vw - write python script to convert .csv to .vw format
- [ ] read original paper for the dataset
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