# Smart Lending: Loan Portfolio's Health Assessment And Monitoring
![Smart Lending](https://github.com/noe2019/Smart-Lending/blob/main/images/loan.gif)
## Table of Contents
1. [Objectives](#objectives)
2. [Data Overview](#data-overview)
   - [Data Description](#data-description)
   - [Data Source and Collection](#data-source-and-collection)
   - [Data Cleaning and Preprocessing](#data-cleaning-and-preprocessing)
3. [Loan portfolio demographics](#loan-portfolio-demographics)
   - [Demographics by Number of Borowers](#demographics-by-number-borowers)
   - [Demographics by Loan Amount](#demographics-by-loan-amount)
   - [Geographic Insights](#geographic-insights)
   - [Recommendations](#recommendations)
4. [Loan Portfolio Health Assessment](#loan-portfolio-health-assessment)
   - [Loan Status Distribution](#loan-status-distribution)
   - [Default Rate in Loan Portfolio](#default-rate-in-loan-portfolio)
   - [Delinquency Rate](#delinquency-rate)
   - [Average Loan Amount](#average-loan-amount)
   - [Interest Rate Analysis](#interest-rate-analysis)
   - [Credit Grade Distribution Analysis](#Credit-grade-distribution-analysis)
   - [Debt-to-Income (DTI) Ratio Distribution Analysis](#debt-to-income-(DTI)-ratio-distribution-analysis)
   - [Recovery Rate Analysis](#recovery-rate-analysis)
5. [Profitability Analysis](#profitability-analysis)
   - [Total Interest Income by Loan Product](#total-interest-income-by-loan-product)
   - [Contribution to Total Interest Income by Loan Product](#contribution-to-total-interest-income-by-loan-product)
   - [Detailed Profitability Metrics](#detailed-profitability-metrics)
   - [Regional Loan Performance Analysis](#regional-loan-performance-analysis)
6. [Automate the decision-making on future loan applications](#Automate-the-decision-making-on-future-loan-applications)
7. [Conclusion and Recommendations](#conclusion-and-recommendations)
8. [Power BI dashboard](#power-BI-dashboard)
---
## 1. Objectives

This banking institution aims to:
1. Understand the demographics of its loan portfolio.
2. Assess its loan portfolio health.
3. Automate the decision-making on future loan applications.

By leveraging this dataset, the goal is to understand patterns and trends that impact the bank's loan portfolio, identify potential areas for improvement, and develop strategies to mitigate risks associated with loan defaults.

## 2. Data Overview

#### 2.1. Data Description

The `financial_loan.csv` dataset contains **38,576 entries (rows)**, where each row represents a unique loan application. These entries detail various attributes associated with the loan applicant and the specifics of the loan itself.

Data collection spans from **January 1, 2020, to December 31, 2023**, providing a detailed look at loan activities over a four-year period. This extensive dataset enables the analysis of emerging trends and patterns, offering valuable insights into the dynamics of loan processing and borrower behavior over time.

The dataset includes twenty-four (24) features (columns, variables):

| Column Name               | Description                                                                                   | Data Type           |
|---------------------------|-----------------------------------------------------------------------------------------------|---------------------|
| **id**                    | A unique identifier for each loan record.                                                     | String/Alphanumeric |
| **address_state**         | The U.S. state where the borrower resides.                                                    | Categorical         |
| **application_type**      | Indicates whether the application is individual or joint.                                     | Categorical         |
| **emp_length**            | The number of years the borrower has been employed at their current job.                      | Categorical/Numeric |
| **emp_title**             | The job title of the borrower.                                                                | Categorical         |
| **grade**                 | The credit grade assigned to the borrower by the lender, reflecting creditworthiness.         | Categorical         |
| **home_ownership**        | The home ownership status of the borrower.                                                    | Categorical         |
| **issue_date**            | The date when the loan was issued.                                                            | DateTime            |
| **last_credit_pull_date** | The date of the most recent credit check performed on the borrower.                           | DateTime            |
| **last_payment_date**     | The date of the borrower's last loan payment.                                                 | DateTime            |
| **loan_status**           | The current status of the loan.                                                               | Categorical         |
| **next_payment_date**     | The scheduled date for the borrower's next loan payment.                                      | DateTime            |
| **member_id**             | A unique identifier for the borrower.                                                         | String/Alphanumeric |
| **purpose**               | The reason for which the loan is being taken out.                                             | Categorical         |
| **sub_grade**             | A finer classification of the borrower's credit grade, providing more granularity.            | Categorical         |
| **term**                  | The length of time for the loan repayment period.                                             | Categorical         |
| **verification_status**   | Indicates whether the borrower’s income or employment details have been verified.             | Categorical         |
| **annual_income**         | The annual income of the borrower at the time of the loan application.                        | Numeric (float)     |
| **dti**                   | Debt-to-Income ratio, a measure of the borrower’s monthly debt payments divided by their gross monthly income. | Numeric (float) |
| **installment**           | The fixed monthly payment amount for the loan.                                                | Numeric (float)     |
| **int_rate**              | The interest rate applied to the loan.                                                        | Numeric (float)     |
| **loan_amount**           | The total amount of money borrowed.                                                           | Numeric (float)     |
| **total_acc**             | The total number of credit accounts the borrower has.                                         | Numeric (integer)   |
| **total_payment**         | The total amount paid by the borrower so far, including principal and interest.               | Numeric (float)     |

![Data Description](https://raw.githubusercontent.com/noe2019/Smart-Lending/main/images/desc.gif)

#### 2.2. Data Source and Collection

The dataset was collected from the bank's internal systems, which record every loan application and its related details. The data is anonymized to protect customer privacy and complies with data protection regulations.

#### 2.3. Data Cleaning and Preprocessing

- Most columns have zero missing values except for `emp_title`, which has 1,438 missing entries. All missing values (NaN) in the `emp_title` column are replaced with the string `Unknown`.
- Date columns are converted to datetime format.

## 3. Loan portfolio demographics

#### 3.1. Top 10 and Bottom 10 States by Number of Borrowers

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

#### 3.2. Top 10 and Bottom 10 States by Amount Borrowed

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

#### 3.3. Geographic Insights

- **High Borrower Concentration**: States like California, New York, and Texas not only have the highest number of borrowers but also record the highest loan volumes, indicating robust economic activities and substantial market penetration.
- **Low Activity Regions**: States such as Maine and Iowa, which show minimal numbers of borrowers and loan amounts, may represent under-served markets with potential for targeted financial product offerings.

#### 3.4. Recommendations

- **Deepen Market Penetration in High-Demand Areas**: Enhance product offerings and marketing strategies in states with high borrower concentrations to capitalize on existing demand.
- **Develop Tailored Products for Low-Demand States**: Research and understand the unique needs of markets with fewer borrowers to offer more appealing product options, could help capture untapped markets. This can be done either by investing in their financial literacy or by reviewing the condition to loan access.

## 4. Loan Portfolio Health Assessment

Analyze the Key Performance Indicators (KPIs) of the loan portfolio, in order to see how the bank is doing.

#### 4.1. Loan Status Distribution
   ##### 4.1.1. Distribution Table
   
   | Loan Status  | Number of Loans | Total Loan Amount (USD) | Average Loan Amount (USD) | Proportion of Total Loans (%) |
   |--------------|-----------------|------------------------|---------------------------|-------------------------------|
   | Charged Off  | 5,333           | 65,532,225             | 12,288.06                  | 13.82                          |
   | Current      | 1,044           | 17,904,100             | 17,149.52                  | 2.71                           |
   | Fully Paid   | 32,145          | 351,358,350            | 10,930.42                  | 83.33                          |
   | Late         | 54              | 962,400                | 17,822.22                  | 0.14                           |

##### 4.1.2. Graphical Representation

![Loan Status Distribution](https://github.com/noe2019/Smart-Lending/blob/main/images/loan_distribution2.png)

##### 4.1.3. Key Insights

1. **Dominance of Fully Paid Loans**: 
   - **Proportion**: Fully Paid loans constitute the vast majority of the portfolio, accounting for 83.33% of all loans. This indicates strong portfolio health, with most borrowers successfully completing their repayments.
   - **Total Loan Amount**: The Fully Paid loans also represent the highest total loan amount, approximately $351 million, indicating that the bulk of the bank's capital has been successfully repaid.

2. **Charged Off Loans**: 
   - **Proportion**: Charged Off loans account for 13.82% of the portfolio, representing a significant portion of loans that have defaulted. This poses a notable risk to the portfolio's profitability.
   - **Total Loan Amount**: The total loan amount for Charged Off loans is over $65 million, indicating substantial losses due to defaults.

3. **Current and Late Loans**: 
   - **Current Loans**: Comprising 2.71% of the portfolio, these loans represent ongoing payments with a higher average loan amount, indicating a potential area for increased monitoring to ensure they do not default.
   - **Late Loans**: Although minimal in number (0.14%), the late loans have the highest average loan amount, suggesting that they could become a significant risk if they progress to default status.

##### 4.1.4. Recommendations

1. **Strengthen Monitoring and Collection Efforts for Charged Off and Late Loans**:
   - Focus on improving collection strategies to reduce the percentage of Charged Off loans.
   - Implement proactive measures for Late loans to prevent them from transitioning into Charged Off status.

2. **Enhanced Risk Management**:
   - Given that Current and Late loans have higher average loan amounts, it's crucial to apply rigorous risk assessment and offer financial counseling to borrowers to ensure these loans are successfully repaid.
   - The proportion of Late loans, while small, still represents a potential risk for further defaults and requires proactive management to prevent escalation to Charged Off status.

3. **Leverage Success of Fully Paid Loans**:
   - Analyze the factors contributing to the high proportion of Fully Paid loans and replicate these practices across other loan categories, especially those at higher risk of default.

4. **Targeted Financial Programs**:
   - Develop specialized financial products or services aimed at borrowers in the Late and Charged Off category to help them manage their finances better and potentially avoid default.

By implementing these strategies, the bank can improve its overall loan portfolio health, reduce defaults, and enhance profitability.

### 4.2. Default Rate in Loan Portfolio

##### 4.2.1. Default Rate Overview

The Default Rate in the loan portfolio currently stands at **13.82%**. This metric is important as it indicates the percentage of the total number of loans that have been written off as losses after the borrowers failed to repay.

##### 4.2.2. Key Insights

- **Risk Profile**: This rate is indicative of the risk level associated with the lending decisions. This rate may point to inadequacies in the credit risk assessment processes of the bank. Moreover, the higher average loan amount in the Charged Off category compared to the Fully Paid category suggests that larger loans are more likely to default, which may point to weaknesses in the credit risk assessment process, especially for higher-value loans.

##### 4.2.3. Recommendations

- **Enhanced Credit Scoring**: Improving the criteria and models used for assessing borrower creditworthiness could help in reducing the default rate.
- **Target High-Value Loans**: Since larger loans are more prone to default, it is crucial to refine credit risk assessment models specifically for high-value loans. This could involve incorporating more granular financial data, stress testing borrowers' ability to repay under adverse conditions, and requiring additional collateral for larger loans.
- **Risk-Based Pricing**: Adjusting interest rates based on the calculated risk of loan defaults can offset potential losses and manage the risk-return profile more effectively.
- **Collection Efforts**: Strengthening the collection process and follow-up on late payments can prevent loans from progressing to default status.

### 4.3. Delinquency Rate

The Delinquency Rate in the loan portfolio currently stands at **0.14%**. This metric represents the percentage of loans that are past due but have not yet reached default status.

##### 4.3.1. Key Insights

- **Early Warning Indicator**: While relatively low, the Delinquency Rate serves as an early warning for loans that might eventually default, allowing for proactive management.
- **Portfolio Health**: A low delinquency rate generally indicates good health of the loan portfolio and effective loan servicing practices.

##### 4.3.2. Recommendations

- **Proactive Loan Servicing**: Implementing early intervention strategies to address late payments before they escalate.
- **Financial Education**: Offering financial education and counseling to borrowers at risk of delinquency.
- **Flexible Repayment Options**: Providing flexible repayment plans for borrowers showing early signs of financial stress.

### 4.4. Average Loan Amount

The average loan amount within our portfolio stands at **$11,296.07**. This figure is crucial for understanding the typical financial commitment undertaken by borrowers and the potential risk exposure for the lender.

##### 4.4.1. Key Insights

- **Portfolio Exposure**: The average loan amount reflects the level of exposure that the loan portfolio has. Larger average loan sizes might indicate higher individual risk per loan, impacting the overall risk profile of the portfolio.
- **Profitability Potential**: This amount also affects potential profitability. Higher loan amounts can lead to increased interest revenue but also carry greater risk of significant losses if defaults occur.

##### 4.4.2. Recommendations

- **Risk Diversification**: To manage exposure, diversifying the types of loans offered can help spread out risk, particularly if larger loans are a significant portion of the portfolio.
- **Loan Pricing Strategy**: Adjusting the pricing strategy to account for the risk associated with larger average loans can optimize profitability while managing risk effectively.
- **Credit Assessment Strengthening**: Enhancing credit assessment processes to ensure that loans are issued to borrowers with the capability and intention to repay, especially for larger loan amounts.
- 
### 4.5. Interest Rate Analysis
##### 4.5.1. Interest Rate Summary Statistics

![Interest Rate Distribution](https://github.com/noe2019/Smart-Lending/blob/main/images/dist_IR.png)

This section presents a detailed summary of the interest rates across our loan portfolio. The following table summarizes key statistical measures:

##### 4.5.2. Summary Statistics Table

| Statistical Measure | Value  | Description                                  |
|---------------------|--------|----------------------------------------------|
| Count of Loans      | 38,576 | Total number of loans in the portfolio       |
| Mean Interest Rate  | 12.05% | Average interest rate across all loans       |
| Standard Deviation  | 3.72%  | Variation in interest rate from the average  |
| Minimum Rate        | 5.42%  | Lowest interest rate in the portfolio        |
| 25th Percentile     | 9.32%  | 25% of loans have interest rates below this  |
| Median Rate         | 11.86% | Middle value of interest rates               |
| 75th Percentile     | 14.59% | 75% of loans have interest rates below this  |
| Maximum Rate        | 24.59% | Highest interest rate in the portfolio       |

##### 4.5.3. Key Insights

- **Distribution Overview**: The distribution is moderately spread around the mean, indicating variability in the risk profiles of borrowers.
- **Risk Indicators**: The range from the minimum to the maximum interest rate highlights the diverse creditworthiness among borrowers.
- **Loan Pricing**: The quartile values suggest a tiered pricing strategy that aligns interest rates with assessed credit risk.

##### 4.5.4. Recommendations

- **Loan Approval Criteria**: The variation in rates calls for robust loan approval criteria that consider borrower risk more effectively.
- **Interest Rate Strategy**: Adjusting the interest rate strategy may help manage risk more efficiently and align with market competition.
- **Portfolio Management**: Continuous monitoring of the interest rate distribution is essential for maintaining a healthy balance between risk and return.

### 4.6. Credit Grade Distribution Analysis

##### 4.6.1. Overview

The distribution of credit grades across our loan portfolio is visualized in the histogram below. This analysis is crucial for understanding the risk profile of our borrowers based on their assigned credit grades from A to G.

![Credit Grade Distribution](https://github.com/noe2019/Smart-Lending/blob/main/images/dist_CC.png)

##### 4.6.2. Credit Grade Counts

This table shows the exact count of loans per credit grade, reflecting the creditworthiness of our borrowers:

| Credit Grade | Number of Loans |
|--------------|-----------------|
| A            | 9,689           |
| B            | 11,674          |
| C            | 7,904           |
| D            | 5,182           |
| E            | 2,786           |
| F            | 1,028           |
| G            | 313             |

##### 4.6.3. Key Insights

- **Dominant Grades**: Grades B and A are the most prevalent in the portfolio, indicating a substantial number of borrowers with good to excellent creditworthiness.
- **Risk Distribution**: The number of loans decreases as the credit grade worsens from B to G, which is typical as fewer borrowers qualify for loans as risk increases.
- **High-Risk Loans**: Loans in grades D through G represent higher risk but are less frequent, which helps mitigate overall portfolio risk.

##### 4.6.4. Recommendations

- **Portfolio Diversification**: The spread across various credit grades suggests a diversified risk profile, with a concentration in the mid to high credit quality.
- **Loan Pricing Strategy**: Higher-risk grades (D, E, F, G) likely carry higher interest rates to compensate for the increased risk, impacting the portfolio’s yield.
- **Credit Risk Management**: The lower frequency of lower-graded loans (E, F, G) indicates a cautious approach to high-risk lending, essential for maintaining portfolio health.

## 4.7. Debt-to-Income (DTI) Ratio Distribution Analysis

##### 4.7.1. Overview

The distribution of Debt-to-Income (DTI) ratios across our loan portfolio is visualized in the histogram below. This analysis helps us evaluate the financial health and repayment capacity of our borrowers.

![Debt-to-Income Ratio Distribution](https://github.com/noe2019/Smart-Lending/blob/main/images/dist_TDI.png)

##### 4.7.2. DTI Ratio Statistics

- **Average DTI Ratio**: 13%
- **Distribution Characteristics**: The histogram peaks around the DTI ratio of 0.13, indicating that the average borrower has a debt load that is 13% of their income.

##### 4.7.3. Key Insights

- **Credit Risk**: The bulk of our loan portfolio has a DTI ratio centered around 13%, which is generally considered manageable in consumer lending. This central clustering suggests that most borrowers are not excessively burdened by debt.
- **Financial Health**: The DTI ratios predominantly range between 5% and 25%, with fewer borrowers at the higher end of the spectrum. This spread indicates a relatively healthy financial status among the majority of our borrowers, where their income levels are sufficient to manage the debt they have incurred.
- **Risk Concentration**: The tail on the right side of the distribution, extending towards a DTI ratio of 30%, highlights a smaller segment of borrowers with higher debt loads relative to their income. These individuals represent a higher risk as they may face difficulties in meeting their loan obligations, especially under financially stressful conditions.

##### 4.7.4. Recommendations

- **Lending Strategies**: Consideration may be given to tightening credit approval criteria or adjusting loan terms for applicants with higher DTI ratios to mitigate potential defaults.
- **Risk Management**: Continuous monitoring of DTI ratios is essential, particularly focusing on trends that may shift more borrowers towards higher DTI categories.
- **Financial Education**: Offering financial advice or planning tools to borrowers, especially those in higher DTI brackets, could improve their debt management and prevent defaults.

## 4.8. Recovery Rate Analysis

##### 4.8.1. Overview

The Recovery Rate of our loan portfolio is currently at **56.90%**. This metric indicates the percentage of the principal amount that has been recovered from loans that defaulted.

##### 4.8.2. Key Insights

- **Financial Recovery**: A Recovery Rate of 56.90% means that for every dollar lost to defaults, we are able to recover approximately 56.9 cents. This rate is crucial for assessing the effectiveness of our collections and loss mitigation strategies.
- **Portfolio Resilience**: This rate reflects the resilience of the portfolio against credit losses, providing insights into the overall risk management effectiveness.

##### 4.8.3. Recommendations

- **Credit Loss Mitigation**: While recovering over half of the defaulted amounts is positive, there is room to enhance recovery strategies to further minimize losses.
- **Risk Management**: The Recovery Rate directly impacts the portfolio's profitability and long-term sustainability. It is essential to continuously develop and refine recovery processes to improve this rate.
- **Strategic Financial Planning**: Understanding the Recovery Rate helps in making informed decisions about loan provisioning, pricing strategies, and risk assessment practices.

- **Enhanced Collection Efforts**: Implementing more aggressive or innovative collection strategies could improve the Recovery Rate.
- **Legal and Negotiation Tactics**: Utilizing legal avenues more effectively and negotiating settlement options might increase the amount recovered from defaulted loans.
- **Data-Driven Recovery Actions**: Analyzing patterns and characteristics of previously defaulted loans that had higher recovery rates to replicate successful recovery strategies across the portfolio.

## 5. Analysis of Loan Products Profitability

#### 5.1. Total Interest Income by Loan Product

The following graph illustrates the total interest income generated from various loan products in our portfolio:

![Total Interest Income by Loan Product](https://github.com/noe2019/Smart-Lending/blob/main/images/dist_IINC.png)

#### 5.2. Contribution to Total Interest Income by Loan Product

The next graph shows the contribution of each loan product to the total interest income, highlighting the relative importance of each product category:

![Contribution to Total Interest Income by Loan Product](https://github.com/noe2019/Smart-Lending/blob/main/images/dist_IINC_PERCENTAGE.png)

#### 5.3. Detailed Profitability Metrics

Here is a breakdown of key profitability metrics for each loan product based on the total loan amount, interest paid, and the number of loans:

| Loan Product        | Loan Amount  | Interest Paid | Number of Loans | Average Interest Rate | Interest Income Contribution (%) |
|---------------------|--------------|---------------|-----------------|-----------------------|----------------------------------|
| Debt Consolidation  | $232,459,675 | $39,604,336   | 18,214          | 12.50%                | 55.48%                           |
| Credit Card         | $58,885,175  | $9,728,876    | 4,998           | 11.73%                | 13.63%                           |
| Home Improvement    | $33,350,775  | $5,413,699    | 2,876           | 11.40%                | 7.58%                            |
| Other               | $31,155,750  | $4,803,155    | 3,824           | 11.86%                | 6.73%                            |
| Small Business      | $24,123,100  | $3,418,171    | 1,776           | 13.03%                | 4.79%                            |
| Major Purchase      | $17,251,600  | $2,522,429    | 2,110           | 10.87%                | 3.53%                            |
| Car                 | $10,223,575  | $1,578,950    | 1,497           | 10.59%                | 2.21%                            |
| Wedding             | $9,225,800   | $1,526,340    | 928             | 11.89%                | 2.14%                            |
| Medical             | $5,533,225   | $821,948      | 667             | 11.57%                | 1.15%                            |
| House               | $4,824,925   | $721,812      | 366             | 12.38%                | 1.01%                            |
| Moving              | $3,748,125   | $567,595      | 559             | 11.59%                | 0.80%                            |
| Educational         | $2,161,650   | $276,156      | 315             | 11.65%                | 0.39%                            |
| Vacation            | $1,967,950   | $275,164      | 352             | 10.88%                | 0.39%                            |
| Renewable Energy    | $845,750     | $123,677      | 94              | 11.50%                | 0.17%                            |


- **High Contribution Products**: Debt consolidation loans are the most significant contributor to interest income, accounting for over half of the total interest revenue, indicating their centrality to our lending business.
- **Risk vs. Reward**: Products like small business loans show higher average interest rates, reflecting their higher risk but also their potential for higher returns.
- **Niche Products**: Renewable energy and vacation loans represent niche markets with lower total loan amounts and contributions but may cater to specific customer segments.

#### 5.4. Regional Loan Performance Analysis

##### 5.4.1. Overview

The following analysis provides a comprehensive breakdown of loan performance across different states, focusing on total loan amounts, average loan amounts, average interest rates, the number of loans, and default rates. This data helps us identify regional trends and assess where strategic interventions or opportunities may exist.

##### 5.4.2. Regional Performance Metrics

Here's a table summarizing key loan performance metrics by state:

| State | Total Loan Amount | Average Loan Amount | Average Interest Rate | Number of Loans | Default Rate (%) |
|-------|-------------------|---------------------|-----------------------|-----------------|------------------|
| CA    | $78,484,125       | $11,384             | 12.15%                | 6,894           | 15.43            |
| NY    | $42,077,050       | $11,369             | 12.11%                | 3,701           | 12.81            |
| TX    | $31,236,650       | $11,725             | 12.05%                | 2,664           | 11.37            |
| FL    | $30,046,125       | $10,835             | 11.98%                | 2,773           | 17.49            |
| NJ    | $21,657,475       | $11,887             | 12.24%                | 1,822           | 15.20            |
| IL    | $17,124,225       | $11,524             | 12.05%                | 1,486           | 13.12            |
| VA    | $15,982,650       | $11,624             | 12.22%                | 1,375           | 12.44            |
| PA    | $15,826,525       | $10,679             | 11.69%                | 1,482           | 11.54            |
| GA    | $15,480,325       | $11,425             | 11.96%                | 1,355           | 15.35            |
| MA    | $15,051,000       | $11,489             | 11.87%                | 1,310           | 11.68            |
| ...   | ...               | ...                 | ...                   | ...             | ...              |

##### 5.4.3. Key Insights

- **High Default Rates in Specific Regions**: Florida (17.49%) and Georgia (15.35%) show higher default rates compared to other states, suggesting potential risk factors or economic conditions that may warrant closer analysis and targeted risk management strategies.
- **High Loan Demand Regions**: California, New York, and Texas lead in total loan amounts and number of loans, indicating significant market activity and potential for further growth or increased financial product offerings.
- **Interest Rate Variability**: States like California and New Jersey have higher average interest rates, reflecting potentially higher risk pricing strategies or different customer credit profiles.

##### 5.4.4. Recommendations

- **Risk Mitigation Initiatives**: In regions with high default rates, consider introducing more rigorous credit screening processes or risk-adjusted pricing models to mitigate potential losses.
- **Marketing and Product Expansion**: In states with high loan volumes and robust performance, explore opportunities for expanding product offerings or marketing efforts to capitalize on strong demand.
- **Customized Financial Solutions**: Tailor financial products to meet the specific needs of regions with unique performance characteristics to enhance customer satisfaction and profitability.

## 6. Automating loan application decisions

## 7. Conclusion and Recommendations

#### 7.1. Key Findings

1. **Regional Disparities in Loan Performance**: The data shows significant variation in loan performance across different states, with states like California, New York, and Texas showing higher loan activity and amounts. This contrasts sharply with states like Maine and Nebraska, which have much lower figures.

2. **Loan Status Insights**: The majority of loans (83.33%) are Fully Paid, showcasing strong portfolio performance. However, a concerning 13.82% Charged Off rate suggests notable default risks impacting overall profitability.

3. **Credit Grade Distribution**: Most loans are issued to borrowers with high credit grades (A and B), indicating a low-risk borrower base. However, the presence of lower grades (D through G) within the portfolio shows controlled acceptance of higher-risk borrowers.

4. **Interest Rate Analysis**: The average interest rate across the portfolio is 12.05%, with variability suggesting diverse borrower risk profiles. Higher rates in specific regions may reflect higher default risks or targeted financial products.

5. **Debt-to-Income Ratio**: Most borrowers have DTI ratios around 13%, suggesting manageable debt levels which is positive for loan servicing capabilities.

6. **Recovery Rate**: The 56.90% Recovery Rate points to moderate success in recouping losses from defaulted loans, indicating potential areas for improvement in collection strategies.

#### 6.2. Recommendations

1. **Enhance Risk Management in High Default Regions**: States like Florida and Georgia with high default rates should see targeted enhancements in risk assessments. Implement stricter credit evaluations and adapt lending criteria based on regional economic trends.

2. **Expand Financial Products in High Activity States**: Leverage the high loan demand in states like California, New York, and Texas by introducing a wider range of financial products tailored to meet diverse demographic needs.

3. **Optimize Interest Rate Strategies**: Regularly review and adjust interest rates to balance risk and competitiveness. Consider implementing dynamic pricing models that reflect real-time credit assessments and regional economic conditions.

4. **Improve Recovery Efforts**: Develop more aggressive and innovative strategies for loan recovery to boost the Recovery Rate. Utilize advanced analytics to identify successful recovery patterns and apply these insights across the portfolio.

5. **Financial Education and Support Programs**: Implement education programs aimed at improving financial health, especially in regions with high DTI ratios or increasing delinquency rates. This could help improve borrowers' financial management skills, reducing the likelihood of defaults.

6. **Monitor and Adapt to Credit Grade Shifts**: Continuously monitor the credit grade distribution within the portfolio. Adjust lending practices as necessary to ensure a balanced risk profile, promoting loans to lower-risk grades while managing the terms and proportion of loans to higher-risk categories.

## 8. Power BI dashboard 

Check out the interactive Power BI dashboard [here](https://app.powerbi.com/view?r=eyJrIjoiZDA1YmZiNzMtZGY5NS00NTJiLTgxYmItNjUyOGVmYWMxZWFkIiwidCI6ImI1NWIwM2YzLTIyZmUtNDAyNi1hM2Y0LWQ2NTVjOThiNDAyMCJ9), to easily access and monitoring of the portfolio KPIs

---
