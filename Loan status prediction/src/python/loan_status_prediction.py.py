#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import classification_report, accuracy_score, roc_auc_score
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, AdaBoostClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.neural_network import MLPClassifier
from sklearn.inspection import permutation_importance
import lime
import lime.lime_tabular
import matplotlib.pyplot as plt
import joblib

# Step 1: Load the dataset
df = pd.read_csv('../data/processed/financial_loan_with_late_status.csv')

# Step 2: Data inspection
print(df.info())
print(df.describe())
print(df.isnull().sum())

# Filter to include only 'Charged Off' and 'Fully Paid' loans
df = df[(df["loan_status"] == "Charged Off") | (df["loan_status"] == "Fully Paid")]

# Handle missing data
df['emp_title'] = df['emp_title'].fillna('Unknown')

# List of columns to convert to datetime
date_columns = ['issue_date', 'last_payment_date', 'next_payment_date']

# Convert each column to datetime
for column in date_columns:
    df[column] = pd.to_datetime(df[column])

# Function to encode loan status
def encode_loan_status(df, column_name='loan_status'):
    encoding_map = {'Charged Off': 1, 'Fully Paid': 0}
    df[column_name] = df[column_name].map(encoding_map)
    if df[column_name].isnull().any():
        raise ValueError("There are loan statuses that are not 'Charged Off' or 'Fully Paid'. Please handle them accordingly.")
    return df

df = encode_loan_status(df)

# Feature Engineering on 'issue_date', 'last_payment_date', 'next_payment_date'
def feature_engineering(df, date_column):
    df[f'{date_column}_year'] = df[date_column].dt.year
    df[f'{date_column}_month'] = df[date_column].dt.month
    df[f'{date_column}_day'] = df[date_column].dt.day
    df[f'{date_column}_dayofweek'] = df[date_column].dt.dayofweek
    df[f'{date_column}_quarter'] = df[date_column].dt.quarter
    df[f'{date_column}_is_weekend'] = df[f'{date_column}_dayofweek'].apply(lambda x: 1 if x >= 5 else 0)

for column in date_columns:
    feature_engineering(df, column)

# Drop original date columns
df = df.drop(columns=date_columns)

# Drop unnecessary columns
df.drop(columns=['id', 'delinquent', 'member_id', 'emp_title'], axis=1, inplace=True)

# Encode categorical variables
label_encoders = {}
categorical_columns = df.select_dtypes(include=['object']).columns
for column in categorical_columns:
    le = LabelEncoder()
    df[column] = le.fit_transform(df[column])
    label_encoders[column] = le

# Split the data into features and target
X = df.drop(columns=['loan_status'], axis=1)
y = df['loan_status']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Standardize the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Initialize models
models = {
    "Logistic Regression": LogisticRegression(random_state=42, max_iter=1000),
    "Random Forest": RandomForestClassifier(random_state=42),
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "K-Nearest Neighbors": KNeighborsClassifier(),
    "Support Vector Machine": SVC(random_state=42, probability=True),
    "Naive Bayes": GaussianNB(),
    "Gradient Boosting": GradientBoostingClassifier(random_state=42),
    "AdaBoost": AdaBoostClassifier(random_state=42),
    "Linear Discriminant Analysis": LinearDiscriminantAnalysis(),
    "MLP_Classifier": MLPClassifier(random_state=42, max_iter=1000)
}

# Evaluate each model
results = {}
for name, model in models.items():
    print(f"Training {name}...")
    model.fit(X_train_scaled, y_train)
    
    y_pred = model.predict(X_test_scaled)
    y_proba = model.predict_proba(X_test_scaled)[:, 1] if hasattr(model, "predict_proba") else None
    
    accuracy = accuracy_score(y_test, y_pred)
    auc_roc = roc_auc_score(y_test, y_proba) if y_proba is not None else "N/A"
    report = classification_report(y_test, y_pred, output_dict=True)
    
    results[name] = {
        "Accuracy": accuracy,
        "AUC-ROC": auc_roc,
        "Precision_Class_0": report["0"]["precision"],
        "Recall_Class_0": report["0"]["recall"],
        "F1-Score_Class_0": report["0"]["f1-score"],
        "Precision_Class_1": report["1"]["precision"],
        "Recall_Class_1": report["1"]["recall"],
        "F1-Score_Class_1": report["1"]["f1-score"],
        "Weighted_Precision": report["weighted avg"]["precision"],
        "Weighted_Recall": report["weighted avg"]["recall"],
        "Weighted_F1-Score": report["weighted avg"]["f1-score"]
    }

