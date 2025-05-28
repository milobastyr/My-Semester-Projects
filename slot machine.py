#Milo Bastyr

#1/29/2025

symbols = [  '♠', '♣', '♥', '♦','7']
import random
def spin_slots():
    # Randomly select three symbols
    slot1 = random.choices(symbols, weights=[100, 100, 100, 100, 50], k=1)
    slot2 = random.choices(symbols, weights=[100, 100, 100, 100, 50], k=1)
    slot3 = random.choices(symbols, weights=[100, 100, 100, 100, 50], k=1)
    slot4 = random.choices(symbols, weights=[100, 100, 100, 100, 50], k=1)
    slot5 = random.choices(symbols, weights=[100, 100, 100, 100, 50], k=1)
    return slot1, slot2, slot3,slot4,slot5,

def check_win(slot1, slot2, slot3):
    # Define winning condition
    return slot1 == slot2 == slot3 == slot4 == slot5


def spin_slots():
    return random.choices(symbols, k=5)

def check_win(slot1, slot2, slot3, slot4, slot5):
    if slot1 == slot2 == slot3 == slot4 == slot5 == "7":
        return "Jackpot!", 100000
    elif slot1 == slot2 == slot3 == slot4 == slot5:
        return "Win!", 10000
    elif slot1 == slot2 == slot3 or slot2 == slot3 == slot4 or slot3 == slot4 == slot5:
        return "3 of a kind", 1500
    elif slot1 == slot2 or slot1 == slot3 or slot1 == slot4 or slot1 == slot5:
        return "2 of a kind", 500
    else:
        return "Loss!", 0

def main():
    credits = 100  # Starting credits
    while credits > 0:
        print(f"Current credits: {credits}")
        try:
            bet = int(input("Enter your bet: "))
            if bet > credits or bet <= 0:
                print("Invalid bet amount.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        slot1, slot2, slot3, slot4, slot5 = spin_slots()
        print(f"Slots: {slot1} | {slot2} | {slot3}| {slot4} | {slot5}")

        result, points = check_win(slot1, slot2, slot3,slot4,slot5)
        print(result)

        if result in ["Jackpot!", "Win!", "3 of a kind", "2 of a kind"]:
            credits += points
        else:
            credits -= bet

        try:
            play_again = input("Play again? (y/n): ").strip().lower()
            if play_again != 'y':
                break
        except Exception as e:
            print("Invalid input. Please enter 'y' or 'n'.")

    print("Game over! You have no more credits.")

if __name__ == "__main__":
    main()
