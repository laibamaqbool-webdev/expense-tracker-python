import datetime


def print_header(title):
    print("\n" + "=" * 50)
    print(title.center(50))
    print("=" * 50)


def input_amount():
    while True:
        user_input = input("Enter expense amount (or type 'done' to finish): ").strip()

        if user_input.lower() == "done":
            return None

        try:
            value = int(user_input)
            if value <= 0:
                print("Amount must be greater than zero.\n")
                continue
            return value
        except ValueError:
            print("Please enter a valid numeric amount.\n")


def input_category():
    category = input("Enter category (optional): ").strip()
    return category.title() if category else "General"


def add_expense(records):
    amount = input_amount()
    if amount is None:
        return None

    category = input_category()
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")

    records.append({
        "amount": amount,
        "category": category,
        "time": timestamp
    })

    return amount


def display_history(records):
    print_header("EXPENSE HISTORY")

    if not records:
        print("No expenses have been recorded yet.")
        return

    print(f"{'#':<4}{'Amount':<15}{'Category':<15}{'Time':<10}")
    print("-" * 50)

    for index, record in enumerate(records, 1):
        print(f"{index:<4}{record['amount']:<15}{record['category']:<15}{record['time']:<10}")


def show_category_summary(records):
    print_header("CATEGORY BREAKDOWN")

    if not records:
        print("No data available to summarize.")
        return

    summary = {}

    for record in records:
        category = record["category"]
        summary[category] = summary.get(category, 0) + record["amount"]

    for category, total in summary.items():
        print(f"{category:<15} : Rs. {total}")


def show_statistics(total, records):
    print_header("EXPENSE STATISTICS")

    if not records:
        print("No expense data found.")
        return

    average = total / len(records)
    highest = max(records, key=lambda x: x["amount"])
    lowest = min(records, key=lambda x: x["amount"])

    print("Total entries :", len(records))
    print("Total spent   :", total)
    print("Average spent :", round(average, 2))
    print(f"Highest expense: {highest['amount']} ({highest['category']})")
    print(f"Lowest expense : {lowest['amount']} ({lowest['category']})")


def save_to_file(total, records, filename="expenses_report.txt"):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write("Expense Tracker Report\n")
            file.write("=" * 30 + "\n")
            file.write(f"Generated on: {datetime.datetime.now()}\n\n")

            for i, record in enumerate(records, 1):
                file.write(f"{i}. {record['amount']} - {record['category']} - {record['time']}\n")

            file.write("\nTOTAL SPENT: " + str(total))

        print(f"\nReport successfully saved as: {filename}")

    except Exception as error:
        print("Error while saving file:", error)


def run_tracker():
    total_spent = 0
    records = []

    print_header("PERSONAL EXPENSE TRACKER")

    print("Add your expenses one by one. Type 'done' when you want to stop.\n")

    while True:
        amount = add_expense(records)

        if amount is None:
            break

        total_spent += amount
        print(f"Recorded: {amount} | Running total: {total_spent}")

    display_history(records)
    show_category_summary(records)
    show_statistics(total_spent, records)

    if input("\nWould you like to save the report? (y/n): ").lower() == "y":
        save_to_file(total_spent, records)

    print_header("SESSION COMPLETED")


if __name__ == "__main__":
    run_tracker()