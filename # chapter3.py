# chapter3.py

# Function for stealth tracking of targets
def stealth_tracking():
    while True:
        choice = input("Follow your targets carefully to avoid detection. Do you want to proceed 'stealthily' or 'carelessly'? (Options: stealthily/carelessly): ").lower()
        if choice == "stealthily":
            print("You successfully follow the targets without being detected.")
            return True  # Successful stealth tracking
        elif choice == "carelessly":
            print("You are noticed due to careless tracking. You must restart the tracking mission.")
            restart = input("Do you want to restart tracking? (Options: yes/no): ").lower()
            if restart == "yes":
                print("Restarting tracking...")
            elif restart == "no":
                print("You abandoned tracking and failed the mission.")
                return False  # Mission failed due to abandonment
            else:
                print("Invalid choice. Please enter 'yes' or 'no'.")
        else:
            print("Invalid choice. Please enter 'stealthily' or 'carelessly'.")

# Function for using gadgets to gather information on the leader
def use_gadgets():
    while True:
        choice = input("Use gadgets to gather intel on the leader. Gadgets may malfunction. Do you want to proceed? (Options: yes/no): ").lower()
        if choice == "yes":
            malfunction = input("Your gadget has a chance to malfunction. Did it work successfully? (Options: yes/no): ").lower()
            if malfunction == "yes":
                print("Gadget worked perfectly, and you gathered valuable information on the leader.")
                return True  # Successfully gathered intel
            elif malfunction == "no":
                print("The gadget malfunctioned, risking your cover. Mission failed due to lack of intel.")
                return False  # Mission failed due to gadget malfunction
            else:
                print("Invalid choice. Please enter 'yes' or 'no'.")
        elif choice == "no":
            print("You chose not to use the gadgets, resulting in incomplete intel. Mission failed.")
            return False  # Mission failed due to lack of intel
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")

# Example of how the functions can be run
if __name__ == "__main__":
    if not stealth_tracking():
        print("Chapter 3 failed. Game over.")
    elif not use_gadgets():
        print("Chapter 3 failed. Game over.")
    else:
        print("Chapter 3 completed successfully. Proceeding to Chapter 4.")
