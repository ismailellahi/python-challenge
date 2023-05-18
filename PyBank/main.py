import os
import csv

budget_data = os.path.join("Resources", "budget_data.csv")
file_output = os.path.join("Analysis", "Results.txt")

# Read the csv and convert it into a list of dictionaries
with open(budget_data, 'r') as file:
    data = csv.reader(file)

    # Read header row
    header = next(data)

    total_months = 0
    total_profit_loss = 0
    changes = []
    greatest_increase = ['', 0]
    greatest_decrease = ['', 0]
    prev_profit_loss = 0

    for row in data:
        date = row[0]
        profit_loss = int(row[1])

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
# Generate Output Summary
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_profit_loss}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# Print the output (to terminal)
print(output)

# Export the results to text file
with open(file_output, "w") as txt_file:
    txt_file.write(output)
    
    
