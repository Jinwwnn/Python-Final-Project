"""
CS5001 Final Project: Blind Auction For Antique Vase

A bind auction with two rounds. The final winner will take the antique vase.
"""
from typing import Tuple, Dict
import os

# use these constants for the prompts and messages.
_WELCOME_MESSAGE = """
Welcome to the Blind Auction for a Diamond!\n
                    '
           '                 '
   '         '      '      '        '
      '        \    '    /       '
          ' .   .-"```"-.  . '
                \`-._.-`/
     - -  =      \  |  /      =  -  -
                ' \ | / '
          . '      \|/     ' .
       .         '  `  '         .
    .          /    .    \           .
             .      .      .
"""
_INTRODUCE_MESSAGE = """
We will have three rounds in this auction.
**Basic Mechanics:**
1. **Blind Bidding Round:**
   - Submit your initial bid without knowing others' bids.
   - Enter your name and bidding price when prompted.
   - The bidding round will end once all participants have submitted their bids.

2. **Summary Statistics Round:**
   - After the blind bidding, you'll see summary statistics:
     - Highest Bid: [Highest Price]
     - Middle Bid: [Middle Price]
   - Participants will have a chance to adjust their bids in the next round.

3. **Adjustment Round:**
   - You can choose to:
     - [1] Keep your original bid.
     - [2] Add your bid (within 50% of the original).
   - Enter your choice when prompted. And if you choose [2], you should give your bid amount.

4. **Final Results:**
    The client with the highest final price is the winner.
"""
_GOODBYE_MESSAGE = """Thank you for participating in this blind auction. See you next time."""
_BIDDING_NAME_PROMPT = """Enter your name:  """
_BIDDING_PRICE_PROMPT = """Enter your innitial bidding price:  """
_NEXT_PROMPT = """Are there any other bidders? Type 'yes or 'no':  """
_ADJUST_PROMPT = """Choose an option:
[1] Keep your original bid.
[2] Add your bid (within 50% of the original).
Enter your choice '1' or '2':  
"""
_ADJUST_PRICE_PROMPT = """ Please enter your final bidding price:  """
_COMFIRMATION_MESSAGE = """Thank you. Your bid has been recorded. """
_INVALID_MESSAGE = """Invalid entry."""
_NAME_ERROR_MESSAGE = """Can't find this name. Please check and entre again."""
_OUTRANGE_ERROR_MESSAGE = """Your adjustment amount is out of range. You cannot add more than 50% of the original price or reduce the price."""


