from nextcord.ext import commands
from utils import database


class ModelSwitch(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="change_model")
    async def change_model(self, ctx, model: str):
        await database.change_channel_model(ctx.channel.id, model)
        await ctx.send(f"Model changed to {model} for this channel.")
