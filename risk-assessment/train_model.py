# Patient health data fed into trained machine learning risk model and Random Forest classification algorithm.
# Implemented the loading of data, model training, evaluation and saving via machine learning workflow.

import pandas as pd

import joblib


from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (

    accuracy_score,

    classification_report

)




# Loading patient dataset
data = pd.read_csv(

    "dataset/patient_health_data.csv"

)



# Selecting input features
X = data[

    [

        "age",

        "blood_pressure",

        "heart_rate",

        "blood_sugar",

        "oxygen",

        "bmi",

        "smoking",

        "exercise"

    ]

]



# Selecting target value
y = data[

    "risk_level"

]





# Splitting training and testing data
X_train, X_test, y_train, y_test = train_test_split(

    X,

    y,

    test_size=0.2,

    random_state=42

)




# Creating random forest model
model = RandomForestClassifier(

    n_estimators=100,

    random_state=42

)



# Training risk model
model.fit(

    X_train,

    y_train

)




# Predicting test results
prediction = model.predict(

    X_test

)



# Calculating model accuracy
accuracy = accuracy_score(

    y_test,

    prediction

)



# Displaying model accuracy
print(

    "Model Accuracy:",

    accuracy

)



# Displaying classification details
print(

    classification_report(

        y_test,

        prediction

    )

)



# Saving trained risk model
joblib.dump(

    model,

    "risk_model.pkl"

)



# Displaying model creation status
print(

    "Risk model created successfully"

)