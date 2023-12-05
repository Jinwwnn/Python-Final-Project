# Python-Final-Project
# Blind Auction for a Diamond

## Overview

The Blind Auction for a diamond is a Python-based command-line program designed for conducting blind auctions with three rounds. The final winner with the highest bids of a diamond is determined through a series of bidding rounds and adjustments.

## Table of Contents

- [About this program](#about-this-program)
- [Basic Mechanics](#basic-mechanics)
- [How it Works](#how-it-works)
- [Usage/Installation Instructions](#usage/installation-instructions)
- [Code Review and Reflection](#code-review-and-reflection)

## About this program

This program aims to recreate the dynamics of a blind auction, where participants place their initial bids without knowledge of others' offers. Unlike typical blind auctions featuring only a single bidding round, this program introduces multiple rounds. This unique approach allows participants to fine-tune their bids based on summary statistics before determining the ultimate winner.
In contrast to conventional blind auctions, this program offers participants another opportunity to adjust their bids. This feature is designed to enhance the chances of achieving higher bids, fostering a more competitive and engaging auction experience. Consequently, individuals with a stronger interest in acquiring the auctioned item, particularly a diamond in this case, stand a better chance of securing the winning bid and claiming their coveted prize.


## Basic Mechanics

1. **Blind Bidding Round:**
   - Participants submit their initial bids without knowing others' bids.
   - Enter name and initial bidding price when prompted.
   - The bidding round ends once all participants have submitted their bids.

2. **Summary Statistics Round:**
   - After the blind bidding, participants see summary statistics, including the highest and middle bids.
   - Participants have a chance to adjust their bids in the next round.

3. **Adjustment Round:**
   - Participants choose to:
     - [1] Keep their original bid.
     - [2] Add their bid (within 50% of the original).
   - Enter the choice when prompted. If choosing [2], participants provide the bid amount.

4. **Final Results:**
   - The client with the highest final price is declared the winner.


## How it Works

- The program is initiated with a welcome message, including a ASCII art of a diamond, and introduction basic rules to the blind auction.
- Participants go through the blind bidding round, providing their names and initial bids. When the client provides name and initial bid, the program will ask if there is another client. After the client submit name and bidding price, it will ask if there is next client. If there is next one, the program will clean the screen to keep every client's bidding price in secret, and pass it to the next client to ask for his/her name and bidding price, until no other participants.
- According to the statistics of bids from last round, the program will calculate the highest price and the middle price in bids. Then, these statistics are displayed to participants.
- After knowing the summary statistics of blind round, participants can choose to keep their original bid or add to it within the specified limit. The specified limit is the final bidding price should not be more than 150% original price. So, the original price is also important to win this auction.
- After all client's operation, we have the final bids, and the program determines the final winner based on the highest final price. If we have more than one client with the same highest value, the client who submit bids early is the winner.


## Usage/ Installation Instructions
1. Download blind_auction.py file or clone it from GitHub.
2. Navigate to the Project Directory, using:
   cd blind_auction
3. Run the Blind Auction for a diamond program:
Run "blind_auction.py" in terminal, using:
   python blind_auction.py
Then follow the on-screen prompts to hold a blind auction for a diamond.


## Code Review and Reflection
1. For this final project of CS5001, I write a project simulating a blind auction scenario. Throughout this project, I applied fundamental concepts I have learned in this course, such as working with basic data types (string, tuple, dictionary), utilizing for loops and while loops, and implementing error handling with try-except blocks to manage user input.

2. Positive Aspects
-  Modularity and Functions
I tried to break the auction process into small pieces and convert them into functions to modularizes the code. For example, clear_screen() function:
```python
def clear_screen():
    """
    Clear the terminal screen.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
```
get_yes_no_answer()function:
```python
def get_yes_no_answer(prompt: str) -> bool:
    """
    Get a yes or no answer from the client.
    ...
    """
    while True:
        # ...
        answer = input(prompt).strip().lower()
        if answer == 'yes':
            return True
        elif answer == 'no':
            return False
        ...
```
-  User Input Validation
Since there are many interaction with users in my project, so input validation is implemented in functions like get_price() and get_yes_no_answer(), ensuring robust error handling. For example, 
   - Error handling if the user don't enter a number as bidding price.
   - When ask if there is next client, only allows 'yes' or 'no' answer in lowercase or uppercase in get_yes_no_answer().
   - For the user's input as name in the adjustment round, only allows the name appeared in the first round (both uppercase or lowercase will work). 
   - For the user's input as choice, only allows '1' or '2' as the answer.
   - For the user's input as new bidding price, it should satisfy the limit: initial price < new price < 1.5 * initial price.

```python
def get_price(message: str) -> float:
    """
    Get a valid bidding price of the client. The price should be a number.
    """
    while True:
        try:
            price = float(input(message))
            return price
        except ValueError:
            print(f"{_INVALID_MESSAGE} Please enter a valid number.")
```

```python
def keep_or_update_bids(name: str, bids: Dict[str, float]) -> Dict[str, float]:
    """
    Keep or add a client's bids according to their answer.
    ...
    """
    while True:
        # ...
        choice = input(_ADJUST_PROMPT).strip()
        # if the client wants to add, the adjustment should satisfy the limit.
        if choice == '2':
            new_price = get_price(_ADJUST_PRICE_PROMPT)
            # ...
            # if the limit is satisfied, update the new price.
            if bids[name] <= new_price <= bids[name] * 1.5:
                bids[name] = new_price
                ...
                break
            else:
                print(_OUTRANGE_ERROR_MESSAGE)
        elif choice == '1':
            ...
            break
        # ...
        else:
            print(f"{_INVALID_MESSAGE} You should enter '1' or '2'.")
    return bids
```

-  ASCII Art of Diamond Display 

3. Challenges: Initially, I envisioned expanding the CLI version into a graphical user interface (GUI) and transforming it into a web application. However, due to time constraints and limited experience with CSS, HTML, and JavaScript, I encountered challenges, particularly in the JavaScript aspect. As a result, I opted to submit the CLI version for the final project but have plans to revisit and complete the web application version in the coming month.

4. Testing: For the testing, I created a dedicated test file to test two crucial functions in blind_auction.py. However, for the comprehensive validation of the entire project, I think it is better to run it in terminals and test with diverse input scenarios to cover various edge cases. I also provied the output of my terminal-based test.






