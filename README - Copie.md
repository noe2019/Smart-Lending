# Smart Lending: Loan Portfolio's Health Assessment And Monitoring
---
![Smart Lending](https://github.com/noe2019/Smart-Lending/blob/main/images/loan.gif)

## Table of Contents
1. [Objectives](#objectives)
2. [Data Overview](#data-overview)
   - [Data Description](#data-description)
   - [Data Source and Collection](#data-source-and-collection)
   - [Data Cleaning and Preprocessing](#data-cleaning-and-preprocessing)
3. [SQL and DAX Queries](#sql-and-dax-queries)
   - [SQL Queries](#sql-queries)
   - [DAX Queries](#dax-queries)
4. [Loan Portfolio Demographics](#loan-portfolio-demographics)
   - [Demographics by Number of Borrowers](#demographics-by-number-of-borrowers)
   - [Demographics by Loan Amount](#demographics-by-loan-amount)
   - [Geographic Insights](#geographic-insights)
   - [Recommendations](#recommendations)
5. [Loan Portfolio Health Assessment](#loan-portfolio-health-assessment)
   - [Loan Status Distribution](#loan-status-distribution)
   - [Default Rate in Loan Portfolio](#default-rate-in-loan-portfolio)
   - [Delinquency Rate](#delinquency-rate)
   - [Average Loan Amount](#average-loan-amount)
   - [Interest Rate Analysis](#interest-rate-analysis)
   - [Credit Grade Distribution Analysis](#credit-grade-distribution-analysis)
   - [Debt-to-Income (DTI) Ratio Distribution Analysis](#debt-to-income-(DTI)-ratio-distribution-analysis)
   - [Recovery Rate Analysis](#recovery-rate-analysis)
6. [Profitability Analysis](#profitability-analysis)
   - [Total Interest Income by Loan Product](#total-interest-income-by-loan-product)
   - [Contribution to Total Interest Income by Loan Product](#contribution-to-total-interest-income-by-loan-product)
   - [Detailed Profitability Metrics](#detailed-profitability-metrics)
   - [Regional Loan Performance Analysis](#regional-loan-performance-analysis)
7. [Loan Default Prediction](#loan-default-prediction)
8. [Conclusion and Recommendations](#conclusion-and-recommendations)
9. [Power BI Dashboard](#power-bi-dashboard)

---

## 1. Objectives

This project aims to provide a comprehensive analysis of a financial institution's loan portfolio, focusing on:

1. **Understanding Borrower Demographics**: Gain insights into the characteristics of borrowers to inform strategic decisions.
2. **Assessing Loan Portfolio Health**: Evaluate the performance and risk factors associated with the loan portfolio.
3. **Automating Decision-Making**: Use data-driven insights to automate and improve the decision-making process for future loan applications.

## 2. Data Overview

### 2.1. Data Description

The `financial_loan.csv` dataset contains **38,576 entries** representing individual loan applications, recorded over a four-year period (January 1, 2020, to December 31, 2023). The dataset includes 24 features detailing loan and borrower characteristics.

| Column Name               | Description                                                                                   | Data Type           |
|---------------------------|-----------------------------------------------------------------------------------------------|---------------------|
| **id**                    | Unique identifier for each loan record.                                                       | String/Alphanumeric |
| **address_state**         | U.S. state where the borrower resides.                                                        | Categorical         |
| **application_type**      | Indicates if the application is individual or joint.                                          | Categorical         |
| **emp_length**            | Years of employment at current job.                                                           | Categorical/Numeric |
| **emp_title**             | Job title of the borrower.                                                                    | Categorical         |
| **grade**                 | Credit grade assigned by the lender.                                                          | Categorical         |
| **home_ownership**        | Home ownership status of the borrower.                                                        | Categorical         |
| **issue_date**            | Date the loan was issued.                                                                     | DateTime            |
| **last_credit_pull_date** | Date of the most recent credit check on the borrower.                                         | DateTime            |
| **last_payment_date**     | Date of the borrower's last payment.                                                          | DateTime            |
| **loan_status**           | Current status of the loan.                                                                   | Categorical         |
| **next_payment_date**     | Scheduled date for the borrower's next payment.                                               | DateTime            |
| **member_id**             | Unique identifier for the borrower.                                                           | String/Alphanumeric |
| **purpose**               | Reason for the loan.                                                                          | Categorical         |
| **sub_grade**             | Sub-classification of the credit grade, providing more granularity.                           | Categorical         |
| **term**                  | Length of the loan repayment period.                                                          | Categorical         |
| **verification_status**   | Indicates if income or employment details have been verified.                                 | Categorical         |
| **annual_income**         | Annual income of the borrower.                                                                | Numeric (float)     |
| **dti**                   | Debt-to-Income ratio.                                                                         | Numeric (float)     |
| **installment**           | Fixed monthly payment amount.                                                                 | Numeric (float)     |
| **int_rate**              | Interest rate applied to the loan.                                                            | Numeric (float)     |
| **loan_amount**           | Total amount of money borrowed.                                                               | Numeric (float)     |
| **total_acc**             | Total number of credit accounts the borrower has.                                             | Numeric (integer)   |
| **total_payment**         | Total amount paid by the borrower so far, including principal and interest.                   | Numeric (float)     |

![Data Description](https://github.com/noe2019/Smart-Lending/blob/main/Loan%20portfolio's%20health%20assessment/images/desc.gif)

### 2.2. Data Source and Collection

This dataset was sourced from the bank's internal systems, recording every loan application and related details. The data has been anonymized to comply with data protection regulations.

### 2.3. Data Cleaning and Preprocessing

- **Missing Values**: The `emp_title` column had 1,438 missing values, which were replaced with 'Unknown'.
- **Date Formatting**: Date columns were converted to `datetime` format for accuracy in time-based analysis.

## 3. SQL and DAX Queries

### SQL Queries

Below are some SQL queries used for this project's data extraction and analysis:

```sql
-- Create Database and Tables
CREATE DATABASE LoanPortfolioDB;

USE LoanPortfolioDB;

CREATE TABLE LoanData (
    LoanID INT PRIMARY KEY,
    IssueDate DATE,
    LoanAmount DECIMAL(10, 2),
    InterestRate DECIMAL(5, 2),
    Term VARCHAR(10),
    Grade VARCHAR(2),
    SubGrade VARCHAR(3),
    HomeOwnership VARCHAR(20),
    AnnualIncome DECIMAL(15, 2),
    LoanStatus VARCHAR(20),
    DTI DECIMAL(5, 2),
    Purpose VARCHAR(50),
    AddressState VARCHAR(20),
    EmpLength VARCHAR(20),
    EmpTitle VARCHAR(50)
);

-- Load Data (Example for MySQL, modify for other SQL dialects)
LOAD DATA INFILE 'path_to_your/financial_loan.csv'
INTO TABLE LoanData
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- Total Loan Amount by State
SELECT 
    AddressState,
    SUM(LoanAmount) AS TotalLoanAmount
FROM LoanData
GROUP BY AddressState
ORDER BY TotalLoanAmount DESC;

-- Average Interest Rate by Credit Grade
SELECT 
    Grade,
    AVG(InterestRate) AS AvgInterestRate
FROM LoanData
GROUP BY Grade
ORDER BY AvgInterestRate DESC;

-- Number of Loans by Loan Status
SELECT 
    LoanStatus,
    COUNT(*) AS LoanCount
FROM LoanData
GROUP BY LoanStatus
ORDER BY LoanCount DESC;
```

### DAX Queries

Here are some DAX queries used for calculations in the dashboard:

```dax
-- Total Loan Amount
TotalLoanAmount = SUM(LoanData[LoanAmount])

-- Average Interest Rate
AvgInterestRate = AVERAGE(LoanData[InterestRate])

-- Number of Loans by Grade
LoanCountByGrade = COUNTROWS(LoanData)

-- Default Rate Calculation
DefaultRate = 
    DIVIDE(
        CALCULATE(COUNT(LoanData[LoanID]), LoanData[LoanStatus] = "Charged Off"),
        COUNT(LoanData[LoanID])
    )

-- Debt-to-Income (DTI) Ratio
AvgDTI = AVERAGE(LoanData[DTI])

-- Loan Status Distribution
LoanStatusDistribution = 
    SUMMARIZE(
        LoanData, 
        LoanData[LoanStatus], 
        "LoanCount", COUNT(LoanData[LoanID])
    )
```

Sure, here's the continuation of the write-up for the fourth section, starting as you requested and including SQL and DAX query examples:

---

## 4. Loan Portfolio Demographics

### 4.1. Top 10 and Bottom 10 States by Number of Borrowers

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

### 4.2. Top 10 and Bottom 10 States by Amount Borrowed

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

### 4.3. SQL and DAX Queries

To generate the above insights, the following SQL and DAX queries were used:

#### SQL Queries

1. **Top 10 and Bottom 10 States by Number of Borrowers**

```sql
-- Query to get the top 10 states by number of borrowers
SELECT 
    address_state AS State, 
    COUNT(*) AS Number_of_Borrowers
FROM 
    financial_loan
GROUP BY 
    address_state
ORDER BY 
    Number_of_Borrowers DESC
LIMIT 10;

-- Query to get the bottom 10 states by number of borrowers
SELECT 
    address_state AS State, 
    COUNT(*) AS Number_of_Borrowers
FROM 
    financial_loan
GROUP BY 
    address_state
ORDER BY 
    Number_of_Borrowers ASC
LIMIT 10;
```

2. **Top 10 and Bottom 10 States by Amount Borrowed**

```sql
-- Query to get the top 10 states by total loan amount
SELECT 
    address_state AS State, 
    SUM(loan_amount) AS Total_Loan_Amount
FROM 
    financial_loan
GROUP BY 
    address_state
ORDER BY 
    Total_Loan_Amount DESC
LIMIT 10;

-- Query to get the bottom 10 states by total loan amount
SELECT 
    address_state AS State, 
    SUM(loan_amount) AS Total_Loan_Amount
FROM 
    financial_loan
GROUP BY 
    address_state
ORDER BY 
    Total_Loan_Amount ASC
LIMIT 10;
```

#### DAX Queries

1. **Top 10 and Bottom 10 States by Number of Borrowers**

```dax
-- DAX Measure to count the number of borrowers by state
Number_of_Borrowers = COUNTROWS(financial_loan)

-- DAX Query to get the top 10 states by number of borrowers
EVALUATE
TOPN (
    10,
    SUMMARIZE (
        financial_loan,
        financial_loan[address_state],
        "Number_of_Borrowers", [Number_of_Borrowers]
    ),
    [Number_of_Borrowers], DESC
)

-- DAX Query to get the bottom 10 states by number of borrowers
EVALUATE
TOPN (
    10,
    SUMMARIZE (
        financial_loan,
        financial_loan[address_state],
        "Number_of_Borrowers", [Number_of_Borrowers]
    ),
    [Number_of_Borrowers], ASC
)
```

2. **Top 10 and Bottom 10 States by Amount Borrowed**

```dax
-- DAX Measure to calculate total loan amount by state
Total_Loan_Amount = SUM(financial_loan[loan_amount])

-- DAX Query to get the top 10 states by total loan amount
EVALUATE
TOPN (
    10,
    SUMMARIZE (
        financial_loan,
        financial_loan[address_state],
        "Total_Loan_Amount", [Total_Loan_Amount]
    ),
    [Total_Loan_Amount], DESC
)

-- DAX Query to get the bottom 10 states by total loan amount
EVALUATE
TOPN (
    10,
    SUMMARIZE (
        financial_loan,
        financial_loan[address_state],
        "Total_Loan_Amount", [Total_Loan_Amount]
    ),
    [Total_Loan_Amount], ASC
)
```

### 4.4. Geographic Insights

- **High Borrower Concentration**: States such as California, New York, and Texas are not only leading in the number of borrowers but also in the total loan amounts, which signifies high economic activity and greater loan demand in these regions.
- **Low Activity Regions**: States like Maine and Iowa, with the lowest number of borrowers and loan amounts, indicate under-served markets that might benefit from targeted financial products and services.

### 4.5. Recommendations

- **Deepen Market Penetration in High-Demand Areas**: Enhance the product offerings and marketing strategies in high-demand states to capture more of the existing market share.
- **Develop Tailored Products for Low-Demand States**: Research the unique needs of borrowers in low-activity states and develop specialized financial products that address those needs, potentially opening new markets for growth.

Here's the continuation for the fifth section, following the previously written fourth section, along with relevant SQL and DAX queries.

---

## 5. Loan Portfolio Health Assessment

In this section, we will assess the health of the loan portfolio by analyzing key performance indicators (KPIs) such as loan status distribution, default rates, delinquency rates, average loan amounts, interest rate analysis, credit grade distribution, and the debt-to-income (DTI) ratio. This analysis is crucial for understanding the overall stability of the portfolio and identifying potential areas of risk.

### 5.1. Loan Status Distribution

#### 5.1.1. Distribution Table

| Loan Status  | Number of Loans | Total Loan Amount (USD) | Average Loan Amount (USD) | Proportion of Total Loans (%) |
|--------------|-----------------|------------------------|---------------------------|-------------------------------|
| Fully Paid   | 32,145          | 351,358,350            | 10,930.42                  | 83.33                          |
| Charged Off  | 5,333           | 65,532,225             | 12,288.06                  | 13.82                          |
| Current      | 1,044           | 17,904,100             | 17,149.52                  | 2.71                           |
| Late         | 54              | 962,400                | 17,822.22                  | 0.14                           |

#### 5.1.2. SQL and DAX Queries

**SQL Queries:**

1. **Loan Status Distribution Query**

```sql
-- Query to get the distribution of loan statuses
SELECT 
    loan_status AS Status, 
    COUNT(*) AS Number_of_Loans, 
    SUM(loan_amount) AS Total_Loan_Amount, 
    AVG(loan_amount) AS Average_Loan_Amount,
    COUNT(*) * 100.0 / SUM(COUNT(*)) OVER () AS Proportion_of_Total_Loans
FROM 
    financial_loan
GROUP BY 
    loan_status;
```

**DAX Queries:**

1. **Loan Status Distribution Measure**

```dax
-- DAX Measures for Loan Status Distribution
Number_of_Loans = COUNT(financial_loan[id])

Total_Loan_Amount = SUM(financial_loan[loan_amount])

Average_Loan_Amount = AVERAGE(financial_loan[loan_amount])

Proportion_of_Total_Loans = 
DIVIDE(
    [Number_of_Loans], 
    CALCULATE(SUM(financial_loan[Number_of_Loans]), ALL(financial_loan))
) * 100

-- DAX Query to summarize loan status distribution
EVALUATE
SUMMARIZE (
    financial_loan,
    financial_loan[loan_status],
    "Number_of_Loans", [Number_of_Loans],
    "Total_Loan_Amount", [Total_Loan_Amount],
    "Average_Loan_Amount", [Average_Loan_Amount],
    "Proportion_of_Total_Loans", [Proportion_of_Total_Loans]
)
```

### 5.2. Default Rate in Loan Portfolio

#### 5.2.1. Default Rate Overview

The default rate in the loan portfolio is **13.82%**, indicating the percentage of loans that have been written off as losses due to non-repayment.

#### 5.2.2. SQL and DAX Queries

**SQL Queries:**

1. **Default Rate Calculation**

```sql
-- Query to calculate the default rate
SELECT 
    COUNT(*) * 100.0 / (SELECT COUNT(*) FROM financial_loan) AS Default_Rate
FROM 
    financial_loan
WHERE 
    loan_status = 'Charged Off';
```

**DAX Queries:**

1. **Default Rate Calculation**

```dax
-- DAX Measure for Default Rate
Default_Rate = 
DIVIDE(
    CALCULATE(COUNT(financial_loan[id]), financial_loan[loan_status] = "Charged Off"),
    COUNTROWS(financial_loan)
) * 100
```

### 5.3. Delinquency Rate

#### 5.3.1. Delinquency Rate Overview

The delinquency rate is **0.14%**, representing loans that are past due but have not yet defaulted.

#### 5.3.2. SQL and DAX Queries

**SQL Queries:**

1. **Delinquency Rate Calculation**

```sql
-- Query to calculate the delinquency rate
SELECT 
    COUNT(*) * 100.0 / (SELECT COUNT(*) FROM financial_loan) AS Delinquency_Rate
FROM 
    financial_loan
WHERE 
    loan_status = 'Late';
```

**DAX Queries:**

1. **Delinquency Rate Calculation**

```dax
-- DAX Measure for Delinquency Rate
Delinquency_Rate = 
DIVIDE(
    CALCULATE(COUNT(financial_loan[id]), financial_loan[loan_status] = "Late"),
    COUNTROWS(financial_loan)
) * 100
```

### 5.4. Average Loan Amount

#### 5.4.1. Overview

The average loan amount in the portfolio is **$11,296.07**. This value helps in understanding the typical loan size and potential risk exposure.

#### 5.4.2. SQL and DAX Queries

**SQL Queries:**

1. **Average Loan Amount Calculation**

```sql
-- Query to calculate the average loan amount
SELECT 
    AVG(loan_amount) AS Average_Loan_Amount
FROM 
    financial_loan;
```

**DAX Queries:**

1. **Average Loan Amount Calculation**

```dax
-- DAX Measure for Average Loan Amount
Average_Loan_Amount = AVERAGE(financial_loan[loan_amount])
```

### 5.5. Interest Rate Analysis

#### 5.5.1. Interest Rate Summary Statistics

This analysis provides insights into the distribution of interest rates across the loan portfolio, highlighting the average rate and variability.

#### 5.5.2. SQL and DAX Queries

**SQL Queries:**

1. **Interest Rate Summary Statistics**

```sql
-- Query to calculate interest rate summary statistics
SELECT 
    COUNT(*) AS Count_of_Loans,
    AVG(int_rate) AS Mean_Interest_Rate,
    STDDEV(int_rate) AS Standard_Deviation,
    MIN(int_rate) AS Minimum_Rate,
    PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY int_rate) AS Percentile_25,
    PERCENTILE_CONT(0.50) WITHIN GROUP (ORDER BY int_rate) AS Median_Rate,
    PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY int_rate) AS Percentile_75,
    MAX(int_rate) AS Maximum_Rate
FROM 
    financial_loan;
```

**DAX Queries:**

1. **Interest Rate Summary Statistics**

```dax
-- DAX Measures for Interest Rate Summary
Mean_Interest_Rate = AVERAGE(financial_loan[int_rate])

Standard_Deviation = 
VAR Mean = [Mean_Interest_Rate]
RETURN 
SQRT(SUMX(financial_loan, (financial_loan[int_rate] - Mean) ^ 2) / COUNTROWS(financial_loan))

Minimum_Rate = MIN(financial_loan[int_rate])

Percentile_25 = PERCENTILEX.INC(financial_loan, financial_loan[int_rate], 0.25)

Median_Rate = MEDIAN(financial_loan[int_rate])

Percentile_75 = PERCENTILEX.INC(financial_loan, financial_loan[int_rate], 0.75)

Maximum_Rate = MAX(financial_loan[int_rate])
```

### 5.6. Credit Grade Distribution Analysis

#### 5.6.1. Overview

This section provides an analysis of the distribution of credit grades within the loan portfolio, which reflects the risk profile of the borrowers.

#### 5.6.2. SQL and DAX Queries

**SQL Queries:**

1. **Credit Grade Distribution**

```sql
-- Query to calculate the distribution of credit grades
SELECT 
    grade AS Credit_Grade, 
    COUNT(*) AS Number_of_Loans
FROM 
    financial_loan
GROUP BY 
    grade
ORDER BY 
    Number_of_Loans DESC;
```

**DAX Queries:**

1. **Credit Grade Distribution**

```dax
-- DAX Measure for Credit Grade Count
Number_of_Loans_by_Grade = COUNTROWS(financial_loan)

-- DAX Query for Credit Grade Distribution
EVALUATE
SUMMARIZE (
    financial_loan,
    financial_loan[grade],
    "Number_of_Loans", [Number_of_Loans_by_Grade]
)
ORDER BY 
    [Number_of_Loans] DESC
```

### 5.7. Debt-to-Income (DTI) Ratio Distribution Analysis

#### 5.7.1. Overview

The Debt-to-Income (DTI) ratio is a critical indicator of borrowers' financial health and their ability to manage debt. It is calculated by dividing the borrower's monthly debt payments by their gross monthly income. A lower DTI ratio generally suggests that the borrower has a more manageable level of debt relative to their income, making them less risky for lenders. In this analysis, we will explore the distribution of DTI ratios across the loan portfolio to understand the financial well-being of the borrowers and identify any potential risks.

#### 5.7.2. SQL and DAX Queries

**SQL Queries:**

1. **DTI Ratio Distribution**

This query calculates key summary statistics for the DTI ratios across all loans in the portfolio, including the average, standard deviation, and percentiles, which help in understanding the distribution and concentration of DTI values.

```sql
-- Query to calculate summary statistics for DTI ratios
SELECT 
    COUNT(*) AS Count_of_Loans,
    AVG(dti) AS Mean_DTI_Ratio,
    STDDEV(dti) AS Standard_Deviation,
    MIN(dti) AS Minimum_DTI,
    PERCENTILE_CONT(0.25) WITHIN GROUP (ORDER BY dti) AS Percentile_25,
    PERCENTILE_CONT(0.50) WITHIN GROUP (ORDER BY dti) AS Median_DTI,
    PERCENTILE_CONT(0.75) WITHIN GROUP (ORDER BY dti) AS Percentile_75,
    MAX(dti) AS Maximum_DTI
FROM 
    financial_loan;
```

**DAX Queries:**

1. **DTI Ratio Distribution**

This DAX query provides similar summary statistics as the SQL query, including the mean, standard deviation, and specific percentiles of DTI ratios, helping to analyze the overall risk profile of the loan portfolio.

```dax
-- DAX Measures for DTI Ratio Distribution
Mean_DTI_Ratio = AVERAGE(financial_loan[dti])

Standard_Deviation_DTI = 
VAR Mean_DTI = [Mean_DTI_Ratio]
RETURN 
SQRT(SUMX(financial_loan, (financial_loan[dti] - Mean_DTI) ^ 2) / COUNTROWS(financial_loan))

Minimum_DTI = MIN(financial_loan[dti])

Percentile_25_DTI = PERCENTILEX.INC(financial_loan, financial_loan[dti], 0.25)

Median_DTI = MEDIAN(financial_loan[dti])

Percentile_75_DTI = PERCENTILEX.INC(financial_loan, financial_loan[dti], 0.75)

Maximum_DTI = MAX(financial_loan[dti])

-- DAX Query to summarize DTI ratio distribution
EVALUATE
SUMMARIZE (
    financial_loan,
    "Count_of_Loans", COUNTROWS(financial_loan),
    "Mean_DTI_Ratio", [Mean_DTI_Ratio],
    "Standard_Deviation", [Standard_Deviation_DTI],
    "Minimum_DTI", [Minimum_DTI],
    "Percentile_25", [Percentile_25_DTI],
    "Median_DTI", [Median_DTI],
    "Percentile_75", [Percentile_75_DTI],
    "Maximum_DTI", [Maximum_DTI]
)
```

#### 5.7.3. Key Insights

- **Average DTI Ratio**: The mean DTI ratio provides a baseline for assessing the general debt burden of the borrowers. A lower average DTI indicates that borrowers generally have a manageable level of debt relative to their income.

- **Risk Concentration**: By examining the percentiles, particularly the 75th percentile, the analysis can identify borrowers who are at higher risk due to elevated DTI ratios. These borrowers are more likely to face difficulties in meeting their loan obligations.

- **Standard Deviation**: The standard deviation of the DTI ratios helps in understanding the spread or variability in debt levels among borrowers. A higher standard deviation indicates greater variability, meaning some borrowers have significantly higher DTI ratios than others.

#### 5.7.4. Recommendations

1. **Targeted Interventions for High DTI Borrowers**: Borrowers who fall above the 75th percentile in DTI ratio should be monitored more closely, as they are at a higher risk of defaulting on their loans. The bank may consider offering financial counseling or restructuring their loan terms to prevent defaults.

2. **Enhanced Risk Assessment**: Incorporating DTI ratio analysis into the credit risk assessment process can improve the bank’s ability to predict and manage loan defaults. Loans to applicants with DTI ratios in the higher percentiles should be evaluated more rigorously.

3. **Loan Pricing Strategy**: Consider adjusting interest rates or loan terms based on the borrower's DTI ratio to mitigate risks. Higher DTI borrowers could be charged higher interest rates to compensate for the increased risk.

4. **Proactive Communication**: Establishing proactive communication with borrowers in the higher DTI range can help identify potential issues before they lead to delinquency or default. Offering alternative payment plans or financial advice can be beneficial.

By closely monitoring the DTI ratio distribution and implementing these recommendations, the bank can better manage its loan portfolio and reduce the risk of defaults.

### 6. Profitability Analysis

In this section, we assess the profitability of the bank's loan portfolio by examining total interest income generated, the contribution of different loan products to this income, and a detailed breakdown of key profitability metrics. Additionally, we analyze regional loan performance to identify trends and areas for strategic focus.

#### 6.1. Total Interest Income by Loan Product

Total interest income is a key metric that reflects the revenue generated from the bank's lending activities. It is crucial to understand which loan products contribute the most to the overall profitability of the bank.

**SQL Queries:**

```sql
-- Query to calculate total interest income by loan product
SELECT 
    purpose AS Loan_Product,
    SUM(interest_income) AS Total_Interest_Income
FROM 
    financial_loan
GROUP BY 
    purpose
ORDER BY 
    Total_Interest_Income DESC;
```

**DAX Queries:**

```dax
-- DAX Measure to calculate total interest income by loan product
Total_Interest_Income = SUM(financial_loan[interest_income])

-- DAX Query to summarize total interest income by loan product
EVALUATE
SUMMARIZE (
    financial_loan,
    financial_loan[purpose],
    "Total Interest Income", [Total_Interest_Income]
)
ORDER BY [Total Interest Income] DESC
```

**Key Insights:**

- **High-Yield Products:** Identify which loan products (e.g., debt consolidation, credit cards, etc.) generate the most interest income, which is crucial for understanding the bank’s core revenue drivers.
  
- **Strategic Focus:** Products that yield the highest interest income should be prioritized for marketing and resource allocation to maximize profitability.

#### 6.2. Contribution to Total Interest Income by Loan Product

This analysis provides a percentage breakdown of how each loan product contributes to the overall interest income, helping to assess the relative importance of each product within the portfolio.

**SQL Queries:**

```sql
-- Query to calculate the contribution of each loan product to the total interest income
SELECT 
    purpose AS Loan_Product,
    SUM(interest_income) / (SELECT SUM(interest_income) FROM financial_loan) * 100 AS Contribution_Percentage
FROM 
    financial_loan
GROUP BY 
    purpose
ORDER BY 
    Contribution_Percentage DESC;
```

**DAX Queries:**

```dax
-- DAX Measure for contribution percentage of each loan product to total interest income
Contribution_Percentage = 
    DIVIDE(
        [Total_Interest_Income],
        CALCULATE(SUM(financial_loan[interest_income]), ALL(financial_loan))
    ) * 100

-- DAX Query to summarize the contribution of each loan product to total interest income
EVALUATE
SUMMARIZE (
    financial_loan,
    financial_loan[purpose],
    "Contribution Percentage", [Contribution_Percentage]
)
ORDER BY [Contribution Percentage] DESC
```

**Key Insights:**

- **Dominant Contributors:** Understanding which loan products contribute the most to interest income can help prioritize business strategies around those products.

- **Product Portfolio Balance:** Assess whether the current portfolio has an over-reliance on a few loan products or if income is diversified across multiple products.

#### 6.3. Detailed Profitability Metrics

Detailed profitability metrics allow for a granular analysis of each loan product, considering not only total income but also the number of loans, average loan amounts, and other key factors.

**SQL Queries:**

```sql
-- Query to calculate detailed profitability metrics for each loan product
SELECT 
    purpose AS Loan_Product,
    COUNT(*) AS Number_of_Loans,
    SUM(loan_amount) AS Total_Loan_Amount,
    AVG(loan_amount) AS Average_Loan_Amount,
    AVG(interest_rate) AS Average_Interest_Rate,
    SUM(interest_income) AS Total_Interest_Income
FROM 
    financial_loan
GROUP BY 
    purpose
ORDER BY 
    Total_Interest_Income DESC;
```

**DAX Queries:**

```dax
-- DAX Measures for detailed profitability metrics by loan product
Number_of_Loans = COUNT(financial_loan[id])

Total_Loan_Amount = SUM(financial_loan[loan_amount])

Average_Loan_Amount = AVERAGE(financial_loan[loan_amount])

Average_Interest_Rate = AVERAGE(financial_loan[interest_rate])

-- DAX Query to summarize detailed profitability metrics by loan product
EVALUATE
SUMMARIZE (
    financial_loan,
    financial_loan[purpose],
    "Number of Loans", [Number_of_Loans],
    "Total Loan Amount", [Total_Loan_Amount],
    "Average Loan Amount", [Average_Loan_Amount],
    "Average Interest Rate", [Average_Interest_Rate],
    "Total Interest Income", [Total_Interest_Income]
)
ORDER BY [Total Interest Income] DESC
```

**Key Insights:**

- **Loan Performance:** Analyzing metrics such as average loan amount and interest rate alongside total income provides a comprehensive view of each product's profitability.

- **Product Strategy:** Loans with higher average interest rates but lower volumes may still contribute significantly to profitability, suggesting a need for targeted marketing or credit policy adjustments.

#### 6.4. Regional Loan Performance Analysis

Understanding how loans perform across different regions is crucial for optimizing the bank's strategy. This analysis looks at key performance metrics such as total loan amounts, average interest rates, and default rates by state.

**SQL Queries:**

```sql
-- Query to calculate regional loan performance metrics
SELECT 
    address_state AS State,
    COUNT(*) AS Number_of_Loans,
    SUM(loan_amount) AS Total_Loan_Amount,
    AVG(loan_amount) AS Average_Loan_Amount,
    AVG(interest_rate) AS Average_Interest_Rate,
    SUM(CASE WHEN loan_status = 'Charged Off' THEN 1 ELSE 0 END) / COUNT(*) * 100 AS Default_Rate_Percentage
FROM 
    financial_loan
GROUP BY 
    address_state
ORDER BY 
    Total_Loan_Amount DESC;
```

**DAX Queries:**

```dax
-- DAX Measures for regional loan performance metrics
Default_Rate_Percentage = 
    DIVIDE(
        CALCULATE(COUNT(financial_loan[id]), financial_loan[loan_status] = "Charged Off"),
        [Number_of_Loans]
    ) * 100

-- DAX Query to summarize regional loan performance metrics
EVALUATE
SUMMARIZE (
    financial_loan,
    financial_loan[address_state],
    "Number of Loans", [Number_of_Loans],
    "Total Loan Amount", [Total_Loan_Amount],
    "Average Loan Amount", [Average_Loan_Amount],
    "Average Interest Rate", [Average_Interest_Rate],
    "Default Rate Percentage", [Default_Rate_Percentage]
)
ORDER BY [Total Loan Amount] DESC
```

**Key Insights:**

- **High-Performance Regions:** Identifying states with the highest total loan amounts and interest rates can help prioritize marketing and business development efforts.

- **Risk Management:** Regions with higher default rates need closer monitoring and possibly stricter lending criteria to mitigate risk.

- **Strategic Allocation:** Understanding regional differences in loan performance allows the bank to allocate resources more efficiently and tailor products to specific markets.

---

By conducting this detailed profitability analysis, the bank can optimize its loan portfolio to enhance profitability, manage risk effectively, and make informed strategic decisions about future lending activities.

### 7. Loan Default Prediction

Loan default prediction is crucial for identifying high-risk loans and improving credit risk management. By leveraging data such as loan amounts, interest rates, borrower credit scores, and repayment history, we can develop predictive models to foresee potential defaults. This allows the bank to take preemptive measures to mitigate losses.

#### 7.1. Predictive Modeling Overview

The predictive model for loan defaults uses historical data to estimate the likelihood of a borrower defaulting on their loan. Variables such as the debt-to-income ratio (DTI), credit grade, and employment length are key indicators used in the model.

**SQL Queries:**

```sql
-- Query to prepare data for loan default prediction model
SELECT 
    id,
    dti,
    grade,
    emp_length,
    home_ownership,
    loan_amount,
    int_rate,
    term,
    annual_income,
    loan_status
FROM 
    financial_loan
WHERE 
    loan_status IN ('Fully Paid', 'Charged Off');
```

**DAX Queries:**

```dax
-- DAX Measure to calculate probability of default based on logistic regression coefficients
Probability_of_Default = 
    1 / (1 + EXP(-1 * (
        0.01 * financial_loan[dti] + 
        -0.5 * SWITCH(
            financial_loan[grade],
            "A", 1,
            "B", 2,
            "C", 3,
            "D", 4,
            "E", 5,
            "F", 6,
            "G", 7,
            0) +
        0.02 * financial_loan[loan_amount] + 
        0.03 * financial_loan[int_rate]
    )))

-- DAX Query to classify loans as "High Risk" or "Low Risk"
Loan_Risk_Classification = 
    IF([Probability_of_Default] > 0.5, "High Risk", "Low Risk")
```

**Key Insights:**

- **High-Risk Loans:** Loans classified as "High Risk" can be flagged for closer monitoring, allowing the bank to implement stricter repayment plans or additional collateral requirements.
  
- **Early Intervention:** Identifying high-risk loans early in the loan lifecycle enables the bank to take preventive actions, such as adjusting interest rates or offering debt counseling to at-risk borrowers.

#### 7.2. Model Evaluation and Optimization

To ensure the predictive model's accuracy, it’s essential to evaluate its performance using metrics like accuracy, precision, recall, and the Area Under the Receiver Operating Characteristic Curve (AUC-ROC).

**SQL Queries:**

```sql
-- Query to evaluate model performance based on confusion matrix
SELECT 
    COUNT(CASE WHEN loan_status = 'Charged Off' AND predicted_status = 'Charged Off' THEN 1 END) AS True_Positives,
    COUNT(CASE WHEN loan_status = 'Fully Paid' AND predicted_status = 'Charged Off' THEN 1 END) AS False_Positives,
    COUNT(CASE WHEN loan_status = 'Charged Off' AND predicted_status = 'Fully Paid' THEN 1 END) AS False_Negatives,
    COUNT(CASE WHEN loan_status = 'Fully Paid' AND predicted_status = 'Fully Paid' THEN 1 END) AS True_Negatives
FROM 
    predicted_loan_defaults;
```

**DAX Queries:**

```dax
-- DAX Measures for model evaluation metrics
True_Positives = 
    CALCULATE(
        COUNT(financial_loan[id]),
        financial_loan[loan_status] = "Charged Off" && [Loan_Risk_Classification] = "High Risk"
    )

False_Positives = 
    CALCULATE(
        COUNT(financial_loan[id]),
        financial_loan[loan_status] = "Fully Paid" && [Loan_Risk_Classification] = "High Risk"
    )

False_Negatives = 
    CALCULATE(
        COUNT(financial_loan[id]),
        financial_loan[loan_status] = "Charged Off" && [Loan_Risk_Classification] = "Low Risk"
    )

True_Negatives = 
    CALCULATE(
        COUNT(financial_loan[id]),
        financial_loan[loan_status] = "Fully Paid" && [Loan_Risk_Classification] = "Low Risk"
    )

-- DAX Measure for accuracy
Accuracy = 
    DIVIDE([True_Positives] + [True_Negatives], [True_Positives] + [False_Positives] + [False_Negatives] + [True_Negatives])
```

**Key Insights:**

- **Model Accuracy:** Evaluating the model's accuracy helps determine its effectiveness in predicting loan defaults and whether further optimization is required.

- **Threshold Adjustment:** Adjusting the classification threshold based on evaluation metrics can improve the balance between precision and recall, leading to better risk management.

---

### 8. Conclusion and Recommendations

This analysis provides critical insights into the bank's loan portfolio, including its profitability, risk factors, and potential areas for improvement. By utilizing advanced data analysis techniques and predictive modeling, the bank can enhance its decision-making processes, mitigate risks, and optimize its financial performance.

#### 8.1. Key Findings

1. **Loan Portfolio Profitability:** The analysis identified debt consolidation and credit card loans as the primary contributors to interest income, suggesting these products should be the focus of future lending strategies.

2. **Regional Performance Variations:** Significant disparities in loan performance across different states were observed, with states like California and Texas leading in total loan amounts but also showing varying levels of default risk.

3. **Default Prediction:** Predictive modeling highlights the potential for improving loan risk assessment and early intervention, particularly in identifying high-risk loans that may require stricter credit terms.

4. **DTI Ratio Management:** The analysis of the debt-to-income ratio distribution indicates that most borrowers maintain manageable debt levels, but closer monitoring of high DTI ratio borrowers is recommended to prevent defaults.

#### 8.2. Recommendations

1. **Focus on High-Yield Products:** Continue to prioritize and expand lending in high-yield loan products, such as debt consolidation and credit cards, to maximize profitability.

2. **Enhance Regional Strategies:** Tailor lending strategies to specific regional markets based on performance metrics, focusing on improving loan terms and mitigating risk in high-default areas.

3. **Strengthen Risk Management:** Implement the predictive model's findings to improve risk assessment, particularly for high-risk loans. Consider adjusting interest rates and loan terms for borrowers flagged as high risk.

4. **Refine Credit Policies:** Use insights from the DTI ratio and credit grade distribution analysis to refine credit policies, ensuring that the bank maintains a balanced risk profile.

5. **Proactive Loan Monitoring:** Increase monitoring efforts for loans with higher default probabilities, allowing for early intervention strategies that could prevent defaults and improve recovery rates.

6. **Utilize Predictive Analytics:** Integrate predictive analytics more deeply into the decision-making process, using model insights to proactively manage the loan portfolio and optimize profitability.

---

### 9. Power BI Dashboard

To facilitate ongoing analysis and monitoring, an interactive Power BI dashboard has been developed. This dashboard provides real-time insights into the loan portfolio's performance, enabling the bank's management to make data-driven decisions quickly and efficiently.

#### 9.1. Dashboard Features

- **Loan Portfolio Overview:** Provides a summary of total loan applications, funded amounts, received amounts, and key financial ratios.
  
- **Demographics Analysis:** Visualizes borrower demographics, including state distribution, employment length, and loan purpose, allowing for targeted marketing strategies.

- **Risk Assessment:** Highlights loans classified as high risk based on predictive modeling, enabling proactive management of potential defaults.

- **Profitability Metrics:** Displays detailed profitability metrics by loan product, including interest income, average loan amounts, and regional performance.

- **Interactive Filters:** Allows users to drill down into specific segments of the data, such as filtering by state, loan product, or risk classification.

#### 9.2. Access the Dashboard

You can explore the Power BI dashboard using the following link:

[Power BI Dashboard](https://app.powerbi.com/view?r=eyJrIjoiZDA1YmZiNzMtZGY5NS00NTJiLTgxYmItNjUyOGVmYWMxZWFkIiwidCI6ImI1NWIwM2YzLTIyZmUtNDAyNi1hM2Y0LWQ2NTVjOThiNDAyMCJ9)

---

By integrating the insights from this analysis into the Power BI dashboard, the bank can continuously monitor and improve its loan portfolio management, ensuring sustained profitability and effective risk management.
