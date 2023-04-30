from nextcord.ext import commands
from utils import database


class TokenStats(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="payment")
    async def payment(self, ctx):
        tokens_used = await database.get_tokens_used(ctx.author.id)
        payment_equiv = (
            tokens_used * 0.002
        )  # Replace this with your actual payment calculation

        message = (
            f"Tokens Used: {tokens_used} \nPayment Equivalence: ${payment_equiv:.2f}"
        )
        await ctx.send(message)
