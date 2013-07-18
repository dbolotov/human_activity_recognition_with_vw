###Human Activity Recognition with Vowpal Wabbit


###Description

* This is a descriptive study on classifying human activities using data from wearable accelerometers.
* The project uses Vowpal Wabbit, python, and linux command line utilities.
* Code and some detail for data processing, learning, and performance evaluation is included.


###Data

The benchmark dataset is from research on human activity recognition, described [here](http://groupware.les.inf.puc-rio.br/har). Each of the 165633 observations contains one of 5 types of activities, performed by human subjects: sitting down, standing up, standing, walking, and sitting. Information about the user, and readings from 4 accelerometers worn by each subject, are available for each observation. Only the accelerometer features are used in building the model here. The process of extracting 12 features from from accelerometer readings is described in the [original paper](http://groupware.les.inf.puc-rio.br/work.jsf?p1=11201).


###Approach

This is a multi-class classification problem with continuous features. The approach consists of the following steps:

1. 'Look' at the data. Check the types of values, ranges, etc., and if there are any quality issues.

2. Convert the data into appropriate format.

3. Perform training and testing.

4. Change algorithm, parameters, etc. based on performance.


This study uses Vowpal Wabbit to build the prediction model, because is fast, fun to use, and fun to pronounce. Modules from the scikit-learn python library are used to evaluate performance. The training, testing and evaluation steps are performed via a python script. All code is run on linux. 


###Data pre-processing

A timestamp was removed from row 122078 in the original .csv file. It was also found that the data contains 1352 duplicate rows; these were not removed.

Data was converted to vw format, which included mapping class names to integer values. Only accelerometer features were retained.The original dataset has observations sorted by class; the vw-formatted dataset was randomized at this point.

The header and one observation in original format looks like this:
```
user;gender;age;how_tall_in_meters;weight;body_mass_index;x1;y1;z1;x2;y2;z2;x3;y3;z3;x4;y4;z4;class
debora;Woman;46;1.62;75;28.6;-3;92;-63;-23;18;-19;5;104;-92;-150;-103;-147;sitting
```
The same observation in vw format (only accelerometer features retained):
```
1  |f1 -3 |f2 92 |f3 -63 |f4 -23 |f5 18 |f6 -19 |f7 5 |f8 104 |f9 -92 |f10 -150 |f11 -103 |f12 -147
```

###Training and testing

Models were built using a 70/30 training/test split, using all accelerometer features, with the following vw command pattern: 
`vw -d <input> -f <output> -c -k --oaa 5 --bfgs --loss_function logistic --passes <n>`.

Performance was evaluated on both sets using classification accuracy and confusion matrices. Tracking both training and test errors allows to get a sense of bias/variance and how well the algorithm generalizes.


###Usage and output example

```bash
## commands:

#convert data to vw format
python raw_to_format.py ../data/input/dataset.csv ../data/working/dataset.vw 
#randomize rows in dataset
sort -R ../data/working/dataset.vw > ../data/working/dataset_rand.vw
#split remaining data into training and test set, learn, and evaluate
python vw_main_train.py 

## output:
Executing: vw -d ../data/working/train.vw -f ../data/output/vw.model -c -k --oaa 5 --bfgs --loss_function logistic --passes 30 --quiet

Evaluate on training set:
accuracy:       0.97027
confusion matrix:
[[40391     4     0    19     4]
 [   19  8585   179   528   170]
 [    0    33 37220   113   410]
 [   38   493   390  8614   399]
 [    1   244   628   258 33433]]

Evaluate on test set:
accuracy:       0.95547
confusion matrix:
[[10173    15     1    20     4]
 [   17  1984    48   209    88]
 [    0    16  9392    43   143]
 [   32   204    98  1970   177]
 [    2    91   175   107  8451]]

```


###Findings

![Loss vs num passes](https://bitbucket.org/dbolotov/human_activity_recognition_with_vw/raw/master/images/loss_vs_num_passes.jpg "Loss vs num passes") ![Error vs num examples](https://bitbucket.org/dbolotov/human_activity_recognition_with_vw/raw/master/images/error_vs_num_examples.jpg "Accuracy vs num examples")


The left figure shows average training loss output from VW when using L-BFGS optimization and a logistic loss function. Test error was not decreasing significantly after the 30-passes mark. The learning curves plot (right figure) was made by training on an increasing number of observations (using 30 passes) and computing test error on the same test set of 49928 examples. These show that test error decreases and both errors converge to a low value. This means that the algorithm is not suffering from outrageous high-bias or high-variance problems.

The features'sitting down' and 'standing up' have the highest errors and the smallest amount of observations. More data for these activities would likely increase overall accuracy.

It is possible to achieve a test accuracy of about 0.95 using the following specification: 
`vw -d <input> -f <output> -c -k --oaa 5 --bfgs --loss_function logistic --passes 30`. 

In a more thorough approach, some percentage of the data would be held out from training/testing and only used to report a final performance. Using k-fold cross-validation could also give a better sense of errors during training.


###Further tasks
 
- Add importance weights to sittingdown and standingup to see how accuracy is affected. Can be done with something like `sed -e 's/<class1> /<class1> <weight1>  /g' <inputfile> > <outputfile>`
- Try nonlinear options in vw
- Try adjusting rank of inverse hessian approximation for bfgs option in vw
- Separate data into 60.20.20 train/cross-validation/test split, and use cv set for tuning.


###Resources
- [Original data source and publication](http://groupware.les.inf.puc-rio.br/har)
- [Detailed data description at UC Irvine database](http://archive.ics.uci.edu/ml/datasets/Wearable+Computing%3A+Classification+of+Body+Postures+and+Movements+%28PUC-Rio%29)
- [Original source for split.py and raw_to_format.py](https://github.com/zygmuntz/phraug)
- [Machine learning experiment organization](http://arkitus.com/PRML/)

###Software summary
- [Vowpal Wabbit](https://github.com/JohnLangford/vowpal_wabbit) 7.3.0
- [Python](http://www.python.org/download/releases/2.7/) 2.7
- [scikits-learn](http://scikit-learn.org/stable/) 0.13.1



####TODO
- [ ] compare to benchmark in original study


####Technical findings
- vw csoaa: will output an additional line in the output prediction file. Ran prediction with labeled examples, and this line did not have an example label.
- vw csoaa: try removing class costs from testing file. Prediction is 100% accurate, not sure if this is because the test examples are labeled. If labels are removed, result is same as when running model with -t option. Seems that csoaa results in perfect prediction.
- vw csoaa: not using any costs with this option will result in 100% accuracy on test set. Is this because the --testonly option does not work if csoaa is specified in the model?

