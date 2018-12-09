
import os
import pandas as pd 

budgetcsv = os.path.join("PyBank","budget_data.csv")


budget_data = pd.read_csv(budgetcsv)


print("Financial Analysis")
print("----------------------------")


total_months = len(budget_data["Date"].value_counts())
print(f'Total Months: {total_months}')


net_amount = budget_data["Profit/Losses"].sum()
print(f'Total: ${net_amount}')


Monthly_Change_List = []
monthly_change  = 0
for i in range(1, len(budget_data["Profit/Losses"].value_counts())):
    monthly_change = budget_data.iloc[i, 1] - budget_data.iloc[i-1, 1]
    Monthly_Change_List.append(monthly_change)


Monthly_Change_List.insert(0, 0)


budget_data["Monthly_Change"] = pd.DataFrame({"Monthly_Change": Monthly_Change_List})


average_change = budget_data["Monthly_Change"].sum()/len(range(1, len(budget_data["Profit/Losses"].value_counts())))
print(f'Average Change: ${average_change.round(2)}')


max_increase = budget_data["Monthly_Change"].max()
month_of_max_increase = budget_data.iloc[budget_data[budget_data['Monthly_Change']==max_increase].index.item(), 0]
print(f'Greatest Increase in Profits: {month_of_max_increase} (${max_increase})')


max_decrease = budget_data["Monthly_Change"].min()
month_of_max_decrease = budget_data.iloc[budget_data[budget_data['Monthly_Change']==max_decrease].index.item(), 0]
print(f'Greatest Decrease in Profits: {month_of_max_decrease} (${max_decrease})')


PyBank_Output = open("PyBank_Output.txt", "w+")
PyBank_Output.write(f'Financial Analysis\n----------------------------\nTotal Months: {total_months}\nTotal: ${net_amount}\nAverage Change: ${average_change.round(2)}\nGreatest Increase in Profits: {month_of_max_increase} (${max_increase})\nGreatest Decrease in Profits: {month_of_max_decrease} (${max_decrease})')