# OpenAI-Discord-Bot

Hello everyone!, I'll explain some things about this repo

- Requirements
- Files & structure
- Functionality
  - High-level explanation
  - Start to develop
  - High-level code explanation
- Features attempts and errors (Here is explained with what idea the bot was born)
- Terms of Use

# Requirements

The necessary requirements to run this bot is inside the requirements.txt file, basically we used:
- nextcord
- openai
- pymongo
- python-dotenv
Install them one by one with the commnand:
```
pip install <dependency_name>
```
or all of them with:
```
pip install -r requirements.txt
```

# Files & Structure

The main / root folder contain the **main.py** file, the _cogs_ folder (where are located functions into the **model_switch.py**, **openai_api.py** and the **token_stats.py** files) and the _utils_ folder (for the **database.py** file).

We used a **.env** file to insert the sensitive data such as the BOT_TOKEN, the GUILD_ID (applicable for slash commands, a feature that we didn't add), the OPENAI_API_KEY and the MONGO_CONNECTION_STRING (because we used Atlas service for the MongoDB database).

# Functionality
## High-level explanation
The first and last commit have only the functionality to answer a prompt by using the _"!ask"_ command in the discord's chat, something like:

```
!ask <your_prompt>
```
And the bot should will answer yout prompt using a message.

![image](https://github.com/Lein-adq/OpenAI-Discord-Bot/assets/111263088/0297e129-535a-43e4-934f-1de29fa51b43)

## Start to develop
OK! You need to create a bot in https://discord.com/developers/applications and add it to your server (give it the recommended permissions or the admin permissions on a test server).
Then, I used Atlas MongoDB service https://www.mongodb.com/atlas. (When you have your account, in order to get your connection string just click Connect -> Drivers and the third step have your connection string).
Then with the necessary sensitive keys, you can create a .env file into the root folder and write down with the follow structure:
```
BOT_TOKEN=<your_bot-token>
GUILD_ID=<your_guild_id>
OPENAI_API_KEY=<your_openai_api_key>
MONGO_CONNECTION_STRING=<your_mongo_connection_string>
```
Without any symbol or quotation mark.

## High level code explanation

Every cog file has a main class, this class is imported in the main.py file, this importation allow us to use the functions inside each cog file.
The important files at the moment are the main.py (I mean, naturally), the cogs/openai_api.py and the utils/database.py.

Inside the cogs/openai_api.py is the function where the gpt model process the user's message (here is possible to edit the model to use, the max tokens, temperature, etc. but these three are the important).

The utils/database.py are the necessary functions that allows the storing of the user_id and the tokens used (explained in the next point).
They are called in the main.py file, and running the main.py file should be run the bot in the server.

# Features attempts and Errors
OK! The main idea of the bot was sharing the payment with friends that don't want to pay the ChatGPT Plus subscription or not have a CC to pay with its owns, so, that's why we used a database to store the User's ID and its usage of tokens in order to distinguish each payment for each user.
Basically, a ChatGPT with our own User Interface (and to pay by usage and not a shared subscription).
Also we wanted to implement the follow functionalities (but they aren't achieved):
- Model (GPT 3.5 and GPT 4) can be changed any time in a channel with a command.
- Each user can check its updated payment quantity by using a command.
- We can delete channels (equivalent to chats in ChatGPT)

There exists some errors also:
- In the main.py file, the counting of tokens is not working correctly, there is counting the quantity of characters of the user and the bot messages, to fix that we wanted to use the tiktoken library.
- We couldn't test the model_switch function.

# Terms of use
Well, this is a public repo, and because we don't consider resuming the project in the future, you can use this project as you want! Obviously, following the Terms of Use and Policies of OpenAI, so that it does not develop as a malicious or harmful project.
It should also be noted that any damage or loss caused as a result of this project, a disclaimer of responsibilities applies to me and to OpenAI

# You can Support us!
Well, we are still students, so any help in our learning, improvement and professional development will be greatly appreciated!!!

<a href='https://ko-fi.com/X8X3L71QJ' target='_blank'><img height='36' style='border:0px;height:36px;' src='https://storage.ko-fi.com/cdn/kofi2.png?v=3' border='0' alt='Buy Me a Coffee at ko-fi.com' /></a>
