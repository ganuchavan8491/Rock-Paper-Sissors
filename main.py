import random
import threading

# ASCII arts
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
ROCK
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
PAPER
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
SCISSORS
'''

choices = [rock, paper, scissors]

# Input with timeout function
def get_input_with_timeout(prompt, timeout):
    user_input = [None]

    def input_thread():
        user_input[0] = input(prompt)

    thread = threading.Thread(target=input_thread)
    thread.daemon = True
    thread.start()
    thread.join(timeout)

    if thread.is_alive():
        return None  # Timeout
    return user_input[0]

# Game starts
print("Welcome to Rock, Paper, Scissors!")

while True:
    text = get_input_with_timeout("Type 0 for Rock, 1 for Paper, 2 for Scissors (or 'bye' to exit): ", 30)

    if text is None:
        print("⏰ No response received in 30 seconds. Shutting down. Bye!")
        break

    if text.lower() in ["exit", "quit", "bye"]:
        print("👋 Thank you! Meet you again.")
        break

    if not text.isdigit() or int(text) not in [0, 1, 2]:
        print("⚠️ Invalid input! Please enter 0, 1, or 2.")
        continue

    user_choice = int(text)
    print("You chose:")
    print(choices[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(choices[computer_choice])

    # Result
    if user_choice == computer_choice:
        print("🤝 It's a draw.\n")
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        print("🎉 You win!\n")
    else:
        print("💻 Computer wins. You lose.\n")
