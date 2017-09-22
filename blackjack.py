import random

cards = []
card_values = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'Jack':10,'Queen':10,'King':10,'Ace':11}

def get_card():
    card = random.choice(cards)
    cards.remove(card)
    return card

def ask_for_card():
    user_wants_another_card = raw_input('Would you like another card? Y/N\n')
    response = user_wants_another_card.lower()
    if response == 'y' or response == 'n':
        return response
    else:
        print 'You need to reply with Y/N'
        return ask_for_card()

def first_deal(user):
    first_card = get_card()
    second_card = get_card()

    user_total = card_values[first_card] + card_values[second_card]
    if user == 'dealer':
        print "The dealer got " + first_card
    else:
        print "You got cards " + first_card + " and " + second_card + " for a value of " + str(user_total)
    return first_card, second_card, user_total

def game():
    game_cards = 4 * ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
    cards.extend(game_cards)

    user_first_card, user_second_card, user_total = first_deal('user')
    dealer_first_card, dealer_second_card, dealer_total = first_deal('dealer')

    response = 'y'
    while user_total < 21 and response == 'y':
        response = ask_for_card()
        if response == 'y':
            next_card = get_card()
            user_total += card_values[next_card]
            if user_total < 21:
                print "You got card " + next_card + ". Your total is now " + str(user_total)
    if user_total == 21:
        print "Your total is 21 so you win!!!!"
        #play again?]
    elif user_total > 21:
        print "You got card " + next_card + ". Your total is now " + str(user_total) + ". You lose sucker!!!!"
    else:
        print "Your total is still " + str(user_total)
        print "the dealer's second card is " + dealer_second_card + " for a total " + str(dealer_total)
game()
