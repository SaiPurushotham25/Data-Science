Expense Tracker 📊💰

A Command-Line Based Expense Tracker built using Python, Pandas, and NumPy to help users manage their spending habits effectively. This 

tool allows users to add expenses, view spending summaries, analyze category-wise expenses, visualize data with pie charts, and export 

reports.

🧩 Features Implemented

✅ Add new expenses with category, amount, and description

✅ Automatically saves expenses to Expenses.csv

✅ View total spending overview (total, highest, lowest expense)

✅ Category-wise analysis:

Total spent per category

Transaction count per category

Percentage of total spending

✅ Filter by month or custom date range

✅ Generate pie chart showing category distribution

✅ Export summary to summary_report.csv

▶️ How to Run
1. conda activate -n env python=3.10
2. conda activate env
3. pip install pandas numpy matplotlib
4. python expense_tracker.py

Follow the On-Screen Menu
Expense Tracker Menu:
1. Add New Expense
2. Show Spending Overview
3. Show Category Analysis
4. Generate Pie Chart
5. Filter by Date Range
6. Filter by Month
7. Export Summary Report
8. Exit
Just type the corresponding number to perform actions.

Folder Structure

ExpenseTracker/

├── expense_tracker.py

├── Expenses.csv  # Auto-created if not present

└── README.md

Sample Input (CSV Format)

Date,Category,Amount,Description

2025-06-10,Food,150,Pizza at Dominos

2025-06-11,Transport,50,Rickshaw fare

2025-06-12,Rent,5000,June Rent

2025-06-12,Utilities,200,Electricity Bill

📌 Sample Output

🔹 Total Spending Overview

Total Spending: ₹5400.00

Highest Expense: ₹5000 (Rent - June Rent)

Lowest Expense: ₹50 (Transport - Rickshaw fare)

🔧 Extra Features

📅 Filter by month (e.g., June 2025)

📆 Filter by custom date range

📤 Export summarized data to CSV (summary_report.csv)

