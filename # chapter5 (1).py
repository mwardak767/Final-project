# chapter5.py

# Function for gathering ammo and supplies before defense
def gather_ammo():
    while True:
        choice = input("Gather ammo and supplies to prepare for the defense. Do you want to gather supplies? (Options: yes/no): ").lower()
        if choice == "yes":
            print("You successfully gathered ammo and supplies, increasing your readiness for the defense.")
            return True  # Successful ammo gathering
        elif choice == "no":
            print("You skipped gathering supplies, leaving you less prepared for the defense.")
            return False  # Skipped gathering, increasing risk
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")

# Function for choosing a defense position with consequences
def defense_position():
    while True:
        choice = input("Choose your defense strategy. Do you want to 'hold' a strong position or 'retreat' if overwhelmed? (Options: hold/retreat): ").lower()
        if choice == "hold":
            print("You held a strong defensive position, successfully defending the city until reinforcements arrived.")
            return True  # Successful defense
        elif choice == "retreat":
            print("The retreat led to chaos among civilians. Mission failed as the city was compromised.")
            return False  # Mission failed due to retreating
        else:
            print("Invalid choice. Please enter 'hold' or 'retreat'.")

# Example of how the functions can be run
if __name__ == "__main__":
    has_ammo = gather_ammo()  # Track if player has gathered ammo and supplies

    if not defense_position():
        print("Chapter 5 failed. Game over.")
    else:
        if has_ammo:
            print("Chapter 5 completed successfully with full preparedness. Mission accomplished!")
        else:
            print("Chapter 5 completed successfully, but without full preparedness. Mission accomplished, though with high risk.")
