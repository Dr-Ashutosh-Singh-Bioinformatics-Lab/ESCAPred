# ESCAPred: A Tool for Identification of Esophageal Cancer using Machine Learning.
Esophageal carcinoma is a malignant tumor that forms in the esophagus, the tube connecting the throat to the stomach. Biomarkers are essential for early detection, prognosis, and personalized treatment. Identifying biomarkers helps improve diagnosis accuracy, monitor disease progression, and enhance treatment strategies, ultimately improving patient survival and outcomes. Biomarkers are pivotal in this regard, providing noninvasive means for early detection, facilitating prompt treatment initiation, and potentially boosting survival rates. Hence, the recognition and validation of biomarkers are of primary importance in effectively addressing esophageal carcinoma.


## Introduction

ESCAPred is an innovative solution for identifying esophageal carcinoma through transcriptomic profiling. By harnessing advanced machine learning algorithms, this state-of-the-art technology analyzes tissue biomarkers to deliver highly accurate prognoses of esophageal cancer.

Additionally, the integration of machine learning enables continuous refinement of the predictive model’s accuracy as more data becomes available, further enhancing its reliability and effectiveness over time. ESCAPred marks a significant advancement in the early detection of esophageal carcinoma, potentially leading to earlier interventions and improved patient outcomes.

To further strengthen our approach, we selected 54 features using a range of Feature Selection Methods. These include the Fast Correlation-Based Filter Method (FCBF), Spike and Slab ("spikeslab"), Univariate statistical tests (F-test), and wrapper methods like Boruta and Recursive Feature Elimination (RFE). Additionally, we employed embedded methods such as XGBoost, SVC linear with the SelectFromModel class from scikit-learn, Random Forest, Extra Trees with Feature Importance, and LASSO (a regularization-based embedded method). By combining Filter, Wrapper, and Embedded feature selection techniques, we used an ensemble approach to identify features present in at least five methods. These 54 features show potential as biomarkers for classifying and predicting normal versus cancerous patients.


Installation and Usage:

You can install the package using the following command:


    git clone https://github.com/GITractCancer/ESCAPred.git
    cd ESCAPred

### Predict using ESCAPred

    import pandas as pd
    from ESCAPred import predict

    df = pd.read_csv("path/to/your/data.csv")

    predict(df, model_type='svc')

    
Specify the model type you want to use Models


## Models

The following classifiers are supported:

    svc
    rf
    ab
    xgb
    dt
    et
    lr
    gnb
    knn
    mlp
