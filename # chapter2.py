# chapter2.py

# Function for searching for supplies
def search_supplies():
    while True:
        choice = input("Do you want to search for supplies? (Options: yes/no): ").lower()
        if choice == "yes":
            print("You successfully gather useful gear and weapons.")
            return True  # Player has supplies and weapons
        elif choice == "no":
            print("You skipped searching for supplies. You may face greater risk later.")
            return False  # Player does not have supplies or weapons
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")

# Function for placing explosives with consequences based on supply search
def place_explosives(has_weapon):
    while True:
        choice = input("Do you want to place explosives carefully? (Options: yes/no): ").lower()
        if choice == "yes":
            print("Explosives placed successfully - Depot destroyed!")
            return True
        elif choice == "no":
            print("Detected! Security is alerted to your presence.")
            if has_weapon:
                fight_back = input("You have a weapon. Do you want to fight back? (Options: yes/no): ").lower()
                if fight_back == "yes":
                    print("You fought off the patrol and escaped successfully.")
                    return True  # Successful escape after fighting back
                elif fight_back == "no":
                    print("You chose not to fight and were captured.")
                    return False  # Mission failed due to no resistance
                else:
                    print("Invalid choice. Please enter 'yes' or 'no'.")
            else:
                print("You have no weapon to defend yourself. Mission failed.")
                return False
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")

# Function for avoiding patrols with detection risk
def avoid_patrols():
    while True:
        choice = input("Will you avoid patrols or engage with them? (Options: avoid/engage): ").lower()
        if choice == "avoid":
            print("You successfully avoid the patrols and remain undetected.")
            return True  # Successful avoidance of patrols
        elif choice == "engage":
            print("You chose to engage with the patrols, risking detection.")
            return False  # Player chose to engage, increasing risk
        else:
            print("Invalid choice. Please enter 'avoid' or 'engage'.")

# Example of how the functions can be run
if __name__ == "__main__":
    has_weapon = search_supplies()  # Track if player has gathered weapons and supplies

    if not place_explosives(has_weapon):
        print("Chapter 2 failed. Game over.")
    elif not avoid_patrols():
        print("Detected by patrols. Chapter 2 failed. Game over.")
    else:
        print("Chapter 2 completed successfully. Proceeding to Chapter 3.")
