# Bank Loan Report Project

## Problem Statement

This project involves the creation of a comprehensive **Bank Loan Report** to monitor and assess the bank's lending activities and performance. The report aims to provide insights into key loan-related metrics and their changes over time. It will help track the health of the bank’s loan portfolio and identify trends that can inform its lending strategies.

### Key Performance Indicators (KPIs) Requirements

The following KPIs are crucial for monitoring the bank's loan activities:

1. **Total Loan Applications**:
    - **Objective**: Calculate the total number of loan applications received during a specified period, including Month-to-Date (MTD) applications and Month-over-Month (MoM) changes.
    - **SQL Queries**:
        ```sql
        -- Total Loan Applications
        SELECT COUNT(*) AS TotalLoanApplications FROM bank_loan;

        -- Month-to-Date (MTD) Loan Applications for the current month
        SELECT COUNT(*) AS MTDTotalLoanApplications 
        FROM bank_loan
        WHERE MONTH(CONVERT(DATE issue_date, 105)) = 12 AND YEAR(issue_date) = 2021;

        -- Month-over-Month (MoM) Changes
        SELECT COUNT(*) AS PMTDTotalLoanApplications 
        FROM bank_loan
        WHERE MONTH(CONVERT(DATE issue_date, 105)) = 11 
          AND YEAR(CONVERT(DATE issue_date, 105)) = 2021;
        ```

2. **Total Funded Amount**:
    - **Objective**: Track the total amount of funds disbursed as loans, with attention to MTD total funded amount and MoM changes.
    - **SQL Queries**:
        ```sql
        -- Total Funded Amount
        SELECT SUM(loan_amount) AS Total_Funded_Amount FROM bank_loan;

        -- MTD Total Funded Amount
        SELECT SUM(loan_amount) AS Total_Funded_Amount 
        FROM bank_loan
        WHERE MONTH(CONVERT(DATE issue_date, 105)) = 12;
        ```

3. **Total Amount Received**:
    - **Objective**: Monitor the total amount received from borrowers, focusing on MTD total amount received and MoM changes.
    - **SQL Queries**:
        ```sql
        -- Total Loan Amount Received
        SELECT SUM(loan_amount) AS TotalAmountReceived FROM bank_loan;
        ```

4. **Average Interest Rate & Debt-to-Income Ratio (DTI)**:
    - **Objective**: Calculate the average interest rate across all loans MTD and monitor MoM variations, alongside the average DTI for all loans.

### Good Loan vs. Bad Loan KPIs

To evaluate the quality of the loan portfolio:

- **Good Loans**:
  - **Metrics**:
    - Good Loan Application Percentage
    - Good Loan Applications
    - Good Loan Funded Amount
    - Good Loan Total Received Amount

- **Bad Loans**:
  - **Metrics**:
    - Bad Loan Application Percentage
    - Bad Loan Applications
    - Bad Loan Funded Amount
    - Bad Loan Total Received Amount

### Loan Status Grid View

The **Loan Status Grid View** report will provide a comprehensive overview of the bank's lending operations, categorized by loan status. This report will include key metrics such as:

- Total Loan Applications
- Total Funded Amount
- Total Amount Received
- Month-to-Date (MTD) Funded Amount
- MTD Amount Received
- Average Interest Rate
- Average Debt-to-Income Ratio (DTI)

## Dashboard Overview

### Dashboard 1: Summary

A high-level summary of the bank's loan performance will be provided, focusing on KPIs like total loan applications, funded amounts, and received amounts.


### Dashboard 2: Overview

This dashboard will visually represent critical loan-related metrics and trends through various chart types:

1. **Monthly Trends by Issue Date (Line Chart)**:
   - Visualize trends in total loan applications, funded amounts, and received amounts over time.

2. **Regional Analysis by State (Filled Map)**:
   - Represent lending metrics by state to identify regional disparities.

3. **Loan Term Analysis (Donut Chart)**:
   - Show distribution of loans across different term lengths.

4. **Employee Length Analysis (Bar Chart)**:
   - Display lending metrics distributed among borrowers with varying employment lengths.

5. **Loan Purpose Breakdown (Bar Chart)**:
   - Provide a breakdown of loan metrics based on the stated purposes of loans.

6. **Home Ownership Analysis (Tree Map)**:
   - Display loan metrics categorized by home ownership status.

### Dashboard 3: Details

The **Details Dashboard** offers a consolidated view of essential loan data, providing a comprehensive snapshot of key metrics and data points related to the loan portfolio.

## Conclusion

This project aims to enhance the bank's ability to monitor and assess its lending activities effectively. Through the creation of detailed reports and dashboards, we can provide actionable insights and support strategic decision-making processes.
