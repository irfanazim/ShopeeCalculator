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


def main() -> None:
    print_colored_block(ASCII_TITLE, ANSI_ORANGE)
    print()
    print("Choose a function:")
    print("1. Discount Calculator")
    print("2. Delivery Fee Calculator")
    print("3. Seller Earnings Calculator")
    # Prompt (no functionality wired yet)
    input("Enter choice: ")


if __name__ == "__main__":
    main()