# Display the results
results_df = pd.DataFrame(results).T
results_df = results_df.sort_values(by="Accuracy", ascending=False)
print("\nModel Comparison:")
print(results_df)

# Save the best model
best_model_name = results_df.index[0]
best_model = models[best_model_name]
joblib.dump(best_model, f'../model/{best_model_name}_loan_status_predictor.pkl')
joblib.dump(scaler, '../model/scaler.pkl')
joblib.dump(label_encoders, '../model/label_encoders.pkl')

print(f"\nBest model '{best_model_name}' saved successfully.")

# Permutation Importance
result = permutation_importance(best_model, X_train_scaled, y_train, n_repeats=10, random_state=42, n_jobs=-1)

# Sort features by importance
sorted_idx = result.importances_mean.argsort()
feature_names = X.columns[sorted_idx]

# Plot the feature importance
plt.figure(figsize=(10, 8))
plt.barh(feature_names, result.importances_mean[sorted_idx], xerr=result.importances_std[sorted_idx])
plt.xlabel("Permutation Importance (Mean Decrease in Accuracy)")
plt.title(f"Feature Importance for {best_model_name}")

# Save the current figure as a .png file
plt.savefig('../results/Importance.png', format='png')

# Display the plot
plt.show()

# LIME explanation

# Ensure the directory exists
output_dir = '../results/lime_explanations/'
os.makedirs(output_dir, exist_ok=True)

# LIME explanation setup
#-------------------------------------------------------------------------------------
explainer = lime.lime_tabular.LimeTabularExplainer(training_data=X_train_scaled, 
                                                   feature_names=X.columns, 
                                                   class_names=['Fully Paid', 'Charged Off'], 
                                                   mode='classification')

# Specify how many instances you want to explain
num_instances = 5

# Loop over a number of random instances to generate and save explanations
for i in range(num_instances):
    # Select a random instance from the test set
    instance_index = np.random.randint(0, X_test_scaled.shape[0])
    
    # Generate explanation for the selected instance
    exp = explainer.explain_instance(X_test_scaled[instance_index], 
                                     best_model.predict_proba, 
                                     num_features=10)
    
    # Render the explanation as a matplotlib figure
    fig = exp.as_pyplot_figure()
    
    # Save the figure as a .png file with a unique name
    fig.savefig(os.path.join(output_dir, f'lime_explanation_{i + 1}.png'), format='png')
    
    # Close the figure to free up memory
    plt.close(fig)

print(f"Saved {num_instances} LIME explanations in {output_dir}")
#--------------------------------
explainer = lime.lime_tabular.LimeTabularExplainer(training_data=X_train_scaled, 
                                                   feature_names=X.columns, 
                                                   class_names=['Fully Paid', 'Charged Off'], 
                                                   mode='classification')

# Explain a random instance
i = np.random.randint(0, X_test_scaled.shape[0])
exp = explainer.explain_instance(X_test_scaled[i], best_model.predict_proba, num_features=10)
exp.show_in_notebook(show_table=True)

# Test on Unseen data
# Step 2: Load the unseen data
df = pd.read_csv('../data/processed/financial_loan_with_late_status.csv')
## Test the model on the current loans
df_unseen = df[df["loan_status"] == "Current"]

# Preprocess the unseen data
df_unseen['emp_title'] = df_unseen['emp_title'].fillna('Unknown')

for column in date_columns:
    df_unseen[column] = pd.to_datetime(df_unseen[column])

for column in date_columns:
    feature_engineering(df_unseen, column)

df_unseen = df_unseen.drop(columns=date_columns + ['id', 'delinquent', 'member_id', 'emp_title','loan_status'])

# Encode categorical variables using the previously saved encoders
for column, le in label_encoders.items():
    df_unseen[column] = le.transform(df_unseen[column])

# Standardize the features
X_unseen = scaler.transform(df_unseen)

# Make predictions on the unseen data
predictions = best_model.predict(X_unseen)
df_unseen['Predicted_Loan_Status'] = predictions

if hasattr(best_model, "predict_proba"):
    probabilities = best_model.predict_proba(X_unseen)
    df_unseen['Prediction_Probability'] = probabilities.max(axis=1)

# Save the predictions
df_unseen.to_csv('../results/unseen_data_with_predictions.csv', index=False)
print(df_unseen.head())

