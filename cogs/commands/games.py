import random

from discord.ext import commands
from discord import app_commands, Interaction
from disckit.utils import SuccessEmbed, ErrorEmbed

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
                    f"The coin landed on... {win}!\nYou won the game!",
                    f"You placed on {option}",
                )
            )

        else:
            await interaction.response.send_message(
                embed=ErrorEmbed(
                    f"The coin landed on... {win}!\nYou lost the game!",
                    f"You placed on {option}",
                )
            )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Games(bot))
