# Loan Status Prediction with Machine Learning

This repository contains a script for predicting the loan status (`Charged Off` or `Fully Paid`) using various machine learning models. The script also includes model evaluation, feature importance analysis, and explanation of model predictions using LIME (Local Interpretable Model-Agnostic Explanations).

## Table of Contents

- [Overview](#overview)
- [Setup](#setup)
- [Data Preprocessing](#data-preprocessing)
- [Model Training and Evaluation](#model-training-and-evaluation)
- [Feature Importance](#feature-importance)
- [Model Interpretability with LIME](#model-interpretability-with-lime)
- [Testing on Unseen Data](#testing-on-unseen-data)
- [Results](#results)
- [Contributors](#contributors)

## Overview

This script processes a dataset containing loan information and builds a machine learning pipeline to classify loans as either `Charged Off` or `Fully Paid`. The pipeline includes:

1. **Data Preprocessing**: Handling missing values, encoding categorical variables, and feature engineering.
2. **Model Training and Evaluation**: Training multiple models, evaluating them based on accuracy, and selecting the best model.
3. **Feature Importance**: Determining the importance of features using permutation importance.
4. **Model Interpretability**: Using LIME to explain individual predictions.
5. **Testing on Unseen Data**: Applying the trained model to new, unseen data.

## Setup

To run this script, ensure you have Python installed along with the following packages:

```bash
pip install pandas numpy scikit-learn lime matplotlib joblib
```

## Data Preprocessing

### Loading the Dataset

The dataset is loaded from a CSV file and includes information about various financial loans. The target variable is the `loan_status`, which is either `Charged Off` or `Fully Paid`.

```python
df = pd.read_csv('../data/processed/financial_loan_with_late_status.csv')
```

### Handling Missing Data

Missing values in the `emp_title` column are filled with `'Unknown'`.

```python
df['emp_title'] = df['emp_title'].fillna('Unknown')
```

### Feature Engineering

Date columns are processed to extract useful features like the year, month, day, and whether the day falls on a weekend.

```python
for column in date_columns:
    feature_engineering(df, column)
```

### Encoding Categorical Variables

Categorical variables are encoded using `LabelEncoder` to convert them into numeric format.

```python
for column in categorical_columns:
    le = LabelEncoder()
    df[column] = le.fit_transform(df[column])
    label_encoders[column] = le
```

## Model Training and Evaluation

The script initializes and trains several machine learning models, including Logistic Regression, Random Forest, Decision Tree, and more. Each model is evaluated based on accuracy, AUC-ROC, and other metrics.

```python
for name, model in models.items():
    model.fit(X_train_scaled, y_train)
    y_pred = model.predict(X_test_scaled)
    y_proba = model.predict_proba(X_test_scaled)[:, 1] if hasattr(model, "predict_proba") else None
    # Model evaluation metrics
```

The best model is saved for later use.

```python
joblib.dump(best_model, f'../model/{best_model_name}_loan_status_predictor.pkl')
```

## Feature Importance

Permutation importance is used to evaluate the importance of features in the best-performing model. The results are visualized in a bar chart and saved as a PNG file.

```python
plt.savefig('../results/Importance.png', format='png')
```

## Model Interpretability with LIME

LIME is used to explain the predictions of the best model on individual instances. Explanations are saved as PNG files.

```python
for i in range(num_instances):
    exp = explainer.explain_instance(X_test_scaled[instance_index], best_model.predict_proba, num_features=10)
    fig.savefig(os.path.join(output_dir, f'lime_explanation_{i + 1}.png'), format='png')
```

## Testing on Unseen Data

The trained model is tested on new data to predict the loan status for loans that are currently active (`loan_status == "Current"`). The predictions are saved in a CSV file.

```python
df_unseen.to_csv('../results/unseen_data_with_predictions.csv', index=False)
```

## Results

The script outputs:

- Model comparison metrics (Accuracy, AUC-ROC, Precision, Recall, F1-Score).
- Feature importance chart.
- LIME explanations for individual predictions.
- Predictions on unseen data.

## Contributors

- **Noé Fouotsa** - Initial work

### Download the README.md file:

I will provide you with the content in a downloadable format as a markdown file.

[Download README.md](https://downfile.herokuapp.com/file/6508/README.md?dl=1)