def clear_screen():
    """
    Clear the terminal screen.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def get_price(message: str) -> float:
    """
    Get a valid bidding price of the client. The price should be a number.
    """
    while True:
        try:
            price = float(input(message))
            return price
        except ValueError:  # if the client don't enter a number, ask him/her to re-entre.
            print(f"{_INVALID_MESSAGE} Please enter a valid number.")


def get_yes_no_answer(prompt: str) -> bool:
    """
    Get a yes or no answer from the client.

    Args:
        prompt (str): The prompt message to client.

    Returns:
        bool: True if the answer is 'yes', False if 'no'. 
    """
    while True:
        answer = input(prompt).strip().lower()
        if answer == 'yes':
            return True
        elif answer == 'no':
            return False
        else:
            print(f"{_INVALID_MESSAGE} Please enter 'yes' or 'no'.")


def blind_round() -> Dict[str,float]:
    """
    In the first bind round, we get all client's names and initial bidding price 
    and save them in a dictionary.
    Clients' name are the keys, and prices are the values in the dictionary.
    
    Returns:
        dict: Dictionary with names as keys and prices as values.
    """
    bids = {}
    while True:
        name = input(_BIDDING_NAME_PROMPT).strip().lower()  # get client's name
        initial_price = get_price(_BIDDING_PRICE_PROMPT)  # get price
        bids[name] = initial_price  # save client's name and price accordingly in the dictinary
        clear_screen()  # after the client submit price, clear the screen.
        print(_COMFIRMATION_MESSAGE)  # comfirm the client's submission
        # ask the current client if we have the next client
        # if don't have the next client, break the loop
        if not get_yes_no_answer(_NEXT_PROMPT):
            break
    return bids


def get_statistics_summary(bids:Dict[str, float]) -> Tuple:
    """
    Get the middle and highest prices in the bids.
    
    Args:
        bids (dict): Dictionary with names as keys and prices as values.

    Return:
        Tuple: The highest_price and middle_price in the bids.
    """
    highest_price = max(bids.values())  # get the maximum value in the dictionary.
    middle_price = sum(bids.values()) / len(bids)  # get the middle value in the bids.
    return highest_price, middle_price
    

def print_statistics_summary(bids:Dict[str, float]) -> None:
    """
    Print the middle and highest prices on the screen as clients' adjustment reference.
    
    Args:
        bids (dict): Dictionary with names as keys and prices as values.
    """
    highest_price, middle_price = get_statistics_summary(bids)
    print(f"The first bind round is finished.\n "
          f"At the first round, the highest bidding price is ${highest_price}, "
          f"and the middle price is ${middle_price:.2f}.")


def keep_or_update_bids(name: str, bids: Dict[str, float]) -> Dict[str, float]:
    """
    Keep or add a client's bids according to their answer. 
    Limit: The client are not allowed to add more than 50% of the original price or reduce the price.
    
    Args:
        name (str): Name of the participant.
        bids (dict): Original bids.

    Returns:
        dict: the dictionary with new values(prices) or original values.
    """
    while True:
        choice = input(_ADJUST_PROMPT).strip()  # ask client if they want to keep or add bids.
        # if the client wants to add, the adjustment should satisfy the limit.
        if choice == '2':
            new_price = get_price(_ADJUST_PRICE_PROMPT)
            # The client are not allowed to add more than 50% of the original price or reduce the price.
            # if the limit is satisfied, update the new price in the dictionary.
            if bids[name] <= new_price <= bids[name] * 1.5:
                bids[name] = new_price
                clear_screen()  # when the client submit price, clear the screen.
                print(_COMFIRMATION_MESSAGE)  # comfirm client's submission.
                break
            else:
                print(_OUTRANGE_ERROR_MESSAGE)
        elif choice == '1':
            break
        else:  # if the client do not choose '1' or '2', he/she needs to re-entre.
            print(f"{_INVALID_MESSAGE} You should enter '1' or '2'.")
    return bids


def adjust_round(bids: Dict) -> Dict:
    """
    Adjust bids in this round.
    
    Args:
        bids (dict): Original bids.

    Returns:
        dict: Updated bids.
    """
    while True:
        # ask for client's name first.
        name = input(_BIDDING_NAME_PROMPT).strip().lower()
        # if the client's name is not exist, ask the client to check typing and re-enter.
        if name not in bids:
            print(_NAME_ERROR_MESSAGE)
            continue
        bids = keep_or_update_bids(name, bids)
        if not get_yes_no_answer(_NEXT_PROMPT):
            break
    return bids


def get_winner(bids: dict) -> Tuple:
    """
    Find the final winner and the highest price.
    If we have more than one client with the same highest value, the client who submit bids early is the winner.
    
    Args:
        bids (dict): Bids after all the rounds.

    Returns:
        Tuple: The winner's name and final bidding price. 
    """
    highest_price = 0
    # Iterate through values in the dictionary
    for key in bids.keys():
        # Update highest_price if the current value is higher
        if bids[key] > highest_price:
            highest_price = bids[key]
            winner_name = key.title()
    return winner_name, highest_price


def run_blind_auction() -> None:
    """
    Runs the blind auction application.
    """
    print(_WELCOME_MESSAGE)
    print(_INTRODUCE_MESSAGE)
    initial_bids = blind_round()
    print_statistics_summary(initial_bids)
    print("Let's come to the Adjustment Round!")
    final_bids = adjust_round(initial_bids)
    winner_name, winner_price = get_winner(final_bids)
    print(f"The final winner is {winner_name} with price $ {winner_price}!")
    print(_GOODBYE_MESSAGE)


if __name__ == "__main__":
    run_blind_auction()
