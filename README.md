# Bank Loan Portfolio Analysis and Reporting
---

### Table of Contents

1. [Objective](#objective)
2. [Data Source and Tools](#data-source-and-tools)
   - 2.1 [Data Sources](#data-sources)
   - 2.2 [Data Access](#data-access)
   - 2.3 [Tools and Technologies](#tools-and-technologies)
3. [Data Analysis Process](#data-analysis-process)
   - 3.1 [Data Collection](#data-collection)
   - 3.2 [Data Cleaning and Preprocessing](#data-cleaning-and-preprocessing)
   - 3.3 [Data Analysis](#data-analysis)
   - 3.4 [Visualization with Power BI](#visualization-with-power-bi)
   - 3.5 [Testing and Validation](#testing-and-validation)
4. [Reproducibility: SQL and DAX Queries](#reproducibility-sql-and-dax-queries)
   - 4.1 [Summary Dashboard](#summary-dashboard)
     - [SQL Query: Loan Summary Data](#sql-query-loan-summary-data)
     - [DAX Measures for Summary Dashboard](#dax-measures-for-summary-dashboard)
   - 4.2 [Overview Dashboard](#overview-dashboard)
     - [SQL Query: Loan Applications Trends](#sql-query-loan-applications-trends)
     - [DAX Measures for Overview Dashboard](#dax-measures-for-overview-dashboard)
   - 4.3 [Details Dashboard](#details-dashboard)
     - [SQL Query: Detailed Loan Information](#sql-query-detailed-loan-information)
     - [DAX Measures for Details Dashboard](#dax-measures-for-details-dashboard)
5. [Key Findings](#key-findings)
   - 5.1 [Loan Portfolio Performance](#loan-portfolio-performance)
   - 5.2 [Risk Assessment](#risk-assessment)
   - 5.3 [Profitability Analysis](#profitability-analysis)
6. [Recommendations](#recommendations)
   - 6.1 [Focus on High-Yield Products](#focus-on-high-yield-products)
   - 6.2 [Targeted Marketing and Regional Strategy](#targeted-marketing-and-regional-strategy)
   - 6.3 [Enhanced Risk Management](#enhanced-risk-management)
   - 6.4 [Optimize Loan Terms](#optimize-loan-terms)
   - 6.5 [Proactive Loan Monitoring](#proactive-loan-monitoring)
   - 6.6 [Continuous Data Analysis and Improvement](#continuous-data-analysis-and-improvement)

## I. Objective

This project aims to provide a comprehensive analysis of a financial institution's loan portfolio with the following key objectives:

1. **Understand Borrower Demographics**: Analyze borrower characteristics, such as geographic distribution, employment details, and loan purposes, to inform strategic decisions.
2. **Assess Loan Portfolio Health**: Evaluate key performance metrics, including loan application volumes, funded amounts, received amounts, and default rates, to identify trends and assess risk.
3. **Automate Decision-Making**: Use predictive modeling to identify borrowers likely to default, enabling proactive risk management and optimized loan approval processes.

## II. Data Source and Tools

### Data Sources
- **Loan Application Data**: Information on loan applications, including purpose, funded amount, and status.
- **Employee Data**: Details about employee tenure and roles, relevant to analyzing loan performance.
- **Customer Data**: Demographic information, such as state of residence, home ownership, and employment length.

### Data Access
The dataset used in this project is available for download [here](https://drive.google.com/file/d/14cXN6kCDDoGRHg1keDzOSoECoKCEUQEH/view?usp=sharing).

### Tools and Technologies
- **Power BI**: For creating interactive dashboards to visualize insights.
- **SQL Server**: For efficient querying and management of datasets.
- **Excel**: For initial data management and preprocessing tasks.
- **DAX (Data Analysis Expressions)**: Used within Power BI to create measures and calculated columns for analysis.

## III. Data Analysis Process

### 1. Data Collection
The data was sourced from the bank's internal systems, focusing on a dataset containing 38,576 loan applications recorded over four years (January 1, 2020, to December 31, 2023). The dataset includes 24 features detailing loan and borrower characteristics, such as loan amount, interest rate, loan status, and borrower demographics.

### 2. Data Cleaning and Preprocessing
- **Missing Values**: Addressed missing values, particularly in the `emp_title` column, by imputing or replacing with 'Unknown'.
- **Date Formatting**: Standardized date columns (`issue_date`, `last_payment_date`, etc.) to `datetime` format for accurate time-based analysis.
- **Data Transformation**: Structured and standardized the data using SQL and DAX to prepare for detailed analysis and visualization.

### 3. Data Analysis
SQL and DAX queries were used to identify trends and calculate key metrics across the loan portfolio, including:
- **Loan Applications**: Analyzed by month, state, employee tenure, and loan purpose.
- **Funded and Received Amounts**: Aggregated to assess financial flows.
- **Default and Delinquency Rates**: Calculated to evaluate the risk profile.

### 4. Visualization with Power BI
Power BI dashboards were created to provide stakeholders with clear, actionable insights, including:
- **Loan Applications by Month**: Visualizing application trends over time.
- **Applications by State**: Geographic distribution of loans.
- **Loan Purpose Distribution**: Understanding the reasons behind loan applications.
- **Loan Status Distribution**: Breakdown of loans by status, including fully paid and charged-off loans.
- **Risk Analysis**: Identifying potential risks through default and delinquency rates.

### 5. Testing and Validation
All data and visualizations were rigorously tested for accuracy. This included cross-verifying calculations with raw data and ensuring correct functionality of interactive features like slicers and filters in Power BI.

## IV. Reproducibility: SQL and DAX Queries

To ensure the dashboards are reproducible, below are the SQL and DAX queries used for each section:

### 1. **Summary Dashboard**

#### **SQL Query: Loan Summary Data**
This query aggregates data on total loan applications, funded amounts, received amounts, and calculates percentages for Good vs. Bad Loans Issued.

```sql
-- Total Loan Applications, Funded Amount, Received Amount, Good vs. Bad Loans
SELECT 
    COUNT(*) AS TotalLoanApplications,
    SUM(LoanAmount) AS TotalFundedAmount,
    SUM(ReceivedAmount) AS TotalAmountReceived,
    SUM(CASE WHEN LoanStatus = 'Fully Paid' THEN 1 ELSE 0 END) * 100.0 / COUNT(*) AS GoodLoanIssuedPercentage,
    SUM(CASE WHEN LoanStatus = 'Charged Off' THEN 1 ELSE 0 END) * 100.0 / COUNT(*) AS BadLoanIssuedPercentage,
    AVG(InterestRate) AS AvgInterestRate,
    AVG(DTI) AS AvgDTI
FROM 
    LoanData;
```

#### **DAX Measures for Summary Dashboard**
These DAX measures display the key performance indicators (KPIs) on the summary page.

```dax
-- Total Loan Applications
TotalLoanApplications = COUNTROWS(LoanData)

-- Total Funded Amount
TotalFundedAmount = SUM(LoanData[LoanAmount])

-- Total Amount Received
TotalAmountReceived = SUM(LoanData[ReceivedAmount])

-- Good Loan Issued Percentage
GoodLoanIssuedPercentage = 
    DIVIDE(
        CALCULATE(COUNT(LoanData[LoanID]), LoanData[LoanStatus] = "Fully Paid"),
        [TotalLoanApplications]
    ) * 100

-- Bad Loan Issued Percentage
BadLoanIssuedPercentage = 
    DIVIDE(
        CALCULATE(COUNT(LoanData[LoanID]), LoanData[LoanStatus] = "Charged Off"),
        [TotalLoanApplications]
    ) * 100

-- Average Interest Rate
AvgInterestRate = AVERAGE(LoanData[InterestRate])

-- Average DTI
AvgDTI = AVERAGE(LoanData[DTI])
```

### 2. **Overview Dashboard**

#### **SQL Query: Loan Applications Trends**
This query provides monthly totals for loan applications, visualizing trends over time.

```sql
-- Loan Applications by Month
SELECT 
    DATEPART(MONTH, IssueDate) AS Month,
    COUNT(*) AS LoanApplications
FROM 
    LoanData
GROUP BY 
    DATEPART(MONTH, IssueDate)
ORDER BY 
    DATEPART(MONTH, IssueDate);
```

#### **DAX Measures for Overview Dashboard**
DAX queries used to calculate metrics across various dimensions like employee length, loan purpose, and state.

```dax
-- Loan Applications by Employee Length
LoanApplicationsByEmployeeLength = 
SUMMARIZE(
    LoanData,
    LoanData[EmpLength],
    "LoanApplications", COUNT(LoanData[LoanID])
)

-- Loan Applications by State
LoanApplicationsByState = 
SUMMARIZE(
    LoanData,
    LoanData[State],
    "LoanApplications", COUNT(LoanData[LoanID])
)

-- Loan Applications by Purpose
LoanApplicationsByPurpose = 
SUMMARIZE(
    LoanData,
    LoanData[Purpose],
    "LoanApplications", COUNT(LoanData[LoanID])
)
```

### 3. **Details Dashboard**

#### **SQL Query: Detailed Loan Information**
This query retrieves detailed information for each loan, which is displayed on the details page.

```sql
-- Detailed Loan Data
SELECT 
    LoanID,
    Purpose,
    HomeOwnership,
    Grade,
    SubGrade,
    IssueDate,
    LoanAmount AS TotalFundedAmount,
    InterestRate,
    Installment,
    ReceivedAmount AS TotalAmountReceived
FROM 
    LoanData
ORDER BY 
    IssueDate DESC;
```

#### **DAX Measures for Details Dashboard**
These DAX measures filter and aggregate data based on selected criteria, allowing for dynamic analysis.

```dax
-- Filtered Loan Data
FilteredLoanData = 
CALCULATETABLE(
    LoanData,
    LoanData[State] = SELECTEDVALUE(LoanData[State]),
    LoanData[Grade] = SELECTEDVALUE(LoanData[Grade]),
    LoanData[Purpose] = SELECTEDVALUE(LoanData[Purpose])
)

-- Total Funded Amount (Filtered)
TotalFundedAmount_Filtered = SUM(FilteredLoanData[LoanAmount])

-- Total Amount Received (Filtered)
TotalAmountReceived_Filtered = SUM(FilteredLoanData[ReceivedAmount])
```

### **Reproducing the Dashboards**

1. **Load Data**: Extract the necessary data from your database using the provided SQL queries.
2. **Create Measures**: Implement the DAX measures within Power BI to generate the required calculations and insights.
3. **Design Dashboards**: Structure the dashboards to mirror the Summary, Overview, and Details sections as outlined above.
4. **Apply Filters**: Use Power BI's slicers and filters to enable dynamic interactions, allowing users to drill down into specific segments of the data based on criteria such as State, Grade, and Loan Type.


## V. Key Findings

### 1. **Loan Portfolio Performance**
- **Steady Growth in Loan Applications**: The analysis showed a steady increase in loan applications over the four-year period, with a notable peak in December. This trend suggests strong demand for loans, particularly towards the end of the year.
- **Debt Consolidation as the Dominant Loan Purpose**: Debt consolidation emerged as the most common purpose for loans, accounting for a significant portion of the total loan applications. This indicates a high level of consumer debt management needs among borrowers.
- **Geographic Distribution**: The majority of loan applications originated from highly urbanized states such as California, New York, and Texas. These states also exhibited higher average loan amounts, indicating stronger economic activity and higher borrowing capacity.

### 2. **Risk Assessment**
- **Good vs. Bad Loans**: The analysis revealed that 86.2% of the loans issued were categorized as "good loans" (i.e., fully paid), while 13.8% were categorized as "bad loans" (i.e., charged off or delinquent). This distribution highlights a relatively healthy loan portfolio, though the proportion of bad loans requires attention.
- **Consistent Interest Rates**: The average interest rates remained consistent across different loan types, suggesting stable lending practices and effective interest rate management.
- **Debt-to-Income (DTI) Ratio**: The average DTI ratio for the loan portfolio was 13.3%, indicating that borrowers generally maintained a manageable level of debt relative to their income. However, loans with higher DTI ratios were more prone to default, emphasizing the need for careful risk management.

### 3. **Profitability Analysis**
- **High-Yield Loan Products**: Debt consolidation loans and credit card loans were identified as the most profitable products, contributing significantly to the bank's interest income. These products should be prioritized for future growth and expansion.
- **Regional Performance Variations**: States with higher loan application volumes, such as California and New York, also showed varying levels of default risk. This suggests that while these regions are lucrative markets, they also require stringent risk management practices.

## VI. Recommendations

### 1. **Focus on High-Yield Products**
- **Expand Debt Consolidation and Credit Card Loans**: Given the profitability of debt consolidation and credit card loans, the bank should prioritize and expand these products. Targeted marketing campaigns could further increase application volumes in these categories, enhancing overall profitability.

### 2. **Targeted Marketing and Regional Strategy**
- **Increase Presence in High-Demand States**: The bank should focus its marketing efforts on states with high demand, such as California and New York, to capture more market share. However, it is equally important to implement stringent risk assessment measures in these regions due to their higher default rates.
- **Develop Tailored Products for Underrepresented States**: In states with lower loan application volumes, the bank could develop tailored financial products that address specific local needs, potentially opening new markets and driving growth.

### 3. **Enhanced Risk Management**
- **Monitor High DTI Loans**: Loans with higher DTI ratios should be closely monitored, as they are more likely to default. The bank could consider offering financial counseling or restructuring options for borrowers with high DTI ratios to reduce default risk.
- **Strengthen Default Prediction Models**: The bank should continue to refine its predictive models to better identify high-risk loans. Early identification of potential defaults allows for proactive interventions, such as adjusting repayment terms or offering alternative payment plans.

### 4. **Optimize Loan Terms**
- **Adjust Loan Terms Based on Borrower Profiles**: The bank should consider offering more competitive loan terms (e.g., lower interest rates or longer repayment periods) to borrowers with lower DTI ratios and strong credit profiles. Conversely, for borrowers with higher risk profiles, stricter loan terms should be applied to mitigate potential losses.

### 5. **Proactive Loan Monitoring**
- **Implement Early Warning Systems**: Develop early warning systems that trigger alerts for loans showing signs of potential default. This could include automated monitoring of payment behaviors, changes in credit scores, and updates to borrower financial information.
- **Increase Engagement with High-Risk Borrowers**: Establish a proactive communication strategy with borrowers identified as high-risk. Regular check-ins and financial planning sessions can help address issues before they lead to defaults.

### 6. **Continuous Data Analysis and Improvement**
- **Regularly Update Predictive Models**: The bank should continually update its predictive models with new data to improve accuracy and adapt to changing economic conditions.
- **Leverage Data Analytics for Strategic Decision-Making**: The insights gained from data analysis should be integrated into the bank’s strategic planning processes, ensuring that data-driven decisions are made at every level of the organization.
---
