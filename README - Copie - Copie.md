---

# Bank Loan Portfolio Analysis and Reporting

## Objective

Develop a comprehensive reporting suite to analyze the performance of a bank's loan portfolio. The focus includes monitoring key metrics like loan applications, funded amounts, and received amounts, identifying trends by state, employee tenure, loan purpose, and home ownership. The final output is a series of interactive Power BI dashboards for stakeholder insights.

## Data Source

The project utilizes multiple data sources:

1. **Loan Application Data**: Information on loan applications, including purpose, funded amount, and status.
2. **Employee Data**: Employee details such as tenure and role.
3. **Customer Data**: Demographics relevant to loan applications.

## Stages

1. **Data Collection**: Gathering data from SQL databases and Excel files.
2. **Data Cleaning**: Handling missing values, ensuring consistency, and formatting.
3. **Data Transformation**: Structuring data for analysis.
4. **Data Analysis**: Identifying trends and key metrics.
5. **Data Visualization**: Creating Power BI dashboards.
6. **Testing**: Validating data accuracy and dashboard functionality.

## Design

The reporting suite includes:

1. **Summary View**: Overview of key metrics like total loan applications and average interest rates.
2. **Overview View**: Insights into loan application trends over time and by various dimensions.
3. **Details View**: Detailed inspection of individual loan applications.

## Tools

- **Power BI**: For creating dashboards.
- **SQL Server**: For querying data.
- **Excel**: For managing employee data.
- **DAX**: For measures and calculated columns in Power BI.

## Development

### Pseudocode

1. **Data Ingestion**:
   - Connect to SQL Server and import Excel files.

2. **Data Cleaning**:
   - Handle missing values and standardize formats.

3. **Data Transformation**:
   - Join SQL and Excel tables and aggregate data.

4. **Dashboard Development**:
   - Create visualizations and implement slicers in Power BI.

## Data Exploration

Exploration of the dataset revealed key variables like loan amount, interest rate, and status. Descriptive statistics and visual summaries were generated.

## Data Cleaning

- **Missing Data**: Imputed or excluded as needed.
- **Inconsistent Data**: Standardized.
- **Outliers**: Identified and treated.

## Transform the Data

Data was transformed using SQL and DAX queries. Key transformations included creating calculated columns (e.g., DTI) and aggregating data.

## Create the SQL View

A SQL view was created to streamline data extraction for Power BI dashboards.

**Sample SQL Query**:
```sql
CREATE VIEW LoanOverview AS
SELECT 
    LoanID, 
    CustomerID, 
    State, 
    LoanAmount, 
    FundedAmount, 
    ReceivedAmount, 
    InterestRate, 
    DTI
FROM 
    LoanData
JOIN 
    CustomerData ON LoanData.CustomerID = CustomerData.CustomerID
WHERE 
    LoanStatus = 'Funded';
```

## Testing

Extensive testing ensured data accuracy and dashboard functionality, including verifying calculations and testing filter operations.

## Data Quality Tests

Implemented to check for consistency, accuracy, and completeness, identifying discrepancies or errors.

## Visualization

Power BI dashboards included:

1. **Loan Applications by Month**: Trend analysis.
2. **Applications by State**: Geographic insights.
3. **Loan Purpose Distribution**: Understanding customer needs.

## Results

Dashboards provided clear insights, such as:

- Steady increase in loan applications, peaking in December.
- Debt consolidation as the top loan purpose.
- High application rates in states like California and New York.

## DAX Measures

DAX measures enabled dynamic calculations in Power BI:

**Example DAX Measure**:
```DAX
Total Funded Amount = SUM(LoanData[FundedAmount])
```

## Analysis

Key trends identified include the dominance of debt consolidation loans and the correlation between employee tenure and loan approval rates.

## Findings

1. **Debt Consolidation**: Most common loan purpose.
2. **Geographic Trends**: High applications in urban states.
3. **Interest Rates**: Consistent across loan types.

## Validation

Results were validated by cross-referencing dashboard outputs with raw data and using statistical tests.

## Discovery

New insights, such as the relationship between home ownership and loan default rates, were discovered, guiding future strategies.

## Recommendations

Based on findings:

- Focus marketing on underperforming states.
- Incentivize loans with longer terms to reduce default rates.

## Potential ROI

Implementing these recommendations could increase loan applications and reduce default rates, potentially boosting profitability.

## Potential Courses of Action

1. **Targeted Marketing**: Focus on low-application states.
2. **Product Diversification**: Introduce new loan products.
3. **Employee Training**: Improve training in high-attrition areas.

## Conclusion

The project successfully developed interactive dashboards that provide valuable insights into the bank’s loan portfolio, aiding in decision-making for loan approvals, risk management, and marketing strategies.

---
