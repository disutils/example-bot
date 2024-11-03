from discord.ext import commands
from discord import app_commands, Interaction
from disckit.utils import MainEmbed


class Misc(commands.Cog):
    """A simple miscelleanous cog."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command()
    @commands.is_owner()
    async def sync(self, interaction: Interaction):
        """Syncs all commands globally"""

        await interaction.response.defer()

        synced_global = await self.bot.tree.sync()
        await interaction.followup.send(
            embed=MainEmbed(
                f"Successfully synced `{len(synced_global)}` slash commands globally!"
            )
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Misc(bot))
