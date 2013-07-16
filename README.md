####Human Activity Recognition

Project folder for human activity recognition project

Original data and publication: http://groupware.les.inf.puc-rio.br/har

####Description
Example of applying Vowpal Wabbit to accelerometer data

####Data Description

- include images



####Approach

- describe vw
- scikit-learn

- describe data processing: omitting 'user', vw namespaces
- describe evaluation strategy

####Usage
python raw_to_format.py ../data/input/dataset.csv ../data/working/dataset.vw vw #convert data to vw format, omitting 'user' feature


####Findings
adding gender actually confuses the classifier

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
- [x] vw - write python script to convert .csv to .vw format
- [ ] compare to benchmark in original study
- [ ] create plots of performance metrics, etc (use skl)
- [ ] create histogram of class distribution
- [ ] create hist/plots of data distribution (age, outliers, etc)
- [ ] skl - use feature scaling