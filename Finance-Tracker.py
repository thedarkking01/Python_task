import csv
import os

def add_expense(expenses):
    """Add a new expense to the tracker."""
    category = input("Enter the category (e.g., Food, Transport, Bills): ").strip()
    description = input("Enter a description: ").strip()
    amount = float(input("Enter the amount spent: "))
    expenses.append({"Category": category, "Description": description, "Amount": amount})
    print("Expense added successfully!")

def view_expenses(expenses):
    """View all recorded expenses."""
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\nExpenses Recorded:")
    print(f"{'Category':<15}{'Description':<30}{'Amount':>10}")
    print("-" * 55)
    for expense in expenses:
        print(f"{expense['Category']:<15}{expense['Description']:<30}{expense['Amount']:>10.2f}")
    print()

def summarize_expenses(expenses):
    """Summarize expenses by category."""
    if not expenses:
        print("No expenses recorded to summarize.")
        return

    summary = {}
    for expense in expenses:
        category = expense["Category"]
        amount = expense["Amount"]
        summary[category] = summary.get(category, 0) + amount

    print("\nExpense Summary:")
    for category, total in summary.items():
        print(f"{category:<15}: ${total:.2f}")
    print()

def save_expenses(expenses, filename="expenses.csv"):
    """Save expenses to a CSV file."""
    with open(filename, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["Category", "Description", "Amount"])
        writer.writeheader()
        writer.writerows(expenses)
    print(f"Expenses saved to {filename}")

def load_expenses(filename="expenses.csv"):
    """Load expenses from a CSV file."""
    if not os.path.exists(filename):
        return []
    
    with open(filename, mode="r") as file:
        reader = csv.DictReader(file)
        return [row for row in reader]

def main():
    """Main function for the expense tracker."""
    print("Welcome to the Personal Finance Tracker!")
    expenses = load_expenses()
    while True:
        print("\nOptions:")
        print("1. Add an expense")
        print("2. View expenses")
        print("3. Summarize expenses")
        print("4. Save expenses")
        print("5. Exit")
        
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            summarize_expenses(expenses)
        elif choice == "4":
            save_expenses(expenses)
        elif choice == "5":
            print("Thank you for using the Personal Finance Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
