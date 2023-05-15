import os
import csv

budget_data = os.path.join("..", "Resources", "budget_data.csv")

with open(budget_data, 'r') as file:
        data = csv.reader(file)
        header = next(data) 
        total_months =0
        total_profit_loss = 0
        changes = []
        greatest_increase = ['',0]
        greatest_decrease = ['',0]
        prev_profit_loss = 0



#     for row in data:
#         date = row[0]
#         profit_loss = int(row[1])
        
        # Calculate total months and total profit/loss
        total_months += 1
        total_profit_loss += profit_loss
        
        # Calculate changes in profit/loss
        if prev_profit_loss != 0:
            change = profit_loss - prev_profit_loss
            changes.append(change)
            
            # Update greatest increase and greatest decrease
            if change > greatest_increase[1]:
                greatest_increase[0] = date
                greatest_increase[1] = change
            elif change < greatest_decrease[1]:
                greatest_decrease[0] = date
                greatest_decrease[1] = change
        
        prev_profit_loss = profit_loss
    
    # Calculate average change
    average_change = round(sum(changes) / len(changes), 2)

    # Print the results
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_profit_loss}")
    print(f"Average Change: ${average_change}")
    print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
    print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")
