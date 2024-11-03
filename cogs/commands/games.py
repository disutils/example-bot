import random

from discord.ext import commands
from discord import app_commands, Interaction
from disutil.utils import SuccessEmbed, ErrorEmbed

from utils.game_utils import CoinFlipOption


class Games(commands.Cog):
    """A simple cog containing small games."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="coin-flip")
    async def coin_flip(self, interaction: Interaction, option: CoinFlipOption):
        """A fun coin flip command!"""

        option = str(option)
        win = random.choice(("Head", "Tails"))

        if win == option:
            await interaction.response.send_message(
                embed=SuccessEmbed(
                    f"The coin landed on... {win}!\n" "You won the game!"
                )
            )

        else:
            await interaction.response.send_message(
                embed=ErrorEmbed(f"The coin landed on... {win}!\n" "You lost the game!")
            )
