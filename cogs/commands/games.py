from __future__ import annotations

import random
from typing import TYPE_CHECKING

from disckit.utils import (
    ErrorEmbed,
    MainEmbed,
    SuccessEmbed,
    make_autocomplete,
)
from discord import app_commands
from discord.app_commands import locale_str as _T
from discord.ext import commands

from utils.game_utils import CoinFlipOption

if TYPE_CHECKING:
    from discord import Interaction

    from core.bot import Bot


class Games(commands.Cog):
    """A simple cog containing small games."""

    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    game_cmds = app_commands.Group(
        name="game",
        description="Fun game commands.",
        guild_only=True,
    )

    @game_cmds.command(name=_T("coin-flip"))
    @app_commands.describe(option=_T("The side you want to bet on!"))
    async def coin_flip(self, interaction: Interaction, option: CoinFlipOption) -> None:
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

    @game_cmds.command()
    @app_commands.describe(lower=_T("The lower range of the random number"))
    @app_commands.describe(upper=_T("The upper range of the random number"))
    async def number(self, interaction: Interaction, lower: int, upper: int) -> None:
        """A random number generator"""

        if lower > upper:
            await interaction.response.send_message(
                embed=ErrorEmbed("The upper number should be bigger than the lower number!")
            )
            return

        num = random.randint(lower, upper)
        await interaction.response.send_message(
            embed=MainEmbed(
                f"Your randomly generated number is: `{num}`!"
                f"\n-# Lower limit: {lower}, upper limit: {upper}"
            )
        )

    @game_cmds.command()
    @app_commands.autocomplete(fruit=make_autocomplete("Apple", "Banana", "Cherry"))
    async def choose_fruit(self, interaction: Interaction, fruit: str) -> None:
        await interaction.response.send_message(embed=MainEmbed(f"You chose the fruit: {fruit}!"))


async def setup(bot: Bot) -> None:
    await bot.add_cog(Games(bot))
