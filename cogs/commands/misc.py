from __future__ import annotations

from discord.ext import commands
from discord import app_commands, Interaction
from disckit.utils import MainEmbed
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core import Bot


class Misc(commands.Cog):
    """A simple miscelleanous cog."""

    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    @app_commands.command()
    @commands.is_owner()
    async def sync(self, interaction: Interaction) -> None:
        """Syncs all commands globally"""

        await interaction.response.defer()

        synced_global = await self.bot.tree.sync()
        await interaction.followup.send(
            embed=MainEmbed(f"Successfully synced `{len(synced_global)}` slash commands globally!")
        )


async def setup(bot: Bot) -> None:
    await bot.add_cog(Misc(bot))
