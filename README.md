# Python-Final-Project
# Blind Auction for a Diamond

## Overview

The Blind Auction for a diamond is a Python-based command-line program designed for conducting blind auctions with three rounds. The final winner with the highest bids of a diamond is determined through a series of bidding rounds and adjustments.

## Table of Contents

- [About this program](#about-this-program)
- [Basic Mechanics](#basic-mechanics)
- [How it Works](#how-it-works)
- [Usage](#usage)
- [Reflection of CS5001](#reflection)

## About this program

This program aims to recreate the dynamics of a blind auction, where participants place their initial bids without knowledge of others' offers. Unlike typical blind auctions featuring only a single bidding round, this program introduces multiple rounds. This unique approach allows participants to fine-tune their bids based on summary statistics before determining the ultimate winner.
In contrast to conventional blind auctions, this program offers participants a second opportunity to adjust their bids. This feature is designed to enhance the chances of achieving higher bids, fostering a more competitive and engaging auction experience. Consequently, individuals with a stronger interest in acquiring the auctioned item, particularly a diamond in this case, stand a better chance of securing the winning bid and claiming their coveted prize.


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
- Participants go through the blind bidding round, providing their names and initial bids. When the client provides name and initial bid, the program will ask if there is another client. If there is another client, the program will clean the screen to keep every client's bidding price in secret, and then ask the next client to provide information, until no other participants.
- According to the statistics of bids from last round, the program will calculate the highest price and the middle price in bids. Then, these statistics are displayed to participants.
- After knowing the summary statistics of blind round, participants can choose to keep their original bid or add to it within the specified limit. The specified limit is the final bidding price should not be more than 150% original price. So, the original price is also important to win this auction.
- After all client's operation, we have the final bids, and the program determines the final winner based on the highest final price. If we have more than one client with the same highest value, the client who submit bids early is the winner.


## Usage

To run the Blind Auction for a diamond program:
Run "blind_auction.py" in terminal, and follow the on-screen prompts to hold a blind auction for a diamond.


## Reflection
For this final project of CS5001, I chose to write a project   simulating a blind auction for a diamond scenario. In this project, I tried to use essential concepts I learned in this course, such as working with basic data types (string, tuple, dictionary), utilizing for loops and while loops, and implementing error handling with try-except blocks to manage user input.

In the initial stages of the project, I emphasized breaking down the problem into manageable pieces and created a flow chart to guide my code. I realized that breaking down the project into manageable pieces and writing functions for each component greatly facilitated the overall implementation. Initially, I envisioned expanding the CLI version into a graphical user interface (GUI) and transforming it into a web application. However, due to time constraints and limited experience with CSS, HTML, and JavaScript, I encountered challenges, particularly in the JavaScript aspect. As a result, I opted to submit the CLI version for the final project but have plans to revisit and complete the web application version in the coming month.

For the testing of two specific important pure functions in the blind_auction.py file, I created a dedicated test file. However, for the comprehensive validation of the entire project, I think it is better to run it in terminals and test with diverse input scenarios to cover various edge cases. I also provied the output of my terminal-based test.






