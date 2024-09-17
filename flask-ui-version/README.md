# Blind Auction Application

## Overview

This is a web-based Blind Auction application built using Flask. Participants can place bids, adjust their bids, and view statistics about the auction. The application provides a user-friendly interface for managing the auction process.

## Features

- **Bidding Round**: Users can enter their name and initial bid.
- **Adjustment Round**: Users can choose to keep their original bid or adjust it within a specified limit.
- **Statistics**: Displays the highest and average bidding prices after the bidding round.
- **Result Announcement**: Shows the winner of the auction based on the highest bid.

## Technologies Used

- **Flask**: A lightweight WSGI web application framework for Python.
- **HTML/CSS**: For structuring and styling the web pages.
- **JavaScript**: For dynamic form behavior.

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```
2. Install the required packages:

   ```bash
   pip install Flask
   ```
3. Run the application:

   ```bash
   python app.py
   ```
4. Open your web browser and navigate to `http://127.0.0.1:5000/`.

## Usage

- Start the auction by clicking on "Start Auction" on the home page.
- Participants can place their bids and proceed through the bidding and adjustment rounds.
- After all bids are placed, the statistics and results will be displayed.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.
