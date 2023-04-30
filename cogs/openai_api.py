import openai
import os
from nextcord.ext import commands


class OpenAI_API(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def gpt3(self, ctx, *, user_message):
        model = "text-davinci-002"
        generated_message = process_message(user_message, model)
        await ctx.send(generated_message)


def setup(bot):
    bot.add_cog(OpenAI_API(bot))


def process_message(user_message, model):
    openai.api_key = os.environ["OPENAI_API_KEY"]
    response = openai.Completion.create(
        engine=model,
        prompt=user_message,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.9,
    )

    generated_message = response.choices[0].text.strip()

    return generated_message
