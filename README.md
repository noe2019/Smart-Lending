# Smart Lending: Enhancing Financial Decisions with Data-Driven Insights


![Smart-Lending/images/](https://github.com/noe2019/Smart-Lending/blob/main/images/loan.gif)

## Introduction

This project involves an in-depth analysis of the `financial_loan.csv` dataset, which contains information related to loan applications, approvals, and performances at a financial institution. As a data analyst, the primary aim is to extract actionable insights that will inform decision-making processes, optimize risk management, and enhance overall customer satisfaction.

The analysis covers various aspects, including customer demographics, loan performance, risk assessment, profitability, and operational efficiency. By leveraging this dataset, the goal is to understand patterns and trends that impact the bank's loan portfolio, identify potential areas for improvement, and develop strategies to mitigate risks associated with loan defaults.

## Table of Contents

1. [Project Setup](#project-setup)
   - [Requirements](#requirements)
   - [Installation](#installation)

2. [Data Overview](#data-overview)
   - [Data Description](#data-description)
   - [Data Cleaning and Preprocessing](#data-cleaning-and-preprocessing)

3. [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
   - [Customer Demographics](#customer-demographics)
   - [Loan Performance](#loan-performance)
   - [Default Rates](#default-rates)

4. [Risk Assessment](#risk-assessment)
   - [Credit Score Analysis](#credit-score-analysis)
   - [Predictors of Default](#predictors-of-default)

5. [Profitability Analysis](#profitability-analysis)
   - [Loan Product Profitability](#loan-product-profitability)
   - [Regional Performance](#regional-performance)

6. [Operational Efficiency](#operational-efficiency)
   - [Loan Processing Workflow](#loan-processing-workflow)
   - [Customer Satisfaction](#customer-satisfaction)

7. [Fraud Detection](#fraud-detection)
   - [Pattern Analysis](#pattern-analysis)
   - [Outlier Detection](#outlier-detection)

8. [Conclusion and Recommendations](#conclusion-and-recommendations)

9. [Future Work](#future-work)

10. [Acknowledgments](#acknowledgments)

11. [References](#references)

---

## Project Setup

### Requirements

List any packages, libraries, or software requirements needed to run the project.

### Installation

Provide instructions for setting up the project environment and installing dependencies.

## Data Overview

### Data Description

The `financial_loan.csv` dataset contains detailed information about loan applications processed by a financial institution. This dataset is used to analyze various aspects of loan performance, customer demographics, and risk management.

#### Number of Entries

The dataset consists of **38576 entries (rows)**. Each entry represents a unique loan application and contains various attributes related to the applicant and the loan itself.
![Data description](https://raw.githubusercontent.com/noe2019/Smart-Lending/main/images/desc.gif)


#### Features

The dataset includes the twenty four (24) features (columns):


| Column Name             | Description                                                                                   | Data Type         |
|-------------------------|-----------------------------------------------------------------------------------------------|-------------------|
| **id**                  | A unique identifier for each loan record.                                                     | String/Alphanumeric|
| **address_state**       | The U.S. state where the borrower resides.                                                    | Categorical       |
| **application_type**    | Indicates whether the application is individual or joint.                                     | Categorical       |
| **emp_length**          | The number of years the borrower has been employed at their current job.                      | Categorical/Numeric|
| **emp_title**           | The job title of the borrower.                                                                | Categorical       |
| **grade**               | The credit grade assigned to the borrower by the lender, reflecting creditworthiness.         | Categorical       |
| **home_ownership**      | The home ownership status of the borrower.                                                    | Categorical       |
| **issue_date**          | The date when the loan was issued.                                                            | DateTime          |
| **last_credit_pull_date** | The date of the most recent credit check performed on the borrower.                          | DateTime          |
| **last_payment_date**   | The date of the borrower's last loan payment.                                                 | DateTime          |
| **loan_status**         | The current status of the loan.                                                               | Categorical       |
| **next_payment_date**   | The scheduled date for the borrower's next loan payment.                                      | DateTime          |
| **member_id**           | A unique identifier for the borrower.                                                         | String/Alphanumeric|
| **purpose**             | The reason for which the loan is being taken out.                                             | Categorical       |
| **sub_grade**           | A finer classification of the borrower's credit grade, providing more granularity.            | Categorical       |
| **term**                | The length of time for the loan repayment period.                                             | Categorical       |
| **verification_status** | Indicates whether the borrower’s income or employment details have been verified.             | Categorical       |
| **annual_income**       | The annual income of the borrower at the time of the loan application.                        | Numeric (float)   |
| **dti**                 | Debt-to-Income ratio, a measure of the borrower’s monthly debt payments divided by their gross monthly income. | Numeric (float) |
| **installment**         | The fixed monthly payment amount for the loan.                                                | Numeric (float)   |
| **int_rate**            | The interest rate applied to the loan.                                                        | Numeric (float)   |
| **loan_amount**         | The total amount of money borrowed.                                                           | Numeric (float)   |
| **total_acc**           | The total number of credit accounts the borrower has.                                         | Numeric (integer) |
| **total_payment**       | The total amount paid by the borrower so far, including principal and interest.               | Numeric (float)   |

#### Background Information

The dataset is compiled from a comprehensive collection of loan applications submitted from **January 1, 2020, to December 31, 2023**. This period provides a comprehensive view of loan activity over four years, allowing for analysis of trends and patterns within this timeframe.

The primary goals of analyzing this dataset include:

1 - Identifying trends in loan applications and approvals.
2 - Understanding customer segments and their borrowing behavior.
3 - Evaluating risk factors associated with loan defaults.
4 - Optimizing loan products and improving customer satisfaction.

#### Data Source and Collection

The dataset was collected from the bank's internal systems, which record every loan application and its related details. The data is anonymized to protect customer privacy and complies with data protection regulations.

### Data Cleaning and Preprocessing
- Most columns have zero missing values except for emp_title', which has 1,438 missing entries. All missing values (NaN) in the `emp_title` column with the string `Unknown`.
![Handling missing data](https://raw.githubusercontent.com/noe2019/Smart-Lending/main/images/md.gif)
- Convert dat columns to datetime.
## Exploratory Data Analysis (EDA)

### Customer Demographics

## Top 10 and Bottom 10 States by Number of Borrowers

| Rank | Top 10 States      | Number of Borrowers | Bottom 10 States         | Number of Borrowers |
|------|--------------------|---------------------|--------------------------|---------------------|
| 1    | California         | 6,894               | Maine                    | 3                   |
| 2    | New York           | 3,701               | Iowa                     | 5                   |
| 3    | Florida            | 2,773               | Nebraska                 | 5                   |
| 4    | Texas              | 2,664               | Idaho                    | 6                   |
| 5    | New Jersey         | 1,822               | Indiana                  | 9                   |
| 6    | Illinois           | 1,486               | Tennessee                | 17                  |
| 7    | Pennsylvania       | 1,482               | Mississippi              | 19                  |
| 8    | Virginia           | 1,375               | Vermont                  | 54                  |
| 9    | Georgia            | 1,355               | South Dakota             | 63                  |
| 10   | Massachusetts      | 1,310               | Alaska                   | 78                  |

### Key Observations

1. **Geographic Diversity:** The top borrowing states span across various U.S. regions, indicating widespread economic activity and access to credit facilities, whereas the bottom borrowing states are predominantly less populous and economically smaller.
2. **Population Impact:** States with larger populations like California and New York dominate the top of the list, suggesting a direct correlation between population size and the number of borrowers.
3. **Economic Factors:** The bottom states generally feature fewer borrowers, which may be influenced by lower levels of economic activity or smaller financial markets.
4. **Variability in Borrowing:** There is a stark contrast in the number of borrowers between the top and bottom states, with California having more than 2,000 times the number of borrowers compared to Maine.
5. **Policy Implications:** This disparity could highlight areas needing targeted economic support or improved access to financial services to stimulate borrowing and economic growth.

### Loan Performance

Analyze the performance of different loan types and identify factors influencing loan success.

### Default Rates

Examine default rates across various segments and identify patterns related to defaults.

## Risk Assessment

### Credit Score Analysis

Assess the distribution of credit scores and their impact on loan approvals and defaults.

### Predictors of Default

Identify key predictors of loan default using statistical models or machine learning algorithms.

## Profitability Analysis

### Loan Product Profitability

Evaluate the profitability of different loan products and their contribution to overall revenue.

### Regional Performance

Analyze loan performance across different regions or branches to identify trends and opportunities.

## Operational Efficiency

### Loan Processing Workflow

Review the efficiency of the loan processing workflow and identify potential bottlenecks.

### Customer Satisfaction

Analyze customer feedback and satisfaction levels related to the loan process.

## Fraud Detection

### Pattern Analysis

Identify unusual patterns or activities that may indicate potential fraudulent behavior.

### Outlier Detection

Use statistical methods to detect outliers and assess their impact on the dataset.

## Conclusion and Recommendations

Summarize key findings from the analysis and propose actionable recommendations for the bank.

## Future Work

Outline potential areas for future analysis or further research that could build upon this work.

## Acknowledgments

Acknowledge any individuals, teams, or resources that contributed to the project.

## References

List any references or external resources used throughout the analysis.
