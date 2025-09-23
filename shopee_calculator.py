ASCII_TITLE = r"""
   _____ _    _  ____  _____  ______ ______    _____          _      _____ _    _ _            _______ ____  _____  
  / ____| |  | |/ __ \|  __ \|  ____|  ____|  / ____|   /\   | |    / ____| |  | | |        /\|__   __/ __ \|  __ \ 
 | (___ | |__| | |  | | |__) | |__  | |__    | |       /  \  | |   | |    | |  | | |       /  \  | | | |  | | |__) |
  \___ \|  __  | |  | |  ___/|  __| |  __|   | |      / /\ \ | |   | |    | |  | | |      / /\ \ | | | |  | |  _  / 
  ____) | |  | | |__| | |    | |____| |____  | |____ / ____ \| |___| |____| |__| | |____ / ____ \| | | |__| | | \ \ 
 |_____/|_|  |_|\____/|_|    |______|______|  \_____/_/    \_\______\_____|\____/|______/_/    \_\_|  \____/|_|  \_\
                                                                                                                    
                                                                                                                    
"""

ANSI_RESET = "\x1b[0m"
ANSI_ORANGE = "\x1b[38;5;208m"  # 256-color orange

def print_colored_block(text: str, color_code: str) -> None:
    for raw_line in text.splitlines():
        print(f"{color_code}{raw_line}{ANSI_RESET}")


def clear_screen() -> None:
    try:
        import os
        os.system("cls" if os.name == "nt" else "clear")
    except Exception:
        pass


# Discount Calculator Feature (CHOICE 1)
def discount_calculator() -> None:

    # Loop until user chooses to go back to main menu
    while True:
        try:
            original_price = float(input("Enter the original price (RM): "))
            discount_percent = float(input("Enter the discount percentage (%): "))
            
            # Calculation for the final price
            final_price = original_price * (1 - discount_percent / 100)

            # Show result rounded to 2 decimal places
            print(f"\nFinal price after {discount_percent}% discount: RM{final_price:.2f}")
            
        except ValueError:
            print("\nInvalid input! Please enter numbers only.")
            continue

        # Keeps looping until valid input (1 or 2) is given
        while True:
            print("\nWhat would you like to do next?")
            print("1. Calculate again")
            print("2. Back to main menu")
            next_choice = input("Enter choice: ").strip()

            if next_choice == "1":
                clear_screen()
                break  
            elif next_choice == "2":
                return  
            else:
                print("\nInvalid choice. Please enter 1 or 2.\n")
                continue  


# Delivery fee parameters (adjust as needed)
WEST_BASE_FEE = 3.00
WEST_RATE_PER_KM = 1.00
WEST_RATE_PER_KG = 0.80

EAST_BASE_FEE = 5.00
EAST_RATE_PER_KM = 1.50  
EAST_RATE_PER_KG = 1.30


def calculate_delivery_fee(region: str, distance_km: float, weight_kg: float) -> float:
    if region == "West Malaysia":
        return WEST_BASE_FEE + (WEST_RATE_PER_KM * distance_km) + (WEST_RATE_PER_KG * weight_kg)
    else:
        return EAST_BASE_FEE + (EAST_RATE_PER_KM * distance_km) + (EAST_RATE_PER_KG * weight_kg)


def delivery_fee_calculator() -> None:
    while True:
        print("Select region:")
        print("1. West Malaysia")
        print("2. East Malaysia")
        region_choice = input("Enter choice (1 or 2): ").strip()

        if region_choice == "1":
            region_name = "West Malaysia"
            base_fee = WEST_BASE_FEE
        elif region_choice == "2":
            region_name = "East Malaysia"
            base_fee = EAST_BASE_FEE
        else:
            print("\nInvalid region choice. Please try again.\n")
            continue

        try:
            distance_km = float(input("\nEnter delivery distance (km): ").strip())
            weight_kg = float(input("Enter parcel weight (kg): ").strip())
        except ValueError:
            print("\nInvalid number entered. Please try again.\n")
            continue

        fee = calculate_delivery_fee(region_name, distance_km, weight_kg)

        print("\n--- Delivery Summary ---")
        print(f"Region: {region_name}")
        print(f"Distance: {distance_km:.1f} km")
        print(f"Weight: {weight_kg:.1f} kg")
        print(f"Base Fee: RM{base_fee:.2f}")
        print(f"Delivery Fee = RM{fee:.2f}")

        print("\nWhat would you like to do next?")
        print("1. Calculate again")
        print("2. Back to main menu")
        next_choice = input("Enter choice: ").strip()
        if next_choice == "1":
            clear_screen()
            continue
        elif next_choice == "2":
            break
        else:
            print("\nInvalid choice. Returning to main menu.")
            break

# Main Menu
def main() -> None:
    while True:
        clear_screen()
        print_colored_block(ASCII_TITLE, ANSI_ORANGE)
        print()
        print("Choose a function:")
        print("1. Discount Calculator")
        print("2. Delivery Fee Calculator")
        print("3. Seller Earnings Calculator")
        choice = input("Enter choice: ").strip().lower()

        if choice == "1":
            clear_screen()
            discount_calculator()
            input("\nPress Enter to return to main menu...")
            clear_screen()
        elif choice =="2":
            clear_screen()
            delivery_fee_calculator()
            clear_screen()
        elif choice == "3":
            clear_screen()
            print("Seller Earnings Calculator is not implemented yet.")
            input("\nPress Enter to return to main menu...")
            clear_screen()
        else:
            print("\nInvalid choice. Please try again.\n")
            input("Press Enter to continue...")
            clear_screen()

if __name__ == "__main__":
    main()


