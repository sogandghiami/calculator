from pathlib import Path
import json

file_path = Path("history.json")

if not file_path.exists():
    file_path.write_text("[]")

def load_history():
    content = file_path.read_text()
    return json.loads(content)

def save_history(history):
    file_path.write_text(json.dumps(history, indent=4))

def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return "Error: Division by zero!" if b == 0 else a / b
def power(a, b): return a ** b

def show_menu():
    print("\n--- Calculator ---")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (**)")
    print("6. Show History")
    print("7. Exit")

def calculate(choice):
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    operations = {
        "1": ("+", add),
        "2": ("-", subtract),
        "3": ("*", multiply),
        "4": ("/", divide),
        "5": ("**", power)
    }

    symbol, func = operations[choice]
    result = func(a, b)
    print(f"Result: {a} {symbol} {b} = {result}")

    history = load_history()
    history.append({"a": a, "b": b, "op": symbol, "result": result})
    save_history(history)

def show_history():
    history = load_history()
    if not history:
        print("No history yet.")
    else:
        print("\n--- Calculation History ---")
        for item in history:
            print(f"{item['a']} {item['op']} {item['b']} = {item['result']}")

while True:
    show_menu()
    choice = input("Choose an option (1–7): ").strip()

    if choice in ["1", "2", "3", "4", "5"]:
        calculate(choice)
    elif choice == "6":
        show_history()
    elif choice == "7":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
