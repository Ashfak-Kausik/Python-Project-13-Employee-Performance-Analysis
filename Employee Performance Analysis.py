import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
employee_data = pd.read_csv('employee_performance.csv')

# Define weights for performance metrics
weights = {'Sales': 0.4, 'Tasks_Completed': 0.3, 'Attendance': 0.2, 'Customer_Satisfaction': 0.1}

# Calculate performance score
employee_data['Performance_Score'] = (
    employee_data['Sales'] * weights['Sales'] +
    employee_data['Tasks_Completed'] * weights['Tasks_Completed'] +
    employee_data['Attendance'] * weights['Attendance'] +
    employee_data['Customer_Satisfaction'] * weights['Customer_Satisfaction']
)

# Rank employees by performance score
employee_data['Rank'] = employee_data['Performance_Score'].rank(ascending=False)

# Visualization
employee_data.sort_values('Performance_Score', ascending=False).plot(kind='bar', x='EmployeeID', y='Performance_Score', color='purple', title='Employee Performance Scores')
plt.ylabel('Performance Score')
plt.show()

# Distribution of performance scores
employee_data['Performance_Score'].plot(kind='hist', bins=10, color='red', title='Distribution of Performance Scores')
plt.xlabel('Performance Score')
plt.show()
