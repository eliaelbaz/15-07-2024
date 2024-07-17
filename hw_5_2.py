##start

print("Welcome to the guessing game!!");

while True:
    target_number = 50;
    attempts = 0;

    while True:
        guess = int(input("Enter a number: "));
        attempts += 1;

        if guess > target_number:
            print("Your number is too big");
        elif guess < target_number:
            print("Your number is too small");
        else:
            print("BINGO");
            break

    print(f"Number of attempts: {attempts}");

    play_again = input("Do you want to play again? (yes/no): ").lower();
    if play_again != 'yes':
        break

print("Thank you for playing the guessing game!");

## End