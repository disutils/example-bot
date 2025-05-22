# from disckit.paginator import Paginator
from disckit.utils import MainEmbed
from discord import Interaction, app_commands
from discord.ext import commands

from paginator import Paginator


class Misc(commands.Cog):
    """A simple miscelleanous cog."""

    def __init__(self, bot: commands.Bot) -> None:
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

    @app_commands.command()
    async def pages(self, interaction: Interaction) -> None:
        """A test command for the custom disckit paginator"""

        home_page = MainEmbed("THIS IS HOME PAGE")

        pages: list[MainEmbed] = [MainEmbed(f"This is embed {i}") for i in range(10)]
        paginator = Paginator(
            interaction=interaction, pages=pages, home_button=True, home_page=home_page
        )
        await paginator.start()


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Misc(bot))
