# Smart Lending: Enhancing Financial Decisions with Data-Driven Insights


![Smart-Lending/images/](https://github.com/noe2019/Smart-Lending/blob/main/images/loan.gif)

## Introduction

This banking institution would like to assess two things: (1) Understand the demographics of its loan portfolio; (2) Assess its loan portfolio heatlh; (3) Automate the decision on future loan applications. By leveraging this dataset, the goal is to understand patterns and trends that impact the bank's loan portfolio, identify potential areas for improvement, and develop strategies to mitigate risks associated with loan defaults.

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

## Top 10 and Bottom 10 States by amount borrowed

| Rank | Top 10 States      | Total Loan Amount (in millions) | Bottom 10 States | Total Loan Amount (in thousands) |
|------|--------------------|---------------------------------|------------------|----------------------------------|
| 1    | California (CA)    | $78.48                          | Maine (ME)       | $9.20                             |
| 2    | New York (NY)      | $42.08                          | Nebraska (NE)    | $31.70                            |
| 3    | Texas (TX)         | $31.24                          | Iowa (IA)        | $56.45                            |
| 4    | Florida (FL)       | $30.05                          | Idaho (ID)       | $59.75                            |
| 5    | New Jersey (NJ)    | $21.66                          | Indiana (IN)     | $86.23                            |
| 6    | Illinois (IL)      | $17.12                          | Mississippi (MS) | $139.13                           |
| 7    | Virginia (VA)      | $15.98                          | Tennessee (TN)   | $162.18                           |
| 8    | Pennsylvania (PA)  | $15.83                          | Vermont (VT)     | $504.10                           |
| 9    | Georgia (GA)       | $15.48                          | South Dakota (SD)| $606.15                           |
| 10   | Massachusetts (MA) | $15.05                          | Montana (MT)     | $829.53                           |

### Key Insights

1. **Significant Disparities**: The loan amounts in the top states are orders of magnitude higher than those in the bottom states, highlighting economic disparities that mirror population and developmental differences across the regions.
2. **Economic Concentration**: The largest loan amounts are concentrated in states known as economic powerhouses with large populations, such as California and New York.
3. **Opportunities for Growth**: The lower loan amounts in states like Maine and Nebraska might indicate under-served markets or areas where economic growth can be stimulated through increased lending and financial services.
4. **Strategic Targeting**: Financial institutions may find strategic value in targeting under-served states with tailored financial products and services that cater to the unique needs of these regions.
5. **Policy Implications**: These insights could be critical for policymakers when considering measures to encourage economic equality and improve access to financial resources across all states.

### Loan Portfolio Health Assessment

Analyze the performance of different loan types and identify factors influencing loan success.

### Loan Status Distribution

## Loan Status Distribution Analysis

### Distribution Table

| Loan Status  | Number of Loans | Proportion of Total Loans |
|--------------|-----------------|---------------------------|
| Fully Paid   | 32,145          | 83.33%                    |
| Charged Off  | 5,333           | 13.82%                    |
| Current      | 1,098           | 2.85%                     |

### Graphical Representation

![Loan Status Distribution](https://github.com/noe2019/Smart-Lending/blob/main/images/loan_distribution.png)

Replace `URL_to_image_here` with the actual URL where your image is hosted.

### Key Insights

1. **Dominance of Fully Paid Loans**: The majority of the loans, constituting approximately 83.33% of the portfolio, are Fully Paid. This indicates a healthy loan portfolio with a high rate of successful repayments.
2. **Charged Off Loans**: About 13.82% of the loans are Charged Off, highlighting potential areas of credit risk within the portfolio. This proportion suggests that while most loans perform well, there is a notable fraction that results in losses.
3. **Current Loans**: A smaller fraction, 2.85%, represents the loans that are currently active. This low percentage of current loans could indicate a mature portfolio where most loans have already been resolved.
4. **Risk Management**: The proportion of Charged Off loans necessitates a review of risk assessment and credit management practices to reduce potential defaults.
5. **Portfolio Growth and Health**: The significant number of Fully Paid loans suggests overall portfolio health but emphasizes the need for ongoing monitoring and adjustment of credit policies to sustain these results and manage the Charged Off rate.

### Recommendations for Further Analysis

- **Enhanced Credit Scoring Models**: Improve prediction accuracy for potential charge-offs using more advanced credit scoring models.
- **Diversification Strategies**: Explore diversifying the types of loans offered to spread risk across different loan categories.
- **Proactive Loan Management**: Implement proactive loan management strategies to identify and mitigate risks early for loans categorized under 'Current'.

### Default Rate

- **Importance**: Calculate the percentage of loans that have defaulted, which is a critical indicator of credit risk within the portfolio.

### Delinquency Rate

- **Purpose**: Assess the proportion of loans that are overdue, indicating potential future defaults and trends in borrower behavior.

### Average Loan Amount

- **Analysis**: Analyze the average loan amount to understand the portfolio's exposure and potential profitability impacts.

### Interest Rate Analysis

- **Strategy Assessment**: Evaluate the distribution of interest rates across the portfolio to assess pricing strategy and risk-adjusted returns.

### Credit Score Distribution

- **Risk Profile**: Examine the distribution of credit scores to understand the risk profile of borrowers and anticipate potential default rates.

### Debt-to-Income (DTI) Ratio

- **Borrower Analysis**: Analyze the average DTI ratio to assess borrowers' ability to repay loans, which can indicate financial stress or stability within the portfolio.

### Recovery Rate

- **Recovery Efficiency**: Determine the percentage of the principal amount recovered from defaulted loans, which helps in assessing the effectiveness of recovery efforts.

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
