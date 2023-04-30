import os
from nextcord.ext import commands
from nextcord import Intents
from cogs import model_switch, token_stats, openai_api
from cogs.openai_api import process_message
from utils.database import (
    initialize_database,
    update_tokens_used,
    get_model_for_channel,
)
from dotenv import load_dotenv


load_dotenv()
initialize_database(os.environ["MONGO_CONNECTION_STRING"])

intents = Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Add cogs
bot.add_cog(model_switch.ModelSwitch(bot))
bot.add_cog(token_stats.TokenStats(bot))
bot.add_cog(openai_api.OpenAI_API(bot))

# Processing message


@bot.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == bot.user:
        return

    # Only process messages that start with the 'ask' command
    if not message.content.startswith("!ask"):
        return

    # Get the user's message without the 'ask' command
    user_message = message.content[4:].strip()

    # Get the model for the current channel
    model = await get_model_for_channel(message.channel.id)

    # Process the user's message and generate a response
    generated_message = await bot.loop.run_in_executor(
        None, process_message, user_message, model
    )

    # Calculate the tokens used for both the user's message and the generated message
    tokens_used = len(user_message) + len(generated_message)

    # Update the user's tokens used in the database
    await update_tokens_used(message.author.id, tokens_used)

    # Send the generated message back to the user
    await message.channel.send(generated_message)


# Run the bot
bot.run(os.environ["BOT_TOKEN"])
