# Report - Model Evaluation

### BASELINE MODEL
I implemented as the baseline model a simple logistic regression with default parameters. This are the metrics obtained for train and test:

              precision    recall  f1-score   support

           0       0.95      1.00      0.97       972
           1       0.00      0.00      0.00        50

    accuracy                           0.95      1022
   macro avg       0.48      0.50      0.49      1022
weighted avg       0.90      0.95      0.93      1022

The roc-auc score obtained is 0.8275

### OTHER MODELS TRAINED
Previous experiments were implemented with this models: 
- RandomForestClassifier: with default parameters and also implementing a RandomizedSearchCV to search for the best hyperparameters
- LGBMClassifier: with default parameters and also implementing a RandomizedSearchCV to search for the best hyperparameters
- XGBoostClassifier: with default parameters and also implementing a RandomizedSearchCV to search for the best hyperparameters
- MLP deep learning model

### SELECTED MODEL
The model selected for implementing in the API to make predictions was the XGBoost with default parameters, taking into account the values obtained in presicion, recall and the roc-auc score of 0.8317. This are the metrics obtained for train and test:

              precision    recall  f1-score   support

           0       0.98      0.74      0.85       972
           1       0.13      0.74      0.22        50

    accuracy                           0.74      1022
   macro avg       0.56      0.74      0.53      1022
weighted avg       0.94      0.74      0.82      1022

### Possible Improvements
The first and main improvement would be to obtain more features related to heart conditions, also, more data. Better knowledge about average glucose levels and body mass index (maximum and minimum) could optimize feature engineering, i.e., outliers detection.



