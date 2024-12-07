# chapter1.py

# Function for changing clothing to blend in
def change_clothing():
    while True:
        choice = input("Choose your clothing: 'traditional' to blend in or 'keep' your current outfit. (Options: traditional/keep): ").lower()
        if choice == "traditional":
            print("You successfully blend in with the locals and avoid suspicion.")
            return True
        elif choice == "keep":
            print("Suspicion raised! You’ve been noticed in your current outfit. Mission compromised.")
            return False
        else:
            print("Invalid choice. Please enter 'traditional' or 'keep'.")

# Function for moving through the marketplace with a risk of detection
def move_through_marketplace():
    while True:
        choice = input("Move carefully through the marketplace to avoid drawing attention. Will you move 'slowly' or 'quickly'? (Options: slowly/quickly): ").lower()
        if choice == "slowly":
            print("You proceed carefully and manage to gather information without being noticed.")
            return True
        elif choice == "quickly":
            print("Moving quickly attracts attention. You've been detected and caught by security!")
            return False
        else:
            print("Invalid choice. Please enter 'slowly' or 'quickly'.")

# Function for gathering intel with a risk of getting caught
def gather_intel():
    while True:
        choice = input("Attempt to gather intel on the terrorist location. If you’re caught, the mission will fail. Do you want to proceed with the intel gathering? (Options: yes/no): ").lower()
        if choice == "yes":
            outcome = input("You attempt to gather intel. Were you successful or caught? (Options: success/caught): ").lower()
            if outcome == "success":
                print("You successfully gathered the intel and got away undetected. Proceeding to the next chapter.")
                return True  # Successful intel gathering and escape
            elif outcome == "caught":
                print("You were caught while gathering intel. Mission failed.")
                return False  # Mission failed due to being caught
            else:
                print("Invalid choice. Please enter 'success' or 'caught'.")
        elif choice == "no":
            print("You chose not to gather intel. Mission incomplete, game over.")
            return False  # Mission failed due to not gathering intel
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")

# Example of how the functions can be run
if __name__ == "__main__":
    if not change_clothing():
        print("Chapter 1 failed. Game over.")
    elif not move_through_marketplace():
        print("Chapter 1 failed. Game over.")
    elif not gather_intel():
        print("Chapter 1 failed. Game over.")
    else:
        print("Chapter 1 completed successfully. Proceeding to Chapter 2.")
