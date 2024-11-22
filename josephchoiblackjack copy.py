import random

# create a standard 52 deck
#rather than typing everything 4 times, i just added *4 since it multiples whatever is in the list by 4 
deck = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"] * 4

# getting the total
def card_total(hand):
    total = 0
    ace_card = hand.count('Ace')
# used for, if your get a J Q or K you get +10, if its an Ace you get +11  
# else used if its any other card thats not the cards listed above   
    for card in hand:
        if card in ["Jack", "Queen", "King"]:
            total += 10
        elif card == "Ace":
            total += 11 
        else:
            total += int(card) 
# if you get an Ace and it brings you to above 21, it gives you 1 instead of 11
    while total > 21 and ace_card:
        total -= 10
        ace_card -= 1 

    return total
# to get the result of the matches, = 0 since well be using +=1 latter
user_wins = 0
programs_win = 0

play_again = True
while play_again:
    rounds_played = 0
    
    while rounds_played < 3:
        users_hand = [] # empty lists, will store the card information
        programs_hand = []
        random.shuffle(deck)

        for _ in range(2): # loop deals two cards aby popping cards from the deck and appending them to the hands
            users_hand.append(deck.pop()) 
            programs_hand.append(deck.pop())

        game_over = False 
        user_input_choice = False
# starts a loop so that will contiue until game over is becomes True since its a game of 3
        while not game_over: # scores are the cards from each users hands
            users_score = card_total(users_hand)
            programs_score = card_total(programs_hand)

            print(f"Here are your cards: {users_hand} and your current score: {users_score}")
            print(f"Your Opponent's first card: {programs_hand[0]}")
# used while loop to take user input, used if else to ensure user enters valid response
            while not user_input_choice:
                # if user inputs hit or stay incorrectly, it tells the user
                user_input = input("Type 'hit' to get another card, Type 'stay' to pass: ").lower()
                if user_input in ['hit', 'stay']:
                    user_input_choice = True
                else:
                    print("You have entered an invalid choice. Enter 'hit' or 'stay': ")
# used conditionals to check conditions during the match, since black jack is 21, used == 
            if users_score == 21 or programs_score == 21 or user_input == "stay":
                game_over = True
            else:
                users_hand.append(deck.pop())
    # used append(deck.pop()) to removed card from deck and appened into the hands
            if programs_score < 17:
                programs_hand.append(deck.pop())
    # condtionals to ensure the games rule are checked
            if users_score > 21 or programs_score > 21:
                game_over = True
            
            user_input_choice = False
#final score print statement 
        print(f"Your final hand is: {users_hand}: The final score: {users_score}")
        print(f"Your opponent's final hand is: {programs_hand}: The final score: {programs_score}")
# conditionals to check score, and print out the result. 
# used +=1 to add to the score board since its out of 3 matches
        if users_score > 21:
            print("You went over, you lose.")
            programs_win += 1 
        elif programs_score > 21:
            print("Your opponent went over, you win.")
            user_wins += 1
        elif users_score > programs_score:
            print("You win!")
            user_wins += 1 
        elif users_score < programs_score:
            print("You lose!")
            programs_win += 1 
        else:
            print("It's a draw!")
# the print statement prints the current score then adds to the amount of rounds played
        print(f"""
    Current Score: User: {user_wins}
    Opponent: {programs_win}""")
        rounds_played += 1 
    # final print statement once match is over
    print("Thanks for playing today.")
    print(f""" 
    FINAL SCORE:
    USER: {user_wins}
    Opponent: {programs_win} 
    """)
    # if elif else to dicate what prints out depending on who wins
    if user_wins > programs_win:
        print("You have WON the match")
    elif user_wins < programs_win:
        print("You have LOST the match")
    else:
        print("ITS A DRAW") 
# play again input, but if user inputs invalid input, lets them know and gives them another chance
    play_again_input = input("Do you want to play another set of matches? Type 'yes' or 'no': ")
    while play_again_input.lower() not in ["yes", "no"]:
        print("You've entered an invalid option. Enter 'yes', or 'no': ")
        play_again_input = input("Do you want to play another set of matches? Type 'yes' or 'no': ")
# play again if the input is yes
    play_again = play_again_input.lower() == "yes" 
#once program is over, prints thank you
print("Thank you for playing my Blackjack Simulator.") 