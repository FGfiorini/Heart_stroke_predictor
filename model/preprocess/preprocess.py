import pandas as pd 
import numpy as np
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.compose import ColumnTransformer
from xgboost import XGBClassifier
import argparse
import os 
import pickle

def parse_args():
    """
    Use argparse to get the input parameters for preprocessing the data.
    """
    parser = argparse.ArgumentParser(description="Preprocess data.")
    parser.add_argument(
        "data_csv",
        type=str,
        help="Full path to the file with the input data . E.g. "
             "Notebooks/healthcare-dataset-stroke-data.csv",
    )

    args = parser.parse_args()
    return args


def main(data_csv):
    """
    This script will be used for preprocessing our raw data. The only input argument it
    should receive is the path to our data_csv. We will store the resulting train/test
    splits and preprossed in pickles directory using pickle.

    Parameters
    ----------
    data_csv : csv or txt file
        Full path to csv or txt file.
    
    """
    heart_stroke_df = pd.read_csv(f"{data_csv}")

    ###let's separate target from other features###

    features = heart_stroke_df.drop(["stroke"], axis=1)
    features = features.drop(["id"], axis=1) #id won't be useful for models' predictions
    target = heart_stroke_df.stroke
    
    features = features.astype({"hypertension": 'str', "heart_disease": 'str'}) # I changed to string beacuse both are binary classified

    ### Now I create a list of Numerical and Categorical Features
    categorical_features = list(features.select_dtypes(include=['object']).columns)
    numerical_features = list(features.select_dtypes(exclude=['object']).columns)

    ### Split in train and test
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=100, stratify=target)
    
    ###### Pipeline for numeric features ######
    #### input all and scale ####

    numeric_pipeline = Pipeline(steps=[         #pipeline for standarization for numerical features
        ("impute", SimpleImputer(strategy='mean')),
        ("standarization", StandardScaler())
    ])

    categoric_pipeline = Pipeline(steps=[
        ("encoding", OneHotEncoder(handle_unknown='ignore', sparse=False, drop='if_binary')),   #pipeline for standarization for numerical features
    ])

    # We merge both pipeline into one single pre-processing object
    # We use ColumnTransformer for this
    full_processor = ColumnTransformer(transformers=[
        ('number', numeric_pipeline, numerical_features),
        ('categories', categoric_pipeline, categorical_features)
    ])
  
     # The final pipeline with all the transformations
    final_pipeline = make_pipeline(full_processor)
    
    final_pipeline_fit = final_pipeline.fit(X_train.copy())
    ##### Let's define X_train_prep #####

    X_train_prep = full_processor.fit_transform(X_train)

    ##### Save final preprocessing pipeline in a pickle, after fitting it
    with open(os.path.join("/src/pickles", "final_pipeline_fit.pickle"), "wb") as f:
        pickle.dump(final_pipeline , f, protocol=pickle.HIGHEST_PROTOCOL)
    
    X_train_prep = final_pipeline_fit.transform(X_train)

    ##### Saving pickles of preprocessed train and test data
    with open(os.path.join("/src/pickles", "X_train_prep.pickle"), "wb") as f:
        pickle.dump(X_train_prep, f, protocol=pickle.HIGHEST_PROTOCOL)           
    with open(os.path.join("/src/pickles", "y_train.pickle"), "wb") as f:
        pickle.dump(y_train, f, protocol=pickle.HIGHEST_PROTOCOL)
    with open(os.path.join("/src/pickles", "y_test.pickle"), "wb") as f:
        pickle.dump(y_test, f, protocol=pickle.HIGHEST_PROTOCOL)

    print("----------------------------")
    print("Preprocessing done")

if __name__ == "__main__":
    args = parse_args()
    main(args.data_csv)




