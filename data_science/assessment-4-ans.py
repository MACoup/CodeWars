

'''
1.
For every one unit decrease X, the y -value (predicted SAT score) will go down 40 points, provided that the other predictors maintain constant.
'''

'''
2.
-0.3 is the difference in the log odds that someone who is homeschooled will be admitted to a 4-year university.
'''

'''
3.
Precision: TP / TP + FP
Recall: TP / TP + FN

Predicted
            ---------
Actual      100 | 5   |
            900 | 100 |
            ---------

'''

'''
5.
You would choose Model B because the False Positive Rate is lower, allowing for less nonspam emails to go to the spam folder.
'''

'''
6.
Because missing potential fraud is so costly, we would want to investigate every possible detection of fraud. Therefore we would choose Model A.
'''

'''
7.
Splitting on the feature Color and Value blue would have the most infomration gain.
'''

'''
8.
Var split 1: 1.6875
Var split 2: 0.959
Var of parent set: 3.432
IG(): 3.432 - (4/9 * 1.6875) - (5/9 * 0.959) = 3.432
'''

'''
9.
'''

'''
10.
The Decision Trees in Random Forests can utilize a feature that limits the number of features to split on randomly. This allows for decorrelation of features in the trees.
'''

'''
11.
'''

'''
12.
Random Forests can be processed across different machines/processors/
'''

'''
13.
Max depth refers to the number of splits/nodes allowed for each tree. This will cut down on variance, and allow for more efficient predicting features to be exposed.
'''

'''
14.
In boosting, learning_rate and n_estimators have an inverse effect on one another. When one goes up, the other must come down. We also have to be careful to avoid overfitting. A large learning_rate can lead to overfitting even when n_estimators is small.
'''

'''
15.
max_features works the same way as n_features in random forests. Sub_sample randomly subsets the training data for each tree. Setting an optimal max_feature hyperparameter will allow for a lower training set absolute error, which is even lower when both methods are applied.
'''

'''
16.
In Random Forests, the test error will more or less stay stagnant as you build more trees.
'''

'''
17.
SVM has the hyperparameter C, which modulates the misclassification penaly. With a large C, we have hard margins and accuracy is more important. With a smaller C, we have softer margins and generaliztion is more important.
'''
