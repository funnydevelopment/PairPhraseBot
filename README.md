# Telegram bot that collects translations

## Description
This Telegram bot streamlines the process of collecting word translations. Users start a conversation, submit a word, 
provide its translation, and optionally include their name. The bot then allows users to confirm or cancel the 
submitted data, ensuring accuracy and user control throughout the translation process.

## Usage
To use this Telegram bot, follow these steps:
1. Start a conversation with the bot on Telegram.
2. Send the word you would like to translate to the bot.
3. In the subsequent step, provide the translation of the word.
4. Enter your name and optionally your surname to help us remember who provided the translations.
5. Confirm all the previous data that you have sent.

## Installation and Configuration
This project serves as an example for running the `bot.py` application. To successfully run the application, you will 
need a Python virtual environment and the installation of required packages from `requirements.txt`.

- Clone the repository: 
```
git clone git@github.com:funnydevelopment/PairPhraseBot.git
```
and navigate to the project folder.

- Create a Python virtual environment: 
```
python3 -m venv venv
```

- Activate the virtual environment:

On Windows:
```
venv\Scripts\activate
```

On macOS and Linux:
```
source venv/bin/activate
```

- Install the necessary dependencies from requirements.txt: 
```
pip install -r requirements.txt
```
- Run the project:
```
python3 bot.py
```