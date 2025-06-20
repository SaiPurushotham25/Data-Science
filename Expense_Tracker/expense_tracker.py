import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import os

class ExpenseTracker:
    def __init__(self, file_path='Expenses.csv'):
        self.file_path = file_path
        self.expenses = self.load_data()
        
    def load_data(self):
        """Load expense data from CSV file"""
        if os.path.exists(self.file_path):
            df = pd.read_csv(self.file_path, parse_dates=['Date'])
            return df
        else:
            return pd.DataFrame(columns=['Date', 'Category', 'Amount', 'Description'])
    
    def save_data(self):
        """Save data to CSV file"""
        self.expenses.to_csv(self.file_path, index=False)
    
    def add_expense(self):
        """Add new expense through user input"""
        date = input("Enter date (YYYY-MM-DD): ")
        category = input("Enter category: ")
        amount = float(input("Enter amount: "))
        description = input("Enter description: ")
        
        new_expense = pd.DataFrame({
            'Date': [pd.to_datetime(date)],
            'Category': [category],
            'Amount': [amount],
            'Description': [description]
        })
        
        self.expenses = pd.concat([self.expenses, new_expense], ignore_index=True)
        self.save_data()
        print("Expense added successfully!")
    
    def get_total_spending(self):
        """Calculate total spending overview"""
        total = np.sum(self.expenses['Amount'])
        max_expense = self.expenses.loc[self.expenses['Amount'].idxmax()]
        min_expense = self.expenses.loc[self.expenses['Amount'].idxmin()]
        return total, max_expense, min_expense
    
    def get_category_analysis(self):
        """Generate category-wise analysis"""
        grouped = self.expenses.groupby('Category')
        category_sum = grouped['Amount'].sum()
        category_count = grouped.size()
        category_percent = (category_sum / np.sum(self.expenses['Amount'])) * 100
        
        analysis_df = pd.DataFrame({
            'Total Amount': category_sum,
            'Transaction Count': category_count,
            'Percentage': category_percent.round(2)
        })
        return analysis_df
    
    def generate_pie_chart(self):
        """Generate pie chart of expense distribution"""
        analysis_df = self.get_category_analysis()
        plt.figure(figsize=(8, 6))
        plt.pie(
            analysis_df['Total Amount'],
            labels=analysis_df.index,
            autopct='%1.1f%%',
            startangle=90
        )
        plt.title('Expense Distribution by Category')
        plt.show()
    
    def filter_by_date_range(self, start_date, end_date):
        """Filter expenses by date range"""
        mask = (self.expenses['Date'] >= start_date) & (self.expenses['Date'] <= end_date)
        return self.expenses.loc[mask]
    
    def filter_by_month(self, year, month):
        """Filter expenses by month"""
        mask = (self.expenses['Date'].dt.year == year) & (self.expenses['Date'].dt.month == month)
        return self.expenses.loc[mask]
    
    def export_summary(self, file_name='summary_report.csv'):
        """Export summary report to CSV"""
        analysis_df = self.get_category_analysis()
        analysis_df.to_csv(file_name)
        print(f"Summary report exported to {file_name}")

def main():
    tracker = ExpenseTracker()
    
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add New Expense")
        print("2. Show Spending Overview")
        print("3. Show Category Analysis")
        print("4. Generate Pie Chart")
        print("5. Filter by Date Range")
        print("6. Filter by Month")
        print("7. Export Summary Report")
        print("8. Exit")
        
        choice = input("Enter your choice (1-8): ")
        
        if choice == '1':
            tracker.add_expense()
        
        elif choice == '2':
            total, max_exp, min_exp = tracker.get_total_spending()
            print(f"\nTotal Spending: ₹{total:.2f}")
            print(f"Highest Expense: ₹{max_exp['Amount']} ({max_exp['Category']} - {max_exp['Description']})")
            print(f"Lowest Expense: ₹{min_exp['Amount']} ({min_exp['Category']} - {min_exp['Description']})")
        
        elif choice == '3':
            analysis = tracker.get_category_analysis()
            print("\nCategory-wise Analysis:")
            print(analysis.to_string())
        
        elif choice == '4':
            tracker.generate_pie_chart()
        
        elif choice == '5':
            start = input("Enter start date (YYYY-MM-DD): ")
            end = input("Enter end date (YYYY-MM-DD): ")
            filtered = tracker.filter_by_date_range(start, end)
            print("\nFiltered Expenses:")
            print(filtered.to_string(index=False))
        
        elif choice == '6':
            year = int(input("Enter year: "))
            month = int(input("Enter month (1-12): "))
            filtered = tracker.filter_by_month(year, month)
            print("\nFiltered Expenses:")
            print(filtered.to_string(index=False))
        
        elif choice == '7':
            tracker.export_summary()
        
        elif choice == '8':
            print("Exiting program...")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()