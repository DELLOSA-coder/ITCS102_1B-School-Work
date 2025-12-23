# =========================================
# PYTHON INTERACTIVE MENU PROGRAM
# =========================================

def pause():
    input("\nPress Enter to continue...")

# ---------- PROGRAM EXAMPLES ----------

def example_print():
    print("\n[PRINT STATEMENT EXAMPLE]")
    print("print('Welcome to Python!')")
    print("\nOutput:")
    print("Welcome to Python!")

def example_variables():
    print("\n[VARIABLES EXAMPLE]")
    a = 25
    name = "Student"
    print("a =", a)
    print("name =", name)

def example_operators():
    print("\n[OPERATORS EXAMPLE]")
    x = 8
    y = 4
    print("Addition:", x + y)
    print("Subtraction:", x - y)
    print("Multiplication:", x * y)
    print("Division:", x / y)

def example_conditionals():
    print("\n[CONDITIONALS EXAMPLE]")
    num = 7
    if num % 2 == 0:
        print(num, "is Even")
    else:
        print(num, "is Odd")

def example_loops():
    print("\n[LOOPS EXAMPLE]")
    for i in range(1, 6):
        print("Number:", i)

def example_lists():
    print("\n[LISTS EXAMPLE]")
    numbers = [10, 20, 30, 40]
    print("List:", numbers)
    print("Last Value:", numbers[-1])

def example_functions():
    print("\n[FUNCTIONS EXAMPLE]")

    def square(n):
        return n * n

    print("Square of 5:", square(5))

# ---------- SUBMENU TEMPLATE ----------

def submenu(title, function_example):
    while True:
        print(f"\n--- {title} MENU ---")
        print("1. Show Example")
        print("2. Back to Main Menu")

        choice = input("Select: ")

        if choice == "1":
            function_example()
            pause()
        elif choice == "2":
            break
        else:
            print("Invalid input. Try again!")

# ---------- USER DEFINED PROGRAM ----------

def run_user_program():
    print("\n--- RUN YOUR OWN PROGRAM ---")
    print("Type your Python code line by line.")
    print("Type 'done' when finished.\n")

    code = ""

    while True:
        line = input(">>> ")
        if line.lower() == "done":
            break
        code += line + "\n"

    try:
        exec(code)
        print("\n✅ Program ran successfully!")
    except Exception as error:
        print("\n❌ Error:", error)

    pause()

# ---------- MAIN MENU ----------

def main_menu():
    while True:
        print("\n==============================")
        print(" PYTHON LEARNING MAIN MENU")
        print("==============================")
        print("1. Print Statements")
        print("2. Variables")
        print("3. Operators")
        print("4. Conditionals")
        print("5. Loops")
        print("6. Lists")
        print("7. Functions")
        print("8. Run Your Own Program")
        print("9. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            submenu("PRINT STATEMENTS", example_print)
        elif choice == "2":
            submenu("VARIABLES", example_variables)
        elif choice == "3":
            submenu("OPERATORS", example_operators)
        elif choice == "4":
            submenu("CONDITIONALS", example_conditionals)
        elif choice == "5":
            submenu("LOOPS", example_loops)
        elif choice == "6":
            submenu("LISTS", example_lists)
        elif choice == "7":
            submenu("FUNCTIONS", example_functions)
        elif choice == "8":
            run_user_program()
        elif choice == "9":
            print("\nThank you for using the program. Goodbye!\n")
            break
        else:
            print("❗ Invalid choice. Try again!")

# ---------- START PROGRAM ----------
print("\nWELCOME TO PYTHON LEARNING PROGRAM!\n")
name = input("What is your name? ")
start = input(f"\nHi {name}! Do you want to proceed to the program?\n1. Yes\n2. No\nEnter: ")
if start == "1":
    main_menu()
elif start == "2":
    print("\nThank you for using the program. Goodbye!\n")
    SystemExit
else:
    print("\nInvalid choice.\n")
     
