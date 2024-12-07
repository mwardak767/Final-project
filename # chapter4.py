# chapter4.py

# Function for entering the meeting with a disguise
def disguise_infiltration():
    while True:
        choice = input("Enter the meeting disguised to avoid detection. Do you want to proceed with a disguise? (Options: yes/no): ").lower()
        if choice == "yes":
            success = input("Did your disguise work successfully? (Options: yes/no): ").lower()
            if success == "yes":
                print("Your disguise was effective. You've blended in with the crowd and avoided detection.")
                return True  # Successful infiltration
            elif success == "no":
                print("Your disguise failed, and you've been detected. Mission failed.")
                return False  # Mission failed due to failed disguise
            else:
                print("Invalid choice. Please enter 'yes' or 'no'.")
        elif choice == "no":
            print("You chose not to disguise yourself, leading to immediate detection. Mission failed.")
            return False  # Mission failed due to lack of disguise
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")

# Function for deciding how to eliminate the leader
def attack_leader():
    while True:
        choice = input("Do you want to take out the leader with a stealthy approach or a forceful assault? (Options: stealth/assault): ").lower()
        if choice == "stealth":
            print("You successfully eliminated the leader quietly and avoided alerting the guards.")
            return True  # Successful stealth kill
        elif choice == "assault":
            escape = input("Assault triggered a quick response from guards. Do you want to escape immediately? (Options: yes/no): ").lower()
            if escape == "yes":
                print("You managed to escape after a quick assault on the leader.")
                return True  # Successful escape after assault
            elif escape == "no":
                print("You were overwhelmed by guards and captured. Mission failed.")
                return False  # Mission failed due to no escape
            else:
                print("Invalid choice. Please enter 'yes' or 'no'.")
        else:
            print("Invalid choice. Please enter 'stealth' or 'assault'.")

# Example of how the functions can be run
if __name__ == "__main__":
    if not disguise_infiltration():
        print("Chapter 4 failed. Game over.")
    elif not attack_leader():
        print("Chapter 4 failed. Game over.")
    else:
        print("Chapter 4 completed successfully. Proceeding to Chapter 5.")
