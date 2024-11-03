import asyncio
import discord
import dotenv
import os

from disckit import UtilConfig, CogEnum
from disckit.cogs import dis_load_extension
from pathlib import Path

from core import Bot


bot_intents = discord.Intents(guilds=True, members=True)
bot_env = dotenv.dotenv_values()
BOT_TOKEN = bot_env["BOT_TOKEN"]

UtilConfig.BUG_REPORT_CHANNEL = 1293653697385205802
UtilConfig.STATUS_COOLDOWN = 600


async def load_extensions(bot: Bot) -> None:
    for folder in os.listdir("cogs/"):
        cog_folder = Path("cogs/", folder)
        for file in os.listdir(cog_folder):
            if file.endswith(".py"):
                cog_dir = cog_folder / file
                await bot.load_extension(".".join(cog_dir.parts)[:-3])
                print(f"Loading Extension: {cog_dir.name}")


async def main() -> None:
    bot = Bot(
        intents=bot_intents,
        status=discord.Status.idle,
    )

    await load_extensions(bot=bot)
    await dis_load_extension(bot, CogEnum.ERROR_HANDLER, CogEnum.STATUS_HANDLER)

    await bot.start(token=BOT_TOKEN)


if __name__ == "__main__":
    asyncio.run(main())
