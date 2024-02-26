import random

def generate_powerball_numbers():
    # Generate the first 5 numbers
    first_five_numbers = [random.randint(1, 69) for _ in range(5)]
    
    # Generate the PowerBall number (6th number)
    powerball_number = random.randint(1, 26)
    
    # Combine the numbers with appropriate spacing
    powerball_numbers = " ".join(map(str, first_five_numbers)) + "    " + str(powerball_number)
    
    return powerball_numbers

def main():
    print("Welcome to the PowerBall number generator!")
    
    user_input = input("Would you like some PowerBall numbers? (yes/no): ").lower()
    
    if user_input == "yes":
        powerball_numbers = generate_powerball_numbers()
        print(f"Here are your PowerBall numbers: {powerball_numbers}")
    else:
        print("Alright, maybe next time!")

if __name__ == "__main__":
    main()
