import sys

def main():
    try:
        print("Welcome to the program!")
        
        # Check for termination condition
        user_input = input("Do you want to exit the program? (y/n): ")
        if user_input.lower() == "y":
            exit_program()
        
        # Continue with other operations
        
    except Exception as e:
        print(f"An error occurred: {e}")
        exit_program()

def exit_program():
    print("Exiting the program...")
    sys.exit(0)

if __name__ == "__main__":
    main()
